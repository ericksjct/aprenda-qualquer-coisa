---
phase: 05-persona-e-feedback-metodo-md-debug-md
plan: 03
subsystem: mentor-docs
tags: [doc-editing, feedback, hattie, debug, overlay]
requires:
  - "05-01 (harness Wave 0: check-phase5.sh + extract-fenced.sh)"
provides:
  - "mentor/debug.md: overlay tri-partido de Hattie (feed-up/feed-back/feed-forward) sobre os 6 passos do forense"
  - "mentor/debug.md: PISTA enquadrada como feed-forward (aponta direcao sem entregar resposta)"
affects:
  - mentor/debug.md
tech-stack:
  added: []
  patterns:
    - "Overlay nao-destrutivo (annotate, nao reescrever) — Pitfall 5"
    - "Source-single: debug.md dono da definicao tri-partida; fundamentos.md so referencia teorica"
    - "Anti-leak escopado a blocos cercados (CONS-01): jargao Hattie/feed-* so na prosa"
key-files:
  created: []
  modified:
    - mentor/debug.md
decisions:
  - "Mapeamento FIXO D-05: feed-up=Observar; feed-back=Isolar+Hipoteses+Testar; feed-forward=Corrigir+PISTA+Documentar"
  - "Rotulo de lente inline em cada um dos 6 sub-headings (overlay reforcado) + blockquote de mapeamento apos o heading da secao — os 6 '### N.' preservados (V-10==6)"
  - "PISTA enquadrada como feed-forward no ponto Corrigir (linha travado ha 10 min); sintaxe do campo PISTA NAO copiada (permanece em reference.md/metodo.md)"
metrics:
  duration: "~1 min"
  completed: 2026-06-16
  tasks: 2
  files: 1
  commits: 2
---

# Phase 5 Plan 03: debug.md — Overlay de Feedback Tri-partido (Hattie) Summary

Adiciona a AVAL-06 ao protocolo de forense por overlay nao-destrutivo: as 3 lentes de
feedback de Hattie & Timperley (feed-up / feed-back / feed-forward) emolduram os 6 passos
existentes, e a PISTA e nomeada como feed-forward que aponta a direcao sem entregar a
resposta — sem renumerar nem reescrever nenhum dos 6 passos.

## What Was Built

- **D-05 (Task 1):** blockquote logo apos `## O protocolo (6 passos)` mapeando feed-up
  (Aonde vou?) = Observar · feed-back (Como estou indo?) = Isolar+Hipoteses+Testar ·
  feed-forward (Para onde a seguir?) = Corrigir+PISTA+Documentar. Cada um dos 6
  sub-headings recebeu um rotulo de lente inline (ex: `### 1. Observar (feed-up: Aonde
  vou?)`) — overlay, nao reescrita. Os 6 `### N.` permanecem contaveis (V-10 == 6).
- **D-06 (Task 2):** no passo `### 5. Corrigir`, junto da linha "travado ha mais de 10
  minutos", adicionada a frase `PISTA = feed-forward: aponta a direcao do proximo passo
  SEM entregar a resposta.` — apenas o PAPEL; a sintaxe do campo PISTA continua em
  reference.md/metodo.md (fonte-unica).

## Verification

Harness Wave 0 completo (`check-phase5.sh`) roda com **exit 0 — 19/19 PASS**. Criterios
desta entrega:
- V-08-lentes: got=9 need>=3 (3 lentes nomeadas)
- V-09-pista: got=2 need>=1 (PISTA = feed-forward)
- V-10-6passos: got=6 need>=6 (6 passos preservados)
- V-17-leak-dbg: got=0 need=0 (anti-leak nos blocos cercados intacto — jargao so na prosa)
- V-18-adapt: got=0 need=0 (Hattie/feed-* nao vazaram para AGENTS.md / .claude/)

Com 05-02 (metodo.md) ja feito, a Fase 5 fecha: toda a suite verde.

## Deviations from Plan

None - plan executed exactly as written. O plano sugeria opcionalmente rotular os
sub-headings inline; foi feito (reforco do overlay, sem custo de contagem) — dentro do
escopo "Claude's discretion" do action.

## Commits

- `6bedadb` feat(05-03): overlay 3 lentes de Hattie sobre os 6 passos do forense
- `12605e8` feat(05-03): enquadra PISTA como feed-forward no ponto Corrigir

## Self-Check: PASSED

- FOUND: mentor/debug.md (modified)
- FOUND: commit 6bedadb
- FOUND: commit 12605e8
- Harness check-phase5.sh: exit 0 (19 PASS / 0 FAIL)
