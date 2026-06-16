---
phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md
plan: 02
subsystem: docs
tags: [markdown, progresso-template, retrieval, cross-file-contract, reference-md]

# Dependency graph
requires:
  - phase: 04-01
    provides: "Harness estatico check-phase4.sh + extract-fenced.sh (padrao anti-leak V-15 ja final, sem o token isolado retrieval)"
provides:
  - "Secao `## Agenda de retrieval` no template PROGRESSO.md (em mentor/reference.md), distinta de `## Dividas de aprendizado`"
  - "Contrato cross-file fixado: nome da secao `## Agenda de retrieval` + formato de entrada `- <conceito> -- revisitar na abertura do marco <NN>`"
affects: [04-03, 04-04]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Insercao de secao dentro de bloco cercado ```markdown como dono de contrato cross-file (verbatim copiado por writer/reader)"

key-files:
  created:
    - .planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/04-02-SUMMARY.md
  modified:
    - mentor/reference.md

key-decisions:
  - "Secao inserida entre `## Dividas de aprendizado` e `## Log` no template PROGRESSO.md (D-09; ambas debt-like forward-looking, mas distintas)"
  - "Padrao anti-leak ja estava resolvido upstream no plano 01 (forma de frase `retrieval practice|testing effect`), entao nenhum ajuste a check-phase4.sh foi necessario neste plano"

patterns-established:
  - "Dono do contrato: reference.md fixa o nome da secao + formato da entrada que fecha-marco.md (plano 03) e tutor.md (plano 04) copiam verbatim"

requirements-completed: [AVAL-02]

# Metrics
duration: 3min
completed: 2026-06-16
---

# Phase 4 Plan 02: Secao `## Agenda de retrieval` no template PROGRESSO.md Summary

**Inserida a secao `## Agenda de retrieval` no template PROGRESSO.md de `mentor/reference.md`, fixando o contrato cross-file (nome da secao + formato de entrada `- <conceito> -- revisitar na abertura do marco <NN>`) que os planos 03 (writer) e 04 (reader) copiam verbatim, livre de jargao de framework e de acentos.**

## Performance

- **Duration:** 3 min
- **Started:** 2026-06-16T01:31:34Z
- **Completed:** 2026-06-16T01:35:00Z
- **Tasks:** 1
- **Files modified:** 1

## Accomplishments
- Secao `## Agenda de retrieval` adicionada ao bloco ` ```markdown ` do template PROGRESSO.md (L247), entre `## Dividas de aprendizado` (L243) e `## Log` (L251)
- Formato de entrada de contrato `- <conceito> -- revisitar na abertura do marco <NN>` fixado em L249 -- a verdade byte-identica para os planos 03 e 04
- Duas secoes mantidas DISTINTAS (Agenda de retrieval vs. Dividas de aprendizado) -- D-09, fonte limpa para o tutor (D-02)
- CONS-01 preservado: zero jargao de framework dentro do fence (V-15 anti-leak == 0)

## Task Commits

Each task was committed atomically:

1. **Task 1: Inserir a secao `## Agenda de retrieval` no template PROGRESSO.md** - `5936d52` (feat)

_Nota TDD: tarefa de edicao de doc markdown sem runtime de teste. O ciclo RED/GREEN foi exercido via grep estatico -- RED: `## Agenda de retrieval` ausente (count 0) antes da edicao; GREEN: presente apos a edicao com anti-leak == 0. Por nao haver arquivo de teste separado, RED e GREEN ficaram no mesmo commit feat._

## Files Created/Modified
- `mentor/reference.md` - Adicionada a secao `## Agenda de retrieval` (com a linha de formato de entrada) no template PROGRESSO.md, entre `## Dividas de aprendizado` e `## Log`

## Decisions Made
- **Posicao da secao:** entre `## Dividas de aprendizado` e `## Log` (recomendacao do 04-RESEARCH Open Question 1; ambas sao secoes forward-looking, mas semanticamente distintas).
- **Conflito anti-leak "retrieval":** o plano 02 trazia uma NOTA pedindo ajustar `check-phase4.sh` para que o token isolado `retrieval` no nome da secao nao gerasse falso-positivo no check V-15. Esse ajuste JA ESTAVA resolvido upstream no plano 01 (wave 0), que autorou o padrao final `SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect` (forma de frase, sem o token isolado). Portanto NENHUMA edicao a `check-phase4.sh` foi feita neste plano -- o requisito da NOTA ja estava satisfeito. Verificado rodando o padrao final contra os blocos cercados de reference.md: resultado 0.

## Deviations from Plan

None - plan executed exactly as written. A NOTA ANTI-LEAK do plano (ajustar check-phase4.sh) ja estava satisfeita pelo padrao final autorado no plano 01; nenhuma alteracao adicional foi necessaria (ver Decisions Made).

## Issues Encountered
- O scripts dir da Fase 4 (`check-phase4.sh`, `extract-fenced.sh`) NAO esta presente neste worktree porque o plano 01 (wave 0) roda em worktree separado e ainda nao foi mesclado. Resolvido usando o `extract-fenced.sh` da Fase 2 (logica byte-identica ao clone do plano 01) para rodar o check anti-leak V-15 localmente. O `check-phase4.sh` completo sera executado pelo orquestrador no merge gate da wave, quando todos os worktrees estiverem juntos.

## Verification Results
- `rg -n "^## Agenda de retrieval" mentor/reference.md` -> 1 linha (L247) -- V-08 PASS
- `rg -n "^## Dividas de aprendizado" mentor/reference.md` -> L243, linha DISTINTA da Agenda -- V-09 PASS
- `rg -n "revisitar na abertura do marco" mentor/reference.md` -> L249 com o formato de contrato -- PASS
- `extract-fenced.sh mentor/reference.md | rg -c "SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect"` -> 0 -- V-15 anti-leak PASS
- Sem acentos introduzidos no bloco inserido (sed L243-252 | rg de chars acentuados -> vazio)

## Next Phase Readiness
- Contrato fixado e pronto: plano 03 (`fecha-marco.md`, writer) e plano 04 (`tutor.md`, reader) devem copiar VERBATIM o nome da secao `## Agenda de retrieval` e o formato `- <conceito> -- revisitar na abertura do marco <NN>`.
- O merge gate da wave deve rodar `check-phase4.sh` + o CONTRACT cross-file grep (V-13) para confirmar que os 3 arquivos concordam.

## Self-Check: PASSED

- FOUND: `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/04-02-SUMMARY.md`
- FOUND: `mentor/reference.md`
- FOUND: commit `5936d52`

---
*Phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md*
*Completed: 2026-06-16*
