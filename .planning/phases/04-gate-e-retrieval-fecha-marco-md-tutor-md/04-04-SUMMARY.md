---
phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md
plan: 04
subsystem: docs
tags: [markdown, tutor-md, retrieval-practice, sdt, cross-file-contract, anti-leak]

# Dependency graph
requires:
  - phase: 04-01
    provides: "Harness estatico check-phase4.sh + extract-fenced.sh (gate FINAL da fase, V-01..V-15)"
  - phase: 04-02
    provides: "Contrato cross-file: nome da secao `## Agenda de retrieval` + formato `- <conceito> -- revisitar na abertura do marco <NN>` em reference.md"
provides:
  - "Passo de Recuperacao ativa em mentor/tutor.md ANTES do recap (D-01), lendo ESTRITAMENTE a `## Agenda de retrieval` (D-02), formativo (D-03), skip-on-empty (D-04)"
  - "Fechamento de sessao cobra exatamente 1 proxima acao (D-12) com ancora SDT na prosa (D-13); Log permanece sem jargao (anti-leak CONS-01)"
  - "Ritual de abertura do tutor renumerado: Passo 1 Recuperacao ativa, 2 Abertura, 3 Conduzir, 4 Revisar, 5 Fechamento"
affects: []

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Reader do contrato cross-file: tutor.md copia VERBATIM o nome da secao `## Agenda de retrieval` fixado por reference.md (plano 02)"
    - "Recall ANTES do recap (V-01) -- ordem por numero de linha garante que o recap nao vaza a resposta da recuperacao (Pitfall 2)"

key-files:
  created:
    - .planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/04-04-SUMMARY.md
    - .planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/deferred-items.md
  modified:
    - mentor/tutor.md

key-decisions:
  - "Gate completo da fase (V-04..V-13-fch) deferido ao merge gate do orquestrador: as 7 falhas sao todas de fecha-marco.md (plano 03, irmao da wave 2 nao mesclado neste worktree), fora do escopo deste plano"
  - "Log line (`proxima acao: <acao concreta de 1 linha>`) mantida intacta sem jargao -- o jargao SDT entra so na prosa do procedimento (anti-leak CONS-01)"

patterns-established:
  - "Ordering check (V-01): heading de Recuperacao ativa em L37 < Abertura da sessao em L52, garantindo recall antes do recap"

requirements-completed: [AVAL-01, ENG-01]

# Metrics
duration: 2min
completed: 2026-06-16
---

# Phase 4 Plan 04: Recuperacao ativa + proxima acao unica em tutor.md Summary

**Inserido em `mentor/tutor.md` um passo proprio de "Recuperacao ativa" ANTES do recap que le ESTRITAMENTE a `## Agenda de retrieval` do PROGRESSO.md (formativo, skip-on-empty), e amarrado o fechamento de sessao a exatamente 1 proxima acao com ancora SDT na prosa -- o ritual de abertura foi renumerado em cascata e o Log do aluno permanece sem jargao.**

## Performance

- **Duration:** ~2 min
- **Started:** 2026-06-16T01:37:02Z
- **Completed:** 2026-06-16T01:39:09Z
- **Tasks:** 2
- **Files modified:** 1 (mentor/tutor.md) + 1 criado (deferred-items.md)

## Accomplishments

- Novo `## Passo 1 — Recuperacao ativa (antes do recap)` inserido ANTES do recap (D-01): le ESTRITAMENTE a `## Agenda de retrieval`, sem pergunta ad-hoc (D-02), formativo sem penalidade -> vira divida e reaponta a aula (D-03), pula quando a agenda esta vazia (D-04)
- Link de retrieval practice -> `fundamentos.md#frameworks-foundational-load-bearing` na prosa do novo passo
- Ritual renumerado em cascata sem duplicatas: Passo 0 Restaurar, 1 Recuperacao ativa, 2 Abertura, 3 Conduzir, 4 Revisar, 5 Fechamento
- Fechamento (Passo 5) agora cobra "exatamente 1 proxima acao concreta (se virou lista, corte para 1)" (D-12)
- Prosa do fechamento nomeia SDT com link supporting + ressalva honesta de relatedness em solo+IA (D-13), seguindo a forma modelada em novo-projeto.md L150
- Log line do aluno mantida intacta e sem jargao (anti-leak CONS-01)
- Dois anti-padroes co-localizados: disparar recuperacao sem entrada na agenda; fechar com lista em vez de exatamente 1

## Task Commits

Cada task foi commitada atomicamente (com `--no-verify`, modo executor paralelo em worktree):

1. **Task 1: Inserir passo Recuperacao ativa antes do recap + renumerar** - `b7759d8` (feat)
2. **Task 2: Fechamento cobra 1 proxima acao + ancora SDT; rodar o gate** - `873ec95` (feat)

_Nota TDD (Task 1): tarefa de edicao de doc markdown sem runtime de teste. O ciclo RED/GREEN foi exercido via grep estatico -- RED: `Recuperacao ativa`/`Agenda de retrieval`/skip-on-empty/link foundational todos count 0 antes da edicao; GREEN: presentes apos a edicao com ordem L37<L52. Por nao haver arquivo de teste separado, RED e GREEN ficaram no mesmo commit feat (mesma convencao do plano 02)._

