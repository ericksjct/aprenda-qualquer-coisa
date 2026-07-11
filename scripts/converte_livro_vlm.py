#!/usr/bin/env python3
"""Converte um PDF de livro em markdown por capitulo via VLM (baidu/Unlimited-OCR).

Motor ALTERNATIVO ao converte_livro.py (docling): usa um VLM local em GPU para
extrair texto + FORMULAS (LaTeX) com fidelidade, inclusive de PDF ESCANEADO --
o caso que o caminho docling nao resolve (decisao G1 revisada da Fase 07.1).
Mesmo contrato de saida: um .md por capitulo em .projetos/<slug>/livro/, cada
pagina com ancora `<!-- page: N -->` (N = pagina NATIVA do PDF).

Requer GPU NVIDIA e o venv opt-in de requirements-ocr.txt (ver instrucoes la).
O core do toolkit continua stdlib-only; sem GPU, use converte_livro.py.

Uso:
    python scripts/converte_livro_vlm.py <pdf> --slug <slug> [--out <dir>]
        [--pages A-B] [--dpi 150] [--cut-regex REGEX] [--crop]

Velocidade (RTX 4070): ~50s/pagina no modo default (sem crop, image_size=1024;
mesma fidelidade de formula do crop mode no teste A/B de 2026-07-11). `--crop`
liga o crop mode (~2x mais lento), tente se alguma pagina sair ruim.

Observacoes:
    - Roda LOCAL, nao consome tokens; 1a execucao baixa o modelo (~GB); ~1-3 min
      por pagina em GPU de 12 GB. Livro grande = deixe rodando (ex: overnight).
    - A revisao do modelo e PINADA (trust_remote_code executa codigo do repo HF;
      o pin evita rodar codigo novo sem revisao).
    - Downside conhecido do motor VLM: erro "plausivel" em scan ilegivel
      (alucinacao). A imagem de cada pagina fica em livro/.paginas/ como rede
      de seguranca de fidelidade (G2).
"""

import argparse
import re
import sys
from pathlib import Path

# Reusa contrato e utilitarios do motor docling (mesma pasta).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from converte_livro import _run_markdownlint, chapter_filename, sanitize_slug  # noqa: E402

MODEL_ID = "baidu/Unlimited-OCR"
MODEL_REVISION = "ee63731b6461c8afcdcc7b15352e7d2ffecc2ead"  # pin (supply chain)
DEFAULT_CUT = r"(?i)^(chapter|cap[ií]tulo|ap[eê]ndice)\b"

_DET_RE = re.compile(r"<\|det\|>(\w+) \[[\d, ]+\]<\|/det\|>", re.S)
_SKIP_TYPES = {"header", "footer", "page_number"}
# Loop degenerado do VLM: runs de `\\ \text {   }` repetidos ate o max_length.
_DEGENERATE_RUN_RE = re.compile(r"(?:\\\\\s*\\text\s*\{\s*\}\s*){3,}")
_DEGENERATE_LEN = 30_000  # chars; pagina normal fica em 2-6k


def _looks_degenerate(raw: str) -> bool:
    return len(raw) > _DEGENERATE_LEN or bool(_DEGENERATE_RUN_RE.search(raw))


def _despace_math(latex: str) -> str:
    """Colapsa o artefato de digitos espacados do modelo ("1. 3 4 9 9")."""
    prev = None
    while prev != latex:
        prev = latex
        latex = re.sub(r"(?<=\d) (?=\d)", "", latex)
        latex = re.sub(r"(?<=\d)\. (?=\d)", ".", latex)
        latex = re.sub(r"(?<=\d), (?=\d)", ",", latex)
    return latex


def parse_det_page(raw: str) -> str:
    """Blocos `<|det|>tipo [coords]<|/det|>conteudo` -> markdown limpo (puro).

    title -> `## `, equation -> bloco $$ (LaTeX despacado), text -> paragrafo;
    header/footer/page_number sao descartados (a ancora usa a pagina do PDF).
    """
    parts = []
    matches = list(_DET_RE.finditer(raw))
    for i, m in enumerate(matches):
        kind = m.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        content = raw[m.end():end].strip()
        if not content or kind in _SKIP_TYPES:
            continue
        if kind == "title":
            parts.append(f"## {content}")
        elif kind == "equation":
            latex = _DEGENERATE_RUN_RE.sub(" ", content)
            if latex.startswith("\\["):
                latex = latex[2:]
            if latex.endswith("\\]"):
                latex = latex[:-2]
            parts.append(f"$$\n{_despace_math(latex.strip())}\n$$")
        else:  # text, table, figure e afins: preserva como paragrafo
            parts.append(content)
    return "\n\n".join(parts)


def _parse_pages_arg(spec: str, total: int):
    if not spec:
        return range(1, total + 1)
    a, _, b = spec.partition("-")
    return range(int(a), min(int(b or a), total) + 1)


