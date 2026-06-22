---
phase: 07-ingestao-pdf-livro-via-docling
plan: 02
subsystem: orchestration
tags: [skill, adapter, bootstrap, harness, consistency, docling, livro-base]

# Dependency graph
requires:
  - "07-01: FIXED CLI signature (python scripts/converte_livro.py <pdf> --slug <slug>), .venv-pdf, requirements-pdf.txt, <!-- page: N --> anchor"
provides:
  - ".claude/skills/converte-livro/SKILL.md: thin adapter pointing to mentor/novo-projeto.md (no duplicated docling logic)"
  - "mentor/novo-projeto.md Passo 3b: optional livro-base bootstrap step (D-15 branch + D-14 pre-warning + livro/ esqueleto)"
  - "AGENTS.md/README.md/mentor/metodo.md: converter + /converte-livro registered, V-15 set-consistent"
  - "check-consistencia.sh NONCMD whitelists converte-livro (V-15 reconciled)"
affects: [07-03, tutor, novo-projeto]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Documented routing exception: /converte-livro -> mentor/novo-projeto.md (livro-base is a bootstrap STEP, not an eponymous procedure; no mentor/converte-livro.md)"
    - "Harness reconciliation BEFORE registration edits: NONCMD whitelist keeps V-15 set-equality green when a real command routes outside the closed V-12 set"

key-files:
  created:
    - .claude/skills/converte-livro/SKILL.md
  modified:
    - scripts/check-consistencia.sh
    - mentor/novo-projeto.md
    - AGENTS.md
    - README.md
    - mentor/metodo.md

key-decisions:
  - "/converte-livro deliberately routes to mentor/novo-projeto.md (livro-base bootstrap step) rather than an eponymous mentor doc; documented as an exception in the skill body, in check-consistencia.sh, and in mentor/metodo.md"
  - "NONCMD in check-consistencia.sh extended to whitelist converte-livro (V-15 reconciliation); V-12 closed set left at 5 commands so no mentor/converte-livro.md is required"
  - "Reworded the D-14 pre-warning onto a single line so the literal phrase 'nao consome tokens' survives markdown line-wrap (acceptance grep is line-based)"

patterns-established:
  - "Thin adapter points, never restates: the skill carries zero docling/engine logic — all method logic single-sourced in mentor/novo-projeto.md (D-02)"

requirements-completed: [D-02, D-06, D-13, D-14, D-15]

# Metrics
duration: 4min
completed: 2026-06-22
---

# Phase 07 Plan 02: Camada de invocacao (skill + bootstrap + harness) Summary

**Tece a camada de invocacao do conversor de livro-base: um skill fino `/converte-livro` que APONTA para `mentor/novo-projeto.md` (sem duplicar docling), o passo opcional "Passo 3b - Livro-base" no bootstrap com a ramificacao D-15 (PDF vs .md) e o pre-aviso D-14, e a reconciliacao do harness (NONCMD whitelist) que mantem a igualdade de conjunto V-15 verde ao registrar o comando em AGENTS.md/README.md/mentor/metodo.md.**

## Routing exception (load-bearing)

`/converte-livro` roteia DELIBERADAMENTE para `mentor/novo-projeto.md` (o passo
livro-base "Passo 3b"), NAO para um `mentor/converte-livro.md` proprio — o livro-base e
um PASSO do bootstrap, nao um procedimento autonomo. Essa excecao a convencao
`/comando -> mentor/<comando>.md` esta documentada em tres lugares (auto-documentada):
o corpo do skill, o comentario in-script de `check-consistencia.sh`, e o cabecalho de
roteamento de `mentor/metodo.md`. Por isso `converte-livro` entrou no NONCMD (whitelist
do lado negativo do V-15) mas NAO no set fechado V-12 (que exigiria o doc eponimo).

## Performance

- **Duration:** ~4 min
- **Started:** 2026-06-22T22:34:34Z
- **Completed:** 2026-06-22T22:38:01Z
- **Tasks:** 4 (all type=auto)
- **Files modified:** 6 (1 created, 5 modified)

