---
gsd_state_version: 1.0
milestone: v2.0
milestone_name: milestone
status: verifying
stopped_at: Completed 07-03-PLAN.md
last_updated: "2026-06-22T22:45:03.898Z"
last_activity: 2026-06-22
progress:
  total_phases: 1
  completed_phases: 1
  total_plans: 3
  completed_plans: 3
  percent: 100
---

# Project State

## Current Position

Phase: 07 (ingestao-pdf-livro-via-docling) — COMPLETE (3/3 plans)
Plan: 3 of 3 — done
Milestone: v1.0 — SHIPPED 2026-06-17 (tag v1.0)
Status: Phase complete — ready for verification
Last activity: 2026-06-22
Stopped at: Completed 07-03-PLAN.md

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-06-17)

**Core value:** O agente ensina a construir (aluno sai capaz de explicar e estender o projeto sozinho), ancorado em ciência da aprendizagem reconhecida — nunca resolve pelo aluno.
**Current focus:** Phase 07 — ingestao-pdf-livro-via-docling

## Accumulated Context

### Roadmap Evolution

- **07-03 (camada de consumo) feito -- Fase 7 FECHADA:** commits `0e2cbca`
  (reference.md) + `1219200` (tutor.md). `mentor/reference.md`: `livro/` no layout do
  repo do aluno (D-08, irmao de `referencias/`, com ancora `<!-- page: N -->`) +
  registro de divergencia no template APRENDIZADO.md (D-04: `o livro diz X / pratica
  diz Y / escolha do mentor`, datado, acentos DENTRO da fence) + prosa ASCII de
  referencia-cruzada apos a fence + `livro/` na lista acentuada de "Idioma e
  acentuacao". `mentor/tutor.md` (ASCII): Passo 0 le `livro/*.md` como baseline teorica
  respeitada (D-01); Passo 3 cita pagina exata via ancora ("ve a pagina X do livro",
  D-10); protocolo de divergencia (D-03 `decide sozinho`) SEMPRE pareado com registro
  datado em `APRENDIZADO.md` (D-04), apontando para `mentor/reference.md` (single-source
  do formato). `sh scripts/check-consistencia.sh` exit 0 (V-12/V-13/V-15/V-16 verdes);
  `tutor.md` zero acentos; greps D-01/D-03/D-04/D-08/D-10 verdes. Vertical completa da
  Fase 7 (motor 07-01 + invocacao 07-02 + consumo 07-03). **Ultimo plano da fase** ->
  Fase 7 pronta para `/gsd-verify-work`.

- **07-02 (camada de invocacao) feito:** commits `7769cb0` (fix harness) + `f0300ac`
  (skill) + `ee4ca31` (Passo 3b) + `1333e5a` (registros). Criado
  `.claude/skills/converte-livro/SKILL.md` (adaptador FINO que aponta para
  `mentor/novo-projeto.md`, sem duplicar logica docling). Tecido o "Passo 3b -
  Livro-base (opcional)" em `mentor/novo-projeto.md`: ramo D-15 (PDF -> comando
  `.venv-pdf` exato ou `/converte-livro`; `.md` -> colar em `livro/`, zero deps),
  pre-aviso D-14 (`nao consome tokens` / `pagina N de M` / ~2GB), regra "NUNCA roda
  docling silenciosamente" e bullet `livro/` no esqueleto do Passo 7. Harness
  reconciliado PRIMEIRO: `NONCMD` whitelista `converte-livro` (V-15 verde), V-12
  set-fechado intocado. Registro set-consistente em `AGENTS.md`/`README.md`/
  `mentor/metodo.md`; `sh scripts/check-consistencia.sh` exit 0 (V-13/V-15/V-16 verdes).
  Excecao de roteamento (`/converte-livro` -> `mentor/novo-projeto.md`, sem
  `mentor/converte-livro.md`) documentada em 3 superficies (skill, script, metodo.md).
  D-02/D-06/D-13/D-14/D-15 satisfeitos. **Plano 03** = ultimo da fase.

