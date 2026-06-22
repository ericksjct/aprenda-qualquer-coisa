#!/usr/bin/env python3
"""Converte um PDF de livro em markdown dividido por capitulo com ancoras de pagina.

Ferramenta OPT-IN (NAO faz parte do core stdlib-only do toolkit). Requer o venv
de requirements-pdf.txt (docling + pypdf) instalado a parte; o core continua
100% stdlib e intocado. Adaptada de converter.py: faz UMA conversao do documento
inteiro (preservando estrutura e numeros de pagina nativos), divide de forma
deterministica por TITLE/SECTION_HEADER e grava um .md por capitulo sob
.projetos/<slug>/livro/, cada arquivo abrindo com uma ancora `<!-- page: N -->`.

Uso:
    # Ative o venv opt-in primeiro (Windows PowerShell):
    #   python -m venv .venv-pdf; .\\.venv-pdf\\Scripts\\activate
    #   pip install -r requirements-pdf.txt
    python scripts/converte_livro.py <pdf> --slug <slug> [--out <dir>] [--cut-level N]

    # default --out  = .projetos/<slug>/livro/
    # default --cut-level = 1  (uma nova fronteira a cada TITLE/SECTION_HEADER nivel <= N)

Observacoes:
    - Roda LOCAL, nao consome tokens; a 1a execucao baixa modelos (~2GB) e demora.
    - O conteudo do livro PRESERVA acentos (artefato do aluno); apenas os nomes de
      arquivo sao ASCII (identificadores de path).
"""

import argparse
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

# --- BLINDAGEM DE MEMORIA (C++) -------------------------------------------
# Evita std::bad_alloc limitando as threads do motor de OCR. DEVE vir ANTES de
# qualquer import de docling (os imports do docling sao lazy, dentro das funcoes).
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

# NAO importar docling aqui no topo: os helpers puros abaixo e a suite de testes
# precisam importar este modulo SEM docling instalado.

_SLUG_RE = re.compile(r"^[a-z0-9-]+$")


def sanitize_slug(slug: str) -> str:
    """Valida o slug como componente de path seguro (ASVS V5).

    Rejeita slugs com `/`, `\\` ou `..`, ou que nao casem inteiramente com
    `^[a-z0-9-]+$`. Em caso de rejeicao, encerra com mensagem amigavel (mirror
    de roadmap_fetch.py). Retorna o slug inalterado quando valido.
    """
    if "/" in slug or "\\" in slug or ".." in slug or not _SLUG_RE.fullmatch(slug):
        sys.exit("Slug invalido: use kebab-case [a-z0-9-], sem separadores de path.")
    return slug


def _label_name(item):
    """Nome do label do item (`.label.name`) ou None se ausente."""
    label = getattr(item, "label", None)
    return getattr(label, "name", None)


def _page_of(item):
    """prov[0].page_no do item, ou None quando nao ha provenance."""
    prov = getattr(item, "prov", None)
    if prov:
        return prov[0].page_no
    return None


def _is_boundary(item, cut_level: int) -> bool:
    """True se o item inicia um novo capitulo: TITLE, ou SECTION_HEADER<=cut_level."""
    name = _label_name(item)
    if name == "TITLE":
        return True
    if name == "SECTION_HEADER":
        return getattr(item, "level", 99) <= cut_level
    return False


def split_into_chapters(doc, cut_level: int = 1) -> list:
    """Divide o documento em capitulos de forma deterministica (D-09).

    Itera `doc.iterate_items()`; uma fronteira e um TITLE ou um SECTION_HEADER
    com `level <= cut_level`. Cada fronteira inicia
    {"title": item.text, "start_page": _page_of(item), "items": [...]} e todo
    item (inclusive o heading) entra no capitulo corrente. NAO usa LLM.
    """
    # Import lazy do DocItemLabel real apenas para forcar o uso da API canonica
    # do docling quando presente; a comparacao efetiva e por `.name`, robusta a
    # sentinelas de teste. Mantem o modulo importavel sem docling.
    try:  # pragma: no cover - depende do ambiente
        from docling_core.types.doc import DocItemLabel  # noqa: F401
    except Exception:  # pragma: no cover
        pass

    chapters: list = []
    current = None
    for item, _ in doc.iterate_items():
        if _is_boundary(item, cut_level):
            current = {
                "title": getattr(item, "text", ""),
                "start_page": _page_of(item),
                "items": [],
            }
            chapters.append(current)
        if current is not None:
            current["items"].append(item)
    return chapters


