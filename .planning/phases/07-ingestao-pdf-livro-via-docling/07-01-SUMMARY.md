---
phase: 07-ingestao-pdf-livro-via-docling
plan: 01
subsystem: testing
tags: [docling, pypdf, pytest, pdf, markdown, cli, python]

# Dependency graph
requires: []
provides:
  - "scripts/converte_livro.py: opt-in docling CLI (whole-doc convert, deterministic chapter split, page anchors, pure importable helpers)"
  - "FIXED CLI signature for Wave 2 docs to cite"
  - "requirements-pdf.txt: isolated opt-in deps (docling+pypdf+pytest), core stays stdlib-only"
  - "pytest logic suite (split/anchor/env/lint/accents/slug) + golden smoke + sample.pdf fixture"
affects: [07-02, 07-03, novo-projeto, tutor, reference, skill-converte-livro]

# Tech tracking
tech-stack:
  added: [docling, pypdf, pytest, markdownlint-cli]
  patterns:
    - "Lazy docling import inside functions so pure helpers + tests import without the heavy dep"
    - "Synthetic DoclingDocument fixture (SimpleNamespace) for sub-second logic tests"
    - "ASCII filename / accent-preserving content split"

key-files:
  created:
    - scripts/converte_livro.py
    - requirements-pdf.txt
    - tests/conftest.py
    - tests/test_converte_livro.py
    - tests/fixtures/sample.pdf
  modified:
    - .gitignore

key-decisions:
  - "Labels compared by .name so the same helper works with real DocItemLabel or a test sentinel"
  - "convert_pdf + main() landed in the same module as the pure helpers (one file) — imports stay lazy so logic tests need no docling"
  - "Hand-built sample.pdf (no PDF-author lib available in env) — valid 2-page PDF with 2 headings"

patterns-established:
  - "Opt-in third-party dep isolated in requirements-pdf.txt + dedicated venv; core remains 100% stdlib"
  - "Deterministic split via doc.iterate_items() on TITLE/SECTION_HEADER<=cut_level; page anchor from prov[0].page_no"

requirements-completed: [D-05, D-07, D-08, D-09, D-10, D-11, D-12]

# Metrics
duration: 7min
completed: 2026-06-22
---

# Phase 07 Plan 01: Motor de conversao deterministica (docling) Summary

**CLI opt-in `scripts/converte_livro.py` que converte um PDF de livro inteiro em UM passe docling, divide deterministicamente por TITLE/SECTION_HEADER e grava um .md por capitulo (acentos preservados) com ancora `<!-- page: N -->`, mais a suite pytest que prova split/anchor/env/lint/acentos/slug sobre um DoclingDocument sintetico.**

## FINAL CLI Signature (cite verbatim in Wave 2)

```bash
# Ative o venv opt-in primeiro (Windows PowerShell):
#   python -m venv .venv-pdf
#   .\.venv-pdf\Scripts\activate
#   pip install -r requirements-pdf.txt
#   npm install -g markdownlint-cli
python scripts/converte_livro.py <pdf> --slug <slug> [--out <dir>] [--cut-level N]
#   default --out       = .projetos/<slug>/livro/
#   default --cut-level = 1
```

Page anchor format (each chapter file starts with): `<!-- page: N -->`

## Performance

- **Duration:** ~7 min
- **Started:** 2026-06-22T22:24:20Z
- **Completed:** 2026-06-22T22:31:05Z
- **Tasks:** 3 (Task 1 via TDD)
- **Files modified:** 6 (5 created, 1 modified)

## Accomplishments
- Deterministic chapter split + page-anchor engine driven from docling's structured model (replaces the base script's pypdf 1-page chunking that destroyed both signals).
- Pure, docling-free importable helpers (`sanitize_slug`, `_page_of`, `split_into_chapters`, `render_chapter`, `chapter_filename`, `heading_histogram`) with memory env guards set before any docling import.
- Full logic suite green sub-second; the slow golden smoke actually RAN end-to-end against a real docling pipeline (docling present in this env) and passed.
- Path-traversal mitigation (T-07-01) + literal-list subprocess (T-07-02) implemented and tested.

## Task Commits

1. **Task 1 (RED): failing tests for split/anchor/slug** - `b0e81b1` (test)
2. **Task 1 (GREEN): implement opt-in docling CLI core** - `8d88a80` (feat)
3. **Task 2: env-guard + markdownlint --fix wiring tests** - `b617cef` (test)
4. **Task 3: deps manifest, golden smoke + sample.pdf fixture** - `2b4254b` (test)

