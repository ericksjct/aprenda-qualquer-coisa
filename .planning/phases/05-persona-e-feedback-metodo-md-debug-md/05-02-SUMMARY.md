---
phase: 05-persona-e-feedback-metodo-md-debug-md
plan: 02
subsystem: mentor-persona
tags: [doc-editing, persona, anti-leak, formative-assessment, source-single]
requires:
  - "05-01 Wave 0 harness (check-phase5.sh + extract-fenced.sh)"
  - "mentor/fundamentos.md (owner of theory vocabulary, FUND-03)"
  - "mentor/reference.md (owner of GRR syntax)"
  - "mentor/tutor.md (owner of retrieval)"
  - "mentor/fecha-marco.md (owner of mastery gate)"
provides:
  - "mentor/metodo.md anti-leak rule (CONS-01) in body + Anti-padroes mirror"
  - "mentor/metodo.md self-explanation step in gate de curadoria (AVAL-05)"
  - "mentor/metodo.md inline-named cycle (GRR/retrieval/mastery gate, Criterio 4)"
  - "mentor/metodo.md short forense pointer to /debug (D-07)"
affects:
  - "Phase 5 success criterion 4 (named cycle)"
  - "05-03 (debug.md, disjoint file, parallel)"
tech-stack:
  added: []
  patterns: [hyperlink-cite, source-single, anti-leak-scoped-to-fenced, mirror-rule, rigid-leveza-guardrail]
key-files:
  created:
    - .planning/phases/05-persona-e-feedback-metodo-md-debug-md/05-02-SUMMARY.md
  modified:
    - mentor/metodo.md
decisions:
  - "Anti-leak jargon stays in prose/bullets only (never in fenced blocks) so V-17 remains 0"
  - "Forense kept as 1-line pointer naming feedback tri-partido + /debug; tri-partite definition stays only in debug.md (source-single)"
  - "Mastery gate named at Fechamento de marco section (in addition to the gate-de-curadoria boundary note) so the cycle/closure also names the gate"
metrics:
  duration: ~12m
  completed: 2026-06-16
  tasks: 3
  files: 1
---

# Phase 5 Plan 02: Persona e feedback (metodo.md) Summary

CONS-01, AVAL-05 e Criterio 4 tecidos em `mentor/metodo.md` por insertos ancorados em headings literais — regra anti-leak no corpo (1a ponte a `fundamentos.md` + FUND-03) com espelho na lista de anti-padroes, passo de auto-explicacao "exatamente 1 pergunta" no gate de curadoria com guardrail rigido + fronteira a `fecha-marco.md`, ciclo nomeando inline retrieval/GRR/mastery gate (3 links, 5 itens preservados), e ponteiro forense curto "feedback tri-partido" -> `/debug` sem copiar a definicao.

## What Was Built

### Task 1 — CONS-01 anti-leak (D-01/D-02) — commit c7cafa4
- Nova regra logo apos `## Regra de ouro`: a fundamentacao guia a conduta, o agente APLICA mas NUNCA cita o nome do framework ao aluno; o porque interno esta em `fundamentos.md` (1a referencia de metodo.md a esse doc). Carrega o lembrete FUND-03 (doc interno, jamais lido pelo aluno nem injetado).
- Espelho curto na lista `## Anti-padroes (NUNCA faca)`: "Citar jargao de framework (Bloom, CLT, retrieval...) ao aluno na sessao — a teoria guia voce, nao e despejada nele."

### Task 2 — AVAL-05 check formativo (D-03/D-04) — commit d49b1ba
- Novo passo no `## Gate de curadoria` ENTRE "codigo funciona" e a curadoria de 1-3 melhorias: exatamente 1 pergunta de auto-explicacao ("me explica por que isso funciona"); so segue se o aluno explica, senao volta ao conceito. Passos seguintes renumerados (3->4).
- Guardrail rigido literal: "check formativo = exatamente 1 pergunta de auto-explicacao; se virou checklist ou rubrica, esta errado."
- Nota de fronteira: o gate de DOMINIO por marco mora em `fecha-marco.md`; aqui e o micro-check por passo, nao o mastery gate por marco.

### Task 3 — Criterio 4 ciclo nomeado (D-08/D-09) + D-07 (forense) — commit dac7d98
- Inline no `## Conduta por marco (ciclo)`: item 1 nomeia "retrieval (recuperacao ativa)" -> `tutor.md`; item 3 nomeia "GRR 3 fases (eu faco -> nos fazemos -> voce faz)" -> `reference.md`.
- `## Fechamento de marco` nomeia "mastery gate" -> `fecha-marco.md`.
- Exatamente 3 nomeacoes com link; backward design / primeiro done leve NAO nomeados; 5 itens do ciclo preservados.
- D-07: `## Protocolo de forense` ganha 1 linha "Esse protocolo e um ciclo de feedback tri-partido — veja `/debug` para a forma completa." Sem copiar feed-up/feed-back/feed-forward (mora so em debug.md).

## Verification

Harness `check-phase5.sh` apos o plano — todos os checks de metodo.md verdes:

| Check | Result |
|-------|--------|
| V-01-link (fundamentos.md) | PASS got=1 |
| V-02-corpo | PASS got=2 |
| V-03-fund03 | PASS got=2 |
| V-04-espelho | PASS got=2 |
| V-05-autoexp | PASS got=2 |
| V-06-guard | PASS got=4 |
| V-07-front | PASS got=3 |
| V-11-grr (reference.md) | PASS got=2 |
| V-12-retr (tutor) | PASS got=2 |
| V-13-gate (fecha-marco) | PASS got=3 |
| V-14-5itens | PASS got=5 |
| V-15-ptr (feedback tri-partido) | PASS got=1 |
| V-16 (ANCHOR-RESOLVE) | PASS |
| V-17-leak-met (fenced anti-leak) | PASS got=0 |

Pitfall 1 guard: `rg -c "feed-up|feed-back|feed-forward" mentor/metodo.md` == 0 (definicao tri-partida nao vazou).
`/debug` literal confirmado presente (linha 107) via Grep (o `rg -c '/debug'` no Git Bash sofre path-expansion do shell — artefato de ambiente, nao do arquivo).

Out of scope (debug.md, owned by plan 05-03, parallel/disjoint): V-08-lentes e V-09-pista permanecem FAIL no harness ate 05-03 rodar. Esperado.

## Deviations from Plan

None - plan executed exactly as written. Each deviation rule was checked; no bugs, missing critical functionality, or blocking issues encountered (doc-editing phase, no runtime surface — consistent with threat register T-05-02 disposition: accept).

## Known Stubs

None.

## Self-Check: PASSED
- mentor/metodo.md: FOUND (modified)
- .planning/phases/05-persona-e-feedback-metodo-md-debug-md/05-02-SUMMARY.md: FOUND
- Commit c7cafa4: FOUND
- Commit d49b1ba: FOUND
- Commit dac7d98: FOUND
