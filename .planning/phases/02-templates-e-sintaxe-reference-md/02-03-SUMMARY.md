---
phase: 02-templates-e-sintaxe-reference-md
plan: 03
subsystem: mentor-docs
tags: [pedagogia, grr, carga-cognitiva, fonte-unica, hyperlinks]
requires:
  - "mentor/fundamentos.md (ancoras de secao reais: #frameworks-foundational-load-bearing, #mayer-so-3-de-12-principios-em-texto-puro)"
provides:
  - "GRR de 3 fases real em reference.md (we-do condicional)"
  - "worked example analogo nomeado no 'eu faco'"
  - "fading nomeado (expertise-reversal) na Sondagem"
  - "regra Mayer com limite honesto '3 de 12' na prosa Regras da aula"
  - "citacoes da teoria por hyperlink relativo (fonte-unica)"
affects:
  - mentor/reference.md
tech-stack:
  added: []
  patterns:
    - "citacao por hyperlink relativo para fundamentos.md (nunca reescrever teoria)"
    - "jargao de framework so na PROSA, nunca dentro de bloco cercado (CONS-01)"
key-files:
  created: []
  modified:
    - mentor/reference.md
decisions:
  - "Links de framework apontam para a SECAO que contem a celula (#frameworks-foundational-load-bearing), pois nao existe ancora por framework em fundamentos.md (D-04)."
  - "'nos fazemos' e etapa CONDICIONAL (liga em zero-absoluto/iniciante ou salto grande; pula em intermediario/avancado) — conecta com o fading."
metrics:
  duration: ~12min
  completed: 2026-06-14
  tasks: 3
  files: 1
---

# Phase 2 Plan 3: GRR 3 fases + fading + Mayer (citacoes por hyperlink) Summary

Teceu 2 fios pedagogicos na PROSA de `mentor/reference.md` e aterrissou as citacoes que
`fundamentos.md` marcava "(Fase 2, pendente)": GRR de 3 fases real com worked example no
"eu faco", fading por substrato nomeado (expertise-reversal), e a regra de Mayer com o
limite honesto "3 de 12" — toda teoria citada por hyperlink relativo, sem reescrever
conteudo (fonte-unica).

## What Was Built

- **Task 1 (EST-04, CARGA-02, EST-02):** Reescreveu o corpo da secao `### Sintaxe nova de
  verdade: "eu faco -> nos fazemos -> voce faz"`. Antes o titulo prometia 3 fases mas o
  corpo entregava 2. Agora as 3 fases estao nomeadas e em ordem; "nos fazemos" e uma etapa
  CONDICIONAL real (gatilho por substrato/salto); o worked example analogo (instancia
  diferente) esta nomeado no "eu faco". Link GRR para
  `fundamentos.md#frameworks-foundational-load-bearing`.
- **Task 2 (CARGA-01, EST-02):** Nomeou o fading por substrato (expertise-reversal effect)
  nas Regras da Sondagem, com a calibragem substrato -> densidade de andaime/pista, e
  citou backward design nas Regras do caminho. Ambos linkam
  `fundamentos.md#frameworks-foundational-load-bearing`.
- **Task 3 (CARGA-03, EST-02):** Adicionou a regra de Mayer na PROSA "Regras da aula"
  (fora do bloco cercado da aula): os 3 principios que transferem para texto (coerencia,
  sinalizacao, segmentacao) + o limite honesto "3 de 12" + link para
  `fundamentos.md#mayer-so-3-de-12-principios-em-texto-puro`.

## Verification

Script de gate da fase (`check-phase2.sh`) rodado da raiz do repo: **0 fail(s)**, todos os
9 criterios PASS.

| Criterio | Antes | Depois |
|----------|-------|--------|
| EST-01a | PASS | PASS |
| EST-01b | PASS | PASS |
| EST-04 | FAIL (1) | PASS (4) |
| EST-02 | FAIL (0) | PASS (4) |
| CARGA-01 | FAIL (0) | PASS (3) |
| CARGA-02 | PASS (3) | PASS (8) |
| CARGA-03 | FAIL (0) | PASS (1) |
| ANCHOR-RESOLVE | PASS | PASS |
| ANTI-LEAK | PASS (0) | PASS (0) |

Os 4 criterios-alvo (EST-04, EST-02, CARGA-01, CARGA-03) viraram PASS; os ja verdes
(EST-01a/b, CARGA-02, ANCHOR-RESOLVE, ANTI-LEAK) continuaram verdes.

Checagens adicionais:
- Os 4 hyperlinks para `fundamentos.md#` resolvem para headings reais (3x
  `#frameworks-foundational-load-bearing`, 1x `#mayer-so-3-de-12-principios-em-texto-puro`).
- "3 de 12" NAO aparece dentro de bloco cercado (esta na prosa Regras da aula).
- 0 acentos no arquivo (convencao de encoding mantida).
- Secao "Sintaxe nova de verdade" nao foi duplicada (count == 1).

## Deviations from Plan

None - plan executed exactly as written. Cada task aplicou as edicoes nas zonas previstas
e passou os criterios de aceitacao na primeira tentativa.

## Decisions Made

- **Link de framework -> secao que contem a celula:** confirmado que `fundamentos.md` nao
  tem ancora por framework (os nomes vivem em celulas de tabela). Usadas as 2 ancoras de
  SECAO reais com o nome do framework no TEXTO do link (D-04).
- **"nos fazemos" condicional:** liga em zero-absoluto/iniciante ou salto grande
  exemplo->solo; pula em intermediario/avancado, onde a pratica conjunta vira atrito. Isso
  amarra a sintaxe GRR ao fading da Sondagem (mesmo principio: mais maestria, menos suporte).

## Commits

- fae6813: feat(02-03): reescrever Z6 com GRR 3 fases real + worked example
- c15c829: feat(02-03): nomear fading (expertise-reversal) e citar backward design
- 7c5c6bd: feat(02-03): regra Mayer com limite honesto na prosa Regras da aula

## Self-Check: PASSED

- mentor/reference.md modificado e presente.
- Os 3 commits existem na historia do worktree.
- check-phase2.sh: 0 fail(s).
