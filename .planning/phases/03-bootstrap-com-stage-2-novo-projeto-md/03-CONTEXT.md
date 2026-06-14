# Phase 3: Bootstrap com Stage 2 (novo-projeto.md) - Context

**Gathered:** 2026-06-14
**Status:** Ready for planning

<domain>
## Phase Boundary

Editar `mentor/novo-projeto.md` (doc EXISTENTE, lido pelo AGENTE) para tecer 2 fios:

1. **EST-03 / Stage 2** — inserir uma etapa leve de "evidencia de maestria por marco":
   ~1 frase de capacidade (verbo de Bloom) por marco, enquadrada como backward design via
   referencia a `fundamentos.md`.
2. **ENG-02 / primeiro done leve** — nomear e reforcar o "primeiro done leve"
   (reduzir time-to-first-success) como principio anti-evasao, conectado explicitamente ao
   Walking Skeleton (Passo 8 / Marco 00).

Entrega EST-03, ENG-02 e os 3 Criterios de Sucesso da Fase 3 no ROADMAP.

O CONTEUDO teorico (backward design/UbD Stage 2, time-to-first-success, Walking Skeleton)
ja esta fixado pela pesquisa (HIGH confidence) e NAO foi rediscutido. As decisoes abaixo
sao sobre a FORMA da costura no procedimento (a parte que a pesquisa marcou MEDIUM).

**Nuance estrutural que governa as decisoes:** `novo-projeto.md` e um procedimento lido
pelo AGENTE (nao um template). O anti-theory-leak (CONS-01) se aplica ao que o agente
ESCREVE nos artefatos do aluno (`PROGRESSO.md`), nao a prosa do procedimento: a prosa pode
nomear frameworks e linkar `fundamentos.md`; a frase de capacidade gravada no
`PROGRESSO.md` (que o aluno le) so tem o verbo de capacidade puro, zero jargao.

**Tensao de ordenacao resolvida (ver D-01):** o ROADMAP pede Stage 2 "entre o Passe 1
(caminho) e a montagem de marcos", mas a frase de capacidade deriva da User Story, que so
nasce no Passo 5 (montagem de marcos). Interpretacao adotada: "entre caminho e marcos" e
CONCEITUALMENTE backward design (definir a evidencia de maestria junto ao marco, antes de
fechar o agrupamento), NAO uma posicao fisica rigida no arquivo.

</domain>

<decisions>
## Implementation Decisions

### Posicionamento do Stage 2 — EST-03 (Criterio 1)
- **D-01:** Stage 2 em DOIS niveis, sem renumerar o doc inteiro:
  - **Nivel macro (Passo 4):** o Passo 4 ja faz "engenharia reversa do output final ->
    capacidades necessarias" — apenas NOMEAR isso explicitamente como backward design,
    com 1 frase + hyperlink para `fundamentos.md`. Nenhuma reescrita do mecanismo (ja
    existe).
  - **Nivel marco (Passo 5):** quando cada marco ganha sua User Story na montagem (Passo
    5), o agente escreve JUNTO a frase de capacidade daquele marco. As duas nascem coladas.
    Este e o "Stage 2" propriamente dito.
  - **Rejeitado:** criar um passo separado novo entre 4 e 5 e mover a User Story pra ele
    (mais invasivo, mesmo resultado); e reembrulhar tudo em "Stages 1/2/3" explicitos
    (reorganizacao grande de um doc ja longo + conflita com a ordem do ROADMAP).
  - Registrar a interpretacao do "entre caminho e marcos" no plano para o planner nao
    tropecar no literal do ROADMAP.

### Onde a frase de capacidade mora — EST-03 (Criterio 2)
- **D-02:** A frase de capacidade por marco vai no `PROGRESSO.md`, colada na User Story de
  cada marco na arvore de marcos. Persistir nesse artefato e obrigatorio: o gate da Fase 4
  (`fecha-marco.md`) vai PROCURAR essa frase ali para cobrar a capacidade. Inline so na
  prosa do procedimento NAO serve (sumiria).
  - **Separacao de niveis:** `CAMINHO.md` mantem a capacidade por PASSO (definida na Fase 2,
    D-01); `PROGRESSO.md` ganha a capacidade por MARCO. Nao misturar os dois no mesmo
    arquivo.
  - **Anti-leak (CONS-01):** como o `PROGRESSO.md` e lido pelo aluno, a frase usa o formato
    de verbo de capacidade puro da Fase 2 ("ao terminar, voce consegue <verbo> <conceito>"),
    sem "Bloom", "maestria" ou "backward design".
  - Forma na arvore de marcos (exemplo, a refinar no plano):
    ```
    Marco 02 — Lista de produtos
      User Story: como visitante, quero ver a lista de produtos
      Capacidade: ao terminar, voce consegue percorrer uma lista de dados e gerar HTML por item
      Passos: P05, P06
    ```
  - **Dependencia de template:** o template do `PROGRESSO.md` mora em `mentor/reference.md`.
    Se a arvore de marcos do template nao tiver o campo de capacidade por marco, o plano da
    Fase 3 precisa adiciona-lo la (o `novo-projeto.md` instrui o preenchimento; o
    `reference.md` define o template). Confirmar no planning se o campo entra aqui ou se
    ficou pendente da Fase 2.

