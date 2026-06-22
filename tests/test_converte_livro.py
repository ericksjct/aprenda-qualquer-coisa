"""Suite de logica para scripts/converte_livro.py (deterministica, sem docling).

Os helpers puros sao importados diretamente; o modulo NAO importa docling no
nivel de modulo, entao esta suite roda sub-segundo sem o pipeline pesado.
"""

import os
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts import converte_livro as cl  # noqa: E402


# --- D-12: blindagem de memoria -------------------------------------------

def test_env_guards():
    # Importar o modulo ja deve ter setado os guards de memoria.
    assert os.environ["OMP_NUM_THREADS"] == "1"
    assert os.environ["OPENBLAS_NUM_THREADS"] == "1"
    assert os.environ["MKL_NUM_THREADS"] == "1"


# --- D-12: markdownlint --fix acionado ------------------------------------

def test_lint_called(synthetic_doc, tmp_path, monkeypatch):
    calls = []

    def fake_run(args, **kwargs):
        calls.append(args)
        return None

    monkeypatch.setattr(cl.subprocess, "run", fake_run)
    # Evita rodar docling: convert_pdf retorna o doc sintetico.
    monkeypatch.setattr(cl, "convert_pdf", lambda pdf_path, cut_level: synthetic_doc)

    fake_pdf = tmp_path / "livro.pdf"
    fake_pdf.write_bytes(b"%PDF-1.4 stub")
    out_dir = tmp_path / "out"

    monkeypatch.setattr(
        sys,
        "argv",
        ["converte_livro.py", str(fake_pdf), "--slug", "meu-livro", "--out", str(out_dir)],
    )
    cl.main()

    assert calls, "markdownlint deveria ter sido chamado"
    first = calls[0]
    assert first[0] == "markdownlint"
    assert first[1] == "--fix"
    # Arquivos de capitulo foram escritos.
    written = list(out_dir.glob("*.md"))
    assert written, "deveria ter escrito ao menos um capitulo"
    assert "<!-- page:" in written[0].read_text(encoding="utf-8")


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


# --- golden smoke (opt-in, lento; pula se docling ausente) -----------------

@pytest.mark.slow
def test_golden_smoke(tmp_path):
    pytest.importorskip("docling")
    sample = Path(__file__).resolve().parent / "fixtures" / "sample.pdf"
    if not sample.is_file():
        pytest.skip("tests/fixtures/sample.pdf ausente")
    out_dir = tmp_path / "livro"
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = cl.convert_pdf(sample, 1)
    chapters = cl.split_into_chapters(doc, 1)
    for i, chapter in enumerate(chapters, 1):
        path = out_dir / cl.chapter_filename(i, chapter["title"])
        path.write_text(cl.render_chapter(chapter), encoding="utf-8")
    written = list(out_dir.glob("*.md"))
    assert written, "golden smoke deveria escrever ao menos 1 capitulo"
    assert any("<!-- page:" in p.read_text(encoding="utf-8") for p in written)
