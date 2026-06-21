# Phase 7: Ingestao de PDF do livro via docling - Context

**Gathered:** 2026-06-21
**Status:** Ready for planning

<domain>
## Phase Boundary

Um utilitario Python (adaptado de um script existente) que converte o PDF do livro-base do
aluno para markdown estruturado via `docling`, gravando em `.projetos/<slug>/livro/`, MAIS a
costura no metodo: o livro convertido vira **guideline/baseline** que o mentor le no bootstrap
e durante a tutoria.

O contrato real do metodo e **"markdown do livro na pasta `livro/`"** — `docling` e apenas um
conversor **opcional** para produzir esse markdown. Um aluno que ja tenha o livro em `.md` cola
o arquivo em `livro/` e nunca toca em `docling`.

**Dentro do escopo:** script de conversao (adaptacao do `converter.py` existente) + ancoras de
pagina + split por capitulo + passo de bootstrap em `novo-projeto.md` + protocolo de divergencia
(livro vs pesquisa do mentor) tecido no metodo.

**Fora do escopo (outras phases / nao agora):** i18n do toolkit; alta-fidelidade de
tabelas/formulas/figuras; qualquer plataforma/UI.

> **Nota de constraint do PROJECT.md:** esta phase **redefine** o item "codigo de aplicacao /
> runtime novo" que estava em *Out of Scope* (era valido para v1.0). v2.0 introduz o PRIMEIRO
> software executavel com dependencia de terceiros (`docling`). O PROJECT.md precisara ser
> atualizado na transicao de phase/milestone.

</domain>

<decisions>
## Implementation Decisions

### Integracao no metodo
- **D-01:** O livro convertido serve como **guideline/baseline teorico** do mentor — nao e so
  combustivel pra ordenar conceitos, e a literatura-base do aluno que o mentor respeita.
- **D-02:** Entra como **passo (opcional) no bootstrap** (`mentor/novo-projeto.md`), proximo do
  Passo 3 de ordenacao de conceitos. Fonte-unica: a logica vive em `mentor/`, nao duplicada nos
  adaptadores.
- **D-03:** **Protocolo de divergencia** — quando a pesquisa do mentor diverge da literatura do
  livro, o **mentor decide sozinho** qual seguir (criterio proprio, ex.: recencia/consenso): ou
  (1) sinaliza que a fonte do livro esta desatualizada e mostra a pratica melhor, ou (2) adota a
  convencao do livro como embasamento. Nao pergunta ao aluno por caso.
- **D-04:** Cada divergencia vira **entrada datada em `.projetos/<slug>/APRENDIZADO.md`**: o que
  o livro diz × o que a pratica atual diz × a escolha do mentor. Reusa artefato existente (diario
  de licoes/decisoes); e o que preserva transparencia e vira material de aprendizado.
  > Nuance para o planner: "mentor decide sozinho" tensiona a regra de ouro (nao resolver pelo
  > aluno). O registro datado em APRENDIZADO.md e o mecanismo que mantem a decisao auditavel e
  > didatica — costurar D-03/D-04 juntos, nunca D-03 sozinho.

### Dependencia / setup
- **D-05:** `docling` e dependencia **OPCIONAL**, isolada nesse script. O core do toolkit segue
  100% stdlib-only e intocado (como `roadmap_fetch.py`: "segue funcionando sem"). O contrato do
  metodo e o markdown em `livro/`, nao o docling.
- **D-06:** Quem ja tem o livro em `.md` apenas **cola o arquivo em `livro/`** — caminho sem
  nenhuma dependencia nova.
- **D-07:** Isolar a dep via **`requirements` opcional + venv** (arquivo de deps so pra esse
  script; ex.: `requirements-pdf.txt` ou extra opt-in). `roadmap_fetch.py` e o core permanecem
  stdlib puro. Deixar explicito que e opt-in. Deps conhecidas do script base: `docling`, `pypdf`,
  `questionary` (a remover — ver D-12), + `markdownlint-cli` (npm, ja convencao do repo).

### Output / forma
- **D-08:** Markdown do livro mora em **`.projetos/<slug>/livro/`** (pasta NOVA no layout de
  `mentor/reference.md`). Separa a fonte-base do aluno de `referencias/` (saida do roadmap.sh).
- **D-09:** **Split por capitulo/secao** seguindo os headings que o docling detecta — feito por
  **script deterministico**, nao pela LLM. Principio geral da phase: maximizar trabalho
  deterministico, tirar responsabilidade operacional da LLM.
- **D-10:** **Ancora de pagina deterministica** em cada trecho convertido, pra o tutor referenciar
  a pagina exata ao aluno ("ve a pagina X do livro") — aprendizado multi-midia. O script base ja
  processa pagina-por-pagina e conhece `num_pagina_atual`; basta gravar um marcador (ex.:
  `<!-- page: N -->`) no lugar do `---` atual. Formato exato e detalhe de planejamento.
- **D-11:** Fidelidade: **estrutura (headings/secoes/ordem) > tabelas/figuras/formulas**.
  Tabelas/formulas/figuras sao best-effort; nao travam a phase se o docling nao extrair perfeito.

### Invocacao / quem roda
- **D-12:** **Adaptar o `converter.py` existente** (ver canonical refs) para o estilo do toolkit:
  remover o `questionary.select` interativo, virar **CLI por args** (ex.:
  `python scripts/<script>.py <pdf> --slug <slug>`), gravando em `.projetos/<slug>/livro/` em vez
  de `pdfs/`+`output/`. Preservar a blindagem de memoria (threads=1 + chunking pagina-a-pagina) e
  o passo de `markdownlint --fix`.