- **07-01 (motor de conversao) feito:** commits `b0e81b1` (RED) + `8d88a80` (GREEN) +
  `b617cef` + `2b4254b`. Criado `scripts/converte_livro.py` (CLI OPT-IN), `requirements-pdf.txt`
  (isolado: docling+pypdf+pytest; core stdlib intocado), `tests/conftest.py`,
  `tests/test_converte_livro.py` (8 logic + 1 golden smoke) e `tests/fixtures/sample.pdf`.
  Arquitetura corrigida da pesquisa: UM `convert()` do doc inteiro + split deterministico
  por `iterate_items()` em TITLE/SECTION_HEADER<=cut_level + ancora `<!-- page: N -->` de
  `prov[0].page_no` (substitui o chunking pypdf 1-pagina que destruia ambos os sinais).
  Helpers puros importam SEM docling (imports lazy dentro das funcoes) -> suite verde
  sub-segundo; o golden smoke RODOU o pipeline docling real (presente neste env) e passou.
  Seguranca: `sanitize_slug` rejeita path-traversal (T-07-01); subprocess markdownlint usa
  lista literal fixa (T-07-02). **CLI FIXA p/ Wave 2:**
  `python scripts/converte_livro.py <pdf> --slug <slug> [--out <dir>] [--cut-level N]`
  (default out `.projetos/<slug>/livro/`, cut-level 1). D-05/D-07/D-08/D-09/D-10/D-11/D-12
  satisfeitos. **Plano 02** = reconciliacao do harness + skill/AGENTS/README/metodo + bootstrap.

- Phase 7 added (marco v2.0): Ingestao de PDF do livro do aluno -> markdown via docling
  (scripts Python). Dir `.planning/phases/07-ingestao-pdf-livro-via-docling/`. v2.0 mantem
  i18n (pre-escopado) + esta phase; formalizar o marco com `/gsd-new-milestone`.

- **06-03 (relatorio de fechamento) feito -- Fase 6 FECHADA:** commit `1d1622d`. Criado
  `.planning/phases/06-auditoria-de-consistencia/06-AUDITORIA.md` (D-01 artefato b), o segundo
  e ultimo entregavel da fase. Cola a prova mecanica (`sh scripts/check-consistencia.sh` =>
  `== 0 fail(s) ==`, exit 0, V-01..V-16) + mapeamento check->V. Confirmacao semantica D-03
  one-time (a unica verificacao MANUAL da fase): o agente ABRIU cada linha de aterrissagem do
  semantic_confirmation_map e julgou o sentido -- 10/10 praticas CONS-02 fazem sentido (citacao
  direta da frase lida em cada veredito; nao mencao incidental). Politica D-05 declarada; 0
  achados estruturais; correcoes triviais (IN-01 + 10 flips D-04) documentadas; FUT-04 + linter
  de acentos permanente marcados fora de escopo (v2). Relatorio com ZERO letras acentuadas
  (`rg -c` => 0). NENHUMA edicao em `mentor/` ou no script -- so documenta o estado verde.
  CONS-02 e CONS-03 fechados. Ambos os artefatos de D-01 entregues. **Milestone v1.0 pronto
  para `/gsd-verify-work` + `/gsd-complete-milestone`.**

- **06-02 (fixes IN-01 + D-04) feito:** commit `086a82b`. IN-01/D-07 quitado: `Peça`/`peça`
  removidos de `debug.md:31-32` (V-16 red->green; `mentor/` com zero acentos). D-04: as 10
  marcas `pendente` da coluna "Aplicado em" de `fundamentos.md` viraram `(aplicado)`; zero
  `pendente` no arquivo; as 3 linhas `(ja presente)` (First Principles, CLT-core, ZPD)
  intactas. Auto-fix (Rule 1): a meta-descricao da coluna (linha 16-17) ainda citava
  `(Fase N, pendente)` como exemplo — reescrita para `(aplicado)`, satisfazendo o criterio
  `rg -c pendente => 0` e mantendo coerencia com a tabela. Suite `check-consistencia.sh`
  agora exit 0 (V-01..V-16 todos PASS). NENHUMA escalacao estrutural (D-05) — os 11 anchors
  CONS-02 ja estavam verdes no Plano 01. **Plano 03** = relatorio de fechamento (D-03
  semantica + D-05 escalacoes, nenhuma esperada).

- **06-01 (harness) feito:** `scripts/check-consistencia.sh` commitado (`2861024`) — PRIMEIRO
  tool de verificacao permanente do toolkit (D-01 artefato a). Codifica V-01..V-16:
  11 `check_has` anti-cargo-cult (CONS-02, todos PASS), V-12 comando<->arquivo (set fechado),
  V-13 backtick-paths (SKIP not-in-repo), V-14 zero jargao nos adaptadores (`AGENTS.md`+`.claude/`),
  V-15 set-equality DOIS-LADOS por arquivo (AGENTS.md/README.md/metodo.md — 3 PASS), V-16 acentos.
  Decisao chave: V-15 negativo extrai `/comando` delimitado por backtick (`` `/x` ``) — o
  `/[a-z-]+` aberto casava componentes de path (`mentor/metodo.md`->`/metodo`) gerando falsos.
  Baseline (confirmado por execucao): V-01..V-15 PASS, V-16 FAIL got=2 (cedilhas em
  `debug.md:31-32`), exit 1 — red ESPERADO. CONS-02 e CONS-03 marcados completos.
  **Plano 02** consome este baseline: fix do IN-01 (V-16->verde) + flip D-04 em `fundamentos.md`

  + relatorio de fechamento (D-03 semantica + D-05 escalacoes, nenhuma esperada).

