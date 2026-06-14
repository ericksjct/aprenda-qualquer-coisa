# Phase 2: Templates e sintaxe (reference.md) - Context

**Gathered:** 2026-06-14
**Status:** Ready for planning

<domain>
## Phase Boundary

Editar `mentor/reference.md` (doc EXISTENTE) para tecer 3 fios nos templates que todos os
procedimentos consomem:
1. O verbo de capacidade ao lado do entregavel de artefato (EST-01).
2. A sintaxe GRR de 3 fases "eu faco -> nos fazemos -> voce faz" (EST-04).
3. Os principios de carga cognitiva: fading por substrato, worked example analogo, e os
   3 principios de Mayer que transferem para texto puro (CARGA-01, CARGA-02, CARGA-03).

Sempre CITANDO `fundamentos.md` (EST-02), nunca reescrevendo a teoria localmente
(fonte-unica). Entrega EST-01, EST-02, EST-04, CARGA-01, CARGA-02, CARGA-03 e os 5
Criterios de Sucesso da Fase 2.

O CONTEUDO teorico (o QUE cada framework diz) ja esta fixado pela pesquisa (HIGH
confidence) e NAO foi rediscutido. As decisoes abaixo sao sobre a FORMA da costura nos
templates (a parte que a pesquisa marcou MEDIUM confidence).

**Insight estrutural que governa todas as decisoes:** `reference.md` e lido pelo AGENTE,
mas seus blocos de template (em ```markdown```) viram artefatos que o ALUNO le
(`CAMINHO.md`, aulas, scaffold). Logo:
- **Prosa do `reference.md`** (instrucao de agente) -> pode nomear frameworks e linkar
  `fundamentos.md`.
- **Dentro dos blocos de template** (vira doc do aluno) -> so o verbo de capacidade puro,
  zero jargao de framework (anti-theory-leak, CONS-01).

</domain>

<decisions>
## Implementation Decisions

### Campo "Objetivo" (capacidade) — EST-01
- **D-01:** (Delegado a Claude.) Adicionar uma linha nova `Objetivo (capacidade):` em
  cada passo do template `CAMINHO.md`, posicionada ACIMA da linha `Entregavel:`
  (capacidade primeiro, artefato como evidencia — ordem backward design). Forma:
  `- Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>`.
  - O template de aula ja tem `## Objetivo do passo` (hoje so descreve o entregavel) —
    ajustar para espelhar capacidade + artefato.
  - O campo `DONE:` do scaffold e reenquadrado como "evidencia observavel de que a
    capacidade foi adquirida", nao so "o codigo roda".
  - **Anti-leak:** dentro dos blocos de template (doc do aluno) aparece SO o verbo de
    capacidade — nunca o rotulo "Bloom" nem "objetivo cognitivo". O "porque" (backward
    design / constructive alignment) fica na PROSA do `reference.md`, via hyperlink (D-04).

### Sintaxe GRR de 3 fases — EST-04
- **D-02:** REESCREVER a secao existente "### Sintaxe nova de verdade: 'eu faco -> nos
  fazemos -> voce faz'" (atual linha ~382). Hoje o TITULO promete 3 fases mas o CORPO so
  entrega 2 (mostra exemplo -> pede variacao solo). A reescrita transforma "nos fazemos"
  numa etapa REAL e CONDICIONAL:
  - **eu faco:** exemplo resolvido em instancia diferente (= worked example, ver D-03).
  - **nos fazemos:** pratica conjunta guiada — o agente puxa cada micro-decisao, o aluno
    responde, o agente confirma — numa instancia ainda diferente do `TODO` solo.
  - **voce faz:** o `TODO(human)` solo.
  - **Gatilho condicional:** ligar "nos fazemos" quando o substrato no conceito dominante
    e zero-absoluto/iniciante OU quando o salto exemplo->solo e grande. Pular para
    intermediario/avancado (onde vira atrito — conecta com o fading, D-03).