def convert(pdf_path: Path, out_dir: Path, pages_spec: str, dpi: int,
            cut_regex: str, crop: bool = False):
    import fitz  # pymupdf
    import torch
    from transformers import AutoModel, AutoTokenizer

    cut = re.compile(cut_regex)
    pages_dir = out_dir / ".paginas"
    pages_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    page_nums = list(_parse_pages_arg(pages_spec, len(doc)))
    print(f"[*] {len(page_nums)} pagina(s) a converter (VLM local, sem tokens; "
          "1a execucao baixa o modelo)...")

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID, revision=MODEL_REVISION, trust_remote_code=True
    )
    model = (
        AutoModel.from_pretrained(
            MODEL_ID, revision=MODEL_REVISION, trust_remote_code=True,
            torch_dtype=torch.bfloat16,
        )
        .eval()
        .cuda()
    )

    import io
    from contextlib import redirect_stdout

    chapters = []  # [{"title", "start_page", "body": [md, ...]}]
    for n in page_nums:
        pix = doc[n - 1].get_pixmap(dpi=dpi)
        img = pages_dir / f"page-{n:04d}.png"
        pix.save(img)

        def _infer(**extra):
            buf = io.StringIO()
            with redirect_stdout(buf):
                res = model.infer(
                    tokenizer,
                    prompt="<image>document parsing.",
                    image_file=str(img),
                    output_path=str(pages_dir / "tmp"),
                    base_size=1024,
                    image_size=640 if crop else 1024,
                    crop_mode=crop,
                    # pagina normal gera 1-2k tokens; o teto curto faz pagina
                    # degenerada falhar em minutos, nao em dezenas de minutos
                    max_length=8192,
                    **extra,
                )
            return res if isinstance(res, str) else buf.getvalue()

        # cache incremental: corrida longa e resumivel (re-rodar pula o ja feito)
        cache = pages_dir / f"page-{n:04d}.md"
        if cache.is_file():
            raw = cache.read_text(encoding="utf-8")
        else:
            raw = _infer()
            if _looks_degenerate(raw):
                # loop de repeticao do VLM: re-tenta com anti-repeticao de n-grams
                print(f"    [!] pagina {n} degenerou; re-tentando com anti-repeticao...")
                raw = _infer(no_repeat_ngram_size=30, ngram_window=120)
            cache.write_text(raw, encoding="utf-8")
        if _looks_degenerate(raw):
            # desiste da pagina: registra e aponta a imagem (rede de seguranca G2)
            md = (f"> **[extração degenerou nesta página; consulte a imagem "
                  f"`.paginas/{img.name}`]**")
        else:
            md = parse_det_page(raw)

        # fronteira de capitulo: 1o title da pagina casa com o cut-regex
        first_title = next(
            (l[3:] for l in md.splitlines() if l.startswith("## ")), None
        )
        if not chapters or (first_title and cut.match(first_title)):
            chapters.append(
                {"title": first_title or f"pagina {n}", "start_page": n, "body": []}
            )
        chapters[-1]["body"].append(f"<!-- page: {n} -->\n\n{md}")
        print(f"    -> pagina {n} OK ({len(md)} chars)")

    doc.close()
    return chapters


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pdf", help="caminho do PDF do livro")
    parser.add_argument("--slug", required=True, help="slug do projeto (kebab-case)")
    parser.add_argument("--out", default=None, help="saida (default: .projetos/<slug>/livro/)")
    parser.add_argument("--pages", default="", help="intervalo 1-indexado, ex: 40-80")
    parser.add_argument("--dpi", type=int, default=150)
    parser.add_argument("--cut-regex", default=DEFAULT_CUT,
                        help="regex de titulo que abre capitulo novo")
    parser.add_argument("--crop", action="store_true",
                        help="liga o crop mode do modelo (~2x mais lento; "
                             "tente se alguma pagina sair ruim no default)")
    args = parser.parse_args()

    slug = sanitize_slug(args.slug)
    pdf_path = Path(args.pdf)
    if not pdf_path.is_file():
        sys.exit(f"PDF nao encontrado: {pdf_path}")
    out_dir = Path(args.out) if args.out else Path(".projetos") / slug / "livro"
    out_dir.mkdir(parents=True, exist_ok=True)

    chapters = convert(pdf_path, out_dir, args.pages, args.dpi, args.cut_regex,
                       crop=args.crop)

    total = len(chapters)
    for i, ch in enumerate(chapters, 1):
        write_path = out_dir / chapter_filename(i, ch["title"])
        body = "\n\n".join(ch["body"])
        write_path.write_text(f"# {ch['title']}\n\n{body}\n", encoding="utf-8")
        print(f"    -> capitulo {i}/{total} (pagina {ch['start_page']})")
        _run_markdownlint(write_path)
    print(f"OK: {out_dir} ({total} capitulos)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