## Files Created/Modified

- `mentor/tutor.md` - Inserido o passo de Recuperacao ativa antes do recap, renumerado o ritual (1..5), reforcada a proxima acao unica no fechamento com ancora SDT na prosa, e adicionados 2 anti-padroes
- `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/deferred-items.md` - Registro do gate completo deferido ao merge gate (falhas de fecha-marco.md / plano 03)

## Decisions Made

- **Gate completo deferido ao merge gate:** `check-phase4.sh` retorna 7 fail(s) NESTE worktree, e todas as 7 sao checks de propriedade do `fecha-marco.md` (plano 03, irmao da wave 2 ainda nao mesclado a esta base cc2da40). Nao editei `fecha-marco.md` (SCOPE BOUNDARY: outro plano e dono) nem `check-phase4.sh` (propriedade do plano 01). O orquestrador roda o gate completo apos mesclar os worktrees da wave -- ai V-04..V-13-fch ficam satisfeitos pelo plano 03 e o gate vira `== 0 fail(s) ==`.
- **Anti-leak no Log:** a linha do Log que o aluno LE (`proxima acao: <acao concreta de 1 linha>`) ficou intacta, sem jargao. O jargao SDT/retrieval entra so na prosa do procedimento do tutor (CONS-01).

## Deviations from Plan

None - plano executado exatamente como escrito. A unica nuance e operacional, nao uma deviation: a Task 2 instrui "rode o gate completo e ajuste o arquivo correspondente ate ficar verde"; como o arquivo que faltava (`fecha-marco.md`) e de outro plano/worktree (plano 03) nao mesclado aqui, o ajuste e impossivel e indesejavel daqui -- o gate completo fica para o merge gate do orquestrador (ver Decisions Made e deferred-items.md). Todos os checks de propriedade deste plano (tutor.md) estao verdes.

## Verification Results

Gate `check-phase4.sh` neste worktree (esperado: checks de tutor/reference/fundamentos verdes; checks de fecha-marco vermelhos por nao-merge):

- V-01 PASS got=2 (heading Recuperacao ativa L37 < Abertura L52 -- recall antes do recap)
- V-02 PASS got=2 (le `Agenda de retrieval`, fonte estrita)
- V-03 PASS got=3 (skip-on-empty; "se a ## Agenda de retrieval esta vazia" casa `[Aa]genda.*vazia`)
- V-07 PASS, V-08 PASS, V-09 PASS (reference.md / fecha-marco pre-existente)
- V-11a PASS got=2 (exatamente 1 proxima acao no tutor)
- V-12-supp-tut PASS got=1, V-12-sdt-anchor PASS got=1 (link SDT + ressalva na prosa do tutor)
- V-13-ref PASS, V-13-tut PASS (contrato `Agenda de retrieval` byte-identico reference<->tutor)
- V-14 PASS (3 ancoras resolvem em fundamentos.md), ANTI-LEAK (V-15) PASS got=0
- FAIL (deferido ao merge gate -- todos fecha-marco.md / plano 03): V-04, V-05, V-06, V-10, V-11b, V-12-supp-fch, V-13-fch
- Log line do aluno sem `SDT` -- anti-leak CONS-01 PASS
- Sem letras acentuadas introduzidas nas regioes editadas

## TDD Gate Compliance

Plano de tipo `execute` (nao `type: tdd`); apenas a Task 1 tinha `tdd="true"`. Para edicao de doc markdown sem arquivo de teste separado, RED (grep count 0) e GREEN (grep presente) foram exercidos no mesmo commit feat, seguindo a convencao ja estabelecida pelo plano 02. Nao ha commit `test(...)` separado por design (sem suite de teste de runtime para esta categoria de mudanca).

## Known Stubs

None. Nenhum valor vazio/placeholder/TODO introduzido; o passo de Recuperacao ativa e funcionalmente completo (le a fonte real `## Agenda de retrieval`, escrita pelo plano 03 no fluxo real).

## Next Phase Readiness

- Merge gate do orquestrador deve mesclar os worktrees dos planos 03 e 04 e rodar `check-phase4.sh` -> esperado `== 0 fail(s) ==` (V-04..V-13-fch satisfeitos por fecha-marco.md do plano 03).
- 1 verificacao manual de hyperlink pendente (A1: `#sdt-relatedness-em-solo-ia` no renderer) antes do /gsd-verify-work, conforme `<verification>` do plano.
- Contrato cross-file confirmado byte-identico entre reference.md e tutor.md; falta apenas fecha-marco.md (plano 03) entrar no merge para fechar V-13 nos 3 arquivos.

## Self-Check: PASSED

- FOUND: `mentor/tutor.md`
- FOUND: `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/deferred-items.md`
- FOUND: commit `b7759d8` (Task 1)
- FOUND: commit `873ec95` (Task 2)

---
*Phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md*
*Completed: 2026-06-16*
