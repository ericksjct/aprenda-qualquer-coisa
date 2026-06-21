---
phase: 7
slug: ingestao-pdf-livro-via-docling
status: draft
nyquist_compliant: true
wave_0_complete: false
created: 2026-06-21
---

# Phase 7 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.
> The verifiable contract is **deterministic conversion output** (split + page anchor),
> testable without an LLM. docling is heavy/opt-in, so tests split into (a) pure-logic
> tests on the split/anchor functions over a synthetic in-memory `DoclingDocument`, and
> (b) one opt-in golden-file smoke on a tiny sample PDF (skipped when docling is absent).

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest (none currently in repo — introduced for this opt-in script ONLY; stdlib core stays test-free) |
| **Config file** | none — Wave 0 installs pytest into the opt-in PDF venv |
| **Quick run command** | `python -m pytest tests/test_converte_livro.py -x -q` |
| **Full suite command** | `python -m pytest tests/ -q` (includes `@pytest.mark.slow` golden-PDF smoke) |
| **Estimated runtime** | ~1 second (logic tests; golden smoke is slow/opt-in) |

---

## Sampling Rate

- **After every task commit:** Run `python -m pytest tests/test_converte_livro.py -x -q` (logic only, sub-second)
- **After every plan wave:** Run full suite incl. `-m slow` golden PDF (once, where the docling venv exists)
- **Before `/gsd-verify-work`:** Logic suite green + one successful golden-PDF smoke + `sh scripts/check-consistencia.sh` exit 0 for any `mentor/`/adapter edits
- **Max feedback latency:** ~1 second for the logic suite

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| split-by-heading | 07-01 | 1 | D-09 | — | N/A | unit | `pytest tests/test_converte_livro.py::test_split_by_heading -x` | ❌ W0 | ⬜ pending |
| chapter-count | 07-01 | 1 | D-09 | — | N/A | unit | `pytest tests/test_converte_livro.py::test_chapter_count -x` | ❌ W0 | ⬜ pending |
| page-anchor-present | 07-01 | 1 | D-10 | — | N/A | unit | `pytest tests/test_converte_livro.py::test_page_anchor_present -x` | ❌ W0 | ⬜ pending |
| page-anchor-value | 07-01 | 1 | D-10 | — | N/A | unit | `pytest tests/test_converte_livro.py::test_page_anchor_value -x` | ❌ W0 | ⬜ pending |
| env-guards | 07-01 | 1 | D-12 | — | N/A | unit | `pytest tests/test_converte_livro.py::test_env_guards -x` | ❌ W0 | ⬜ pending |
| lint-called | 07-01 | 1 | D-12 | — | N/A | unit | `pytest tests/test_converte_livro.py::test_lint_called -x` | ❌ W0 | ⬜ pending |
| accents-preserved | 07-01 | 1 | D-15 | — | N/A | unit | `pytest tests/test_converte_livro.py::test_accents_preserved -x` | ❌ W0 | ⬜ pending |
| slug-path-safety | 07-01 | 1 | D-08 / V5 | path-traversal via `--slug` | reject `..`/separators, whitelist `[a-z0-9-]` | unit | `pytest tests/test_converte_livro.py::test_slug_rejected -x` | ❌ W0 | ⬜ pending |
| golden-smoke | 07-01 | 1 | D-09+D-10 | — | N/A | slow/manual | `pytest tests/ -m slow -q` (skips if docling not installed) | ❌ W0 | ⬜ pending |
| harness-reconcile | 07-02 | 2 | D-13 | — | N/A | existing harness | `sh scripts/check-consistencia.sh` | ✅ | ⬜ pending |
| skill-adapter | 07-02 | 2 | D-13/D-14 | — | N/A | existing harness | `sh scripts/check-consistencia.sh` | ✅ | ⬜ pending |
| novo-projeto-bootstrap | 07-02 | 2 | D-02/D-06/D-15 | — | N/A | existing harness | `sh scripts/check-consistencia.sh` | ✅ | ⬜ pending |
| agents-readme-metodo | 07-02 | 2 | D-02/D-13 | — | N/A | existing harness (V-15 set-equality) | `sh scripts/check-consistencia.sh` | ✅ | ⬜ pending |
| reference-livro-divergencia | 07-03 | 3 | D-04/D-08 | — | N/A | existing harness + grep | `sh scripts/check-consistencia.sh && grep -q "o livro diz" mentor/reference.md && grep -q "escolha do mentor" mentor/reference.md` | ✅ | ⬜ pending |
| tutor-baseline-divergencia | 07-03 | 3 | D-01/D-03/D-04/D-10 | — | N/A | existing harness + grep | `sh scripts/check-consistencia.sh && grep -q "decide sozinho" mentor/tutor.md && grep -q "APRENDIZADO.md" mentor/tutor.md` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

> Plan/Wave mapping: 07-01 (Wave 1, the docling engine + pytest scaffolding), 07-02 (Wave 2, harness
> reconciliation + skill/AGENTS/README/metodo registration + novo-projeto bootstrap), 07-03 (Wave 3,
> reference.md + tutor.md consumption layer; depends on 07-02 so the harness is reconciled first).

---

## Wave 0 Requirements

- [ ] `tests/test_converte_livro.py` — unit tests over split/anchor/env/lint/accents/slug using a synthetic `DoclingDocument` (build minimal items in-memory; no pipeline run)
- [ ] `tests/conftest.py` — fixture building the synthetic document + `@pytest.mark.slow` skip-if-docling-missing
- [ ] `tests/fixtures/sample.pdf` — tiny 2-3 page PDF with 2 headings for the golden smoke
- [ ] Framework install: `pip install pytest` into the opt-in PDF venv (NOT into the stdlib core)
- [ ] Keep tests OUT of the stdlib-only core's "zero setup" promise — they live with the opt-in script and run only when the PDF venv exists

> Wave 0 scaffolding lives in Plan 07-01 Task 3 (requirements-pdf.txt + tests/conftest.py +
> tests/test_converte_livro.py + tests/fixtures/sample.pdf). Every MISSING-referenced test in the
> Per-Task map above is created there before any 07-01 logic assertion runs — the strategy is
> nyquist-compliant; `wave_0_complete` flips to true only after execution actually runs Wave 0.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Whole-book convert fits memory with threads=1 | A2 (research) | Depends on the student's real book size; synthetic tests cannot exercise docling's OCR memory | Run the CLI on the actual book PDF once; if `std::bad_alloc`/OOM, fall back to `page_range` batches (10-20 pages) |
| docling produces real `SECTION_HEADER` items (not flat text) | A1 (research) | Depends on whether the book PDF is born-digital/OCR-able | Run `--cut-level` histogram on the real book; if 1 giant file or >50 tiny files, adjust cut level |
| Agent pre-warning surfaced before firing the script | D-14 | LLM-side behavior in `mentor/`; verified by reading the produced method text | Inspect that `mentor/novo-projeto.md` + the skill instruct "demora / 0 tokens / progresso" before invoking |

---

## Validation Sign-Off

- [x] All tasks have automated verify or Wave 0 dependencies
- [x] Sampling continuity: no 3 consecutive tasks without automated verify
- [x] Wave 0 covers all MISSING references (synthetic-document fixture + pytest install) — provided by 07-01 Task 3
- [x] No watch-mode flags
- [x] Feedback latency < ~1s for the logic suite
- [x] `nyquist_compliant: true` set in frontmatter

**Approval:** 2026-06-21
