---
phase: 07-ingestao-pdf-livro-via-docling
verified: 2026-06-22T22:51:32Z
status: passed
score: 19/19 must-haves verified
overrides_applied: 0
---

# Phase 07: Ingestao de PDF do livro via docling — Verification Report

**Phase Goal:** O aluno consegue transformar um PDF do livro-base em markdown por capitulo, page-anchored, sob `.projetos/<slug>/livro/` via um CLI Python opt-in (docling) deterministico, e o mentor consome esse `livro/` como literatura-base durante o bootstrap e a tutoria (referencia de pagina + protocolo de divergencia registrado).
**Verified:** 2026-06-22T22:51:32Z
**Status:** passed
**Re-verification:** No — initial verification

## Goal Achievement

The phase delivers a complete three-layer vertical: a deterministic opt-in conversion engine (07-01), an invocation layer that surfaces — never silently runs — the converter (07-02), and a consumption layer that makes the converted book real literatura-base in the tutoria flow (07-03). All three layers exist, are substantive, and are wired end-to-end. The conduct/anti-drift harness (`check-consistencia.sh`) exits 0 and the logic test suite (8 tests) passes.

### Observable Truths

**Layer 1 — Engine (07-01)**

| #   | Truth | Status | Evidence |
| --- | ----- | ------ | -------- |
| 1 | CLI writes one .md per chapter under `.projetos/<slug>/livro/` | ✓ VERIFIED | `main()` builds `out_dir = .projetos/<slug>/livro` (converte_livro.py:246), loops chapters writing per-file (253-255) |
| 2 | Each chapter file begins with `<!-- page: N -->` anchor (docling page of first element) | ✓ VERIFIED | `render_chapter` emits `<!-- page: {start_page} -->` (126); `start_page=_page_of(item)` reads `prov[0].page_no` (67-72); test_page_anchor_value asserts N==prov page |
| 3 | New chapter at every TITLE / SECTION_HEADER ≤ --cut-level (default 1) | ✓ VERIFIED | `_is_boundary` (75-82) + `split_into_chapters` iterate_items (103); test_split_by_heading + test_chapter_count pass |
| 4 | Book markdown preserves accents (no ASCII fold) | ✓ VERIFIED | `render_chapter` concatenates raw `item.text` (no normalization); test_accents_preserved asserts "função código" survives |
| 5 | Unsafe --slug (.., path sep, non `[a-z0-9-]`) rejected before write | ✓ VERIFIED | `sanitize_slug` (49-58) rejects `/ \ ..` + regex; called before mkdir (240); test_slug_rejected passes |
| 6 | Memory env guards set before docling import; markdownlint --fix once at end | ✓ VERIFIED | OMP/MKL/etc set at module top (37-41) above lazy docling imports; `_run_markdownlint` literal list + FileNotFoundError skip (204-220); test_env_guards + test_lint_called pass |
| 7 | Logic tests pass without running docling (synthetic doc) | ✓ VERIFIED | `8 passed, 1 deselected in 1.15s`; synthetic SyntheticDoc fixture; lazy docling imports |

**Layer 2 — Invocation (07-02)**