### Carga cognitiva: fading + worked example — CARGA-01, CARGA-02
- **D-03:** Forma otimizada para AGENTE (regra mecanica, nao prosa pro aluno) — confirmado
  pelo usuario: "instrucao pra ele [o tutor] ... escolha o que funcionar melhor com agentes".
  - **Fading (CARGA-01, expertise-reversal):** regra de calibragem explicita na secao de
    substrato — uma tabela/lista substrato -> densidade de andaime+pista, com o principio
    nomeado: "o suporte recua conforme a maestria sobe; suporte demais ATRAPALHA o
    avancado". Formaliza o que hoje so esta implicito ("mais buraco, menos pista").
  - **Worked example analogo (CARGA-02):** NAO cria secao nova — FUNDE no "eu faco" do
    D-02. A regra: para substrato zero-absoluto no conceito dominante, o agente DEVE dar
    um exemplo resolvido em instancia DIFERENTE antes do `TODO` solo. (Ja alinha com a
    secao "Exemplos de aplicacao" do template de aula.)

### Mayer + citacao de fundamentos.md — CARGA-03, EST-02
- **D-04:** Citacao via HYPERLINK markdown (escolha do usuario: "fica mais facil para
  humanos navegarem tambem").
  - **EST-02:** toda mencao a framework na PROSA do `reference.md` (backward design, GRR,
    expertise-reversal, etc.) vira `[nome do framework](fundamentos.md#ancora)`, sem
    reescrever a teoria (fonte-unica). `reference.md` e `fundamentos.md` moram ambos em
    `mentor/`, entao o link e relativo no mesmo diretorio.
  - **CARGA-03 (Mayer):** os 3 principios que transferem para texto puro (coerencia,
    sinalizacao, segmentacao) + linguagem simples/legivel entram como REGRA DE AGENTE na
    secao "Regras da aula" (sobre COMO escrever a aula). Registrar honestamente o limite
    "so 3 de 12 principios transferem para texto puro", com hyperlink para `fundamentos.md`.

### Claude's Discretion
- D-01 foi delegado integralmente (decisao acima ja e a escolhida).
- Posicionamento exato das ancoras de hyperlink (D-04) depende da estrutura de cabecalhos
  do `fundamentos.md` produzido na Fase 1 (formato hibrido tabela+secoes, ver Fase 1 D-01/
  D-03). O executor deve conferir as ancoras reais ao linkar.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Doc que e EDITADO nesta fase
- `mentor/reference.md` — o unico arquivo editado na Fase 2. Secoes-chave para as
  decisoes: "Template — CAMINHO.md" (D-01), "Template — aula" + "Regras da aula"
  (D-01, D-04), "Formato do scaffold (TODO human)" e "Sintaxe nova de verdade:
  'eu faco -> nos fazemos -> voce faz'" (D-02, D-03), "Sondagem de substrato" +
  "Regra de granularidade" (D-03 fading).

### Doc CITADO (upstream, fonte da teoria — nunca redefinir)
- `mentor/fundamentos.md` — saida da Fase 1; alvo dos hyperlinks de D-04. As ancoras de
  link dependem da estrutura de cabecalhos desse doc; conferir ao linkar.
- `.planning/phases/01-fundacao-teorica-fundamentos-md/01-CONTEXT.md` — formato decidido
  do `fundamentos.md` (hibrido tabela+secoes, D-01/D-03) e o forward-reference D-05
  ("aplicado em reference.md (Fase 2, pendente)" — esta fase faz a aterrissagem; Fase 6
  confirma o status).

### Conteudo teorico (o QUE citar — ja decidido pela pesquisa)
- `.planning/research/SUMMARY.md` — GRR 3 fases (Pearson & Gallagher; Fisher & Frey),
  verbo de capacidade (Bloom revisado / constructive alignment Biggs), expertise-reversal
  (Kalyuga), worked example (Sweller & Cooper), Mayer limite 3-de-12.
- `.planning/research/FEATURES.md` — mapeamento pratica -> doc; tags reinforce/new.
- `.planning/research/STACK.md` — fontes primarias com atribuicao rastreada.

### Contrato da fase (o que tem de ficar VERDADEIRO)
- `.planning/REQUIREMENTS.md` §EST (EST-01, EST-02, EST-04), §CARGA (CARGA-01, CARGA-02,
  CARGA-03), §CONS (CONS-01 anti-leak, CONS-02 aplicado-em verificavel).
- `.planning/ROADMAP.md` §"Phase 2" — os 5 Criterios de Sucesso.

### Convencoes e arquitetura do toolkit (COMO editar sem quebrar o design)
- `.planning/codebase/ARCHITECTURE.md` — fonte-unica: teoria so em `mentor/`, citada por
  link, nunca duplicada nos adaptadores (`.claude/`, `AGENTS.md`).
- `.planning/codebase/STRUCTURE.md` — lugar de `reference.md` e `fundamentos.md` em `mentor/`.
- `.planning/codebase/CONVENTIONS.md` — portugues sem acentos; paths/identificadores em backticks.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `mentor/reference.md` ja contem todas as secoes-alvo; a fase EDITA, nao cria. Notavel:
  - O template de aula ja tem `## Objetivo do passo` e `## O que o tutor espera de voce`
    (gancho pronto para D-01).
  - A secao "Sintaxe nova de verdade" (linha ~382) ja tem o TITULO de 3 fases mas corpo
    de 2 — D-02 e uma reescrita do corpo, nao uma secao nova.
  - A calibragem de andaime por nivel ja existe parcial ("Granularidade ~ 1/nivel" linha
    ~44; "mais buraco, menos pista" para avancado) — D-03 formaliza isso como fading.
  - A secao "Exemplos de aplicacao" do template de aula ja pede instancia DIFERENTE do
    `TODO` — alinha com o worked example de D-03.

### Established Patterns
- Fonte-unica: teoria nova nao e escrita aqui; `reference.md` cita `fundamentos.md` por
  hyperlink (D-04). Inegociavel.
- Anti-theory-leak: prosa do `reference.md` (agente) pode nomear frameworks; blocos de
  template (aluno) so verbo de capacidade puro.
- Estilo: portugues SEM acentos; paths/identificadores em backticks.

### Integration Points
- `reference.md` -> `fundamentos.md` via hyperlinks relativos (mesmo diretorio `mentor/`).
- Downstream: a Fase 3 (`novo-projeto.md`) CONSOME o campo Objetivo/capacidade definido
  aqui (Stage 2 deriva 1 frase de capacidade por marco). A Fase 4 consome o campo de
  agenda de retrieval do `PROGRESSO.md` — NOTA: esse campo e mencionado na pesquisa como
  parte de "reference.md", mas no ROADMAP cai no escopo da Fase 4; nao e requisito da
  Fase 2 (EST/CARGA). Nao adicionar agora salvo se o planner confirmar pelo ROADMAP.

</code_context>

<specifics>
## Specific Ideas

- D-01: linha `- Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>`
  ACIMA de `Entregavel:` em cada passo do template `CAMINHO.md`.
- D-04: formato de link `[backward design](fundamentos.md#backward-design)` (ancora a
  confirmar contra o `fundamentos.md` real).
- D-02 gatilho do "nos fazemos": zero-absoluto/iniciante no conceito dominante OU salto
  exemplo->solo grande; pula para intermediario/avancado.
- D-03 fading: tabela substrato -> densidade de andaime+pista, com o principio nomeado
  ("suporte recua conforme maestria sobe; suporte demais atrapalha o avancado").

</specifics>

<deferred>
## Deferred Ideas

- Campo de agenda de retrieval/dividas no template `PROGRESSO.md` — pertence a Fase 4 no
  ROADMAP (ENG-01/AVAL-02), nao a Fase 2. Registrado para o planner nao confundir com a
  mencao da pesquisa.
- Confirmacao final de que cada "(Fase 2, pendente)" do `fundamentos.md` virou aplicacao
  real — auditoria da Fase 6 (CONS-02), nao desta fase.
- Productive Failure / modo tente-antes — FUT-02 (v2), evidencia MEDIUM.

</deferred>

---

*Phase: 02-templates-e-sintaxe-reference-md*
*Context gathered: 2026-06-14*
