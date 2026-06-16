---
phase: 05-persona-e-feedback-metodo-md-debug-md
plan: 01
subsystem: testing
tags: [shell, awk, ripgrep, static-gate, anti-leak, harness]

# Dependency graph
requires:
  - phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md
    provides: extract-fenced.sh + check-phase4.sh (scaffold do harness de verificacao estatica)
provides:
  - "scripts/extract-fenced.sh (clone byte-a-byte) — filtro stdin->stdout que isola blocos cercados"
  - "scripts/check-phase5.sh — gate estatico PASS/FAIL codificando V-01..V-18"
  - "Baseline coerente: positivos red, V-16/V-17/V-18 green (Wave 0)"
affects: [05-02, 05-03]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Static-gate harness por fase (clone do scaffold das Fases 2/4)"
    - "Anti-leak (V-17) escopado a blocos cercados via extract-fenced.sh"
    - "ANCHOR-RESOLVE no heading literal, nunca slug reconstruido"

key-files:
  created:
    - .planning/phases/05-persona-e-feedback-metodo-md-debug-md/scripts/extract-fenced.sh
    - .planning/phases/05-persona-e-feedback-metodo-md-debug-md/scripts/check-phase5.sh
  modified: []

key-decisions:
  - "V-14 implementado via awk (isola a secao 'Conduta por marco (ciclo)' e conta itens 1-5) — count simples nao escopa a secao"
  - "V-18 implementado como check_zero defensivo sobre AGENTS.md/.claude/ (anti-drift P12)"

patterns-established:
  - "Harness Wave 0: scripts existem e rodam ANTES das edicoes; positivos em red ate 05-02/05-03 entregarem GREEN"

requirements-completed: [AVAL-05, AVAL-06, CONS-01]

# Metrics
duration: 8min
completed: 2026-06-16
---

# Phase 5 Plan 01: Harness de verificacao estatica (Wave 0) Summary

**Clone do harness da Fase 4 para a Fase 5: extract-fenced.sh byte-a-byte + check-phase5.sh codificando os 18 checks V-01..V-18 (positivos CONS-01/AVAL-05/AVAL-06/Criterio 4, ANCHOR-RESOLVE, anti-leak escopado a blocos cercados, anti-drift de adaptadores).**

## Performance

- **Duration:** ~8 min
- **Completed:** 2026-06-16
- **Tasks:** 2
- **Files modified:** 2 (ambos criados)

## Accomplishments
- `extract-fenced.sh` clonado byte-a-byte da Fase 4 (`diff` vazio, logica awk `inside = !inside` preservada); isola corretamente o conteudo de blocos cercados.
- `check-phase5.sh` autorado a partir do scaffold de `check-phase4.sh` (helpers `count`/`check_min`/`check_zero`/`check_has` verbatim), codificando V-01..V-18.
- V-17 (anti-leak) consome `extract-fenced.sh` e roda SO sobre blocos cercados, com `LEAK_PAT` estendido com o jargao novo da Fase 5 (`feed-up`/`feed-back`/`feed-forward`/`Hattie`/`formativ`/`auto-explicacao`).
- Baseline Wave 0 coerente com a convencao das Fases 2/4: V-16 (ANCHOR-RESOLVE, 3 headings ja existem), V-17 (leak-met + leak-dbg) e V-18 (anti-drift) PASSAM; os checks de prosa ainda nao escrita falham; exit code 7 (!= 0) — esperado e correto antes das edicoes.

## Task Commits

1. **Task 1: Clonar extract-fenced.sh byte-a-byte** - `b9c8b8d` (chore)
2. **Task 2: Autorar check-phase5.sh com V-01..V-18** - `e827e3d` (test)

## Files Created/Modified
- `.planning/phases/05-.../scripts/extract-fenced.sh` - Filtro stdin->stdout que imprime so o conteudo dentro de blocos cercados ``` (clone byte-a-byte da Fase 4).
- `.planning/phases/05-.../scripts/check-phase5.sh` - Gate estatico PASS/FAIL que codifica V-01..V-18 (positivos + ANCHOR-RESOLVE V-16 + anti-leak V-17 + anti-drift V-18).

## Decisions Made
- **V-14 via awk, nao count simples:** o criterio (preservar os 5 itens do ciclo) exige contar itens numerados DENTRO da secao "Conduta por marco (ciclo)". Um `rg -c '^[1-5]\.'` no doc inteiro contaria itens de outras secoes; o `awk` isola a secao (do heading ate o proximo `## `) e conta so ali. Resultado baseline: 5 (PASS).
- **V-18 como check_zero defensivo:** soma `rg -c` sobre `AGENTS.md` e `.claude/` via `awk -F:` para nao quebrar se `.claude/` tiver subpastas; se `rg` nao achar arquivos a soma -> 0 (PASS no baseline).

## Deviations from Plan

None - plan executed exactly as written. Os 18 checks foram codificados literalmente conforme o `<action>` do Task 2 (incluindo os idioms sugeridos para V-14 e V-18); o estilo (portugues sem acentos, paths em backticks) e o scaffold da Fase 4 foram preservados.

## Issues Encountered

Nenhum. Nota sobre o baseline: o plano descreve "os positivos V-01..V-15 falham" como expectativa; na pratica varios positivos de PRESERVACAO ja passam no baseline (V-02, V-06, V-07, V-10, V-11, V-12, V-13, V-14) porque casam literais/estruturas que ja existem nos docs hoje. Isso e esperado e correto — esses checks verificam que conteudo pre-existente nao foi destruido, e o GREEN total vira quando 05-02/05-03 escreverem a prosa nova (V-01, V-03, V-04, V-05, V-08, V-09, V-15). O criterio de aceite do Wave 0 (scripts existem, rodam sem erro de shell, V-16/V-17/V-18 passam, exit != 0) foi atendido.

## Next Phase Readiness
- Harness pronto e executavel: `sh .planning/phases/05-.../scripts/check-phase5.sh`.
- 05-02 e 05-03 podem editar `mentor/metodo.md` e `mentor/debug.md` com prova objetiva por check.
- Lembrete A1 / Pitfall 4: ao adicionar os links D-09, confirmar o `#slug` exato por 1 clique manual no gate da fase (o V-16 prova so que o heading literal existe).

## Self-Check: PASSED

- `scripts/extract-fenced.sh` — FOUND
- `scripts/check-phase5.sh` — FOUND
- Commit `b9c8b8d` (Task 1) — FOUND
- Commit `e827e3d` (Task 2) — FOUND