## Accomplishments
- Harness reconciled FIRST (Task 1): NONCMD whitelists converte-livro, V-12 set-fechado untouched, exception documented in-script — harness stayed green BEFORE any registration edit, exactly as the plan ordered.
- Thin `/converte-livro` skill (Task 2) mirrors tutor/SKILL.md: ASCII, points to mentor/novo-projeto.md, echoes the D-14 pre-warning, and self-documents the routing exception — zero docling/engine logic duplicated.
- Optional livro-base bootstrap step (Task 3): D-15 PDF-vs-.md branch (.md -> paste into livro/, zero deps; PDF -> exact .venv-pdf command or /converte-livro), D-14 pre-warning verbatim (demora / nao consome tokens / pagina N de M / ~2GB), the "NUNCA roda docling silenciosamente" rule, and a livro/ esqueleto bullet in Passo 7.
- Set-consistent registration (Task 4) across AGENTS.md/README.md/mentor/metodo.md; harness exits 0 with V-15 set-equality, V-13 backtick paths, and V-16 accents all clean.

## Task Commits

1. **Task 1: whitelist converte-livro in NONCMD (V-15 reconciliation)** - `7769cb0` (fix)
2. **Task 2: thin /converte-livro skill adapter** - `f0300ac` (feat)
3. **Task 3: optional livro-base bootstrap step (Passo 3b)** - `ee4ca31` (feat)
4. **Task 4: register converter + skill across V-15 files** - `1333e5a` (feat)

## Files Created/Modified
- `.claude/skills/converte-livro/SKILL.md` (new) - Thin Claude Code adapter pointing to mentor/novo-projeto.md; documents the routing exception; no method logic.
- `scripts/check-consistencia.sh` - NONCMD alternation gains `converte-livro` + an ASCII comment documenting the routing exception (V-15 reconciliation).
- `mentor/novo-projeto.md` - New "Passo 3b - Livro-base (opcional)" with D-15 branch, D-14 pre-warning, exact venv command, D-15 silent-run rule; Passo 7 esqueleto gains a livro/ bullet.
- `AGENTS.md` - converte_livro.py registered under `## Ferramentas` (OPCIONAL/isolado/Passo 3b); `/converte-livro` added to the Claude Code native-skills bullet.
- `README.md` - `/converte-livro` added to the Adaptadores Claude Code table row + a skill-tree line + a converte_livro.py script-tree line.
- `mentor/metodo.md` - routing-exception sentence in the routing-convention header.

## Decisions Made
- The skill and metodo.md both state the routing exception explicitly so it is self-documenting and survives future audits (pattern-compliance: an adapter that points outside the /comando convention must say so).
- Kept `converte-livro` OUT of the V-12 hardcoded set on purpose — adding it there would (wrongly) demand a mentor/converte-livro.md, contradicting the single-source bootstrap-step design.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] D-14 pre-warning phrase split by markdown line-wrap**
- **Found during:** Task 3 verification
- **Issue:** The first draft wrapped `**nao consome\n  tokens**` across two lines (with bold markers), so the literal acceptance phrase `nao consome tokens` did not appear on a single line — the plan's line-based grep (and acceptance criterion) would not match it.
- **Fix:** Reworded the bullet so `"vai demorar, nao consome tokens (roda local), e mostra o progresso (pagina N de M)"` sits on one line; dropped the bold markers (also cleaner markdownlint-wise).
- **Verification:** `grep -c "nao consome tokens" mentor/novo-projeto.md` = 1; harness exits 0.
- **Committed in:** `ee4ca31` (Task 3 commit, before the commit was made).

---

**Total deviations:** 1 auto-fixed (1 bug). No scope creep.

## Known Stubs
None. The skill points to a real, populated bootstrap step; the bootstrap step surfaces the FIXED CLI from Plan 01; all backtick paths (`scripts/converte_livro.py`, `requirements-pdf.txt`, `mentor/novo-projeto.md`) resolve on disk (V-13 green).

## Issues Encountered
- The RTK proxy rewrites `grep` into a token-saving wrapper that occasionally renders matched lines oddly (showing `0:` line numbers / partial lines); cross-checked the load-bearing greps with the dedicated Grep tool and the harness itself. No code impact.
- Em-dash (`—`, U+2014) appears in mentor/novo-projeto.md (pre-existing convention throughout the file); it is NOT in the V-16 accent set, so V-16 stays green.

## Next Phase Readiness
- 07-03 can build on the wired invocation layer: the skill, the bootstrap step, and the registrations are in place and harness-green.
- The /converte-livro -> mentor/novo-projeto.md routing exception is documented in three surfaces, so downstream docs/audits will not mistake the missing mentor/converte-livro.md for drift.

## Self-Check: PASSED

All deliverables verified on disk; all 4 task commits present in git history (see below).
