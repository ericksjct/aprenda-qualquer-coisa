"""Testes do parser puro do motor VLM (sem GPU/modelo: so texto -> markdown)."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from converte_livro_vlm import _despace_math, parse_det_page  # noqa: E402

RAW = (
    "<|det|>page_number [166, 69, 201, 84]<|/det|>286\n"
    "<|det|>header [759, 69, 878, 84]<|/det|>CHAPTER 13\n"
    "<|det|>title [165, 256, 573, 274]<|/det|>13.8 THE BINOMIAL TREE FORMULAS\n"
    "<|det|>text [225, 293, 880, 327]<|/det|>we should match volatility by setting\n"
    "<|det|>equation [512, 339, 880, 360]<|/det|>\\[\n"
    "u = e ^ {\\sigma \\sqrt {\\Delta t}} \\tag {13.15}\n\\]\n"
    "<|det|>equation [130, 89, 262, 104]<|/det|>\\[\nF V = 1. 2 1 0, 0 0\n\\]\n"
)


def test_despace_math():
    assert _despace_math("1. 3 4 9 9") == "1.3499"
    assert _despace_math("1. 2 1 0, 0 0") == "1.210,00"
    assert _despace_math(r"e ^ {0. 3 \times 1} = 1. 3 4 9 9") == r"e ^ {0.3 \times 1} = 1.3499"


def test_degenerate_run_collapsed_and_detected():
    from converte_livro_vlm import _looks_degenerate

    run = "\\\\ \\text {   } " * 500
    raw = f"<|det|>equation [1, 2, 3, 4]<|/det|>\\[\nFV = 1.210,00 {run}\n\\]\n"
    assert _looks_degenerate(raw)
    md = parse_det_page(raw)
    assert "FV = 1.210,00" in md
    assert "\\text {   } \\\\ \\text" not in md
    assert not _looks_degenerate("<|det|>text [1, 2, 3, 4]<|/det|>pagina normal")


def test_parse_det_page():
    md = parse_det_page(RAW)
    assert "## 13.8 THE BINOMIAL TREE FORMULAS" in md
    assert "$$\nu = e ^ {\\sigma \\sqrt {\\Delta t}} \\tag {13.15}\n$$" in md
    assert "$$\nF V = 1.210,00\n$$" in md
    # header e page_number sao descartados (a ancora usa a pagina do PDF)
    assert "CHAPTER 13" not in md
    assert "286" not in md
