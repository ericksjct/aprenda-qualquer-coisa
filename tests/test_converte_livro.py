"""Suite de logica para scripts/converte_livro.py (deterministica, sem docling).

Os helpers puros sao importados diretamente; o modulo NAO importa docling no
nivel de modulo, entao esta suite roda sub-segundo sem o pipeline pesado.
"""

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts import converte_livro as cl  # noqa: E402


# --- D-09: split deterministico por heading -------------------------------

def test_split_by_heading(synthetic_doc):
    chapters = cl.split_into_chapters(synthetic_doc, cut_level=1)
    # Um novo capitulo comeca em cada fronteira (TITLE, SECTION_HEADER<=cut).
    assert chapters[0]["title"] == "Capitulo 1"
    assert chapters[1]["title"] == "Secao A"
    # Itens nao-heading caem no capitulo corrente.
    titles_cap1 = [it.text for it in chapters[0]["items"]]
    assert "corpo do cap 1" in titles_cap1
    assert "corpo do cap 1" not in [it.text for it in chapters[1]["items"]]


def test_chapter_count(synthetic_doc):
    chapters = cl.split_into_chapters(synthetic_doc, cut_level=1)
    assert len(chapters) == 2


# --- D-10: ancora de pagina ------------------------------------------------

def test_page_anchor_present(synthetic_doc):
    chapters = cl.split_into_chapters(synthetic_doc, cut_level=1)
    rendered = cl.render_chapter(chapters[0])
    assert "<!-- page:" in rendered


def test_page_anchor_value(synthetic_doc):
    chapters = cl.split_into_chapters(synthetic_doc, cut_level=1)
    # start_page do capitulo == prov[0].page_no do seu item de fronteira.
    assert chapters[0]["start_page"] == 1
    assert chapters[1]["start_page"] == 4
    rendered = cl.render_chapter(chapters[1])
    assert "<!-- page: 4 -->" in rendered


# --- D-15: acentos preservados --------------------------------------------

def test_accents_preserved(synthetic_doc):
    chapters = cl.split_into_chapters(synthetic_doc, cut_level=1)
    rendered = cl.render_chapter(chapters[1])
    assert "função código" in rendered


# --- D-08 / ASVS V5: slug path-safety -------------------------------------

def test_slug_rejected():
    with pytest.raises(SystemExit):
        cl.sanitize_slug("../etc")
    with pytest.raises(SystemExit):
        cl.sanitize_slug("a/b")
    with pytest.raises(SystemExit):
        cl.sanitize_slug("a\\b")
    assert cl.sanitize_slug("meu-livro") == "meu-livro"
