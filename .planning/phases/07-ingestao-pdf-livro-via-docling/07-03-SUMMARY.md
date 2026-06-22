---
phase: 07-ingestao-pdf-livro-via-docling
plan: 03
subsystem: method-docs
tags: [livro-base, divergencia, tutor, reference, docling, page-anchor, consumption-layer]

# Dependency graph
requires:
  - "07-01: <!-- page: N --> anchor format (HTML comment at the start of each chapter file in .projetos/<slug>/livro/)"
  - "07-02: livro/ esqueleto bullet + Passo 3b bootstrap in mentor/novo-projeto.md; harness reconciled green"
provides:
  - "mentor/reference.md: livro/ in the student-repo layout (D-08) + divergence-record format in the APRENDIZADO.md template (D-04)"
  - "mentor/tutor.md: livro/ consulted as theoretical baseline (D-01), page-precise references via the anchor (D-10), divergence protocol (D-03) always paired with the dated APRENDIZADO.md record (D-04)"
affects: [tutor, reference, novo-projeto]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Consumption layer woven into the method (not the engine): the converted book becomes literatura-base the tutor RESPECTS and cites by page"
    - "D-03 never ships without D-04: the autonomous-decision rule and its dated APRENDIZADO.md record live in the SAME sub-paragraph, grep-asserted (decide sozinho + APRENDIZADO.md co-occur)"
    - "Accent-scope discipline: accented divergence record sits strictly INSIDE the APRENDIZADO fenced template; reference.md surrounding prose ASCII; tutor.md fully ASCII (V-16 scanned)"

key-files:
  created: []
  modified:
    - mentor/reference.md
    - mentor/tutor.md

key-decisions:
  - "tutor.md POINTS to mentor/reference.md for the divergence-record format (single-source); it does not redefine the format — only the rule (decide sozinho) and the mandatory dated record live in tutor.md"
  - "The divergence record extends the EXISTING 'Decisoes arquiteturais' dated-bullet pattern in the APRENDIZADO template rather than introducing a new section/artifact (reuses the forense Passo 6 target)"
  - "livro/ added as a NEW sibling of referencias/ in the layout (D-08 separates book-base from roadmap output), distinct from it"

patterns-established:
  - "Adapters point, method consumes: the book is consumed AS literatura-base via tutor.md/reference.md edits; zero docling logic restated in the method docs"

requirements-completed: [D-01, D-03, D-04, D-08, D-10]

# Metrics
duration: 3min
completed: 2026-06-22
---

# Phase 07 Plan 03: Camada de consumo (livro-base no metodo) Summary

**Tece a camada de consumo do livro-base no metodo: `mentor/reference.md` ganha `livro/` no layout do repo do aluno (D-08, irmao de `referencias/`, com a ancora `<!-- page: N -->`) e o formato do registro de divergencia no template APRENDIZADO.md (D-04: livro diz X / pratica diz Y / escolha do mentor, datado); `mentor/tutor.md` passa a consultar `livro/*.md` como baseline teorica que RESPEITA (D-01), cita a pagina exata via a ancora ("ve a pagina X do livro", D-10) e carrega o protocolo de divergencia (D-03: decide sozinho) SEMPRE pareado com o registro datado em APRENDIZADO.md (D-04). Ultimo plano da Fase 7.**

## Performance

- **Duration:** ~3 min
- **Started:** 2026-06-22T22:41:05Z
- **Completed:** 2026-06-22T22:43:44Z
- **Tasks:** 2 (both type=auto)
- **Files modified:** 2 (0 created, 2 modified)

## Accomplishments

- **reference.md layout (D-08):** `livro/` added as a NEW sibling of `referencias/` in the "Layout do repo do aluno" tree, mirroring the `|--` comment style, with the `0x-<capitulo>.md` child line carrying the `<!-- page: N -->` anchor note. ASCII (outside any fence).
- **reference.md divergence format (D-04):** the "Decisoes arquiteturais" section of the APRENDIZADO.md fenced template gains the dated divergence bullet (`o livro diz <X> / a pratica atual diz <Y> / escolha do mentor: <Z>`) in ACCENTED Portuguese, strictly INSIDE the fence; an ASCII cross-reference prose sentence after the fence pairs the record with the mentor's autonomous decision and points to `mentor/tutor.md`.
- **reference.md accent rule:** `livro/` added to the "Idioma e acentuacao" student-facing accented list, so the converted book is explicitly covered by the accented-Portuguese rule.
- **tutor.md baseline (D-01):** Passo 0 read-list gains a `livro/*.md` bullet — the book-base the mentor RESPECTS and consults as theoretical baseline, with the anchor note.
- **tutor.md page reference (D-10):** Passo 3 step 1 gains a refinement sentence (not a new top-level step) — cite the exact page via the `<!-- page: N -->` anchor ("ve a pagina X do livro").
- **tutor.md divergence protocol (D-03 + D-04 together):** Passo 3 step 1 gains a sub-paragraph where the tutor `decide sozinho` on a livro-vs-pratica divergence AND every divergence becomes a dated `APRENDIZADO.md` entry pointing to the format in `mentor/reference.md` — D-03 never ships alone. tutor.md stays fully ASCII.

