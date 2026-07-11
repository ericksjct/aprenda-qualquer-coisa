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
    monkeypatch.setattr(
        cl, "convert_pdf", lambda *args, **kwargs: synthetic_doc
    )

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


# --- Fase 07.1 Fatia 1: item FORMULA vira bloco de display math -------------

def test_formula_rendered_as_math_block():
    from tests.conftest import make_item

    chapter = {
        "title": "Juros",
        "start_page": 47,
        "items": [
            make_item("SECTION_HEADER", level=1, text="Juros", page_no=47),
            make_item("TEXT", text="A taxa continua e dada por:", page_no=47),
            make_item("FORMULA", text=r"I = \ln(1+i)", page_no=47),
        ],
    }
    rendered = cl.render_chapter(chapter)
    assert "$$\nI = \\ln(1+i)\n$$" in rendered
    # Formula sem texto (enriquecimento desligado) segue descartada, sem lixo.
    chapter["items"][2] = make_item("FORMULA", text="", page_no=47)
    assert "$$" not in cl.render_chapter(chapter)


# --- D-08 / ASVS V5: slug path-safety -------------------------------------

def test_slug_rejected():
    with pytest.raises(SystemExit):
        cl.sanitize_slug("../etc")
    with pytest.raises(SystemExit):
        cl.sanitize_slug("a/b")
    with pytest.raises(SystemExit):
        cl.sanitize_slug("a\\b")
    assert cl.sanitize_slug("meu-livro") == "meu-livro"


# --- D-12: chunking em lotes (anti std::bad_alloc) -------------------------

def test_page_batches_basic():
    # 32 paginas, lotes de 15 -> [(1,15), (16,30), (31,32)]
    assert cl._page_batches(32, 15) == [(1, 15), (16, 30), (31, 32)]


def test_page_batches_exact_multiple():
    # 30 paginas, lotes de 15 -> exatamente 2 lotes, sem lote vazio/residual.
    assert cl._page_batches(30, 15) == [(1, 15), (16, 30)]


def test_page_batches_single_batch_when_smaller_than_size():
    # Livro menor que o batch_size cabe em 1 lote so.
    assert cl._page_batches(5, 15) == [(1, 5)]


def test_page_batches_zero_pages():
    assert cl._page_batches(0, 15) == []


def test_page_batches_invalid_batch_size_falls_back_to_default():
    # batch_size <= 0 nao deve gerar loop infinito nem lote invertido;
    # cai no DEFAULT_BATCH_SIZE.
    batches = cl._page_batches(20, 0)
    assert batches == cl._page_batches(20, cl.DEFAULT_BATCH_SIZE)


def test_page_batches_never_uses_single_page_batches():
    # Pitfall 1: nunca gerar lotes de 1 pagina por causa do batch_size default.
    batches = cl._page_batches(100)
    assert all((end - start) >= 1 for start, end in batches[:-1])


def test_chained_doc_concatenates_items_in_order():
    # _ChainedDoc encadeia iterate_items() de cada lote, preservando a ordem
    # (capitulo pode atravessar fronteira de lote sem se quebrar).
    from tests.conftest import make_item

    doc_a = type(
        "FakeDoc",
        (),
        {"iterate_items": lambda self: iter([(make_item(text="a1"), 0)])},
    )()
    doc_b = type(
        "FakeDoc",
        (),
        {"iterate_items": lambda self: iter([(make_item(text="b1"), 0)])},
    )()
    chained = cl._ChainedDoc([doc_a, doc_b])
    texts = [item.text for item, _ in chained.iterate_items()]
    assert texts == ["a1", "b1"]


