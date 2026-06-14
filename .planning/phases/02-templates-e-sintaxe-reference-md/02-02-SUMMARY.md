---
phase: 02-templates-e-sintaxe-reference-md
plan: 02
subsystem: docs
tags: [mentor-method, reference-md, backward-design, capacidade, anti-theory-leak]

# Dependency graph
requires:
  - phase: 02-01
    provides: "extract-fenced.sh + check-phase2.sh (anti-leak verifier e smoke-test gate)"
provides:
  - "Linha 'Objetivo (capacidade):' em cada passo do template CAMINHO.md (acima de Entregavel)"
  - "Template de aula '## Objetivo do passo' espelhando capacidade + artefato-como-evidencia"
  - "Campo 'DONE:' do scaffold reenquadrado como evidencia observavel de capacidade"
  - "Forma do campo de capacidade que a Fase 3 (novo-projeto.md Stage 2) vai consumir"
affects: [02-03, novo-projeto.md, fundamentos.md, fecha-marco.md]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Capacidade-primeiro / artefato-como-evidencia (backward design) tecido nos 3 templates do aluno"
    - "Edicoes DENTRO de blocos cercados sempre validadas com extract-fenced.sh (anti-theory-leak, CONS-01)"

key-files:
  created:
    - .planning/phases/02-templates-e-sintaxe-reference-md/02-02-SUMMARY.md
  modified:
    - mentor/reference.md

key-decisions:
  - "Verbo de capacidade entra como placeholder <verbo> <conceito> puro — zero jargao de framework dentro dos blocos cercados (CONS-01)"
  - "DONE reenquadrado para combater proxy-completion: evidencia de capacidade demonstrada, nao 'o codigo compila'"
  - "Ordem fixa dos campos do scaffold (META..PISTA) preservada; so o TEXTO de DONE mudou (CONVENTIONS.md)"

patterns-established:
  - "Fio do verbo de capacidade: declarado no CAMINHO, espelhado na aula, cobrado no DONE (alinhamento construtivo)"
  - "O 'porque' teorico fica fora dos blocos cercados — vai na prosa via hyperlink no plano 02-03 (D-04)"

requirements-completed: [EST-01]

# Metrics
duration: 7min
completed: 2026-06-14
---

# Phase 2 Plan 02: Fio do verbo de capacidade nos templates Summary

**Tecido o fio capacidade-primeiro/artefato-como-evidencia (EST-01, backward design) nos 3 templates do aluno em `mentor/reference.md` — CAMINHO, aula e scaffold — sem vazar nenhum jargao de framework para dentro dos blocos cercados (CONS-01).**

## Performance

- **Duration:** 7 min
- **Started:** 2026-06-14T15:16:00Z
- **Completed:** 2026-06-14T15:23:00Z
- **Tasks:** 2
- **Files modified:** 1 (mentor/reference.md)

## Accomplishments
- Z3: linha `- Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>` inserida em P01 e P02 do template CAMINHO.md, exatamente acima de `Entregavel:` (capacidade como norte, entregavel como evidencia).
- Z4: corpo de `## Objetivo do passo` do template de aula reescrito para espelhar CAPACIDADE + ARTEFATO (antes so descrevia o entregavel), alinhando a aula com a nova linha do CAMINHO.
- Z5: campo `DONE:` do scaffold reenquadrado como evidencia observavel de que a capacidade foi adquirida (combate proxy-completion), com a ordem inviolavel dos campos (META..PISTA) preservada.
- Anti-leak (CONS-01) verde apos cada commit: 0 jargao de framework dentro dos blocos cercados.

## Task Commits

Each task was committed atomically:

1. **Task 1: Linha "Objetivo (capacidade):" em cada passo do CAMINHO (Z3)** - `6256549` (feat)
2. **Task 2: Espelhar capacidade+artefato na aula (Z4) e reenquadrar DONE do scaffold (Z5)** - `bb0e4a3` (feat)

_Note: SUMMARY.md committed separately in worktree mode (orchestrator owns STATE.md/ROADMAP.md)._

## Files Created/Modified
- `mentor/reference.md` - Editado em 3 zonas: linha de capacidade nos passos do CAMINHO (Z3), objetivo da aula espelhando capacidade+artefato (Z4), campo DONE do scaffold reenquadrado (Z5).
- `.planning/phases/02-templates-e-sintaxe-reference-md/02-02-SUMMARY.md` - Este resumo.

## Decisions Made
- Mantido o placeholder `<verbo> <conceito>` como verbo concreto de acao (template, nao instancia) — nunca a palavra "Bloom" ou qualquer nome de framework, respeitando a fronteira anti-theory-leak.
- DONE explicitamente contrasta "ja consegue demonstrar a capacidade" vs. "o codigo compila", para o aluno nao confundir conclusao mecanica com aprendizado.
- A justificativa teorica (backward design / constructive alignment) NAO foi inserida aqui por design — fica para a prosa do plano 02-03 via hyperlink (D-04). Este plano so insere os campos em linguagem pura.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered
- O smoke-test `check-phase2.sh` usa paths relativos (`mentor/reference.md`) e o helper `extract-fenced.sh` via `$DIR`; precisa ser rodado a partir da raiz do repo (nao do diretorio `scripts/`). Rodando da raiz, os criterios deste plano passam: EST-01a (got=2), EST-01b (got=1), ANTI-LEAK (got=0).
- Os FAILs restantes do smoke-test (EST-04, EST-02, CARGA-01, CARGA-03) sao de OUTROS planos (02-03 e os de `fundamentos.md`) — fora do escopo deste plano (que so cobre EST-01). Esperado e correto neste estagio.

## User Setup Required
None - no external service configuration required.

## Next Phase Readiness
- A FORMA do campo de capacidade esta estabelecida e pronta para o plano 02-03 (prosa + hyperlinks D-04) e para a Fase 3 (`novo-projeto.md` Stage 2) consumir.
- `extract-fenced.sh` / `check-phase2.sh` continuam o gate anti-leak para qualquer edicao futura de blocos cercados.

## Self-Check: PASSED

- FOUND: mentor/reference.md (modified)
- FOUND: .planning/phases/02-templates-e-sintaxe-reference-md/02-02-SUMMARY.md
- FOUND commit: 6256549 (Task 1)
- FOUND commit: bb0e4a3 (Task 2)
- Acceptance: EST-01a got=2, EST-01b got=1, ANTI-LEAK got=0, scaffold field order intact, 0 accents.

---
*Phase: 02-templates-e-sintaxe-reference-md*
*Completed: 2026-06-14*
