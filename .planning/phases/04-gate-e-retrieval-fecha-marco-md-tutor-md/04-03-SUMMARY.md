---
phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md
plan: 03
subsystem: docs
tags: [markdown, fecha-marco, mastery-gate, retrieval, cross-file-contract, sdt]

# Dependency graph
requires:
  - phase: 04-01
    provides: "Harness estatico check-phase4.sh + extract-fenced.sh (padrao anti-leak V-15)"
  - phase: 04-02
    provides: "Contrato cross-file fixado em reference.md: secao `## Agenda de retrieval` + formato `- <conceito> -- revisitar na abertura do marco <NN>`"
provides:
  - "Passo 1 de fecha-marco.md como mastery gate: criterio de capacidade (le **Capacidade:** do PROGRESSO.md) + 1 pergunta de extensao/transferencia, bloqueante-formativo"
  - "Passo 4 escreve 1 entrada na `## Agenda de retrieval` (lado WRITER do loop AVAL-02), formato byte-identico ao contrato do plano 02"
  - "Checkpoint final cobra exatamente 1 proxima acao concreta (D-12), ancorada em SDT na prosa (D-13)"
affects: [04-04]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "fecha-marco.md e o WRITER do contrato cross-file: copia verbatim o nome da secao e o formato de entrada que reference.md (plano 02) fixou; tutor.md (plano 04) e o READER"
    - "Anti-leak editorial: a prosa do procedimento pode nomear mastery/SDT, mas o artefato que o aluno LE (entrada da agenda, proxima acao no Log) fica sem jargao"

key-files:
  created:
    - .planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/04-03-SUMMARY.md
  modified:
    - mentor/fecha-marco.md

key-decisions:
  - "Passo 1 renomeado para `## Passo 1 — Mastery gate: verificacao do \"done\"`, nomeando o framework com link a fundamentos.md#frameworks-supporting-ancoram-um-doc"
  - "Os 3 checkboxes originais (codigo roda / explica / User Story) foram PRESERVADOS; capacidade e extensao foram ADICIONADOS (5 checkboxes no total)"
  - "Item de agenda (Passo 4, item 6) mantido DISTINTO do item de dividas de aprendizado (item 4); o `<conceito>` e instrucao de escrever artefato do aluno em linguagem plana"
  - "Em-dash (—) mantido por consistencia com o estilo ja existente do arquivo (L9, L20 originais usam —); nenhum acento de fato introduzido"

patterns-established:
  - "WRITER do contrato de retrieval: fecha-marco.md grava a entrada que tutor.md vai cobrar na abertura do proximo marco"

requirements-completed: [AVAL-02, AVAL-03, AVAL-04, ENG-01]

# Metrics
duration: 2min
completed: 2026-06-16
---

# Phase 4 Plan 03: Mastery gate + agenda de retrieval (writer) em fecha-marco.md Summary

**O Passo 1 de `mentor/fecha-marco.md` virou mastery gate (criterio de capacidade que LE o campo `**Capacidade:**` do PROGRESSO.md + 1 pergunta de extensao/transferencia sem andaime, bloqueante-formativo); o Passo 4 agora grava 1 entrada na `## Agenda de retrieval` no formato de contrato byte-identico ao reference.md; e o Checkpoint final cobra exatamente 1 proxima acao concreta ancorada em SDT na prosa — tudo sem acentos e com o artefato que o aluno LE livre de jargao.**

## Performance

- **Duration:** ~2 min
- **Started:** 2026-06-16T01:36:29Z
- **Completed:** 2026-06-16T01:38:41Z
- **Tasks:** 2
- **Files modified:** 1

## Accomplishments
- **Mastery gate (D-05/06/07/08):** Passo 1 renomeado, abre com prosa nomeando mastery learning + link a `fundamentos.md`; ganha checkbox de capacidade (le e cobra `**Capacidade:**` literalmente) e checkbox de sintese+transferencia (1 pergunta oral "como voce mudaria isso para fazer X?" sem andaime); linha bloqueante-formativa reforcada ("o marco NAO fecha — volte ao ciclo... diagnostico, nao punicao: sem nota"); guardrail de leveza escrito no doc.
- **Agenda de retrieval — lado WRITER (D-10, AVAL-02):** Passo 4 ganha item 6 que grava 1 entrada na `## Agenda de retrieval` do PROGRESSO.md no formato `- <conceito> -- revisitar na abertura do marco <NN>`, byte-identico ao contrato do plano 02; distinto do item de dividas de aprendizado.
- **Proxima acao unica + SDT (D-12, D-13, ENG-01):** Checkpoint troca o checkbox vago "Aluno sabe qual e o proximo passo" por "Aluno tem exatamente 1 proxima acao concreta (se virou lista, corte para 1)"; prosa do checkpoint ancora a acao em autonomia+competencia com link `[SDT]` e a `[ressalva honesta sobre relatedness em solo+IA]`; o que o aluno LE no Log fica sem jargao.
- **Leveza:** anti-padrao adicionado ("NAO agende mais de 1 conceito por fechamento").

