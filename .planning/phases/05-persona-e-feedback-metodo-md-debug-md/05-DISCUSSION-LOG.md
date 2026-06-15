# Phase 5: Persona e feedback (metodo.md + debug.md) - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-15
**Phase:** 5-persona-e-feedback-metodo-md-debug-md
**Areas discussed:** Anti theory-leak (CONS-01), Check formativo no gate (AVAL-05), Forense tri-partido (AVAL-06), Ciclo nomeado (Criterio 4)

> Nota: o aluno pediu explicitamente, ao escolher as areas, que cada arquivo citado tivesse
> seu motivo de existencia relembrado e que termos tecnicos fossem explicados. A discussao
> foi conduzida nesse registro (glossario por area antes de cada pergunta).

---

## Anti theory-leak (CONS-01) — em metodo.md

| Option | Description | Selected |
|--------|-------------|----------|
| Regra positiva no corpo + espelho na lista de anti-padroes | Regra afirmativa com link p/ fundamentos.md + 1 item na checklist "NUNCA faca" | ✓ |
| So item na lista de anti-padroes | Apenas 1 linha na checklist | |
| So secao positiva nova | So no corpo, sem tocar na lista | |

**User's choice:** Regra positiva + espelho na lista.

| Option | Description | Selected |
|--------|-------------|----------|
| Sim, FUND-03 na mesma regra | A mesma frase diz "doc interno, nunca vai pro aluno" | ✓ |
| Nao, so o anti-leak aqui | FUND-03 fica so no fundamentos.md (Fase 1) | |

**User's choice:** Sim, FUND-03 na mesma regra.
**Notes:** metodo.md hoje nao cita fundamentos.md — D-01 cria a primeira ponte.

---

## Check formativo no gate (AVAL-05) — em metodo.md

| Option | Description | Selected |
|--------|-------------|----------|
| Novo passo antes de abrir a curadoria | 1 pergunta de auto-explicacao antes das melhorias; so segue se o aluno explica | ✓ |
| Dobrado no passo 2 existente | Pergunta dentro do passo 2 atual | |
| Voce decide a posicao exata | Executor escolhe a ancora | |

**User's choice:** Novo passo antes de abrir a curadoria.

| Option | Description | Selected |
|--------|-------------|----------|
| Teto rigido de 1 pergunta + nota de fronteira | Guardrail anti-quiz + nota de que o mastery gate por marco mora em fecha-marco.md | ✓ |
| So o teto de 1 pergunta | Guardrail de leveza sem a nota de fronteira | |

**User's choice:** Teto rigido de 1 pergunta + nota de fronteira.
**Notes:** Pesquisa marca AVAL-05 como LOW ("1 pergunta, nao vire quiz").

---

## Forense tri-partido (AVAL-06) — em debug.md

| Option | Description | Selected |
|--------|-------------|----------|
| Overlay sobre os 6 passos | Manter os 6 passos e agrupar sob feed-up/feed-back/feed-forward | ✓ |
| Reestruturar em 3 fases | Rescrever debug.md inteiro nas 3 perguntas de Hattie | |

**User's choice:** Overlay sobre os 6 passos.

| Option | Description | Selected |
|--------|-------------|----------|
| Em debug.md, no passo da PISTA | Regra PISTA=feed-forward onde a PISTA e invocada; scaffold nao muda | ✓ |
| Tambem reforcar no scaffold (metodo.md) | Anotar tambem no campo PISTA do metodo.md | |

**User's choice:** Em debug.md, no passo da PISTA.

| Option | Description | Selected |
|--------|-------------|----------|
| Resumo no metodo.md continua ponteiro curto | metodo.md aponta /debug; tri-partido so em debug.md | ✓ |
| Espelhar o tri-partido no metodo.md tambem | Reescrever tambem o resumo na persona | |

**User's choice:** Continua ponteiro curto p/ debug.md.

---

## Ciclo nomeado (Criterio 4) — em metodo.md

| Option | Description | Selected |
|--------|-------------|----------|
| Anotar os 5 passos inline | Nomear GRR/retrieval/gate em cada ponto do ciclo, por link ao dono | ✓ |
| Bloco de visao geral novo no topo | Paragrafo nomeando as etapas antes dos 5 passos | |

**User's choice:** Anotar os 5 passos inline.

| Option | Description | Selected |
|--------|-------------|----------|
| As 3 do criterio: gate, retrieval, GRR | Nomear exatamente as 3 etapas exigidas | ✓ |
| As 3 + backward design / primeiro done leve | Nomear tambem as praticas da Fase 3 | |

**User's choice:** As 3 do criterio (gate, retrieval, GRR).
**Notes:** retrieval (tutor.md) e gate (fecha-marco.md) sao forward-references seguros — a
Fase 4 roda antes da 5 (ordem de execucao 1->...->5).

## Claude's Discretion

- Texto exato das regras/nomeacoes e posicao das ancoras de hyperlink (dependem dos
  cabecalhos de fundamentos.md e dos docs da Fase 4).
- Mapeamento exato dos 6 passos do debug.md nas 3 perguntas de Hattie.

## Deferred Ideas

- Rubrica de criterios observaveis para curadoria (v2 / FUT-05).
- Nomear backward design / primeiro done leve no ciclo (rejeitado para nao inchar).
- Confirmacao de aterrissagem "(Fase 5, pendente)" em fundamentos.md -> auditoria Fase 6.
