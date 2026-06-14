# Phase 2: Templates e sintaxe (reference.md) - Research

**Researched:** 2026-06-14
**Domain:** Edicao de doc de metodo (markdown) — costura de pedagogia ja decidida nos templates de `mentor/reference.md`
**Confidence:** HIGH (estrutura/arquivo verificada por leitura direta; teoria fixada pela Fase 1)

## Summary

Esta fase EDITA um unico arquivo — `mentor/reference.md` — para tecer 3 fios nos templates
que todos os procedimentos downstream consomem: (1) o verbo de capacidade ao lado do
entregavel de artefato (EST-01), (2) a sintaxe GRR de 3 fases "eu faco -> nos fazemos ->
voce faz" (EST-04), e (3) os principios de carga cognitiva — fading por substrato,
worked example analogo, e os 3 principios de Mayer que transferem para texto puro
(CARGA-01/02/03). Sempre CITANDO `fundamentos.md` por hyperlink relativo (EST-02), nunca
reescrevendo a teoria localmente (fonte-unica). A teoria (o QUE cada framework diz) ja
esta fixada em HIGH confidence pela Fase 1 e NAO foi re-pesquisada; o trabalho aqui e
puramente estrutural/editorial.

A leitura direta dos dois arquivos confirmou tres fatos que governam o plano. **Primeiro:**
todos os ganchos que as decisoes D-01..D-04 precisam JA existem em `reference.md` — a fase
edita corpo de secoes existentes, nao cria secoes novas. **Segundo, e o achado mais
load-bearing:** os nomes de framework em `fundamentos.md` vivem em CELULAS DE TABELA, nao em
cabecalhos `##`/`###`. Logo NAO existem ancoras como `#backward-design` ou `#grr`. As unicas
ancoras reais sao as 9 ancoras de SECAO (calculadas abaixo). O formato `[backward
design](fundamentos.md#backward-design)` sugerido no CONTEXT D-04 NAO resolve — apontaria
para uma ancora inexistente. **Terceiro:** a fronteira anti-theory-leak e nitida — a prosa de
`reference.md` (instrucao de agente, FORA dos blocos ```` ```markdown ````/```` ```text ````)
pode nomear frameworks e linkar; o conteudo DENTRO dos blocos de template vira artefato do
aluno e so pode conter o verbo de capacidade puro, zero jargao.

**Primary recommendation:** Editar 6 zonas de `reference.md` em uma unica passada coerente,
linkando frameworks SO na prosa para a ancora de SECAO correta de `fundamentos.md` (nunca uma
ancora de framework, que nao existe), e mantendo todo bloco ```` ```markdown ````/```` ```text ````
livre de jargao. Resolver D-02 reescrevendo o CORPO da secao da linha 382 (titulo ja promete 3
fases, corpo entrega 2).

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**D-01 — Campo "Objetivo" (capacidade), EST-01 (delegado a Claude, decisao ja escolhida):**
Adicionar uma linha nova `Objetivo (capacidade):` em cada passo do template `CAMINHO.md`,
posicionada ACIMA da linha `Entregavel:` (capacidade primeiro, artefato como evidencia — ordem
backward design). Forma: `- Objetivo (capacidade): ao terminar, voce consegue <verbo>
<conceito>`.
- O template de aula ja tem `## Objetivo do passo` (hoje so descreve o entregavel) — ajustar
  para espelhar capacidade + artefato.
- O campo `DONE:` do scaffold e reenquadrado como "evidencia observavel de que a capacidade foi
  adquirida", nao so "o codigo roda".
- **Anti-leak:** dentro dos blocos de template (doc do aluno) aparece SO o verbo de capacidade —
  nunca o rotulo "Bloom" nem "objetivo cognitivo". O "porque" (backward design / constructive
  alignment) fica na PROSA do `reference.md`, via hyperlink (D-04).

**D-02 — Sintaxe GRR de 3 fases, EST-04:** REESCREVER a secao existente "### Sintaxe nova de
verdade: 'eu faco -> nos fazemos -> voce faz'" (atual linha ~382). Hoje o TITULO promete 3 fases
mas o CORPO so entrega 2 (mostra exemplo -> pede variacao solo). A reescrita transforma "nos
fazemos" numa etapa REAL e CONDICIONAL:
- **eu faco:** exemplo resolvido em instancia diferente (= worked example, ver D-03).
- **nos fazemos:** pratica conjunta guiada — o agente puxa cada micro-decisao, o aluno responde,
  o agente confirma — numa instancia ainda diferente do `TODO` solo.
- **voce faz:** o `TODO(human)` solo.
- **Gatilho condicional:** ligar "nos fazemos" quando o substrato no conceito dominante e
  zero-absoluto/iniciante OU quando o salto exemplo->solo e grande. Pular para
  intermediario/avancado (onde vira atrito — conecta com o fading, D-03).

**D-03 — Carga cognitiva: fading + worked example, CARGA-01, CARGA-02:** Forma otimizada para
AGENTE (regra mecanica, nao prosa pro aluno) — confirmado pelo usuario.
- **Fading (CARGA-01, expertise-reversal):** regra de calibragem explicita na secao de substrato
  — uma tabela/lista substrato -> densidade de andaime+pista, com o principio nomeado: "o
  suporte recua conforme a maestria sobe; suporte demais ATRAPALHA o avancado". Formaliza o que
  hoje so esta implicito ("mais buraco, menos pista").