_Task 2's `convert_pdf`/`main()` implementation shipped inside Task 1's GREEN commit (same module, lazy imports); Task 2's commit adds its verifying tests._

## Files Created/Modified
- `scripts/converte_livro.py` - Opt-in docling CLI: whole-doc convert, deterministic split, page anchors, pure helpers, markdownlint --fix with graceful skip.
- `requirements-pdf.txt` - Isolated opt-in deps (docling+pypdf+pytest); questionary-free; never merged into the stdlib core.
- `tests/conftest.py` - Synthetic DoclingDocument fixture + `slow` marker registration.
- `tests/test_converte_livro.py` - 8 logic tests + 1 golden smoke (1:1 with 07-VALIDATION map).
- `tests/fixtures/sample.pdf` - Hand-built 2-page PDF (2 headings) for the golden smoke.
- `.gitignore` - Ignore `__pycache__/`, `.pytest_cache/`, `.venv-pdf/`.

## Decisions Made
- Helpers compare label by `.name` (not identity) so the same code path serves the real `DocItemLabel` and the test sentinel — keeps the module importable without `docling`.
- `convert_pdf` + `main()` live in the same module as the pure helpers; all docling imports are lazy (inside functions) so `import scripts.converte_livro` and every logic test work with docling absent.
- `sample.pdf` was hand-authored (raw PDF bytes with computed xref) because no PDF-writing lib (reportlab/fpdf) is installed; validated with pypdf (2 pages, both heading texts extractable).

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Test file missing `import os`**
- **Found during:** Task 2 (test_env_guards)
- **Issue:** `test_env_guards` referenced `os.environ` but the test module didn't import `os` (NameError on collection/run).
- **Fix:** Added `import os` to `tests/test_converte_livro.py`.
- **Verification:** `test_env_guards` + `test_lint_called` pass.
- **Committed in:** `b617cef` (Task 2 commit)

**2. [Rule 3 - Blocking] Generated artifacts untracked / would pollute tree**
- **Found during:** Task 3 (running pytest generated `__pycache__/` and `.pytest_cache/`)
- **Issue:** This plan introduces the first Python tests; the existing `.gitignore` did not ignore Python build artifacts or the opt-in `.venv-pdf/`.
- **Fix:** Appended `__pycache__/`, `*.pyc`, `.pytest_cache/`, `.venv-pdf/` to `.gitignore`.
- **Verification:** `git status` no longer lists generated dirs.
- **Committed in:** `2b4254b` (Task 3 commit)

---

**Total deviations:** 2 auto-fixed (2 blocking)
**Impact on plan:** Both necessary to keep the suite runnable and the tree clean. No scope creep.

## Issues Encountered
- The RTK proxy rewrites bare `python -m pytest` to a filtering wrapper that reported a misleading "No tests collected"; ran the suite via `rtk proxy python -m pytest ...` to get true results. No code impact.
- docling turned out to be importable in this environment, so the `@pytest.mark.slow` golden smoke executed the real OCR pipeline (~30s) and passed — stronger validation than a skip.

## Known Stubs
None. All helpers are wired and exercised by tests; the golden smoke runs the real pipeline.

## Out-of-scope items observed (NOT touched)
- Pre-existing untracked entries present at session start: `--raw`, `.temp/`, `.planning/phases/07-.../.gitkeep`, and pre-modified `.planning/config.json`. Left untouched (not caused by this plan).

## User Setup Required
**Opt-in venv required to actually run the converter** (logic tests do NOT need it):
```
python -m venv .venv-pdf
.\.venv-pdf\Scripts\activate
pip install -r requirements-pdf.txt
npm install -g markdownlint-cli
```

## Next Phase Readiness
- Wave 2 (07-02) can cite the FIXED CLI signature and `<!-- page: N -->` anchor above without re-reading the script.
- Engine, deps manifest, and test suite are in place; harness reconciliation + mentor doc weaving (07-02/07-03) are unblocked.

## Self-Check: PASSED

All 5 deliverable files + SUMMARY exist on disk; all 4 task commits (`b0e81b1`, `8d88a80`, `b617cef`, `2b4254b`) present in git history.

## TDD Gate Compliance

Task 1 (`tdd="true"`) followed RED -> GREEN: `test(07-01)` commit `b0e81b1` (failing tests) precedes `feat(07-01)` commit `8d88a80` (implementation). RED was confirmed failing (ImportError) before GREEN. No REFACTOR commit needed.

---
*Phase: 07-ingestao-pdf-livro-via-docling*
*Completed: 2026-06-22*
