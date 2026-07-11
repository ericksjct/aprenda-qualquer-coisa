"""Testes das funcoes puras do indice do livro (sem modelo/GPU)."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from consulta_livro import _fts_query, chunk_sections, parse_livro_md  # noqa: E402

MD = (
    "# Capítulo 2\n\n"
    "<!-- page: 40 -->\n\n"
    "## 2.2 Taxas equivalentes\n\n"
    "Duas taxas são equivalentes quando produzem o mesmo montante.\n\n"
    "$$\ni_q = (1 + i)^{q} - 1\n$$\n\n"
    "<!-- page: 41 -->\n\n"
    "## 2.3 Taxa nominal\n\n"
    "A taxa nominal difere da efetiva.\n"
)


def test_parse_sections_with_pages():
    sections = parse_livro_md(MD, "02-cap.md")
    titles = [(s["section"], s["page"]) for s in sections]
    assert ("2.2 Taxas equivalentes", 40) in titles
    assert ("2.3 Taxa nominal", 41) in titles
    eq_section = next(s for s in sections if s["section"].startswith("2.2"))
    assert "i_q = (1 + i)^{q} - 1" in eq_section["text"]


def test_chunk_overlap_and_parent():
    sections = [{"file": "f.md", "section": "s", "page": 7, "text": "x" * 3000}]
    chunks = chunk_sections(sections, size=1200, overlap=200)
    assert len(chunks) == 3
    assert all(c["page"] == 7 and c["parent"] == "x" * 3000 for c in chunks)
    # overlap: o inicio do chunk 2 repete o fim do chunk 1
    assert chunks[0]["text"][-200:] == chunks[1]["text"][:200]


def test_fts_query_sanitized():
    assert _fts_query('taxa "over" (efetiva)') == '"taxa" OR "over" OR "efetiva"'


def test_breadcrumbs_hierarchy():
    from consulta_livro import add_breadcrumbs

    def sec(title):
        return {"file": "f.md", "section": title, "page": 1, "text": "t"}

    sections = add_breadcrumbs([
        sec("3 Descontos, 53"),          # linha de sumario semeia o capitulo
        sec("3.5 Desconto composto"),
        sec("3.5.2 Desconto composto por dentro"),
        sec("Solução"),                   # sem numero: herda o pai numerado
        sec("Apresentação"),              # sem numero e sem pai... herda tb
    ])
    crumbs = [s["crumb"] for s in sections]
    assert crumbs[0] == "3 Descontos"     # ", 53" descartado
    assert crumbs[2] == ("3 Descontos > 3.5 Desconto composto > "
                         "3.5.2 Desconto composto por dentro")
    assert crumbs[3] == ("3 Descontos > 3.5 Desconto composto > "
                         "3.5.2 Desconto composto por dentro > Solução")


def test_breadcrumb_without_any_number():
    from consulta_livro import add_breadcrumbs

    sections = add_breadcrumbs(
        [{"file": "f.md", "section": "Apresentação", "page": 1, "text": "t"}]
    )
    assert sections[0]["crumb"] == "Apresentação"