- **Worked example analogo (CARGA-02):** NAO cria secao nova — FUNDE no "eu faco" do D-02. A
  regra: para substrato zero-absoluto no conceito dominante, o agente DEVE dar um exemplo
  resolvido em instancia DIFERENTE antes do `TODO` solo. (Ja alinha com a secao "Exemplos de
  aplicacao" do template de aula.)

**D-04 — Mayer + citacao de fundamentos.md, CARGA-03, EST-02:** Citacao via HYPERLINK markdown.
- **EST-02:** toda mencao a framework na PROSA do `reference.md` (backward design, GRR,
  expertise-reversal, etc.) vira `[nome do framework](fundamentos.md#ancora)`, sem reescrever a
  teoria (fonte-unica). `reference.md` e `fundamentos.md` moram ambos em `mentor/`, entao o link
  e relativo no mesmo diretorio.
- **CARGA-03 (Mayer):** os 3 principios que transferem para texto puro (coerencia, sinalizacao,
  segmentacao) + linguagem simples/legivel entram como REGRA DE AGENTE na secao "Regras da aula"
  (sobre COMO escrever a aula). Registrar honestamente o limite "so 3 de 12 principios transferem
  para texto puro", com hyperlink para `fundamentos.md`.

### Claude's Discretion
- D-01 foi delegado integralmente (decisao acima ja e a escolhida).
- Posicionamento exato das ancoras de hyperlink (D-04) depende da estrutura de cabecalhos do
  `fundamentos.md` produzido na Fase 1. O executor deve conferir as ancoras reais ao linkar.
  **[RESOLVIDO NESTA PESQUISA — ver secao "D-04: Mapa real de ancoras de `fundamentos.md`".]**

### Deferred Ideas (OUT OF SCOPE)
- Campo de agenda de retrieval/dividas no template `PROGRESSO.md` — pertence a Fase 4 no ROADMAP
  (ENG-01/AVAL-02), nao a Fase 2. NAO adicionar agora.
- Confirmacao final de que cada "(Fase 2, pendente)" do `fundamentos.md` virou aplicacao real —
  auditoria da Fase 6 (CONS-02), nao desta fase.
- Productive Failure / modo tente-antes — FUT-02 (v2), evidencia MEDIUM.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| EST-01 | Template `CAMINHO.md` ganha campo "Objetivo" (capacidade, verbo de Bloom) ao lado do "Entregavel" de artefato | Gancho confirmado: `reference.md:69,77` (`Entregavel:` em cada passo); template de aula `## Objetivo do passo` em `:280`; campo `DONE:` do scaffold em `:347`. D-01 define a forma exata. |
| EST-02 | Backward design e GRR nomeados onde ja ocorrem, referenciando `fundamentos.md` | Ancoras de SECAO reais de `fundamentos.md` calculadas abaixo (NAO ha ancora de framework). Backward design vive na celula `fundamentos.md:24`; GRR/worked-example na celula `:27`; constructive alignment `:25`. Link aponta para a ancora de SECAO que CONTEM a celula. |
| EST-04 | Fase "nos fazemos" (we do) do GRR formalizada como etapa intermediaria explicita entre exemplo resolvido e `TODO(human)` solo | Secao-alvo confirmada em `reference.md:382` ("Sintaxe nova de verdade"); titulo ja diz 3 fases, corpo (`:384-395`) entrega 2. D-02 = reescrita do corpo. |
| CARGA-01 | Fading de scaffold por substrato (andaime recua conforme dominio sobe), tratando expertise-reversal | Calibragem parcial ja existe: `reference.md:17-22` (tabela substrato->andaime na "Sondagem de substrato"); `:43-44` ("Granularidade ~ 1/nivel"); `:22` ("mais buraco, menos pista"). D-03 formaliza como fading nomeado. |
| CARGA-02 | Worked example analogo antes do `TODO(human)` para substrato baixo (instancia diferente) | Gancho ja existe: `reference.md:299-303` ("Exemplos de aplicacao", "este e o 'eu faco'"); `:267-270` (contrato "instancia DIFERENTE"). D-03 funde no "eu faco" do D-02. |
| CARGA-03 | Aula/scaffold aplica 3 principios de Mayer (coerencia, sinalizacao, segmentacao) + linguagem simples; cita limite honesto | Limite ja registrado em `fundamentos.md:70-75` (ressalva Mayer). D-04 adiciona regra de agente em "Regras da aula" (`reference.md:318-330`), linkando a ressalva. |
</phase_requirements>

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Definir verbo de capacidade (EST-01) | `reference.md` template (Camada Referencia) | `novo-projeto.md` (Fase 3 consome) | Templates sao a fonte unica da FORMA do campo; bootstrap so deriva 1 frase por marco depois. |
| Sintaxe GRR 3 fases (EST-04) | `reference.md` prosa + secao de scaffold | `tutor.md` (Fase 4 aciona "nos fazemos") | Sintaxe e definida no doc de referencia; o tutor a executa em runtime. |
| Fading por substrato (CARGA-01) | `reference.md` "Sondagem de substrato" | — | Regra de calibragem de andaime e parte das regras de referencia; o agente a le sob demanda. |
| Worked example (CARGA-02) | `reference.md` "eu faco" + template de aula | — | Funde na sintaxe GRR e na secao "Exemplos de aplicacao" da aula; nenhuma camada nova. |
| Citacao de teoria (EST-02, CARGA-03) | `fundamentos.md` (Camada upstream, dono da teoria) | `reference.md` prosa (cita por link) | Fonte-unica: teoria so em `fundamentos.md`; `reference.md` referencia, nunca redefine. |

**Nota:** Este "sistema" e um toolkit de instrucoes markdown, nao software em runtime. As "tiers"
sao camadas conceituais de documento (Persona / Procedimentos / Referencia / upstream-teoria),
conforme `ARCHITECTURE.md`. Nenhuma camada de execucao envolvida.

## Standard Stack

Nao ha stack de software nesta fase. O "stack" sao convencoes editoriais do toolkit (de
`CONVENTIONS.md`), tratadas como restricoes inegociaveis:

| Convencao | Regra | Por que e padrao |
|-----------|-------|------------------|
| Idioma | Portugues **SEM acentos** ("voce", "metodo", "codigo") | `CONVENTIONS.md` — consistente em todo `mentor/`; robustez de encoding [VERIFIED: CONVENTIONS.md:8-11] |
| Identificadores inline | Sempre em backticks (`TODO(human)`, `CAMINHO.md`, `/tutor`) | `CONVENTIONS.md:12-14` — padrao rigoroso [VERIFIED] |
| Paths de arquivo | Relativos a raiz do repo, em backticks | `CONVENTIONS.md:15` [VERIFIED] |
| Blocos de exemplo | Cercados com linguagem (```` ```markdown ````, ```` ```text ````) | `CONVENTIONS.md:16-18`; templates longos vivem como blocos ```` ```markdown ```` [VERIFIED] |
| Enfase | **negrito** para regras inegociaveis; `>` blockquote para notas de contrato no topo | `CONVENTIONS.md:19-20` [VERIFIED] |
| Tom | 2a pessoa, imperativo, falando COM o agente | `CONVENTIONS.md` [VERIFIED] |
| Tabelas | Para mapeamentos (substrato->andaime, situacao->procedimento) | `CONVENTIONS.md:21` [VERIFIED] |

**Instalacao:** Nenhuma. Edicao de markdown existente.

## Architecture Patterns

### Mapa preciso de `mentor/reference.md` (alvo da edicao)

Leitura direta verificou as seguintes zonas-alvo (numeros de linha do estado atual do arquivo):

| Zona | Secao (linha do `##`/`###`) | Range atual | Conteudo atual (1 linha) | Decisao que toca |
|------|------------------------------|-------------|--------------------------|------------------|
| Z1 | `## Sondagem de substrato` (L3) | 3-32 | Sondas + classificacao 4-niveis (`L17-22` ja mapeia substrato->andaime); `L22` "mais buraco, menos pista" | **CARGA-01** (fading nomeado aqui, D-03) |
| Z2 | `## Regra de granularidade` (L34) | 34-44 | `L43-44` "Granularidade ~ 1/nivel" (andaime ~ 1/nivel) | **CARGA-01** (reforco; principio expertise-reversal nomeado) |
| Z3 | `## Template — CAMINHO.md` (L46) | 46-94 | Bloco ```` ```markdown ```` `L51-84` com passos P01/P02; cada passo tem `Entregavel:` (`L69`, `L77`) mas NAO `Objetivo (capacidade)` | **EST-01** (D-01: add linha `Objetivo (capacidade):` ACIMA de `Entregavel:`) |
| Z4 | `## Template — aula` (L260) | 260-330 | `## Objetivo do passo` (`L280`, hoje so espelha entregavel); `## Exemplos de aplicacao` (`L299-303`, ja diz "este e o 'eu faco'"); `Regras da aula` (`L318-330`) | **EST-01** (espelhar capacidade+artefato em `L280`); **CARGA-02** (worked example, `L299-303`); **CARGA-03** (regra Mayer em `Regras da aula`) |
| Z5 | `## Formato do scaffold (TODO human)` (L332) | 332-395 | Bloco ```` ```text ```` `L337-353` com campos META..PISTA; `DONE:` em `L347` ("como o aluno sabe que terminou") | **EST-01** (reenquadrar `DONE:` como evidencia de capacidade, D-01) |
| Z6 | `### Sintaxe nova de verdade: "eu faco -> nos fazemos -> voce faz"` (L382) | 382-395 | **Titulo promete 3 fases; corpo (`L384-395`) entrega 2** (mostra exemplo -> pede variacao solo). "nos fazemos" ausente. | **EST-04** (D-02: reescrever corpo, "nos fazemos" condicional); **CARGA-02** ("eu faco" = worked example) |

**Achado D-02 confirmado:** em `reference.md:382` o titulo lista 3 fases, mas o corpo `L388-389`
diz apenas "MOSTRE um exemplo resolvido primeiro (o 'eu faco') ... e so entao peca ao aluno pra
APLICAR numa VARIACAO (... o 'voce faz')". A etapa "nos fazemos" NAO aparece no corpo. D-02 e
literalmente preencher essa lacuna. [VERIFIED: leitura de reference.md]

### D-04: Mapa real de ancoras de `fundamentos.md` (CRITICO)

**Achado central:** os nomes de framework em `fundamentos.md` vivem em CELULAS DE TABELA, nao
em cabecalhos. Os unicos cabecalhos `##`/`###` do arquivo sao 9, listados abaixo com a ancora
GitHub/markdown correspondente. NAO existe `#backward-design`, `#grr`, `#expertise-reversal`,
etc. O formato `[backward design](fundamentos.md#backward-design)` sugerido em CONTEXT D-04
(linha 171-172) apontaria para ancora INEXISTENTE — link quebrado.

Algoritmo de ancora GitHub/markdown aplicado: minusculas, espacos -> hifen, pontuacao removida
(parenteses, dois-pontos), `--` colapsa (sem hifens duplos pendentes nas bordas).

| Cabecalho real em `fundamentos.md` | Linha | Ancora computada | Frameworks que essa secao cobre |
|-------------------------------------|-------|------------------|---------------------------------|
| `## Como ler este doc` | 10 | `#como-ler-este-doc` | (meta) |
| `## Frameworks foundational (load-bearing)` | 19 | `#frameworks-foundational-load-bearing` | Backward Design, Constructive Alignment, Cognitive Load Theory, Worked-Example+Expertise-Reversal, First Principles, Retrieval |
| `## Frameworks supporting (ancoram um doc)` | 41 | `#frameworks-supporting-ancoram-um-doc` | SDT, ZPD/Scaffolding, Mastery, Avaliacao Formativa, Feedback Hattie, Spacing |
| `## Limites e ressalvas` | 58 | `#limites-e-ressalvas` | (container das 2 ressalvas) |
| `### SDT relatedness em solo+IA` | 62 | `#sdt-relatedness-em-soloia` | ressalva SDT (nota: `+` removido, `solo+IA` -> `soloia`) |
| `### Mayer: so 3 de 12 principios em texto puro` | 70 | `#mayer-so-3-de-12-principios-em-texto-puro` | **ressalva Mayer (alvo de CARGA-03)** |
| `## O que NAO usamos e por que` | 77 | `#o-que-nao-usamos-e-por-que` | mitos refutados |
| `## Nice-to-cite` | 89 | `#nice-to-cite` | Bloom revisado (verbos), Mayer ponteiro |

> **Verificacao obrigatoria do executor:** o algoritmo de ancora pode variar entre renderizadores
> (GitHub vs VS Code preview vs pandoc). As ancoras acima seguem a convencao GitHub. O executor
> DEVE confirmar contra o renderizador-alvo e, se possivel, validar que cada link resolve.
> Confianca da ancora `#sdt-relatedness-em-soloia`: MEDIUM (tratamento de `+` em `solo+IA` e o
> caso mais arriscado). As demais: HIGH.

### Mapa decisao -> framework -> ancora de link (D-04 EST-02)

| Decisao na prosa | Framework a nomear | Link recomendado | Justificativa |
|------------------|--------------------|--------------------------|---------------|
| D-01 "porque" do Objetivo | backward design / constructive alignment | `[backward design](fundamentos.md#frameworks-foundational-load-bearing)` | celula vive nessa secao (`fundamentos.md:24-25`) |
| D-02 sintaxe GRR | Gradual Release / worked-example | `[liberacao gradual de responsabilidade](fundamentos.md#frameworks-foundational-load-bearing)` | GRR/worked-example na celula `:27` (mesma secao) |
| D-03 fading | expertise-reversal effect | `[expertise-reversal effect](fundamentos.md#frameworks-foundational-load-bearing)` | celula `:27` |
| D-03 worked example | worked-example effect | (mesmo link da secao foundational) | celula `:27` |
| D-04 Mayer | principios de Mayer (limite 3-de-12) | `[so 3 de 12 principios transferem](fundamentos.md#mayer-so-3-de-12-principios-em-texto-puro)` | a ressalva tem cabecalho proprio (`:70`) — UNICA ancora de framework-especifico que existe |

**Implicacao para o planner:** so a ressalva Mayer e as 2 ressalvas tem ancora granular. Todos os
demais frameworks compartilham a ancora `#frameworks-foundational-load-bearing`. Isso e aceitavel
para fonte-unica (o leitor cai na secao certa e ve a celula), mas o planner deve escrever o
texto-ancora do link com o NOME do framework para o link ser auto-descritivo. Opcao alternativa de
maior fidelidade: linkar com texto que cite a celula ("ver a entrada Backward Design em
[fundamentos](...#frameworks-foundational-load-bearing)").

### Anti-Patterns to Avoid

- **Linkar para ancora de framework inexistente:** `fundamentos.md#backward-design` NAO resolve.
  Usar a ancora de SECAO (tabela acima).
- **Reescrever teoria em `reference.md`:** viola fonte-unica. Citar por link, 0 redefinicao.
- **Vazar jargao para dentro dos blocos de template:** ver secao Anti-Theory-Leak abaixo.
- **Criar secao nova quando a decisao pede edicao de corpo:** D-02 e D-03 EDITAM secoes
  existentes (Z6, Z1, Z4); nao criar duplicatas.
- **Adicionar acentos:** todo `mentor/` e portugues sem acentos.
- **Tocar `PROGRESSO.md` (Z fora de escopo):** o campo de retrieval e Fase 4. Nao adicionar.

## Anti-Theory-Leak Boundary (CONS-01) — mapa de zona segura vs zona de risco

A regra: **prosa de `reference.md`** (instrucao de agente, fora dos blocos cercados) PODE nomear
frameworks e linkar `fundamentos.md`. **Dentro dos blocos** ```` ```markdown ```` (CAMINHO,
PROGRESSO, APRENDIZADO, aula) e ```` ```text ```` (scaffold) — que viram artefato lido pelo ALUNO
— so o verbo de capacidade puro, ZERO jargao de framework.

| Local da edicao | Tipo | Pode nomear framework + linkar? | Risco de leak |
|-----------------|------|-------------------------------|---------------|
| Z1/Z2 prosa de Sondagem/Granularidade | prosa de agente | SIM (nomear expertise-reversal + link) | BAIXO |
| Z3 dentro do bloco ```` ```markdown ```` do CAMINHO (`L51-84`) | artefato do aluno | NAO — so `- Objetivo (capacidade): ... <verbo> <conceito>` | **ALTO** — nunca escrever "Bloom"/"objetivo cognitivo" aqui |
| Z3 prosa "Regras do caminho" (`L86-94`) | prosa de agente | SIM | BAIXO |
| Z4 dentro do bloco da aula (`L272-316`) | artefato do aluno | NAO — `## Objetivo do passo` mostra capacidade+artefato em linguagem simples | **ALTO** |
| Z4 prosa "Regras da aula" (`L318-330`) | prosa de agente | SIM — aqui entra a regra Mayer + link (D-04) | BAIXO |
| Z5 dentro do bloco ```` ```text ```` do scaffold (`L337-353`) | artefato do aluno | NAO — `DONE:` reenquadrado em linguagem de capacidade observavel, sem jargao | **ALTO** |
| Z6 prosa "Sintaxe nova de verdade" (`L382-395`) | prosa de agente | SIM — nomear GRR + link (D-02/EST-02) | BAIXO |

**Pontos de risco concretos (o planner deve marcar como verificacao):**
1. A linha `- Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>` (D-01) entra
   DENTRO do bloco ```` ```markdown ```` do CAMINHO (Z3). O `<verbo>` e um verbo de Bloom mas a
   palavra "Bloom" NAO pode aparecer. So o verbo concreto ("explicar", "construir", "depurar").
2. O reenquadramento de `DONE:` (Z5) acontece DENTRO do bloco ```` ```text ````. Reformular como
   "evidencia observavel de que voce consegue <capacidade>" — sem citar "constructive alignment".
3. A regra Mayer (D-04, CARGA-03) e regra de AGENTE: vai na prosa "Regras da aula" (Z4 prosa),
   NUNCA dentro do bloco da aula. So la ela pode nomear "Mayer" e linkar.

**Provenance:** boundary derivada de CONTEXT.md `<domain>` (`L24-30`), confirmada contra a
estrutura real dos blocos cercados em `reference.md` [VERIFIED]. Alinhada com `fundamentos.md:3-8`
(preambulo "nunca lido pelo aluno") e REQUIREMENTS CONS-01.

## Don't Hand-Roll

| Problema | Nao faca | Use em vez | Por que |
|----------|----------|------------|---------|
| Definir o que cada framework significa | Reescrever a definicao de backward design / GRR / Mayer em `reference.md` | Linkar `fundamentos.md` (fonte-unica) | Duplicacao gera drift; CONS-02/fonte-unica proibe |
| Computar ancora "no olho" | Inventar `#backward-design` | Usar a tabela de ancoras de SECAO acima | Ancora de framework nao existe; so secao |
| Inventar verbos de capacidade | Criar lista nova de verbos | Citar Bloom revisado como banco de verbos (`fundamentos.md` nice-to-cite `:94`) | Ja decidido; banco de verbos, nao piramide |
| Reordenar campos do scaffold | Mudar a ordem META..PISTA | Manter ordem fixa (`CONVENTIONS.md:27-29`); so reenquadrar `DONE:` | Ordem e contrato inviolavel |

**Key insight:** Toda "teoria" desta fase ja foi escrita na Fase 1 (`fundamentos.md`). O trabalho e
APONTAR para ela, nao re-escreve-la. O unico conteudo novo legitimo em `reference.md` sao REGRAS DE
AGENTE (mecanica de como aplicar) e a FORMA dos campos de template.

## Common Pitfalls

### Pitfall 1: Link para ancora de framework inexistente
**O que da errado:** `[backward design](fundamentos.md#backward-design)` resolve para nada (404 de
ancora). **Por que acontece:** CONTEXT D-04 (`L171-172`) sugeriu esse formato como exemplo, mas
`fundamentos.md` poe frameworks em tabelas. **Como evitar:** usar a tabela de ancoras de SECAO
desta pesquisa. **Sinal de alerta:** clicar o link e nao pular para a secao certa.

### Pitfall 2: Jargao vazando para dentro de bloco de template
**O que da errado:** escrever "objetivo cognitivo (Bloom)" dentro do bloco ```` ```markdown ````
do CAMINHO ou da aula. Vira artefato do aluno -> recria o "paredao de teoria". **Por que
acontece:** a linha do Objetivo (D-01) e tecnicamente derivada de Bloom, tentando-se nomear a
fonte. **Como evitar:** dentro do bloco, so o verbo concreto. Frameworks so na prosa. **Sinal de
alerta:** grep por `Bloom|cognitiv|backward|GRR|Mayer|expertise` DENTRO de um bloco cercado.

### Pitfall 3: D-02 vira secao nova em vez de reescrita
**O que da errado:** criar uma secao "### Pratica guiada (nos fazemos)" separada, deixando o corpo
de `L382` ainda com 2 fases. Resultado: titulo e corpo contraditorios + duplicacao. **Como
evitar:** reescrever o CORPO de Z6 (`L384-395`) inline. **Sinal de alerta:** duas secoes falando de
"eu faco -> voce faz".

### Pitfall 4: Inflar o claim de Mayer
**O que da errado:** escrever "aplicamos os principios de Mayer" sem o limite. **Por que
acontece:** simplificacao. **Como evitar:** registrar honestamente "so 3 de 12 transferem para
texto puro (coerencia, sinalizacao, segmentacao)" e linkar a ressalva. `fundamentos.md:70-75` ja
tem o texto-fonte. **Sinal de alerta:** ausencia do numero "3 de 12" na regra Mayer.

### Pitfall 5: Acentos ou path sem backtick
**O que da errado:** "você"/"método" ou `fundamentos.md` sem backtick na prosa. **Como evitar:**
portugues sem acentos; paths em backticks (`CONVENTIONS.md`). **Sinal de alerta:** grep por
caracteres acentuados nas linhas editadas.

## Code Examples

Padroes editoriais verificados no proprio `reference.md` (a serem espelhados):

### Linha de Objetivo dentro do bloco CAMINHO (D-01) — SEM jargao
```markdown
### P01 — <titulo curto>

- Conceito dominante (novo): c01-<slug>
- Pressupoe: (nenhum — entrada coberta pelo substrato)
- Substrato exigido: <assunto>: zero-absoluto ok ("eu faco -> voce faz")
- Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>
- Entregavel: <o que o aluno ESCREVE> + <o que ele VE funcionando ao terminar>
- Arquivos: <paths em projeto/>
```
> Fonte do gancho: `reference.md:64-71` (estado atual; linha Objetivo e a insercao de D-01,
> ACIMA de `Entregavel:`). Verbo concreto, zero "Bloom".

### Citacao por link na prosa (D-04 EST-02) — COM framework nomeado
```markdown
A ordem capacidade-primeiro, artefato-como-evidencia segue
[backward design](fundamentos.md#frameworks-foundational-load-bearing): defina o
resultado desejado antes da atividade.
```
> So na prosa. O link aponta a SECAO que contem a celula do framework.

### Regra Mayer em "Regras da aula" (D-04 CARGA-03) — limite honesto + link
```markdown
- **Apresentacao (texto puro):** aplique os 3 principios de Mayer que transferem para
  texto — coerencia (corte o superfluo), sinalizacao (destaque o essencial), segmentacao
  (um passo atomico por vez) — e linguagem simples. Os outros 9 tratam de audio/video e
  nao se aplicam: ver [so 3 de 12 principios transferem](fundamentos.md#mayer-so-3-de-12-principios-em-texto-puro).
```
> Fonte do texto-limite: `fundamentos.md:70-75` [VERIFIED]. Entra na prosa "Regras da aula"
> (`reference.md:318-330`), nunca dentro do bloco da aula.

## State of the Art

| Old Approach (estado atual de `reference.md`) | Current Approach (apos Fase 2) | Impact |
|-----------------------------------------------|--------------------------------|--------|
| Passo so tem `Entregavel:` (artefato) | `Objetivo (capacidade):` ACIMA + `Entregavel:` | Backward design explicito; capacidade vira o norte |
| `## Objetivo do passo` so descreve entregavel | espelha capacidade + artefato | Alinhamento construtivo CAMINHO->aula->scaffold |
| `DONE:` = "como sabe que terminou" (codigo roda) | evidencia observavel de CAPACIDADE | Combate proxy-completion |
| Secao L382: titulo 3 fases, corpo 2 fases | corpo com "nos fazemos" condicional real | GRR completo; we-do deixa de ser implicito |
| Fading implicito ("mais buraco, menos pista") | regra nomeada (expertise-reversal) + link | Calibragem por substrato formalizada |
| Mayer ausente | regra de agente + limite honesto + link | Carga cognitiva em apresentacao de texto |

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | A ancora GitHub para `### Mayer: so 3 de 12 principios em texto puro` e `#mayer-so-3-de-12-principios-em-texto-puro` | D-04 ancoras | Link quebrado; executor deve validar no renderizador-alvo |
| A2 | A ancora para `### SDT relatedness em solo+IA` colapsa `solo+IA` -> `soloia` (`#sdt-relatedness-em-soloia`) | D-04 ancoras | MEDIUM — tratamento de `+` varia; nao usada nesta fase (SDT e Fase 4), so listada por completude |
| A3 | Os numeros de linha de `reference.md` permanecem estaveis ate a execucao (arquivo nao editado entre research e plan) | Mapa de Z1-Z6 | Linhas deslocam se o arquivo mudar; ranges sao guia, ancorar por TITULO de secao e mais robusto |
| A4 | Linkar para `#frameworks-foundational-load-bearing` (secao, nao framework) satisfaz EST-02 ("referenciando fundamentos.md") | D-04 EST-02 | BAIXO — o requisito pede referencia, nao ancora granular; secao certa cumpre |

**Nota:** A1 e A2 sao as unicas assuncoes de risco real. Mitigacao: o executor valida a resolucao
de cada hyperlink contra o renderizador-alvo antes de fechar a fase (ver Validation Architecture).

## Open Questions

1. **Renderizador-alvo das ancoras**
   - O que sabemos: as ancoras seguem a convencao GitHub; ambos os docs estao em `mentor/`.
   - O que e incerto: se o consumo primario e GitHub web, VS Code preview, ou leitura raw pelo
     agente (caso em que a ancora nem importa — o agente le o arquivo inteiro).
   - Recomendacao: usar ancoras GitHub (mais comum); validar 1 link manualmente na execucao. Se o
     consumo for so o agente lendo raw, o link ainda e util para humanos navegarem (intencao do
     usuario em D-04).

2. **Texto-ancora compartilhado para multiplos frameworks**
   - O que sabemos: 4 frameworks (backward design, GRR, worked-example, expertise-reversal)
     compartilham `#frameworks-foundational-load-bearing`.
   - O que e incerto: se isso confunde o leitor (varios links para a mesma secao).
   - Recomendacao: escrever o texto-ancora com o NOME do framework para autodescricao; aceitar o
     destino compartilhado (fonte-unica nao exige ancora por framework).

## Validation Architecture

> `nyquist_validation` esta `true` em `.planning/config.json`. Esta fase e trabalho de doc/metodo
> (sem codigo executavel), entao a "validacao" e VERIFICACAO ESTATICA: presenca de strings,
> presenca de campos/secoes, e resolucao de hyperlinks. Sem framework de teste de runtime.

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Nenhum (verificacao estatica via `grep`/`rg` + inspecao manual de link) |
| Config file | none — ver Wave 0 |
| Quick run command | `rg -n "<padrao>" mentor/reference.md` por criterio |
| Full suite command | Script de checagem (lista abaixo) rodado contra `mentor/reference.md` e `mentor/fundamentos.md` |

### Phase Requirements -> Test Map

Cada Criterio de Sucesso da Fase 2 mapeado a uma verificacao grep-avel. "File Exists?" indica se o
alvo da verificacao ja existe (arquivo) — todos sim, pois a fase EDITA.

| Req / SC | Behavior verificavel | Test Type | Comando automatizado (estatico) | Existe? |
|----------|----------------------|-----------|----------------------------------|---------|
| EST-01 / SC1 | Linha `Objetivo (capacidade):` existe DENTRO do bloco CAMINHO, ACIMA de `Entregavel:` | grep + ordem | `rg -n "Objetivo \(capacidade\):" mentor/reference.md` E confirmar que aparece antes de `Entregavel:` no mesmo passo | sim |
| EST-01 / SC1 | `## Objetivo do passo` espelha capacidade + artefato | grep + inspecao | `rg -n "## Objetivo do passo" mentor/reference.md` + leitura do corpo | sim |
| EST-01 / SC1 | `DONE:` reenquadrado como evidencia de capacidade | grep | `rg -n "DONE:.*capacidade\|evidencia" mentor/reference.md` (inspecionar texto do campo no bloco scaffold) | sim |
| EST-04 / SC2 | Corpo da secao L382 contem as 3 fases nomeadas | grep | `rg -n "nos fazemos" mentor/reference.md` deve achar no CORPO (nao so no titulo) | sim |
| EST-04 / SC2 | "nos fazemos" enquadrado como condicional (gatilho substrato/salto) | inspecao | leitura: presenca de gatilho zero-absoluto/iniciante OU salto grande | sim |
| EST-02 / SC3 | Backward design e GRR nomeados + linkam `fundamentos.md` | grep link | `rg -n "\]\(fundamentos\.md#" mentor/reference.md` retorna >= 2 links | sim |
| CARGA-01 / SC4 | Fading nomeado (expertise-reversal) na secao de substrato | grep | `rg -n "recua\|expertise-reversal\|suporte demais" mentor/reference.md` na zona Z1/Z2 | sim |
| CARGA-02 / SC4 | Worked example analogo (instancia diferente) no "eu faco" | grep | `rg -n "instancia diferente\|exemplo resolvido" mentor/reference.md` na zona Z6/Z4 | sim |
| CARGA-03 / SC5 | 3 principios de Mayer + limite honesto + link, em "Regras da aula" | grep | `rg -n "coerencia.*sinalizacao.*segmentacao\|3 de 12\|3 principios" mentor/reference.md` | sim |
| CONS-01 (anti-leak) | NENHUM jargao de framework DENTRO de bloco cercado | grep negativo | extrair blocos ```` ``` ```` e confirmar 0 ocorrencias de `Bloom\|backward design\|GRR\|Mayer\|expertise-reversal\|constructive alignment\|cognitive load` | sim |
| EST-02 (link resolve) | Cada `fundamentos.md#ancora` aponta a um cabecalho real | resolucao de ancora | extrair ancoras dos links e cruzar com `rg -n "^#" mentor/fundamentos.md` (tabela desta pesquisa) | sim |

### Sampling Rate
- **Por edicao/commit:** rodar o grep do criterio tocado + o grep negativo anti-leak (Pitfall 2).
- **No fechamento da fase:** rodar a suite completa (todos os comandos da tabela) + validar
  manualmente a resolucao de >= 1 hyperlink no renderizador-alvo.
- **Gate da fase:** todos os 5 Criterios de Sucesso verdadeiros + anti-leak verde + links resolvem
  antes de `/gsd-verify-work`.

### Wave 0 Gaps
- [ ] Nenhum arquivo de teste de runtime aplicavel (doc/metodo).
- [ ] Recomendado: um pequeno script de checagem estatica (`bash`/`rg`) consolidando os comandos da
  tabela como "smoke test" reproduzivel da fase. Opcional, mas reduz erro manual no gate.
- [ ] Extrator de blocos cercados para a verificacao anti-leak (CONS-01): isolar o conteudo dentro
  de ```` ``` ```` e rodar o grep negativo so nesse subconjunto. Sem ele, o grep negativo daria
  falso-positivo (acharia "backward design" na prosa legitima).

*(O extrator de blocos cercados e o unico utilitario nao-trivial; o resto e grep direto.)*

## Environment Availability

Step 2.6: SKIPPED parcialmente — a fase e edicao de markdown, sem dependencias de runtime. Unicas
ferramentas usadas sao de verificacao estatica, todas presentes no ambiente.

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| `rg` (ripgrep) | Verificacao estatica (Validation Architecture) | assumido (ambiente Claude Code) | — | `grep -n` |
| Renderizador markdown (GitHub/VS Code) | Validacao manual de resolucao de hyperlink (D-04) | depende do consumo humano | — | Inspecao manual da tabela de ancoras desta pesquisa |

**Sem dependencias bloqueantes.**

## Security Domain

Nao aplicavel. Esta fase edita um doc de metodo pedagogico em markdown; nao ha autenticacao,
input de usuario em runtime, criptografia, nem superficie de ataque. `security_enforcement` nao
e relevante para edicao de prosa. (ASVS V1-V14 todas inaplicaveis: sem sistema executavel.)

## Sources

### Primary (HIGH confidence)
- `mentor/reference.md` (leitura integral, 419 linhas) — mapa de secoes Z1-Z6, ganchos D-01..D-04,
  confirmacao do gap de 2-vs-3 fases em L382.
- `mentor/fundamentos.md` (leitura integral) — estrutura de cabecalhos (9 secoes), confirmacao de
  que frameworks vivem em tabelas (sem ancora propria), texto-fonte da ressalva Mayer (L70-75).
- `.planning/phases/02-.../02-CONTEXT.md` — decisoes D-01..D-04 (locked), boundary anti-leak.
- `.planning/REQUIREMENTS.md` — EST-01/02/04, CARGA-01/02/03, CONS-01/02.
- `.planning/ROADMAP.md` — 5 Criterios de Sucesso da Fase 2 (L48-53).
- `.planning/codebase/CONVENTIONS.md` — convencoes editoriais (sem acento, backticks, blocos).
- `.planning/codebase/ARCHITECTURE.md` — fonte-unica + camadas conceituais.

### Secondary (MEDIUM confidence)
- `.planning/research/SUMMARY.md`, `FEATURES.md` — teoria ja decidida (GRR, Bloom, expertise-
  reversal, Mayer 3-de-12); usados como contexto, nao re-pesquisados.
- `.planning/STATE.md` — decisao de NAO gerar CLAUDE.md GSD; build order; estilo sem acento.

### Tertiary (LOW confidence)
- Nenhuma. Esta pesquisa e 100% grounded em arquivos lidos; nenhuma fonte web foi necessaria
  (teoria fixada na Fase 1).

## Metadata

**Confidence breakdown:**
- Mapa de `reference.md` (Z1-Z6): HIGH — leitura direta, linhas verificadas.
- Ancoras de `fundamentos.md` (D-04): HIGH para secoes ASCII simples; MEDIUM para
  `#sdt-relatedness-em-soloia` (tratamento de `+`); a ancora Mayer (a unica usada nesta fase) e
  HIGH.
- Boundary anti-leak: HIGH — derivada de CONTEXT + estrutura real de blocos cercados.
- Validation Architecture: HIGH — verificacoes sao grep-aveis e mapeadas 1:1 aos Criterios.

**Research date:** 2026-06-14
**Valid until:** ate `mentor/reference.md` ou `mentor/fundamentos.md` serem editados por outra
fase (ranges de linha deslocam; ancorar por TITULO de secao mitiga). Estimativa: 30 dias.

**Provenance tags:** [VERIFIED] = confirmado por leitura de arquivo neste sessao. Claims [ASSUMED]
estao isolados no Assumptions Log (A1-A4); todos sao sobre resolucao de ancora em renderizador
especifico, validaveis na execucao.