- **05-03 (debug.md) feito — Fase 5 FECHADA:** AVAL-06 entregue por overlay
  nao-destrutivo. D-05: blockquote + rotulo inline por sub-heading mapeando as 3 lentes de
  Hattie (feed-up=Observar; feed-back=Isolar+Hipoteses+Testar; feed-forward=Corrigir+
  PISTA+Documentar) sobre os 6 passos PRESERVADOS (V-10==6). D-06: `PISTA = feed-forward:
  aponta a direcao do proximo passo SEM entregar a resposta` no passo 5 Corrigir (so o
  PAPEL; sintaxe do campo PISTA permanece em reference.md/metodo.md — fonte-unica). Jargao
  Hattie/feed-* so na prosa (V-17 leak-dbg==0); nao vazou para adaptadores (V-18==0).
  Harness `check-phase5.sh` agora exit 0 — 19/19 PASS. A1 ainda pendente: confirmar
  `#slug` GRR/D-09 por 1 clique no gate da fase.

- **05-02 (metodo.md) feito:** CONS-01 (regra anti-leak no corpo + 1a ponte a
  `fundamentos.md` + FUND-03 + espelho na lista), AVAL-05 (passo de auto-explicacao
  "exatamente 1 pergunta" + guardrail rigido + fronteira a `fecha-marco.md`), Criterio 4
  (ciclo nomeia inline retrieval/GRR/mastery gate por link, 5 itens preservados) e D-07
  (ponteiro forense curto "feedback tri-partido" -> `/debug`). Decisao: jargao anti-leak
  vive SO em prosa/bullets (nunca em bloco cercado) -> V-17 fica 0; definicao tri-partida
  mora so em debug.md (fonte-unica). Falta so 05-03 (debug.md) para fechar a Fase 5.
  A1 ainda pendente: confirmar `#slug` GRR por 1 clique no gate da fase.

- **Harness Wave 0 da Fase 5 pronto** (05-01): `scripts/extract-fenced.sh` (clone
  byte-a-byte da Fase 4) + `scripts/check-phase5.sh` codificam V-01..V-18. Baseline
  coerente com Fases 2/4: positivos de prosa-nao-escrita em red, V-16 (ANCHOR-RESOLVE),
  V-17 (anti-leak escopado a blocos cercados) e V-18 (anti-drift adaptadores) em green.
  05-02/05-03 editam `mentor/metodo.md` e `mentor/debug.md` com prova por check.
  Lembrete A1: confirmar o `#slug` dos links D-09 por 1 clique no gate (V-16 so prova
  que o heading literal existe).

- Projeto brownfield: o toolkit "Mentor de Aprendizado por Projeto" já existe e está
  mapeado em `.planning/codebase/`. Este milestone edita docs de `mentor/`, não cria
  software.

- **Build order inegociável** (fonte-única → evita drift semântico):
  `fundamentos.md` → `reference.md` → `novo-projeto.md` → (`fecha-marco.md` + `tutor.md`)
  → (`metodo.md` + `debug.md`) → auditoria de consistência. Reflete nos Depends-on do roadmap.

- **Decisão de setup:** NÃO foi gerado `CLAUDE.md` de instrução GSD. O repo ignora
  `CLAUDE.md` no `.gitignore` e usa `AGENTS.md` para a persona mentor; um CLAUDE.md GSD
  aplicaria regras de workflow a sessões de tutoria (conflito). Contexto GSD vive só em
  `.planning/`.

- **Estilo dos deliverables:** arquivos de `mentor/` em português SEM acentos (robustez de
  encoding); paths/identificadores em backticks. Manter o padrão ao editar.

- **Anti-drift / anti-cargo-cult:** toda prática nova em `fundamentos.md` precisa de
  "aplicado em <doc>" verificável; teoria nunca vaza para a sessão do aluno; nada de
  conteúdo de método duplicado nos adaptadores (`.claude/`, `AGENTS.md`).

- Pesquisa em `.planning/research/` (SUMMARY.md é o doc decision-ready). Confiança HIGH
  nos frameworks; MEDIUM nas escolhas exatas de costura — validar leveza na execução
  (esp. Stage 2 do bootstrap e a pergunta de retrieval no tutor).
