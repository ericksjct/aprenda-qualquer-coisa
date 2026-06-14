---
phase: 01-fundacao-teorica-fundamentos-md
plan: 01
subsystem: docs
tags: [learning-science, instructional-design, fundamentos, source-of-truth, anti-drift]

# Dependency graph
requires:
  - phase: 01-RESEARCH
    provides: catalogo canonico verbatim (6 foundational + 6 supporting), ressalvas SDT/Mayer, 4 mitos, skeleton
provides:
  - "mentor/fundamentos.md: doc interno fonte-unica do vocabulario de ciencia da aprendizagem"
  - "Catalogo de 12 frameworks (6 foundational + 6 supporting), cada um com def 1-linha + fonte + termo no metodo + aplicado em <doc> + status"
  - "Secao 'O que NAO usamos e por que' (4 mitos refutados)"
  - "Ressalvas honestas: SDT relatedness fraca em solo+IA; Mayer 3-de-12 (coerencia/sinalizacao/segmentacao)"
  - "Forward-references (aplicado em) que ancoram as Fases 2-6 da build order"
affects: [reference, novo-projeto, tutor, fecha-marco, metodo, debug, auditoria-consistencia]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Design fonte-unica: teoria definida 1x aqui; outros docs CITAM, nunca redefinem"
    - "Forward-reference com marcador de status (D-05): (Fase N, pendente) | (ja presente)"

key-files:
  created:
    - mentor/fundamentos.md
  modified: []

key-decisions:
  - "Montagem, nao criacao: conteudo copiado traceable de 01-RESEARCH.md para evitar drift semantico"
  - "Catalogo = exatamente 6+6=12; GRR coberto por Worked-Example, sem 13a entrada (D-07)"
  - "Mini-notas opcionais, so onde ha nuance (D-06) — nao para as 12"
  - "Mayer registrado como EXATAMENTE coerencia/sinalizacao/segmentacao; sem inflar (Criterio #4)"

patterns-established:
  - "Preambulo de uso interno no topo (D-04): doc nunca lido pelo aluno nem injetado na sessao (FUND-03)"
  - "Tabela-resumo por bloco com 4 campos canonicos (D-01/D-02)"
  - "Ressalvas e mitos em secoes dedicadas, fora do catalogo (D-03)"

requirements-completed: [FUND-01, FUND-02, FUND-03]

# Metrics
duration: ~4min
completed: 2026-06-14
---

# Phase 01: Fundacao teorica (`fundamentos.md`) Summary

**`mentor/fundamentos.md` criado: catalogo interno fonte-unica de 12 frameworks de ciencia da aprendizagem (6 foundational + 6 supporting), com ressalvas honestas (SDT/Mayer) e 4 mitos refutados.**

## Performance

- **Duration:** ~4 min
- **Completed:** 2026-06-14
- **Tasks:** 3
- **Files modified:** 1 (novo)

## Accomplishments
- Preambulo de uso interno no topo (FUND-03): declara doc INTERNO, nunca lido pelo aluno nem injetado na sessao
- Catalogo foundational (6): First Principles, Backward Design, Constructive Alignment, CLT, Worked-Example/Expertise-Reversal, Retrieval Practice — cada um com def 1-linha + fonte + termo no metodo + aplicado em + status
- Catalogo supporting (6): SDT, Scaffolding/ZPD, Mastery Learning, Avaliacao Formativa, Feed Up/Back/Forward, Spacing Effect
- Secao "Limites e ressalvas": SDT relatedness fraca em solo+IA; Mayer 3-de-12 (coerencia/sinalizacao/segmentacao) — sem inflar (Criterio #4)
- Secao "O que NAO usamos e por que": 4 mitos (estilos de aprendizagem, nativos digitais, Cone de Dale/percentuais, Bloom-piramide-rigida), cada um com razao + fonte
- Bloco "Nice-to-cite" (D-08): Bloom-verbos, Mayer-contexto, ADDIE/SAM/Gagne — 1 linha cada, fora do catalogo canonico

## Task Commits

Each task was committed atomically:

1. **Task 1: Esqueleto + preambulo interno + catalogo foundational (6)** - `3305922` (feat)
2. **Task 2: Catalogo supporting (6) + mini-notas** - `23c57d1` (feat)
3. **Task 3: Limites/ressalvas + o que NAO usamos + nice-to-cite** - `ebc442a` (feat)

## Files Created/Modified
- `mentor/fundamentos.md` - Catalogo canonico interno (fonte-unica) do vocabulario de frameworks de ciencia da aprendizagem; lido pelo agente, nunca pelo aluno

## Decisions Made
- None - plano executado conforme escrito. Conteudo copiado traceable de `01-RESEARCH.md` (montagem, nao criacao).

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered
- O agente executor sofreu um erro de socket (transporte) apos escrever o conteudo da Task 3 no working tree mas antes de commitar a Task 3 e criar este SUMMARY. Recuperado via spot-check do worktree: Task 3 estava integralmente escrita (40 linhas, todas as secoes e os 4 mitos presentes); o orquestrador commitou a Task 3 (`ebc442a`) e criou este SUMMARY. Nenhuma perda de conteudo.

## User Setup Required
None - no external service configuration required.

## Next Phase Readiness
- `fundamentos.md` e a fonte upstream da build order. Pronto para Fase 2 (`reference.md`), que CITA este catalogo.
- Todos os campos "aplicado em" apontam docs existentes em `mentor/` com status coerente; as aplicacoes pendentes (Fases 2-6) sao forward-references intencionais — nenhum doc-alvo foi tocado nesta fase (anti-drift).

---
*Phase: 01-fundacao-teorica-fundamentos-md*
*Completed: 2026-06-14*