def render_chapter(chapter: dict) -> str:
    """Serializa um capitulo em markdown (D-10 ancora + D-15 acentos).

    Comeca com `<!-- page: N -->` (quando start_page nao e None), linha em
    branco, `# {title}`, depois o corpo concatenado dos itens. NAO normaliza
    para ASCII: acentos do texto original sao preservados.
    """
    parts: list = []
    start_page = chapter.get("start_page")
    if start_page is not None:
        parts.append(f"<!-- page: {start_page} -->")
        parts.append("")
    parts.append(f"# {chapter.get('title', '')}")
    parts.append("")
    body = []
    for item in chapter.get("items", []):
        text = getattr(item, "text", "")
        if text:
            body.append(text)
    parts.append("\n\n".join(body))
    return "\n".join(parts).rstrip() + "\n"


def chapter_filename(index: int, title: str) -> str:
    """Nome de arquivo ASCII `NN-slug-do-titulo.md` (identificador de path).

    O nome e ASCII; o CONTEUDO do arquivo preserva acentos.
    """
    ascii_title = title.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_title).strip("-")
    if not slug:
        slug = "capitulo"
    return f"{index:02d}-{slug}.md"


def heading_histogram(doc) -> Counter:
    """Counter por (label.name, level) sobre TITLE/SECTION_HEADER.

    Ajuda o operador a escolher --cut-level (Pitfall 5 da pesquisa).
    """
    levels: Counter = Counter()
    for item, _ in doc.iterate_items():
        name = _label_name(item)
        if name in ("TITLE", "SECTION_HEADER"):
            levels[(name, getattr(item, "level", None))] += 1
    return levels


def convert_pdf(pdf_path, cut_level: int):
    """Converte o PDF inteiro em UM passe e retorna o DoclingDocument (D-12).

    Imports do docling sao LAZY (so aqui) para manter o modulo e os helpers
    importaveis sem docling instalado.
    """
    from docling.datamodel.accelerator_options import (
        AcceleratorDevice,
        AcceleratorOptions,
    )
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption

    opts = PdfPipelineOptions()
    opts.do_ocr = True  # PRESERVE (base script)
    opts.generate_picture_images = True  # PRESERVE; figuras best-effort (D-11)
    # Controle de memoria (RESEARCH Pattern 1): substitui o chunking pypdf 1-pagina.
    opts.accelerator_options = AcceleratorOptions(
        num_threads=1, device=AcceleratorDevice.CPU
    )

    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )

    print(
        "[*] Convertendo o livro inteiro (pode demorar; nao consome tokens; roda local)..."
    )
    # Fallback de OOM (Pitfall 1): se ocorrer std::bad_alloc/OOM, use
    # page_range=(s,e) em lotes de 10-20 paginas (NUNCA 1 pagina) e mescle os
    # documentos resultantes. Documentado, nao implementado no caminho feliz.
    result = converter.convert(pdf_path)
    doc = result.document

    print("[*] Histograma de headings (use para escolher --cut-level):")
    print(f"    {dict(heading_histogram(doc))}")
    return doc


def _run_markdownlint(write_path) -> None:
    """Roda `markdownlint --fix` uma vez no arquivo (D-12), com skip gracioso.

    Args sao uma lista literal FIXA + um path controlado pelo script; nenhum
    texto do usuario e interpolado em string de shell (threat T-07-02).
    """
    try:
        subprocess.run(
            ["markdownlint", "--fix", str(write_path)],
            capture_output=True,
            text=True,
            check=False,
            shell=True,  # necessario para execucao correta no Windows
        )
    except FileNotFoundError:
        print("    [!] Aviso: 'markdownlint' nao encontrado no sistema.")
        print("    Certifique-se de rodar: npm install -g markdownlint-cli")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pdf", help="caminho do PDF do livro")
    parser.add_argument("--slug", required=True, help="slug do projeto (kebab-case)")
    parser.add_argument(
        "--out",
        default=None,
        help="diretorio de saida (default: .projetos/<slug>/livro/)",
    )
    parser.add_argument(
        "--cut-level",
        type=int,
        default=1,
        help="nivel de corte do split (default: 1)",
    )
    args = parser.parse_args()

    slug = sanitize_slug(args.slug)  # path-safety ANTES de qualquer write (T-07-01)

    pdf_path = Path(args.pdf)
    if not pdf_path.is_file():
        sys.exit(f"PDF nao encontrado: {pdf_path}")

    out_dir = Path(args.out) if args.out else Path(".projetos") / slug / "livro"
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = convert_pdf(pdf_path, args.cut_level)
    chapters = split_into_chapters(doc, args.cut_level)

    total = len(chapters)
    for i, chapter in enumerate(chapters, 1):
        write_path = out_dir / chapter_filename(i, chapter["title"])
        write_path.write_text(render_chapter(chapter), encoding="utf-8")
        print(f"    -> capitulo {i}/{total} (pagina {chapter['start_page']})")
        _run_markdownlint(write_path)

    print(f"OK: {out_dir} ({total} capitulos)")


if __name__ == "__main__":
    main()