| #   | Truth | Status | Evidence |
| --- | ----- | ------ | -------- |
| 8 | Bootstrap asks "tem livro-base? (PDF ou .md)" and branches (.md→paste, PDF→venv cmd/skill) | ✓ VERIFIED | novo-projeto.md Passo 3b (52-69): question + both branches |
| 9 | Pre-warns before firing: demora, nao consome tokens (local), progresso pagina N de M | ✓ VERIFIED | novo-projeto.md:62 literal "nao consome tokens (roda local)...(pagina N de M)" |
| 10 | Mentor never runs docling silently; surfaces command/skill, consumes livro/ once populated | ✓ VERIFIED | "O mentor NUNCA roda docling silenciosamente" (novo-projeto.md:77); echoed in AGENTS.md:59 and SKILL.md |
| 11 | Thin /converte-livro skill POINTS to mentor/novo-projeto.md (no duplicated method logic) | ✓ VERIFIED | SKILL.md body points to novo-projeto.md; rg for docling/AcceleratorOptions/iterate_items = 0 matches |
| 12 | AGENTS.md registers converte_livro.py as opt-in tool + lists /converte-livro skill | ✓ VERIFIED | AGENTS.md:55-60 Ferramentas bullet (OPCIONAL/requirements-pdf.txt); :65 native-skill list |
| 13 | NONCMD whitelists converte-livro (V-15 green); README + metodo.md list it; harness exits 0 | ✓ VERIFIED | check-consistencia.sh:54 NONCMD has converte-livro; README:118,178; metodo.md:7; harness EXIT=0 |
| 14 | /converte-livro→novo-projeto.md recorded as DOCUMENTED routing exception (no mentor/converte-livro.md) | ✓ VERIFIED | Documented in SKILL.md (13-15), check-consistencia.sh:52-53 comment, metodo.md:7; V-12 loop still 5 cmds |

**Layer 3 — Consumption (07-03)**

