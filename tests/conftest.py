"""Fixtures de teste para scripts/converte_livro.py.

Constroi um DoclingDocument SINTETICO em memoria para exercitar a logica de
split/anchor SEM rodar o pipeline pesado do docling (OCR/torch/HF). Os helpers
testados sao puros e nao importam docling no nivel de modulo; aqui montamos
itens minimos que expoem o subconjunto de atributos que os helpers leem:
.label (com .name), .level, .text e .prov (lista cujo [0] tem .page_no).

Tambem registra o marker `slow` e um helper de skip-if-docling-missing para o
golden smoke (tests/fixtures/sample.pdf).
"""

import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

# Garante que `import scripts.converte_livro` funcione a partir da raiz do repo.
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _label(name):
    """Sentinela de label que expoe `.name` (igual a DocItemLabel.<NAME>.name).

    Os helpers comparam por `.name`, entao funciona tanto com este sentinela
    quanto com o DocItemLabel real do docling-core.
    """
    return SimpleNamespace(name=name)


def _prov(page_no):
    return [SimpleNamespace(page_no=page_no)]


def make_item(label_name=None, level=None, text="", page_no=None):
    """Constroi um item sintetico no formato que os helpers leem."""
    item = SimpleNamespace(text=text)
    if label_name is not None:
        item.label = _label(label_name)
    if level is not None:
        item.level = level
    if page_no is not None:
        item.prov = _prov(page_no)
    return item


class SyntheticDoc:
    """Stand-in de DoclingDocument: expoe apenas iterate_items()."""

    def __init__(self, items):
        self._items = items

    def iterate_items(self):
        # docling yields (item, level_int); o segundo valor e ignorado pelos helpers.
        for it in self._items:
            yield it, 0


@pytest.fixture
def synthetic_doc():
    """Documento sintetico: 2 headings de fronteira (cut_level=1) => 2 capitulos.

    Layout:
      TITLE          "Capitulo 1"            pagina 1
      paragrafo      "corpo do cap 1"        pagina 1
      SECTION_HEADER "Secao A" (level 1)     pagina 4
      paragrafo      "funcao codigo"         pagina 4  (acentos preservados)
    """
    items = [
        make_item("TITLE", level=1, text="Capitulo 1", page_no=1),
        make_item(None, text="corpo do cap 1", page_no=1),
        make_item("SECTION_HEADER", level=1, text="Secao A", page_no=4),
        make_item(None, text="função código", page_no=4),
    ]
    return SyntheticDoc(items)


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "slow: testes que exigem o pipeline docling (golden smoke); pulam se docling ausente",
    )
