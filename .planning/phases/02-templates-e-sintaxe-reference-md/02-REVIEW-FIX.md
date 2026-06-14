---
phase: 02-templates-e-sintaxe-reference-md
fixed_at: 2026-06-14T00:00:00Z
review_path: .planning/phases/02-templates-e-sintaxe-reference-md/02-REVIEW.md
iteration: 1
findings_in_scope: 2
fixed: 2
skipped: 0
status: all_fixed
---

# Phase 2: Code Review Fix Report

**Fixed at:** 2026-06-14
**Source review:** .planning/phases/02-templates-e-sintaxe-reference-md/02-REVIEW.md
**Iteration:** 1

**Summary:**
- Findings in scope: 2 (WR-01, WR-02)
- Fixed: 2
- Skipped: 0
- Out of scope (Info, not attempted): 3 (IN-01, IN-02, IN-03)

## Fixed Issues

### WR-01: Scaffold field order contradicts the documented reading sequence

**Files modified:** `mentor/reference.md`
**Commit:** d19f7ca
**Applied fix:** Swapped the `DONE` and `PERGUNTA-GUIA` lines in the scaffold TEMPLATE
block (lines 365-366) so PERGUNTA-GUIA now precedes DONE. The in-artifact field order is
now META, PORQUE, PRESSUPOE, ARQUIVOS, EXEMPLO-DE-RESULTADO, PERGUNTA-GUIA, DONE — which
matches the "Como o aluno le o scaffold" reading-sequence guide (lines 391-398, where
PERGUNTA-GUIA precedes TODO and DONE follows). A student scanning the comment block now
hits PERGUNTA-GUIA before DONE, preserving the stated "think before you type" flow.

### WR-02: Encoding convention diverges from the approved sibling file fundamentos.md

**Files modified:** `mentor/reference.md`
**Commit:** 6c78375
**Applied fix:** Normalized `reference.md` to ASCII-only, matching the established
convention of the approved Phase-1 sibling `mentor/fundamentos.md` (verified 0 non-ASCII
codepoints). Changes:
- 47 Unicode em-dashes (`—`, U+2014) replaced with ` -- ` (the ` -- ` form used in
  fundamentos.md).
- 2 Unicode arrows (`→`, U+2192, both on line 261) replaced with `->` (the ASCII arrow
  used 22+ times elsewhere in the same file).
- Box-drawing tree on lines 186-195 (`├ │ └ ─`, U+2500/2502/251C/2514) replaced with an
  ASCII tree (`|--`, `|`, `` `-- ``).

Verified: `reference.md` now has 0 non-ASCII codepoints, and the phase-2 validation gate
(`scripts/check-phase2.sh`) remains fully green (0 fails) after the change.

## Out-of-Scope Issues (Info findings — not attempted)

The configured fix scope was `critical_warning`, so the three Info findings below were
intentionally NOT attempted. They are documented here for the developer to address
manually if desired.

### IN-01: Dangling reference to roadmap.sh (file does not exist)

**File:** `mentor/reference.md:105`
**Reason:** Out of scope (Info severity; fix scope is critical_warning).
**Original issue:** Line 105 references `roadmap.sh`, which does not exist. The real
script is `scripts/roadmap_fetch.py` (correctly named at line 190). Suggested fix:
change `roadmap.sh` to `roadmap_fetch.py`.

### IN-02: "curadoria" referenced but never defined within reference.md

**File:** `mentor/reference.md:243` and `:267`
**Reason:** Out of scope (Info severity; fix scope is critical_warning).
**Original issue:** Both "Dividas de aprendizado" blocks point to a "curadoria" step not
defined within reference.md — likely a soft cross-reference to another mentor/ doc rather
than a hard dangling link.

### IN-03: ARQUIVOS field present in template but absent from the reading-order guide

**File:** `mentor/reference.md:362` (template) vs `:391-398` (guide)
**Reason:** Out of scope (Info severity; fix scope is critical_warning).
**Original issue:** The scaffold template includes an `ARQUIVOS:` field, but the
reading-order sequence omits it. Defensible (orientation metadata, not a reading step),
but a cross-checking reader may wonder if the omission is intentional.

---

_Fixed: 2026-06-14_
_Fixer: Claude (gsd-code-fixer)_
_Iteration: 1_