| #   | Truth | Status | Evidence |
| --- | ----- | ------ | -------- |
| 15 | reference.md layout shows livro/ as NEW sibling of referencias/, anchor noted (D-08) | ✓ VERIFIED | reference.md:234-235 `livro/` tree line + `<!-- page: N -->` child comment |
| 16 | reference.md documents divergence record (livro X / pratica Y / escolha, dated) (D-04) | ✓ VERIFIED | reference.md:317-318 dated bullet INSIDE APRENDIZADO fence (303-323) |
| 17 | tutor.md Passo 0 reads livro/*.md as baseline when it exists (D-01) | ✓ VERIFIED | tutor.md:29-31 `livro/*.md (se existir)...baseline teorica` |
| 18 | tutor.md Passo 3 cites "ve a pagina X do livro" via anchor (D-10) | ✓ VERIFIED | tutor.md:79-80 page reference via `<!-- page: N -->` anchor |
| 19 | Divergence protocol (decide sozinho) ALWAYS ships with dated APRENDIZADO.md record — D-03 never alone | ✓ VERIFIED | tutor.md:83-86 `decide sozinho` + `entrada DATADA em APRENDIZADO.md` co-occur; points to reference.md for format |

**Score:** 19/19 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
| -------- | -------- | ------ | ------- |
| `scripts/converte_livro.py` | opt-in CLI: split, anchors, pure helpers | ✓ VERIFIED | 263 lines; env guards before lazy docling; sanitize_slug/_page_of/split_into_chapters/render_chapter present; convert() once |
| `requirements-pdf.txt` | isolated docling+pypdf+pytest | ✓ VERIFIED | docling>=2.104.0, pypdf>=4.0, pytest>=8.0; no questionary |
| `tests/test_converte_livro.py` | 8 logic tests + golden smoke | ✓ VERIFIED | all 8 named tests present; 8 passed / 1 slow deselected |
| `tests/conftest.py` | synthetic doc fixture + slow marker | ✓ VERIFIED | synthetic_doc fixture, iterate_items, pytest_configure slow marker |
| `tests/fixtures/sample.pdf` | tiny PDF for golden smoke | ✓ VERIFIED | 879 bytes, exists |
| `.claude/skills/converte-livro/SKILL.md` | thin adapter → novo-projeto.md | ✓ VERIFIED | points to novo-projeto.md, routing exception, zero engine logic, ASCII |
| `scripts/check-consistencia.sh` | NONCMD whitelist reconciled | ✓ VERIFIED | converte-livro in NONCMD; V-12 set still 5; harness exits 0 |
| `AGENTS.md` | tool + skill registration | ✓ VERIFIED | Ferramentas bullet + native-skill list; ASCII |
| `README.md` | /converte-livro listed (V-15) | ✓ VERIFIED | adapter table row + skill tree + script tree lines |
| `mentor/metodo.md` | routing-exception note | ✓ VERIFIED | exception sentence; ASCII |
| `mentor/novo-projeto.md` | Passo 3b livro-base step | ✓ VERIFIED | question, D-15 branch, D-14 pre-warning, venv cmd, silent-run rule, livro/ esqueleto |
| `mentor/reference.md` | livro/ layout + divergence format | ✓ VERIFIED | tree sibling + anchor note + dated divergence bullet in fence |
| `mentor/tutor.md` | livro/ baseline + page ref + D-03/D-04 | ✓ VERIFIED | Passo 0 read, Passo 3 page ref, paired divergence protocol; fully ASCII |

### Key Link Verification

| From | To | Via | Status |
| ---- | -- | --- | ------ |
| converte_livro.py | `.projetos/<slug>/livro/` | write_text per chapter (utf-8) | ✓ WIRED |
| split helper | DocItemLabel TITLE/SECTION_HEADER + level | iterate_items boundary | ✓ WIRED |
| page anchor | item.prov[0].page_no | _page_of helper | ✓ WIRED |
| tests | converte_livro helpers | `from scripts import converte_livro` | ✓ WIRED (8 passed) |
| SKILL.md | mentor/novo-projeto.md | thin pointer body | ✓ WIRED |
| novo-projeto.md Passo 3b | converte_livro.py | surfaced venv command | ✓ WIRED |
| AGENTS.md registration | check-consistencia.sh NONCMD | harness reconciliation | ✓ WIRED (harness=0) |
| tutor.md Passo 0 | livro/*.md | ordered read-list bullet | ✓ WIRED |
| tutor.md Passo 3 | `<!-- page: N -->` anchor | "ve a pagina X" reference | ✓ WIRED |
| divergence protocol D-03 | APRENDIZADO.md dated record D-04 | always-together sub-paragraph | ✓ WIRED (co-occur grep) |

### Data-Flow Trace (Level 4)

Not applicable — this phase produces a CLI/scripts + method-doc prose, not a dynamic-data-rendering UI. The engine's data flow (PDF → docling DoclingDocument → split → chapter files) is exercised end-to-end by the golden smoke (per 07-01-SUMMARY, ran against a real docling pipeline) and by the synthetic-doc logic tests. No hollow/static-data render path exists.

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
| -------- | ------- | ------ | ------ |
| Conduct/anti-drift harness green | `sh scripts/check-consistencia.sh` | 0 fail(s), EXIT=0 (V-12..V-16 all PASS) | ✓ PASS |
| Logic suite passes without docling | `pytest tests/test_converte_livro.py -m "not slow"` | 8 passed, 1 deselected in 1.15s | ✓ PASS |
| tutor.md fully ASCII (V-16) | `rg -c '[accents]' mentor/tutor.md` | 0 matches | ✓ PASS |
| Skill duplicates no engine logic | `rg -c 'docling\|AcceleratorOptions\|iterate_items' SKILL.md` | 0 matches | ✓ PASS |
| No questionary/PdfWriter remnants | `rg -c 'questionary\|PdfWriter' converte_livro.py` | 0 matches | ✓ PASS |
| sample.pdf fixture present | `ls tests/fixtures/sample.pdf` | 879B | ✓ PASS |

### Requirements Coverage

Every decision D-01..D-15 (the CONTEXT.md decisions that ARE the requirements) is claimed by a plan and verified in code/docs. D-08 and D-10 are intentionally shared across plans (engine produces, method consumes).

| Req | Source Plan | Description | Status | Evidence |
| --- | ----------- | ----------- | ------ | -------- |
| D-01 | 07-03 | livro como baseline teorico do mentor | ✓ SATISFIED | tutor.md:29-31 |
| D-02 | 07-02 | passo opcional bootstrap, fonte-unica em mentor/ | ✓ SATISFIED | Passo 3b; skill/AGENTS carry no method logic |
| D-03 | 07-03 | mentor decide sozinho na divergencia | ✓ SATISFIED | tutor.md:83 "decide sozinho" |
| D-04 | 07-03 | divergencia datada em APRENDIZADO.md | ✓ SATISFIED | reference.md:317-318 + tutor.md:85-86 |
| D-05 | 07-01 | docling dependencia OPCIONAL isolada | ✓ SATISFIED | requirements-pdf.txt; lazy imports; core stdlib |
| D-06 | 07-02 | .md cola direto em livro/ (zero dep) | ✓ SATISFIED | novo-projeto.md:58 paste branch |
| D-07 | 07-01 | requirements-pdf.txt + venv opt-in | ✓ SATISFIED | requirements-pdf.txt header + venv instructions |
| D-08 | 07-01/03 | output em .projetos/<slug>/livro/ (layout novo) | ✓ SATISFIED | converte_livro.py:246; reference.md:234 |
| D-09 | 07-01 | split deterministico por heading (script, nao LLM) | ✓ SATISFIED | split_into_chapters; tests |
| D-10 | 07-01/03 | ancora de pagina deterministica `<!-- page: N -->` | ✓ SATISFIED | render_chapter:126; tutor.md:80 page cite |
| D-11 | 07-01 | estrutura > tabelas/figuras (best-effort) | ✓ SATISFIED | generate_picture_images True, commented best-effort (180) |
| D-12 | 07-01 | adaptar converter.py: CLI por args, sem questionary, blindagem+lint | ✓ SATISFIED | argparse CLI; no questionary; env guards; markdownlint --fix |
| D-13 | 07-02 | dois caminhos: aluno terminal + skill /converte-livro | ✓ SATISFIED | SKILL.md + venv command surface |
| D-14 | 07-02 | pre-aviso demora/0 tokens/progresso | ✓ SATISFIED | novo-projeto.md:62; SKILL.md |
| D-15 | 07-02 | bootstrap pergunta PDF vs .md; nunca roda silencioso | ✓ SATISFIED | novo-projeto.md:55,77 |

No orphaned requirements: there is no formal REQUIREMENTS.md; CONTEXT.md D-01..D-15 are the contract and all 15 are claimed and satisfied.

### Anti-Patterns Found

None blocking. Notes:

| File | Line | Pattern | Severity | Impact |
| ---- | ---- | ------- | -------- | ------ |
| scripts/check-consistencia.sh | 74 | accent-set chars `[áàâ...]` inside an rg pattern | ℹ️ Info | Literal regex class of the V-16 rule itself, not document content; the harness only V-16-scans `mentor/` so the script's own pattern is out of scope. Harness exits 0. |
| scripts/converte_livro.py | 196 | single `converter.convert(...)` | ℹ️ Info | Intentional whole-doc single pass (replaces base script's pypdf 1-page chunking) — a design requirement, not a stub |

The OOM `page_range` fallback (line 193-194) is a documented comment, not an unimplemented happy-path stub — matches the plan's explicit "documented, not implemented" intent.

### Human Verification Required

None. Every must-have was verifiable programmatically: the harness exit code, the passing pytest suite (including a golden smoke that 07-01-SUMMARY reports ran against the real docling pipeline in this environment), grep-asserted doc wiring, and ASCII/accent discipline checks all confirm goal achievement without needing visual or runtime human judgment. The phase output is deterministic scripting + method-doc prose, not UI/UX surface.

### Gaps Summary

No gaps. All 19 observable truths across the three layers are verified, all 13 artifacts exist and are substantive and wired, all 10 key links are connected, all 15 requirement decisions (D-01..D-15) are satisfied, the consistency harness exits 0, and the logic test suite passes. The three layers compose into the full vertical the phase goal describes: opt-in deterministic PDF→markdown engine → invocation that surfaces (never silently runs) the converter → consumption of `livro/` as page-anchored literatura-base with a registered divergence protocol.

---

_Verified: 2026-06-22T22:51:32Z_
_Verifier: Claude (gsd-verifier)_
