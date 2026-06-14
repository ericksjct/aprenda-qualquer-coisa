---
phase: 03-bootstrap-com-stage-2-novo-projeto-md
plan: 01
subsystem: docs
tags: [mentor, progresso-md, novo-projeto, backward-design, mastery, anti-leak]

# Dependency graph
requires:
  - phase: 02-templates-e-sintaxe-reference-md
    provides: formato verbo-capacidade canonico no nivel de passo (ao terminar, voce consegue <verbo> <conceito>)
provides:
  - Campo **Capacidade:** na arvore de marcos do template PROGRESSO.md (mentor/reference.md), 2 blocos
  - Instrucao no Passo 5 de novo-projeto.md para gravar a frase de capacidade por marco (D-01 marco)
  - Guardrail de leveza D-04 (teto rigido: exatamente 1 frase por marco)
  - Reforco D-03 (dimensionar o primeiro marco como o menor possivel)
affects: [04-fecha-marco, mastery-gate]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "PAR DE EDICAO ACOPLADA (D-02): campo no template + instrucao de preenchimento nascem juntos"
    - "Dois registros, dois publicos (Pattern 3 anti-leak): instrucao ao agente nomeia o framework; valor gravado pelo aluno e verbo puro"
    - "Edicao 100% aditiva: nenhum bullet/campo pre-existente reescrito"

key-files:
  created: []
  modified:
    - mentor/reference.md
    - mentor/novo-projeto.md

key-decisions:
  - "Campo Capacidade colado abaixo da User Story (nasce junto com a historia), nao em secao separada"
  - "Anti-leak CONS-01: valor placeholder do campo e so o verbo de capacidade puro, zero jargao no bloco lido pelo aluno"

patterns-established:
  - "PAR DE EDICAO ACOPLADA: campo de template (dono reference.md) + instrucao de preenchimento (novo-projeto.md) editados no mesmo plano"
  - "Backward design conceitual no nivel de marco: definir a capacidade-alvo antes de detalhar os passos"

requirements-completed: [EST-03]

# Metrics
duration: 4min
completed: 2026-06-14
---

# Phase 3 Plan 01: Stage 2 no nivel de marco (campo Capacidade + instrucao Passo 5) Summary

**Campo `**Capacidade:**` adicionado na arvore de marcos do template PROGRESSO.md e Passo 5 de novo-projeto.md instruido a grava-lo por marco, com guardrail de 1 frase e reforco de primeiro marco menor — o contrato que o mastery gate da Fase 4 vai consumir.**

## Performance

- **Duration:** 4 min
- **Started:** 2026-06-14T22:38:00Z
- **Completed:** 2026-06-14T22:42:32Z
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments
- Campo `**Capacidade:** ao terminar, voce consegue <verbo> <conceito>` inserido nos 2 blocos de marco (00 Walking Skeleton e 01) do template PROGRESSO.md em `mentor/reference.md`, abaixo da User Story
- Passo 5 de `mentor/novo-projeto.md` ganhou 3 costuras aditivas: gravar a frase de capacidade colada a User Story (D-01 marco), teto rigido de exatamente 1 frase (D-04), e dimensionar o primeiro marco como o menor possivel (D-03)
- PAR ACOPLADO satisfeito: o campo do template e a instrucao de preenchimento existem juntos
- Anti-leak verde: zero jargao de framework (Bloom/Stage 2/maestria/backward design) dentro do bloco `## Marcos` lido pelo aluno; a instrucao ao agente no Passo 5 nomeia "backward design" (permitido na prosa lida pelo agente)

## Task Commits

Each task was committed atomically:

1. **Task 1: Adicionar campo Capacidade no template PROGRESSO.md (reference.md)** - `660e2f4` (feat)
2. **Task 2: Instruir Passo 5 a gravar frase de capacidade + D-04 + D-03 (novo-projeto.md)** - `52bf712` (feat)

## Files Created/Modified
- `mentor/reference.md` - Campo `**Capacidade:**` adicionado nos 2 blocos de marco do template PROGRESSO.md (2 insercoes)
- `mentor/novo-projeto.md` - Passo 5 ganhou 3 bullets aditivos: instrucao de gravar a frase, guardrail D-04, reforco D-03 (11 insercoes)

## Decisions Made
- None - followed plan as specified. Textos literais e posicoes de insercao seguiram exatamente as ancoras textuais do plano; estado real dos arquivos confirmou os offsets documentados (reference.md:225-239, novo-projeto.md:68-81).

## Deviations from Plan

None - plan executed exactly as written. Ambas as edicoes foram 100% aditivas; nenhum bullet ou campo pre-existente reescrito; nenhuma secao "## Stage 2" criada; nenhum commit com delecoes.

## Issues Encountered
None.

## User Setup Required
None - no external service configuration required.

## Verification Results
- `grep -c "^\*\*Capacidade:\*\* ao terminar, voce consegue" mentor/reference.md` == 2 (PASS)
- `grep "exatamente 1 frase" mentor/novo-projeto.md` retorna match (PASS)
- `grep "frase de capacidade" mentor/novo-projeto.md` retorna match (PASS)
- `grep "ao terminar, voce consegue" mentor/novo-projeto.md` retorna match (PASS)
- `grep "primeiro marco" mentor/novo-projeto.md` retorna match (PASS)
- `grep "backward design" mentor/novo-projeto.md` retorna match na prosa do Passo 5 (PASS, esperado)
- Anti-leak: `awk '/^## Marcos/{f=1;next} /^## /{f=0} f' mentor/reference.md | grep "Bloom\|Stage 2\|maestria\|backward design"` vazio (PASS - CLEAN)
- `grep "## Stage 2" mentor/novo-projeto.md` vazio (PASS - nenhuma secao nova)
- Diff NAO toca `.claude/` nem `AGENTS.md` (PASS - fonte-unica preservada)

## Next Phase Readiness
- O contrato `**Capacidade:**` esta gravado no template e instruido no bootstrap. A Fase 4 (`fecha-marco.md`) pode agora PROCURAR essa frase no `PROGRESSO.md` para o mastery gate.
- EST-03 (Criterios 1 e 2 do ROADMAP) coberto.

## Self-Check: PASSED

- FOUND: mentor/reference.md
- FOUND: mentor/novo-projeto.md
- FOUND: .planning/phases/03-bootstrap-com-stage-2-novo-projeto-md/03-01-SUMMARY.md
- FOUND: commit 660e2f4 (Task 1)
- FOUND: commit 52bf712 (Task 2)

---
*Phase: 03-bootstrap-com-stage-2-novo-projeto-md*
*Completed: 2026-06-14*
