#!/usr/bin/env python3
"""Converte um PDF de livro em markdown dividido por capitulo com ancoras de pagina.

Ferramenta OPT-IN (NAO faz parte do core stdlib-only do toolkit). Requer o venv
de requirements-pdf.txt (docling + pypdf) instalado a parte; o core continua
100% stdlib e intocado. Adaptada de converter.py: converte o PDF em LOTES de
paginas (via `page_range` nativo do docling, com `gc.collect()` entre lotes
para evitar std::bad_alloc em livros grandes), preservando os numeros de
pagina NATIVOS, divide de forma deterministica por TITLE/SECTION_HEADER e
grava um .md por capitulo sob .projetos/<slug>/livro/, cada arquivo abrindo
com uma ancora `<!-- page: N -->`.

Uso:
    # Ative o venv opt-in primeiro (Windows PowerShell):
    #   python -m venv .venv-pdf; .\\.venv-pdf\\Scripts\\activate
    #   pip install -r requirements-pdf.txt
    python scripts/converte_livro.py <pdf> --slug <slug> [--out <dir>] [--cut-level N] [--batch-size N] [--formulas] [--threads N] [--no-ocr]

    # default --out  = .projetos/<slug>/livro/
    # default --cut-level = 1  (uma nova fronteira a cada TITLE/SECTION_HEADER nivel <= N)
    # default --batch-size = 15  (paginas convertidas por lote; nunca usar 1)

Observacoes:
    - Roda LOCAL, nao consome tokens; a 1a execucao baixa modelos (~2GB) e demora.
    - O conteudo do livro PRESERVA acentos (artefato do aluno); apenas os nomes de
      arquivo sao ASCII (identificadores de path).
"""

import argparse
import gc
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
        if not text:
            continue
        if _label_name(item) == "FORMULA":
            # Equacao enriquecida (LaTeX) vira bloco de display math; antes
            # era descartada (item sem .text) ou colada como prosa.
            body.append(f"$$\n{text}\n$$")
        else:
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


DEFAULT_BATCH_SIZE = 15  # paginas por lote (Pitfall 1: 10-20, nunca 1)


def _page_batches(total_pages: int, batch_size: int = DEFAULT_BATCH_SIZE) -> list:
    """Gera lotes de paginas 1-indexados e inclusivos: [(1,15), (16,30), ...].

    Pura/sem docling: usada tanto pelo caminho real (via pypdf.PdfReader para
    contar paginas) quanto pelos testes (chamada direto com um total_pages
    sintetico). `batch_size` NUNCA deve ser 1 (Pitfall 1: temp PDF de 1 pagina
    e o que a referencia faz e o que queremos evitar aqui, pois converte_livro
    depende de page_no nativo, e page_range preserva isso so quando convertemos
    em lotes reais via docling, nao via temp-PDF de 1 pagina).
    """
    if total_pages <= 0:
        return []
    if batch_size <= 0:
        batch_size = DEFAULT_BATCH_SIZE
    batches = []
    start = 1
    while start <= total_pages:
        end = min(start + batch_size - 1, total_pages)
        batches.append((start, end))
        start = end + 1
    return batches


class _ChainedDoc:
    """Encadeia `iterate_items()` de varios DoclingDocument (um por lote).

    Os helpers (`split_into_chapters`, `heading_histogram`) so chamam
    `doc.iterate_items()` e leem atributos do item (`.label`, `.level`,
    `.text`, `.prov`); por isso basta encadear os iteradores dos lotes, na
    ordem em que foram convertidos, sem mesclar objetos DoclingDocument
    internamente (operacao fragil e nao suportada publicamente pela API).
    """

    def __init__(self, docs: list):
        self._docs = docs

    def iterate_items(self):
        for doc in self._docs:
            yield from doc.iterate_items()


