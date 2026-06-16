---
status: partial
phase: 05-persona-e-feedback-metodo-md-debug-md
source: [05-VERIFICATION.md]
started: 2026-06-16T00:00:00Z
updated: 2026-06-16T00:00:00Z
---

## Current Test

[awaiting human testing]

## Tests

### 1. Navegacao dos links inline (metodo.md e debug.md)
expected: Renderizar `mentor/metodo.md` e `mentor/debug.md` e clicar nos links inline para
`reference.md` (GRR), `tutor.md` (retrieval), `fecha-marco.md` (mastery gate) e `/debug`
(forense). Cada link navega para o arquivo/secao correto. Nota A1: os links do ciclo usam
referencia de arquivo plana (`[reference.md](reference.md)`), sem `#slug`, entao a fragilidade
do slug do GRR NAO se aplica ao link renderizado — ele aponta para o arquivo, que existe.
Confirmar visualmente.
result: [pending]

### 2. Tom editorial (gate de curadoria + overlay de Hattie)
expected: Ler a secao "Gate de curadoria" e confirmar que o check formativo le como UMA
pergunta de auto-explicacao (nao um quiz/rubrica). Ler o overlay de Hattie em `debug.md` e
confirmar que ele ENQUADRA os 6 passos (lente por cima), sem reescreve-los.
result: [pending]

## Summary

total: 2
passed: 0
issues: 0
pending: 2
skipped: 0
blocked: 0

## Gaps

## Advisory (nao e gap da Fase 5)

- `mentor/debug.md:31-32` — acentos pre-existentes `Peça`/`peça` (IN-01), anteriores a esta
  fase. Registrado como Info; limpeza pode ser feita na auditoria da Fase 6 (estilo
  portugues SEM acentos).
