#### Phase 7: Ingestao de PDF do livro via docling (PDF -> markdown)

**Goal:** O aluno consegue transformar um PDF do livro-base em markdown por capitulo,
page-anchored, sob `.projetos/<slug>/livro/` via um CLI Python opt-in (docling) deterministico,
e o mentor consome esse `livro/` como literatura-base durante o bootstrap e a tutoria
(referencia de pagina + protocolo de divergencia registrado).
**Requirements**: D-01..D-15 (CONTEXT.md — nao ha REQUIREMENTS.md formal; as decisoes sao os requisitos)
**Depends on:** none (inicia o marco v2.0; independente das phases v1.0)
**Plans:** 3 plans

Plans:
- [x] 07-01-PLAN.md — Engine deterministico: CLI converte_livro.py (whole-doc convert, split por heading, ancora de pagina) + requirements-pdf.txt + suite pytest (D-05/D-07/D-08/D-09/D-10/D-11/D-12)
- [x] 07-02-PLAN.md — Invocacao: reconcilia harness (NONCMD whitelist) + skill /converte-livro + AGENTS.md/README.md/metodo.md + passo livro-base no bootstrap com pre-aviso D-14 (D-02/D-06/D-13/D-14/D-15)
- [x] 07-03-PLAN.md — Consumo no metodo: tutor.md le livro/ como baseline + referencia de pagina + protocolo de divergencia datado em reference.md (D-01/D-03/D-04/D-08/D-10)

## Progress

| Phase                                        | Milestone | Plans Complete | Status      | Completed  |
| -------------------------------------------- | --------- | -------------- | ----------- | ---------- |
| 1. Fundacao teorica (fundamentos.md)         | v1.0      | 1/1            | Complete    | 2026-06-17 |
| 2. Templates e sintaxe (reference.md)        | v1.0      | 3/3            | Complete    | 2026-06-17 |
| 3. Bootstrap com Stage 2 (novo-projeto.md)   | v1.0      | 2/2            | Complete    | 2026-06-17 |
| 4. Gate e retrieval (fecha-marco + tutor)    | v1.0      | 4/4            | Complete    | 2026-06-17 |
| 5. Persona e feedback (metodo + debug)       | v1.0      | 3/3            | Complete    | 2026-06-17 |
| 6. Auditoria de consistencia                 | v1.0      | 3/3            | Complete    | 2026-06-17 |
| 7. Ingestao de PDF via docling               | v2.0      | 0/3            | Planned     | —          |
### Phase 07.1: RAG de livro-base sobre dado desestruturado com alta-fidelidade de formula (INSERTED)

**Goal:** O tutor consulta a teoria do livro-base (PDF escaneado, denso em formula) por busca
semantica e recebe, com fidelidade, o trecho certo + a(s) formula(s) + a pagina exata. Ingestao
100% local (MinerU emite LaTeX + imagem-de-pagina como rede; chunking layout-aware; indice
sqlite-vec hibrido denso+esparso) e consulta por CLI que devolve dados, sem token pago. Gate =
golden set ~15 conceitos de mat-financeira (hit@3 pagina >=80%, hit@1 >=60%, formula presente 100%).
Escopo = Fatias 1-3; Fatia 4 (ColPali) e fidelidade de TABELA DEFERIDAS.
**Requirements**: D-01..D-18 (+A5) (CONTEXT.md — sao os requisitos de-facto; nao ha REQUIREMENTS.md formal)
**Depends on:** Phase 7
**Plans:** 5 plans

Plans:
- [ ] 07.1-01-PLAN.md — Wave 0: recriar .venv-pdf py -3.12 (BLOQUEANTE) + deps RAG opt-in + fixtures/golden_set.json + testes RED (D-01/D-03/D-04/D-05/D-07/D-09/D-14/D-15/D-17)
- [ ] 07.1-02-PLAN.md — Wave 1: extracao MinerU (CPU/lotes/blindagem) + render_block $$LaTeX$$ + boundary real + build_chunks provenance (D-01/D-02/D-03/D-04/D-05/D-14)
- [ ] 07.1-03-PLAN.md — Wave 2: indexacao .index/ — bge-m3 (fp16=False) + sqlite-vec vec0 + FTS5 + corpus.jsonl (D-06/D-07/D-08/D-14/D-15)
- [ ] 07.1-04-PLAN.md — Wave 3: scripts/consulta_livro.py — CLI hibrida vec0+FTS5 fundida por RRF + saida por dados (D-07/D-09/D-10/D-14)
- [ ] 07.1-05-PLAN.md — Wave 4: costura no metodo (tutor/novo-projeto/reference/skill/ps1) + re-ingest mat-financeira (D-18) + golden set gate (D-11/D-12/D-13/D-15/D-16/D-17/D-18)
