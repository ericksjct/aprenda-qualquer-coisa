---
phase: 02-templates-e-sintaxe-reference-md
reviewed: 2026-06-14T00:00:00Z
depth: standard
files_reviewed: 1
files_reviewed_list:
  - mentor/reference.md
findings:
  critical: 0
  warning: 2
  info: 3
  total: 5
status: issues_found
---

# Phase 2: Code Review Report

**Reviewed:** 2026-06-14
**Depth:** standard
**Files Reviewed:** 1 (mentor/reference.md)
**Status:** issues_found

## Summary

Reviewed `mentor/reference.md` as a methodology/documentation artifact (not executable code).
The phase-2 validation gate (`scripts/check-phase2.sh`) is fully green (0 fails), and I
confirmed its strongest claims independently: anchor integrity resolves, anti-theory-leak is
clean even under a broadened jargon pattern, and the capability-verb / artifact-as-evidence
framing is consistent across all three student-facing templates.

Two real issues remain that the script does not catch:

1. A genuine **field-order contradiction** between the scaffold TEMPLATE block and the
   "Como o aluno le o scaffold" reading-sequence guide — the doc explicitly asserts the
   fields are a SEQUENCE, yet the two places disagree on where DONE and PERGUNTA-GUIA sit.
2. An **encoding-convention divergence** from the sibling file `fundamentos.md`. That
   already-approved Phase-1 file is 100% ASCII and uses `--`/`->`; `reference.md` mixes ASCII
   `->` (22 occurrences) with Unicode em-dash (`—`), a Unicode arrow (`→`), and box-drawing
   characters. No accented characters were found, so a strict "no accents" reading passes —
   but the inconsistency with the established convention is worth a decision.

Plus one dangling filename reference and two minor consistency notes.

## Detailed verification performed

- **Anchors (PASS):** Both `fundamentos.md#frameworks-foundational-load-bearing` (3 uses) and
  `fundamentos.md#mayer-so-3-de-12-principios-em-texto-puro` (1 use) resolve to real headings
  in `mentor/fundamentos.md` under the GitHub slug algorithm. No theory is duplicated into
  reference.md (single-source respected).
- **Anti-theory-leak (PASS):** `extract-fenced.sh` output contains zero framework jargon, even
  against an expanded pattern (bloom, backward design, mayer, sweller, merrill, zpd, vygotsky,
  worked example, fading, gradual release, retrieval, spacing, sdt, etc.). Theory lives in
  prose only.