## Task Commits

Each task was committed atomically:

1. **Task 1: Passo 1 vira mastery gate (capacidade + extensao + bloqueante-formativo) com link** - `e7e35e7` (feat)
2. **Task 2: Passo 4 escreve a agenda de retrieval; Checkpoint cobra 1 proxima acao + ancora SDT** - `bf931bf` (feat)

_Nota TDD (Task 1, tdd="true"): edicao de doc markdown sem runtime de teste. O ciclo RED/GREEN foi exercido via grep estatico — RED: `mastery gate`, `como voce mudaria`, `Capacidade`, link mastery todos ausentes (count 0) antes da edicao; GREEN: presentes apos a edicao. Por nao haver arquivo de teste separado, RED e GREEN ficaram no mesmo commit feat (o `volte ao ciclo` de D-08 ja preexistia)._

## Files Created/Modified
- `mentor/fecha-marco.md` - Passo 1 reescrito como mastery gate (heading + prosa + 2 checkboxes + linha bloqueante reforcada + guardrail); Passo 4 ganha item 6 (agenda de retrieval); Checkpoint final troca checkbox de proxima acao + prosa SDT; 1 anti-padrao de leveza adicionado.

## Decisions Made
- **Preservacao dos checkboxes originais:** os 3 criterios de "done" existentes foram mantidos; capacidade e extensao entram como 4o e 5o checkboxes — o gate fica mais forte sem perder o que ja funcionava.
- **Distincao agenda vs. dividas:** o item 6 (agenda de retrieval, forward-looking de revisao espacada) e semanticamente distinto do item 4 (dividas de aprendizado da curadoria), espelhando a distincao que o plano 02 fixou em reference.md (D-09).
- **Em-dash:** o arquivo ja usa `—` no estilo original (L9, L20 antigas); mantive por consistencia. `—` nao e caractere acentuado; o check de acentos no diff retornou vazio.

## Deviations from Plan

None - plan executed exactly as written. Inclui o item OPCIONAL do anti-padrao de leveza (Task 2) por reforcar o guardrail co-localizado.

## Verification Results
- V-04 `rg "mastery gate|gate de maestria"` -> 1 (L12 heading) — PASS
- V-05 `rg "Capacidade"` -> 1 (L22, cobra o campo `**Capacidade:**` literalmente) — PASS
- V-06 `rg "como voce mudaria|estender|extensao|transferencia"` -> presente (L24 "como voce mudaria isso para fazer X?", L26 estender) — PASS
- V-07 `rg "NAO .*fecha|volte ao ciclo"` -> 1 (L28 "o marco NAO fecha — volte ao ciclo") — PASS
- V-10 `rg "Agenda de retrieval"` -> 1 (L73, Passo 4 item 6) — PASS
- V-11b `rg "exatamente 1|1 proxima acao"` -> 1 (L124 "exatamente 1 proxima acao concreta") — PASS
- V-12 mastery link `rg "fundamentos\.md#frameworks-supporting-ancoram-um-doc"` -> presente (L15, L128) — PASS
- V-12 SDT caveat `rg "fundamentos\.md#sdt-relatedness-em-solo-ia"` -> 1 (L129) — PASS
- V-13 contrato byte-identico: `- <conceito> -- revisitar na abertura do marco <NN>` casa entre fecha-marco.md (L76) e reference.md (L249); `## Agenda de retrieval` consistente — PASS
- Sem acentos introduzidos: `git diff | grep '^+' | grep -P '[accentos]'` -> vazio — PASS

## Issues Encountered
- O scripts dir da Fase 4 (`check-phase4.sh`, `extract-fenced.sh`) NAO esta presente neste worktree (plano 01 roda em worktree separado, ainda nao mesclado). Verificacao feita via `rg` direto sobre os arquivos. O `check-phase4.sh` completo e o CONTRACT cross-file grep (V-13) serao executados pelo orquestrador no merge gate da wave, quando todos os worktrees estiverem juntos.

## Next Phase Readiness
- Lado WRITER do loop de retrieval pronto: `fecha-marco.md` grava a entrada na `## Agenda de retrieval`. O plano 04 (`tutor.md`, READER) deve copiar VERBATIM o nome da secao e cobrar a entrada na abertura do proximo marco, fechando o loop AVAL-02.
- Merge gate da wave deve confirmar que reference.md (02), fecha-marco.md (03) e tutor.md (04) concordam byte-a-byte no nome da secao e no formato da entrada.

## Self-Check: PASSED

- FOUND: `mentor/fecha-marco.md`
- FOUND: commit `e7e35e7` (Task 1)
- FOUND: commit `bf931bf` (Task 2)
- FOUND: `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/04-03-SUMMARY.md`

---
*Phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md*
*Completed: 2026-06-16*