- **D-13:** **Dois caminhos de execucao**: (a) o **aluno** roda no terminal; (b) o **agente**
  dispara via **skill** (ex.: `/converte-livro`) ou passo do bootstrap.
- **D-14:** Quando o **agente** dispara o script, ele **avisa ANTES**: que a acao vai **demorar**,
  que **nao consome tokens** (roda localmente), e **mostra o progresso** (o script ja imprime
  "pagina N de M" — expor essa saida).
- **D-15:** No bootstrap (`novo-projeto.md`), o mentor **pergunta**: "tem livro-base? (PDF ou
  `.md`)". Se `.md`: instrui colar em `livro/`. Se PDF: mostra a linha de comando exata (ou
  dispara via skill conforme D-13/D-14) e segue quando `livro/` estiver populado. **O mentor nunca
  roda docling silenciosamente; so consome o resultado.**

### Claude's Discretion
- Nome exato da skill e do script; formato exato da ancora de pagina (HTML comment vs heading);
  nome do arquivo de requirements opcional; criterio de corte do split (H1 vs H2); tratamento de
  livro em idioma diferente do repo (preservar idioma da fonte e o esperado).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Script base a adaptar (EXTERNO ao repo — ponto de partida obrigatorio)
- `C:\Users\Erick\Documents\Projetos\docling-extrair-pdf\converter.py` — script funcional que o
  usuario quer aproveitar. Faz: selecao interativa (questionary) de PDF em `pdfs/`, conversao
  pagina-a-pagina via docling com blindagem de memoria (`OMP_NUM_THREADS=1` etc. + chunking de 1
  pagina por vez via pypdf), OCR ligado, `generate_picture_images`, append num `.md` unico com
  separador `---`, e `markdownlint --fix` no final. NAO faz split nem marca o numero da pagina —
  estas sao as adicoes da phase (D-09, D-10). Manter a blindagem de memoria e o lint.

### Precedente / convencao do toolkit
- `scripts/roadmap_fetch.py` — precedente de script utilitario: stdlib, opcional, "segue
  funcionando sem", CLI por args, grava em `.projetos/<slug>/`. Modelo de estilo para D-12.
- `mentor/novo-projeto.md` (Passo 3, ordenacao de conceitos) — ponto de integracao do passo de
  bootstrap (D-02, D-15).
- `mentor/tutor.md` — onde a referencia de pagina (D-10) e a consulta ao livro durante a tutoria
  serao tecidas.
- `mentor/reference.md` — layout de `.projetos/<slug>/` (adicionar `livro/`, D-08) e definicao de
  `APRENDIZADO.md` (D-04); tambem secao "Idioma e acentuacao".
- `mentor/debug.md` — protocolo de forense / feedback tri-partido; referencia de estilo se o
  protocolo de divergencia (D-03) virar um mini-procedimento.

### Codebase maps
- `.planning/codebase/STACK.md`, `STRUCTURE.md`, `INTEGRATIONS.md` — natureza do repo
  (markdown + 1 script stdlib), layout, e a unica integracao externa (roadmap.sh).

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `C:\Users\Erick\Documents\Projetos\docling-extrair-pdf\converter.py`: motor de conversao ja
  funcional — base do D-12. Reaproveitar pipeline pagina-a-pagina, blindagem de memoria e lint.
- `scripts/roadmap_fetch.py`: molde de CLI/estilo (args, grava em `.projetos/<slug>/`, opcional).

### Established Patterns
- Saidas de utilitarios vao para `.projetos/<slug>/` (gitignored, repo proprio do aluno).
- Core do toolkit e stdlib-only e "sem setup"; deps novas devem ser opt-in e isoladas (D-05/D-07).
- Fonte-unica: logica de metodo vive em `mentor/`, adaptadores so apontam (sem duplicar).
- Artefatos do aluno (`.projetos/`) em portugues acentuado; docs internos do agente sem acento.
- Repo ja adota `markdownlint` (commit recente exige personas obedecerem markdownlint).

### Integration Points
- `mentor/novo-projeto.md` — novo passo opcional de bootstrap (livro-base).
- `mentor/tutor.md` — consulta ao livro + referencia de pagina durante os passos.
- `mentor/reference.md` — adicionar `livro/` ao layout `.projetos/<slug>/`.
- `.projetos/<slug>/APRENDIZADO.md` — registro de divergencias (D-04).
- `scripts/` — novo script de conversao (adaptado).
- (provavel) `.claude/skills/<comando>/SKILL.md` + entrada em `AGENTS.md` para a skill de conversao.

</code_context>

<specifics>
## Specific Ideas

- Aprendizado **multi-midia**: o tutor referencia a pagina exata do livro ao aluno — por isso a
  ancora de pagina deterministica (D-10) e importante para o usuario.
- Principio condutor da phase: **maximo deterministico, minima responsabilidade operacional da
  LLM** (split e ancora de pagina sao trabalho de script, nao de modelo).
- Pre-aviso obrigatorio quando o agente dispara o script: "vai demorar, nao consome tokens (roda
  local), aqui esta o progresso" (D-14).

</specifics>

<deferred>
## Deferred Ideas

- **Alta-fidelidade de tabelas/formulas/figuras** — best-effort agora (D-11); virar foco proprio
  se o docling nao entregar bem e o usuario precisar.
- **i18n do toolkit** — outro item pre-escopado do v2.0; nao se mistura com esta phase.
- **Atualizar PROJECT.md** — mover "codigo de aplicacao / runtime novo" de Out of Scope para
  Validated na transicao (esta phase o torna realidade no v2.0).

None — discussion stayed within phase scope (alem das notas acima, que sao transicoes esperadas).

</deferred>

---

*Phase: 07-ingestao-pdf-livro-via-docling*
*Context gathered: 2026-06-21*