def convert_pdf(
    pdf_path,
    cut_level: int,
    batch_size: int = DEFAULT_BATCH_SIZE,
    formulas: bool = False,
    threads: int = 1,
    ocr: bool = True,
):
    """Converte o PDF em LOTES de paginas e retorna um doc encadeado (D-12).

    Substitui a conversao whole-document (que estourava memoria/std::bad_alloc
    em livros grandes) por chamadas `converter.convert(pdf_path, page_range=
    (s, e))` em lotes de `batch_size` paginas, com `gc.collect()` entre lotes -
    mesma estrategia da referencia (converter.py), mas via `page_range` nativo
    do docling em vez de PdfWriter/temp-PDF de 1 pagina. Isso preserva os
    numeros de pagina NATIVOS (page_range nao reseta page_no, ao contrario de
    um temp-PDF de 1 pagina isolado), o que e essencial para as ancoras
    `<!-- page: N -->` e para `split_into_chapters`.

    Imports do docling/pypdf sao LAZY (so aqui) para manter o modulo e os
    helpers importaveis sem docling instalado.
    """
    if threads > 1:
        # Solta a blindagem do topo do modulo ANTES dos imports lazy do
        # docling/torch (que leem estas vars no proprio import). A blindagem
        # threads=1 protege o OCR em scan; com --no-ocr ela so custa tempo.
        for var in (
            "OMP_NUM_THREADS",
            "OPENBLAS_NUM_THREADS",
            "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS",
            "NUMEXPR_NUM_THREADS",
        ):
            os.environ[var] = str(threads)

    from pypdf import PdfReader

    from docling.datamodel.accelerator_options import (
        AcceleratorDevice,
        AcceleratorOptions,
    )
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption

    opts = PdfPipelineOptions()
    opts.do_ocr = ocr  # default True (scan); --no-ocr para PDF nativo
    opts.generate_picture_images = True  # PRESERVE; figuras best-effort (D-11)
    if formulas:
        # Equacao -> LaTeX no .text do item FORMULA (senao o renderer nao tem
        # o que emitir). 1a execucao baixa o modelo CodeFormula (~GB); avisar.
        opts.do_formula_enrichment = True
        print("[*] Enriquecimento de formula LIGADO (1a execucao baixa modelo extra).")
    opts.accelerator_options = AcceleratorOptions(
        num_threads=threads, device=AcceleratorDevice.CPU
    )

    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )

    total_pages = len(PdfReader(pdf_path).pages)
    batches = _page_batches(total_pages, batch_size)

    print(
        f"[*] Convertendo o livro em {len(batches)} lote(s) de até "
        f"{batch_size} paginas (total {total_pages} paginas; nao consome "
        "tokens; roda local)..."
    )

    docs = []
    for i, (start, end) in enumerate(batches, 1):
        print(f"    -> lote {i}/{len(batches)} (paginas {start}-{end})...", end=" ")
        result = converter.convert(pdf_path, page_range=(start, end))
        docs.append(result.document)
        print("OK")
        gc.collect()  # Fallback de OOM (Pitfall 1): libera memoria entre lotes.

    doc = _ChainedDoc(docs)

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
    parser.add_argument(
        "--formulas",
        action="store_true",
        help=(
            "liga o enriquecimento de formula do docling (equacao -> LaTeX no "
            "markdown); mais lento, 1a execucao baixa modelo extra"
        ),
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=1,
        help=(
            "threads dos modelos (default: 1, blindagem anti-bad_alloc para "
            "scan+OCR; em PDF nativo com --no-ocr pode subir para acelerar)"
        ),
    )
    parser.add_argument(
        "--no-ocr",
        action="store_true",
        help="desliga o OCR (use em PDF nativo com camada de texto; mais rapido)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help=(
            "paginas convertidas por lote (default: "
            f"{DEFAULT_BATCH_SIZE}; evita std::bad_alloc em livros grandes; "
            "nunca usar 1)"
        ),
    )
    args = parser.parse_args()

    slug = sanitize_slug(args.slug)  # path-safety ANTES de qualquer write (T-07-01)

    pdf_path = Path(args.pdf)
    if not pdf_path.is_file():
        sys.exit(f"PDF nao encontrado: {pdf_path}")

    out_dir = Path(args.out) if args.out else Path(".projetos") / slug / "livro"
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = convert_pdf(
        pdf_path,
        args.cut_level,
        args.batch_size,
        formulas=args.formulas,
        threads=args.threads,
        ocr=not args.no_ocr,
    )
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
