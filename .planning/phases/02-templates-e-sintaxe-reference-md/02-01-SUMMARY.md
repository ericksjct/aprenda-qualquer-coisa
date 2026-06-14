---
phase: 02-templates-e-sintaxe-reference-md
plan: 01
subsystem: testing
tags: [shell, awk, ripgrep, static-verification, anti-leak, posix-sh]

# Dependency graph
requires:
  - phase: 01-foundation
    provides: mentor/reference.md e mentor/fundamentos.md (alvos da verificacao estatica)
provides:
  - "extract-fenced.sh: extrator de blocos cercados que isola conteudo dentro de ``` (habilita CONS-01 sem falso-positivo)"
  - "check-phase2.sh: smoke-test estatico consolidando os 9 comandos rg da Validation Architecture (gate da fase)"
affects: [02-02, 02-03, plan-check, verify-work]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Verificacao estatica via awk (toggle de cerca) + rg, sem framework de runtime"
    - "Gate de fase como script sh: exit = numero de falhas; positivos >= N, anti-leak == 0"

key-files:
  created:
    - .planning/phases/02-templates-e-sintaxe-reference-md/scripts/extract-fenced.sh
    - .planning/phases/02-templates-e-sintaxe-reference-md/scripts/check-phase2.sh
  modified: []

key-decisions:
  - "Extrator implementado com awk (toggle de estado de cerca) em vez de loop de shell, por robustez"
  - "ANTI-LEAK e a unica checagem negativa (== 0); demais sao positivas (>= N); diferenca comentada no script"
  - "check-phase2.sh chama extract-fenced.sh via dirname \"$0\" para portabilidade de path"

patterns-established:
  - "Anti-leak boundary: grep negativo roda SO contra a saida do extrator (conteudo de bloco), nunca contra a prosa"
  - "Baseline esperado pre-edicao: positivos falham ate planos 02/03 editarem reference.md; ANTI-LEAK ja verde"

requirements-completed: []

# Metrics
duration: 12min
completed: 2026-06-14
---

# Phase 2 Plan 01: Extrator de blocos cercados + smoke-test estatico Summary

**Extrator awk que isola conteudo dentro de blocos ``` de reference.md, mais smoke-test sh consolidando os 9 comandos rg da Validation Architecture como gate da Fase 2.**

## Performance

- **Duration:** ~12 min
- **Completed:** 2026-06-14
- **Tasks:** 2
- **Files modified:** 2 (ambos criados)

## Accomplishments
- `extract-fenced.sh`: isola SO o conteudo dentro de blocos cercados via toggle de estado awk, habilitando o grep negativo CONS-01 sem falso-positivo na prosa legitima
- `check-phase2.sh`: roda as 9 checagens da Per-Task Verification Map (EST-01a/b, EST-04, EST-02, CARGA-01/02/03, ANCHOR-RESOLVE, ANTI-LEAK), imprime PASS/FAIL e retorna exit = numero de falhas
- Baseline validado: no estado pre-edicao a checagem ANTI-LEAK ja passa (0 ocorrencias) e ANCHOR-RESOLVE resolve as 2 ancoras esperadas em fundamentos.md

## Task Commits

Each task was committed atomically:

1. **Task 1: Extrator de blocos cercados (extract-fenced.sh)** - `dcd1b4b` (feat)
2. **Task 2: Smoke-test estatico consolidado (check-phase2.sh)** - `51452d9` (feat)

## Files Created/Modified
- `.planning/phases/02-templates-e-sintaxe-reference-md/scripts/extract-fenced.sh` - extrator awk de blocos cercados (default mentor/reference.md), com guarda de arquivo inexistente
- `.planning/phases/02-templates-e-sintaxe-reference-md/scripts/check-phase2.sh` - smoke-test/gate da fase com helpers check_min, check_zero, check_has e resolucao de ancora

## Decisions Made
- Extrator usa awk com toggle `inside` (alterna na cerca, pula a propria cerca) em vez de loop de shell, por robustez POSIX
- ANTI-LEAK isolado num helper `check_zero` separado dos `check_min` positivos, com comentario explicando que e a unica checagem negativa
- `check-phase2.sh` resolve o path do extrator via `dirname "$0"` para funcionar de qualquer cwd
- Adicionada guarda de "arquivo nao encontrado" no extrator (exit 2) — robustez alem do esqueleto do plano

## Deviations from Plan

None - plan executed exactly as written. (O extrator ganhou uma guarda de arquivo inexistente e o smoke-test ganhou um helper `check_has` reutilizavel para a resolucao de ancora; ambos sao refinamentos de robustez dentro do escopo do plano, nao mudancas de comportamento especificado.)

## Issues Encountered
None. Todos os acceptance criteria de ambas as tasks passaram na primeira execucao. Nota de ambiente: git avisa que LF sera convertido para CRLF (autocrlf) — esperado no Windows e sem efeito no comportamento dos scripts sob Git Bash.

## Known Stubs
None. Ambos os scripts sao funcionais e verificados. As checagens positivas que aparecem como FAIL no baseline NAO sao stubs — sao o comportamento de gate correto: ficam verdes quando os planos 02 e 03 editarem `reference.md`.

## Next Phase Readiness
- Gate da fase pronto: planos 02-02 e 02-03 podem rodar `sh .../check-phase2.sh` apos cada edicao de bloco cercado para verificacao continua
- ANTI-LEAK (CONS-01) operacional desde o baseline; protege contra vazamento de jargao de framework para dentro dos artefatos do aluno
- Sem blockers

## Self-Check: PASSED

- FOUND: scripts/extract-fenced.sh
- FOUND: scripts/check-phase2.sh
- FOUND: 02-01-SUMMARY.md
- FOUND commit: dcd1b4b (Task 1)
- FOUND commit: 51452d9 (Task 2)

---
*Phase: 02-templates-e-sintaxe-reference-md*
*Completed: 2026-06-14*