### "Primeiro done leve" — ENG-02 (Criterio 3)
- **D-03:** Ancorar o principio no Passo 8 (Walking Skeleton), que e onde ele ja materializa.
  - **Passo 8:** nomear "primeiro done leve" + o porque (reduzir time-to-first-success =
    anti-evasao do async) + hyperlink para `fundamentos.md`. E ROTULAGEM de algo que ja
    existe (reinforce LOW na pesquisa), nao mecanismo novo: o Marco 00 / Walking Skeleton
    ja entrega vitoria rapida.
  - **Passo 5:** reforco leve de 1 linha — dimensionar o primeiro marco como o menor
    possivel, para a primeira vitoria vir rapido.
  - **Rejeitado (mas oferecido):** principio geral no topo do doc — preferiu-se ancorar onde
    o mecanismo mora.

### Leveza / guardrail anti over-formalizacao — EST-03 (Criterio 2) + Pitfall 10
- **D-04:** Stage 2 OBRIGATORIO por marco, com TETO RIGIDO de exatamente 1 frase no formato
  verbo-capacidade. Guardrail explicito escrito no `novo-projeto.md`: "Stage 2 = exatamente
  1 frase de capacidade por marco. Se virou lista, rubrica ou sub-doc, esta errado — corte."
  - **Nao opcional / nao escalavel:** rejeitada a opcao de pular em projetos com muitos
    marcos. Razao: o gate da Fase 4 depende da frase existir; opcionalidade faria o agente
    pular justamente quando der atrito, deixando o gate sem chao. O controle de leveza e o
    TAMANHO (1 frase), nao a opcionalidade. 15 marcos = 15 linhas, barato.

### Claude's Discretion
- Texto exato das frases de nomeacao (backward design no Passo 4; primeiro done leve no
  Passo 8) e a posicao precisa das ancoras de hyperlink dependem da estrutura de cabecalhos
  do `fundamentos.md` (Fase 1) e da secao de template do `PROGRESSO.md` em `reference.md`
  (Fase 2). O executor confere as ancoras reais ao linkar.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Doc que e EDITADO nesta fase
- `mentor/novo-projeto.md` — unico arquivo editado na Fase 3. Secoes-chave:
  - "Passo 4 — Passe 1: o caminho completo" (D-01 macro: nomear backward design).
  - "Passo 5 — Passe 2: montagem dos marcos" (D-01 marco: frase de capacidade junto da
    User Story; D-03 reforco: primeiro marco menor).
  - "Passo 8 — Walking Skeleton (Marco 00)" (D-03: nomear primeiro done leve).

### Docs CITADOS / consumidos (upstream — nunca redefinir)
- `mentor/fundamentos.md` — saida da Fase 1; alvo dos hyperlinks de D-01 e D-03 (backward
  design / UbD; engajamento-evasao async / time-to-first-success). Ancoras dependem da
  estrutura de cabecalhos desse doc; conferir ao linkar.
- `mentor/reference.md` — saida da Fase 2; dono do formato verbo-capacidade
  ("ao terminar, voce consegue <verbo>...") que D-02 reusa no nivel de marco, e dono do
  template do `PROGRESSO.md` onde a frase por marco e gravada.

### Contexto das fases anteriores (decisoes que esta fase herda)
- `.planning/phases/02-templates-e-sintaxe-reference-md/02-CONTEXT.md` — D-01 (formato do
  verbo de capacidade no nivel de PASSO; o nivel de MARCO aqui e o complemento), D-04
  (citacao via hyperlink), e a nota de Integration Points que ja antecipa que a Fase 3
  consome o campo Objetivo/capacidade.
- `.planning/phases/01-fundacao-teorica-fundamentos-md/01-CONTEXT.md` — formato hibrido do
  `fundamentos.md` e a regra do campo "aplicado em <doc>" (D-05 forward-reference): esta
  fase aterrissa as praticas de backward design e engajamento; a Fase 6 confirma o status.

### Conteudo teorico (o QUE citar — ja decidido pela pesquisa)
- `.planning/research/SUMMARY.md` — Stage 2 do UbD (lacuna L1), backward design
  (Wiggins & McTighe), primeiro done leve / time-to-first-success + Walking Skeleton,
  ressalva de leveza (~1 frase por marco, nao sub-doc).