def test_split_into_chapters_across_chained_batches(synthetic_doc):
    # O documento sintetico (4 itens / 2 capitulos) e dividido artificialmente
    # em 2 "lotes" (2 itens cada) e encadeado via _ChainedDoc; o split
    # deterministico deve produzir o MESMO resultado que rodar sobre o doc
    # inteiro de uma vez - prova que chunking nao quebra D-09 nem D-10.
    items = list(synthetic_doc.iterate_items())
    half = len(items) // 2

    class _BatchDoc:
        def __init__(self, batch_items):
            self._batch_items = batch_items

        def iterate_items(self):
            return iter(self._batch_items)

    chained = cl._ChainedDoc([_BatchDoc(items[:half]), _BatchDoc(items[half:])])

    expected = cl.split_into_chapters(synthetic_doc, cut_level=1)
    actual = cl.split_into_chapters(chained, cut_level=1)

    assert len(actual) == len(expected) == 2
    assert [c["title"] for c in actual] == [c["title"] for c in expected]
    assert [c["start_page"] for c in actual] == [c["start_page"] for c in expected]
    rendered_actual = cl.render_chapter(actual[1])
    assert "<!-- page: 4 -->" in rendered_actual
    assert "função código" in rendered_actual


def test_convert_pdf_batches_via_page_range(tmp_path, monkeypatch):
    # convert_pdf deve: (1) contar paginas via pypdf.PdfReader, (2) chamar
    # converter.convert(pdf_path, page_range=(s,e)) uma vez por lote, (3)
    # chamar gc.collect() apos cada lote, e (4) retornar um doc cujo
    # iterate_items() encadeia os resultados na ordem dos lotes. Tudo via
    # monkeypatch - nenhum docling real e importado/executado.
    import types

    fake_pdf_module = types.ModuleType("pypdf")

    class _FakeReader:
        def __init__(self, path):
            self.pages = list(range(7))  # 7 paginas sinteticas

    fake_pdf_module.PdfReader = _FakeReader
    monkeypatch.setitem(sys.modules, "pypdf", fake_pdf_module)

    calls = []

    class _FakeBatchDoc:
        """Stand-in de DoclingDocument por lote: so expoe iterate_items()."""

        def __init__(self, label):
            self.label = label

        def iterate_items(self):
            return iter([(self.label, 0)])

    class _FakeResult:
        def __init__(self, label):
            self.document = _FakeBatchDoc(label)

    class _FakeConverter:
        def __init__(self, format_options=None):
            pass

        def convert(self, pdf_path, page_range=None):
            calls.append(page_range)
            return _FakeResult(label=f"doc-{page_range}")

    fake_accel_module = types.ModuleType("docling.datamodel.accelerator_options")
    fake_accel_module.AcceleratorDevice = types.SimpleNamespace(CPU="cpu")
    fake_accel_module.AcceleratorOptions = lambda **kwargs: kwargs

    fake_base_models_module = types.ModuleType("docling.datamodel.base_models")
    fake_base_models_module.InputFormat = types.SimpleNamespace(PDF="pdf")

    fake_pipeline_options_module = types.ModuleType(
        "docling.datamodel.pipeline_options"
    )
    fake_pipeline_options_module.PdfPipelineOptions = lambda: types.SimpleNamespace()

    fake_document_converter_module = types.ModuleType("docling.document_converter")
    fake_document_converter_module.DocumentConverter = _FakeConverter
    fake_document_converter_module.PdfFormatOption = lambda **kwargs: kwargs

    monkeypatch.setitem(
        sys.modules,
        "docling.datamodel.accelerator_options",
        fake_accel_module,
    )
    monkeypatch.setitem(
        sys.modules, "docling.datamodel.base_models", fake_base_models_module
    )
    monkeypatch.setitem(
        sys.modules,
        "docling.datamodel.pipeline_options",
        fake_pipeline_options_module,
    )
    monkeypatch.setitem(
        sys.modules, "docling.document_converter", fake_document_converter_module
    )

    gc_calls = []
    monkeypatch.setattr(cl.gc, "collect", lambda: gc_calls.append(True))

    fake_pdf = tmp_path / "livro.pdf"
    fake_pdf.write_bytes(b"%PDF-1.4 stub")

    doc = cl.convert_pdf(fake_pdf, cut_level=1, batch_size=3)

    # 7 paginas / lotes de 3 -> (1,3), (4,6), (7,7)
    assert calls == [(1, 3), (4, 6), (7, 7)]
    assert len(gc_calls) == 3  # gc.collect() uma vez por lote
    chained_labels = [item for item, _ in doc.iterate_items()]
    assert chained_labels == ["doc-(1, 3)", "doc-(4, 6)", "doc-(7, 7)"]


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