## Task Commits

1. **Task 1: livro/ in layout + divergence record in APRENDIZADO template** - `0e2cbca` (feat)
2. **Task 2: tutor consults livro/ baseline + page ref + divergence protocol** - `1219200` (feat)

## Files Created/Modified

- `mentor/reference.md` - `livro/` in the layout tree (D-08) with the anchor note; divergence-record bullet in the APRENDIZADO "Decisoes arquiteturais" template (D-04, accents inside the fence); ASCII cross-reference prose after the fence; `livro/` added to the accented student-artifact list in "Idioma e acentuacao".
- `mentor/tutor.md` - Passo 0 `livro/*.md` baseline read (D-01); Passo 3 step 1 page reference via the anchor (D-10) and divergence protocol (D-03) paired with the dated APRENDIZADO.md record (D-04), pointing to `mentor/reference.md` for the format. Fully ASCII.

## Decisions Made

- tutor.md is a consumer of the format, not its source: it cites `mentor/reference.md` for the divergence-record shape (single-source) and only carries the behavioral rule (`decide sozinho`) plus the mandatory dated record. This keeps the format defined in exactly one place.
- The divergence record reuses the existing dated-bullet pattern of "Decisoes arquiteturais" and the existing forense Passo 6 target (`APRENDIZADO.md`), introducing no new section or artifact.

## Deviations from Plan

None - plan executed exactly as written. Both tasks landed their edits, harness stayed green throughout, and every acceptance grep passed on the first verification.

## Known Stubs

None. Both edits wire real, consumable behavior: tutor.md reads `livro/*.md` (populated by the 07-01 converter / 07-02 paste path) and cites the `<!-- page: N -->` anchor the engine writes; reference.md documents a format the tutor actually points to. No empty/placeholder data paths introduced.

## Threat Flags

None. The edits are method-doc prose only — no new network endpoints, auth paths, file-access patterns, or schema changes at trust boundaries. The slug/path-safety surface lives in the 07-01 converter and is unchanged here.

## Issues Encountered

- The RTK proxy rewrites bare `grep -c` into a fuzzy token-matching wrapper that renders odd line/`0:` output; cross-checked the load-bearing counts with the dedicated Grep tool (reference.md=2, tutor.md=2) and the harness itself. The literal `grep -q` co-occurrence checks (D-03+D-04, D-04 format) returned clean. No content impact.
- A default `markdownlint` run flags MD013 (line-length) and MD004 across BOTH files, but these rules are PRE-EXISTING noise outside the project's enforced rule set (`mentor/reference.md:5-20` enumerates MD022/031/032/040/025/012/009/047/034). Filtering to the enforced rules over the edited files returns zero violations. Out of scope; not introduced by this plan.

## Verification

- `sh scripts/check-consistencia.sh` exits 0 (V-12/V-13/V-15/V-16 all PASS; tutor.md ASCII-clean under V-16; reference.md template accents stay inside the fence).
- `grep -c "livro/"` >= 1 in both files (reference.md=2, tutor.md=2) — D-01/D-08 wiring present.
- `grep -q "ve a pagina X"` matches in tutor.md — D-10 page reference.
- `grep -q "decide sozinho" && grep -q "APRENDIZADO.md"` both match in tutor.md — D-03 + D-04 never split.
- `grep -q "o livro diz" && grep -q "escolha do mentor"` both match in reference.md — D-04 divergence format present.
- `grep -q "<!-- page: N -->"` matches in reference.md — anchor note in the layout.
- `rg -c '[accent-set]' mentor/tutor.md` = 0 — tutor.md fully ASCII.

## Phase 7 Readiness

This is the LAST plan of Phase 7. The full vertical is now complete:

- **07-01:** the docling conversion engine (`scripts/converte_livro.py`) — opt-in, deterministic split, `<!-- page: N -->` anchors.
- **07-02:** the invocation layer — `/converte-livro` thin skill, "Passo 3b - Livro-base (opcional)" bootstrap step, harness reconciliation, set-consistent registration.
- **07-03 (this plan):** the consumption layer — the book is now USED as literatura-base in the tutoria flow (D-01), cited by exact page (D-10), with a transparent, auditable divergence trail (D-03 + D-04).

D-01/D-03/D-04/D-08/D-10 satisfied. Phase 7 ready for `/gsd-verify-work` / phase close.

## Self-Check: PASSED

Both modified files (`mentor/reference.md`, `mentor/tutor.md`) and the SUMMARY exist on disk; both task commits (`0e2cbca`, `1219200`) present in git history.