- `.planning/research/FEATURES.md` — "reduzir time-to-first-success" e "uma unica proxima
  acao" (tags reinforce); mapeamento pratica -> doc.
- `.planning/research/PITFALLS.md` — Pitfall 10 (over-formalizacao do backward design),
  P9 (teoria vazando), P12 (drift fonte-unica).

### Contrato da fase (o que tem de ficar VERDADEIRO)
- `.planning/REQUIREMENTS.md` §EST (EST-03), §ENG (ENG-02), §CONS (CONS-01 anti-leak,
  CONS-02 aplicado-em verificavel).
- `.planning/ROADMAP.md` §"Phase 3" — os 3 Criterios de Sucesso.

### Convencoes e arquitetura do toolkit (COMO editar sem quebrar o design)
- `.planning/codebase/ARCHITECTURE.md` — fonte-unica: teoria so em `mentor/`, citada por
  link, nunca duplicada nos adaptadores.
- `.planning/codebase/STRUCTURE.md` — lugar de `novo-projeto.md` e dos artefatos do aluno.
- `.planning/codebase/CONVENTIONS.md` — portugues sem acentos; paths/identificadores em
  backticks.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `mentor/novo-projeto.md` ja contem todos os passos-alvo; a fase EDITA, nao cria. Notavel:
  - **Passo 4** ja abre com "engenharia reversa do output final -> capacidades necessarias
    -> conceitos necessarios -> ordene" — o backward design macro ja esta la, so falta o
    NOME + link (D-01).
  - **Passo 5** ja enquadra cada marco como User Story e ja distribui a Definition of Done
    — gancho pronto para colar a frase de capacidade (D-01) e o reforco do primeiro marco
    menor (D-03).
  - **Passo 8** ja descreve o Walking Skeleton / Marco 00 como "o esqueleto mais fino que
    prova que todas as camadas funcionam juntas" — gancho pronto para nomear o primeiro
    done leve (D-03).
- `mentor/reference.md` — dono do template do `PROGRESSO.md` (arvore de marcos com User
  Stories) e do formato verbo-capacidade da Fase 2. D-02 grava a frase nesse template.

### Established Patterns
- Fonte-unica: teoria nova nao e escrita aqui; `novo-projeto.md` cita `fundamentos.md` por
  hyperlink (D-01, D-03). Inegociavel.
- Anti-theory-leak: prosa do procedimento (agente) pode nomear frameworks; a frase gravada
  no `PROGRESSO.md` (aluno) so tem o verbo de capacidade puro.
- Estilo: portugues SEM acentos; paths/identificadores em backticks.

### Integration Points
- Upstream consumido: formato verbo-capacidade + template `PROGRESSO.md` (Fase 2);
  `fundamentos.md` (Fase 1) como alvo dos links.
- Downstream: a Fase 4 (`fecha-marco.md` + `tutor.md`) CONSOME a frase de capacidade por
  marco gravada no `PROGRESSO.md` — o mastery gate cobra exatamente essa capacidade. A
  leveza decidida aqui (D-04, 1 frase) e o contrato que a Fase 4 espera encontrar.

</code_context>

<specifics>
## Specific Ideas

- Frase de capacidade por marco no formato da Fase 2:
  "Capacidade: ao terminar, voce consegue <verbo> <conceito>", colada abaixo da User Story
  na arvore de marcos do `PROGRESSO.md`.
- Guardrail literal sugerido para o `novo-projeto.md`: "Stage 2 = exatamente 1 frase de
  capacidade por marco. Se virou lista, rubrica ou sub-doc, esta errado — corte."
- Interpretacao do ROADMAP a registrar: "entre caminho e marcos" = backward design
  conceitual (evidencia definida junto ao marco), nao posicao fisica antes do Passo 5.

</specifics>

<deferred>
## Deferred Ideas

- Campo de agenda de retrieval/dividas no `PROGRESSO.md` — pertence a Fase 4 (ENG-01/
  AVAL-02), nao a esta fase. So registrar para o planner nao confundir.
- Confirmacao final de que cada "(Fase 3, pendente)" do `fundamentos.md` virou aplicacao
  real (backward design, primeiro done leve) — auditoria da Fase 6 (CONS-02).
- Mitigacao "campo opcional para muitos marcos" sugerida na pesquisa — REJEITADA aqui
  (D-04): leveza vem do teto de 1 frase, nao da opcionalidade.

</deferred>

---

*Phase: 03-bootstrap-com-stage-2-novo-projeto-md*
*Context gathered: 2026-06-14*