- **Capability framing (PASS):** CAMINHO ("Objetivo (capacidade): ao terminar, voce consegue
  <verbo> <conceito>" + "Entregavel"), aula (line 294-296, explicitly mirroring CAMINHO), and
  scaffold ("DONE: evidencia observavel de que voce JA CONSEGUE <a capacidade>") agree.
- **Accented chars (PASS):** No accented characters present.

## Warnings

### WR-01: Scaffold field order contradicts the documented reading sequence

**File:** `mentor/reference.md:356-371` (template) vs `mentor/reference.md:391-398` (guide)
**Issue:** The doc states at line 387 that "Os campos sao uma SEQUENCIA, nao um menu" — the
fields are an ordered sequence — but the two places define different orders:

- Scaffold template block (lines 358-366): META, PORQUE, PRESSUPOE, ARQUIVOS,
  EXEMPLO-DE-RESULTADO, **DONE, PERGUNTA-GUIA** (DONE precedes PERGUNTA-GUIA).
- Reading-order guide (lines 391-398): META, PORQUE, PRESSUPOE, EXEMPLO-DE-RESULTADO,
  **PERGUNTA-GUIA -> TODO(human) -> DONE** (PERGUNTA-GUIA precedes TODO; DONE follows TODO).

So in the artifact the student physically reads, DONE sits ABOVE PERGUNTA-GUIA, while the
guide that teaches reading order puts PERGUNTA-GUIA first and DONE near the end. A student
following the guide ("PERGUNTA-GUIA -> PENSE antes de digitar") will scan the comment block
and hit DONE before PERGUNTA-GUIA, defeating the stated "think before you type" flow. This is
exactly the META..PISTA order-integrity concern called out for this phase.

**Fix:** Make the template comment block match the reading sequence. Recommended: in the
template, move PERGUNTA-GUIA above DONE so the in-artifact order is META, PORQUE, PRESSUPOE,
ARQUIVOS, EXEMPLO-DE-RESULTADO, PERGUNTA-GUIA, DONE — i.e. swap lines 365 and 366:

```text
  EXEMPLO-DE-RESULTADO: <...>
  PERGUNTA-GUIA: <pergunta socratica que o aluno responde ANTES de codar>
  DONE: <evidencia observavel de que voce JA CONSEGUE <a capacidade do passo>: ...>
*/
```

(DONE conceptually evaluates the result, so it reads naturally just before the TODO/PISTA
action block.) Alternatively, decide the template order is canonical and rewrite the guide to
match — but the guide's "PERGUNTA-GUIA before you type" logic is sound, so adjust the template.

### WR-02: Encoding convention diverges from the approved sibling file `fundamentos.md`

**File:** `mentor/reference.md` — em-dash `—` on 32+ lines (e.g. 1, 17, 53, 59, 261, 295);
Unicode arrow `→` on line 261; box-drawing chars `├ │ └` on lines 190-195.
**Issue:** The Phase-1, already-reviewed sibling `mentor/fundamentos.md` is 100% ASCII (0
non-ASCII bytes) and consistently uses ` -- ` for em-dashes and `->` for arrows. `reference.md`
is internally inconsistent: it uses ASCII `->` in 22 places (lines 18, 37, 38, 47, 50, 75, 89,
116, 127, 187, 316, 379, 382, 391-398...) yet also uses Unicode `—`, one Unicode `→` (line
261), and box-drawing characters. The phase brief states "mentor/ files must have NO accented
characters" — strictly, none are present, so a literal reading passes. But the mixed ASCII /
Unicode dashes and arrows break the convention established by the sibling file and make the two
mentor docs inconsistent.
**Fix:** Decide the convention explicitly. If "ASCII-only" (matching `fundamentos.md`), replace
`—` with ` -- `, the `→` on line 261 with `->`, and the box-drawing tree on lines 185-196 with
ASCII (`|`, `+--`, backtick-fenced as-is). If em-dashes/box-drawing are intentionally allowed in
reference.md, document that exception so the divergence is a choice, not drift — and at minimum
normalize line 261's lone Unicode `→` to the `->` used everywhere else in this same file.

## Info

### IN-01: Dangling reference to `roadmap.sh` (file does not exist)

**File:** `mentor/reference.md:105`
**Issue:** Line 105 says "Se a referencia do roadmap.sh (em `referencias/`) introduz um
conceito...". No `roadmap.sh` exists in the repo. The actual script is
`scripts/roadmap_fetch.py`, which the same document correctly names at line 190
("roadmaps de referencia (scripts/roadmap_fetch.py)"). Internal contradiction + dangling
filename.
**Fix:** Change `roadmap.sh` to `roadmap_fetch.py` (or to "o roadmap de referencia em
`referencias/`") so it agrees with line 190 and the real file `scripts/roadmap_fetch.py`.

### IN-02: "curadoria" referenced but never defined within reference.md

**File:** `mentor/reference.md:243` and `:267`
**Issue:** Both `## Dividas de aprendizado` blocks point to a "curadoria" step ("registradas na
curadoria", "Dividas de aprendizado (da curadoria)") that is not defined anywhere in
reference.md. It is likely defined in another `mentor/` doc (the curation/gate step), so this is
a soft cross-reference rather than a hard dangling link.
**Fix:** Either add a one-line pointer to where "curadoria" is defined, or confirm the term is
introduced upstream in the method docs the student/agent will already have read. No change
needed if the surrounding workflow guarantees prior context.

### IN-03: ARQUIVOS field present in template but absent from the reading-order guide

**File:** `mentor/reference.md:362` (template) vs `:391-398` (guide)
**Issue:** The scaffold template includes an `ARQUIVOS:` field (line 362), but the
"Como o aluno le o scaffold" sequence (lines 391-398) omits it entirely. Defensible — ARQUIVOS
is orientation metadata, not a reading-sequence step — but a reader cross-checking the two lists
may wonder whether the omission is intentional.
**Fix:** Optional. If intentional, no change. If you want the guide to fully mirror the artifact,
add a brief "ARQUIVOS -> quais arquivos voce vai tocar (orientacao, nao acao)" line, or add a
one-line note that ARQUIVOS/MARCO are header metadata excluded from the action sequence.

---

_Reviewed: 2026-06-14_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
