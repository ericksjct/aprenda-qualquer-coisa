# Phase 1: Fundacao teorica (fundamentos.md) - Research

**Researched:** 2026-06-14
**Domain:** Documentacao-autoria (catalogo interno de frameworks de ciencia da aprendizagem em markdown)
**Confidence:** HIGH (conteudo travado por pesquisa previa; forma travada por CONTEXT.md D-01..D-05)

> Esta e uma fase de AUTORIA DE DOC, nao de codigo/biblioteca. Nao ha "stack" de software,
> nao ha dependencias externas, nao ha testes automatizados. O entregavel e UM arquivo
> markdown novo: `mentor/fundamentos.md`. O CONTEUDO (quais frameworks, mitos, ressalvas)
> ja esta fixado em `.planning/research/*` (HIGH). A FORMA esta fixada em CONTEXT.md
> (D-01..D-05). O valor desta pesquisa e MONTAR para o planner a costura exata: skeleton,
> listas canonicas verbatim, mapeamento framework->termo-do-metodo, redacao precisa das
> ressalvas, e as armadilhas que fariam o doc drift ou virar cargo-cult.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01 — Formato HIBRIDO:** Uma tabela-resumo no topo (relance de todas as entradas) +
  abaixo, notas curtas SO para os frameworks que pedem nuance. Vale para o bloco
  foundational E o supporting. Junta "escaneavel" com "espaco pra nuance onde precisa".
- **D-02 — Profundidade por entrada:** Cada entrada tem a DEFINICAO de 1 linha (campo
  distinto, cumpre FUND-01) MAIS uma mini-nota "como usamos no metodo" (1-2 frases). A
  definicao continua sendo EXATAMENTE 1 linha; a mini-nota e campo adicional separado, nao
  inchaco da definicao. A mini-nota tem de ficar curta (anti "paredao de teoria").
- **D-03 — Ressalvas e mitos em SECOES DEDICADAS, separadas do catalogo:**
  - Secao "Limites e ressalvas" agrupa as ressalvas honestas (SDT relatedness fraca em
    solo+IA; Mayer 3 de 12). Cobre Criterio de Sucesso #4.
  - Secao "O que NAO usamos e por que" agrupa os mitos refutados (estilos de aprendizagem,
    nativos digitais, Cone de Dale/percentuais, Bloom-piramide-rigida) — cada um com razao.
    Cobre FUND-02.
- **D-04 — Declaracao de uso interno:** O doc declara EXPLICITAMENTE que `fundamentos.md`
  e interno (guia o agente) e nunca lido pelo aluno nem injetado na sessao. Posicionar como
  cabecalho/preambulo no TOPO do arquivo, antes do catalogo (FUND-03 + Criterio #3).

### Claude's Discretion

- **D-05 — campo "aplicado em <doc>" antecipado (delegado, abordagem adotada):**
  **forward-reference com marcador de status.** O campo aponta o DESTINO futuro com status:
  ex. `aplicado em tutor.md (Fase 4, pendente)`. Para frameworks cuja aplicacao JA existe
  implicitamente hoje (ex: First Principles ja estrutura a espinha), marca `(ja presente)`
  sem marcador de pendencia.
  - O "done" da Fase 1 e o campo PREENCHIDO com destino + status, NAO a aterrissagem
    verificada (essa e a Fase 6 / CONS-02).
  - As Fases 2-6 NAO reescrevem o campo — elas fazem a aterrissagem acontecer; a Fase 6
    confirma e troca o status. Isso e problema das fases seguintes, nao da Fase 1.

### Deferred Ideas (OUT OF SCOPE)

- Aterrissagem real das praticas nos docs-alvo (`reference.md`, `tutor.md`, etc.) — Fases 2-6.
- Verificacao automatizada de drift `mentor/` <-> adaptadores — FUT-04 (v2).
- Productive Failure como modo opcional — FUT-02 (v2), evidencia MEDIUM.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| FUND-01 | `mentor/fundamentos.md` cataloga 6 foundational + 6 supporting, cada um com definicao de 1 linha, fonte primaria, termo equivalente no metodo e "aplicado em <doc>" | Listas canonicas verbatim (secao "Catalogo Canonico"); mapeamento framework->termo-do-metodo (secao "Mapeamento Framework -> Termo do Metodo"); fontes primarias rastreadas em STACK.md |
| FUND-02 | Secao "O que NAO usamos e por que" sinaliza os mitos refutados (estilos de aprendizagem, nativos digitais, Cone de Dale/percentuais, Bloom como piramide rigida) com a razao | Secao "Mitos Refutados (verbatim para a secao)" com 4 mitos + razao + fonte de refutacao |
| FUND-03 | O metodo declara que `fundamentos.md` e doc interno que guia o agente — nunca lido pelo aluno nem injetado na sessao | Secao "Preambulo de uso interno (D-04)" com redacao sugerida |

> CONS-02 ("cada pratica tem aplicado em <doc> verificavel") e contrato da FASE 6, mas a
> Fase 1 PREPARA o terreno: o campo "aplicado em" deve apontar um destino REAL (doc que
> existe) com status — senao a Fase 6 nao tem o que auditar. Ver D-05 e a secao
> "Docs-alvo do campo aplicado-em (paths verificados)".
</phase_requirements>

## Summary

Fase 1 cria UM arquivo: `mentor/fundamentos.md`. E o doc interno upstream que define o
vocabulario canonico de frameworks de ciencia da aprendizagem que TODOS os outros docs de
`mentor/` vao CITAR (nunca redefinir). E lido pelo agente, nunca pelo aluno, nunca injetado
na sessao. Nao ha software, nao ha dependencias, nao ha testes automatizados — a verificacao
e revisao de doc contra os 4 Criterios de Sucesso e FUND-01/02/03.

O conteudo esta 100% determinado pela pesquisa previa (HIGH confidence): os 6 foundational
(First Principles/Merrill, Backward Design/UbD, Constructive Alignment/Biggs, CLT/Sweller,
Worked-Example+Expertise-Reversal, Retrieval Practice), os 6 supporting (SDT, ZPD/Scaffolding,
Mastery, Avaliacao Formativa, Feedback Hattie, Spacing), os 4 mitos a refutar e as 2 ressalvas
honestas (SDT relatedness fraca em solo+IA; Mayer so 3 de 12 em texto puro). A forma esta
determinada por D-01..D-05.

**Primary recommendation:** Escrever `mentor/fundamentos.md` seguindo o skeleton da secao
"Recommended Skeleton" deste doc: preambulo de uso interno (D-04) -> tabela-resumo foundational
-> mini-notas "como usamos" so onde precisa -> tabela-resumo supporting -> mini-notas ->
secao "Limites e ressalvas" (D-03) -> secao "O que NAO usamos e por que" (D-03). Cada entrada
mapeia o framework para o termo JA existente no metodo (sem inventar jargao novo) e preenche
"aplicado em <doc> (Fase N, pendente|ja presente)" (D-05). Estilo: portugues SEM acentos,
paths em backticks.

## Architectural Responsibility Map

> "Tier" aqui = camada conceitual do toolkit (nao tiers de software). O design e
> fonte-unica + adaptadores finos (`ARCHITECTURE.md`).

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Definir vocabulario canonico de frameworks | `mentor/fundamentos.md` (NOVO, upstream teorico) | — | Regra de ouro do design: teoria mora SO aqui; todos os outros citam por referencia, nunca redefinem |
| Catalogar fonte primaria de cada framework | `mentor/fundamentos.md` | — | Rastreabilidade e a razao do doc existir; fontes em `STACK.md` |
| Mapear framework -> termo do metodo | `mentor/fundamentos.md` | docs donos do termo (`metodo.md`, `reference.md`...) | O termo JA existe nos docs donos; fundamentos.md so cataloga o mapeamento |
| Aplicar a teoria (aterrissagem) | docs-alvo (`reference.md`, `tutor.md`, etc.) | `mentor/fundamentos.md` (so aponta via "aplicado em") | Fase 1 NAO aterrissa; so cria o ponteiro forward-reference (D-05). Aterrissagem = Fases 2-6 |
| Regra "teoria invisivel ao aluno" | `mentor/metodo.md` (Fase 5, CONS-01) | `mentor/fundamentos.md` (preambulo D-04) | fundamentos.md declara o proprio uso interno; metodo.md fixa a regra de conduta downstream |
| Adaptadores (`.claude/`, `AGENTS.md`) | — (NAO tocados nesta fase) | — | Inegociavel: nenhum conteudo de teoria nos adaptadores (anti-drift, P12) |

## Standard Stack

**N/A — fase de autoria de documentacao.** Nao ha bibliotecas, runtimes ou pacotes a
instalar. O unico "stack" e o conjunto de frameworks pedagogicos a catalogar, ja
selecionado e verificado em `.planning/research/STACK.md` (HIGH confidence, fontes
primarias rastreadas). Nenhuma verificacao de versao npm/pip se aplica.

Ferramenta de autoria: editor de markdown. Convencoes editoriais em `.planning/codebase/CONVENTIONS.md`.

## Catalogo Canonico (conteudo travado — montar verbatim/rastreavel)

> Ordem do catalogo segue `SUMMARY.md`: foundational (6, load-bearing) primeiro, depois
> supporting (6, ancoram 1 doc). Cada entrada abaixo ja traz: definicao de 1 linha (FUND-01),
> fonte primaria (FUND-01), termo no metodo (FUND-01), aplicado-em sugerido (D-05). As
> definicoes vem de `STACK.md` coluna "1-linha". Fontes de `STACK.md` secao Sources.

### Foundational (6) — `[CITED: .planning/research/STACK.md]`

| # | Framework | Fonte primaria | Definicao (1 linha) |
|---|-----------|----------------|---------------------|
| 1 | First Principles of Instruction | Merrill (2002; livro 2013) | Aprendizagem e promovida por 5 fases: problema real -> ativacao do conhecimento previo -> demonstracao -> aplicacao -> integracao. |
| 2 | Backward Design / Understanding by Design | Wiggins & McTighe (1ed 1998, 2ed 2005, ASCD) | Projete de tras pra frente: resultados desejados -> evidencia de dominio -> atividades. Nunca atividade-primeiro. |
| 3 | Constructive Alignment | Biggs (1996; Biggs & Tang) | Objetivos, atividades de ensino e avaliacao devem estar alinhados; o "done" deve medir exatamente o objetivo declarado. |
| 4 | Cognitive Load Theory | Sweller (1988; + Sweller, Ayres & Kalyuga 2011) | Memoria de trabalho e severamente limitada; instrucao deve cortar carga extranea e dosar a intrinseca (3 cargas: intrinseca, extranea, germane). |
| 5 | Worked-Example Effect + Expertise-Reversal Effect | Sweller & Cooper (1985); Kalyuga et al. (2003) | Novatos aprendem mais estudando exemplos resolvidos; conforme a expertise sobe, esse apoio vira estorvo e deve recuar. |
| 6 | Retrieval Practice / Testing Effect | Roediger & Karpicke (2006); Dunlosky et al. (2013) | Recuperar da memoria (vs reler) fortalece a retencao de longo prazo; uma das 2 estrategias "alta utilidade" de Dunlosky. |

### Supporting (6) — `[CITED: .planning/research/STACK.md + SUMMARY.md]`

| # | Framework | Fonte primaria | Definicao (1 linha) |
|---|-----------|----------------|---------------------|
| 1 | Self-Determination Theory (SDT) | Deci & Ryan (1985; 2017) | Motivacao sustentavel exige 3 necessidades: autonomia, competencia, relacionamento. |
| 2 | Scaffolding + Zona de Desenvolvimento Proximal (ZPD) | Vygotsky (ZPD); Wood, Bruner & Ross (1976) | Ensine no espaco entre o que o aluno faz sozinho e o que faz com apoio; reduza o apoio gradualmente. |
| 3 | Mastery Learning | Bloom (1968); Guskey | Avancar so apos dominio do pre-requisito; correcao antes de prosseguir. |
| 4 | Avaliacao Formativa | Black & Wiliam (1998) | Avaliacao a servico do aprendizado (durante), nao so do julgamento (depois). |
| 5 | Modelo de Feedback (Feed Up / Back / Forward) | Hattie & Timperley (2007) | Bom feedback responde 3 perguntas: Aonde vou? Como estou indo? Para onde a seguir? |
| 6 | Spacing Effect / Pratica Distribuida | Cepeda et al. (2006); Dunlosky (2013) | Estudo espalhado no tempo retem mais que massado; segunda estrategia "alta utilidade" de Dunlosky. |

> **Nota sobre Gradual Release of Responsibility (GRR / "eu faco -> nos fazemos -> voce faz"):**
> Aparece em REQUIREMENTS (EST-02, EST-04) e em FEATURES.md (Pearson/Gallagher 1983; Fisher/Frey)
> como pratica a NOMEAR nos docs. NAO esta na lista canonica dos 12 de FUND-01/ROADMAP Criterio #1.
> `[ASSUMED]` (A1): provavelmente entra como nice-to-cite OU dentro da entrada de Worked-Example
> (a sintaxe "eu faco -> voce faz" do metodo ja e a materializacao do GRR). O planner deve decidir
> se cria uma 13a entrada ou aninha em Worked-Example. Recomendacao: NAO inflar a lista canonica
> de 12; tratar GRR como termo coberto pela entrada Worked-Example (ver mapeamento abaixo) e
> deixar a nomeacao explicita de GRR para a Fase 2 (dona de reference.md). Confirmar com o usuario.

### Nice-to-cite (reforco, NAO estrutura — opcional no doc) — `[CITED: STACK.md]`

So mencionar de passagem; nao construir secao em torno. Decisao do planner se incluem:
- Taxonomia de Bloom revisada (Anderson & Krathwohl 2001) — banco de VERBOS para objetivos; NAO usar como piramide.
- Principios Multimidia de Mayer (2001/2021) — ver ressalva (so 3 de 12 transferem).
- ADDIE / SAM / Gagne — citar 1x so para situar linhagem; nao estruturar nada neles.
- ARCS (Keller 1987), Microlearning, Interleaving, Goal-setting — reforco operacional.

## Mapeamento Framework -> Termo do Metodo (campo "termo no metodo" de FUND-01)

> CRITICO: o campo "termo equivalente no metodo" deve usar vocabulario JA EXISTENTE nos docs
> de `mentor/`. NAO inventar jargao novo. As celulas abaixo foram extraidas dos docs reais
> (`metodo.md`, `reference.md`, `novo-projeto.md`, `tutor.md`, `fecha-marco.md`, `debug.md`)
> lidos nesta sessao. `[VERIFIED: leitura dos docs mentor/*.md]`

### Foundational

| Framework | Termo(s) no metodo (verbatim dos docs) | Onde o termo vive hoje |
|-----------|----------------------------------------|------------------------|
| First Principles (Merrill) | A espinha inteira: problema real (marco como User Story / entregavel observavel) -> ativacao (sondagem de substrato) -> demonstracao (aula por passo) -> aplicacao (scaffold com `TODO(human)`) -> integracao (fecha-marco + roadmap vivo) | `metodo.md` (ciclo por marco), `reference.md` (templates), `novo-projeto.md` (espinha) |
| Backward Design (UbD) | Ordem inegociavel "caminho completo antes dos marcos"; Passe 1 -> Passe 2 ("engenharia reversa do output final") | `novo-projeto.md` (Passos 4-5), `reference.md` (template CAMINHO.md) |
| Constructive Alignment (Biggs) | Par "META -> DONE" do scaffold; gate de curadoria "so depois de funcionar"; entregavel observavel alinhado ao objetivo | `metodo.md` (gate de curadoria), `reference.md` (formato do scaffold, campo DONE) |
| Cognitive Load Theory (Sweller) | "1 conceito dominante (novo) por passo" (regra de granularidade); aula minima just-in-time; "salto suave / sem degraus"; paredao de teoria (anti-padrao) | `reference.md` (regra de granularidade), `metodo.md` (anti-padroes) |
| Worked-Example + Expertise-Reversal | "eu faco -> voce faz" (worked example); `TODO(human)` como completion problem; calibragem por substrato; drill condicional; "fading" do andaime conforme substrato sobe | `reference.md` (sintaxe "eu faco -> voce faz", drill condicional), `metodo.md` (calibragem) |
| Retrieval Practice | (LACUNA hoje — sera aterrissada na Fase 4) "pedir a sintese antes de comemorar" / "me explica em 2 frases por que isso funciona" e o embriao; abertura do tutor com recuperacao ativa e a aterrissagem futura | hoje parcial em `tutor.md` (Passo 3 sintese); aterrissagem em `tutor.md` (Fase 4) |

### Supporting

| Framework | Termo(s) no metodo (verbatim dos docs) | Onde o termo vive hoje |
|-----------|----------------------------------------|------------------------|
| SDT | Anti-evasao; "proxima acao unica" (`PROGRESSO.md` Log + despedida do tutor); autonomia (aluno escolhe o projeto real) + competencia (entregavel observavel por marco / micro-vitorias) | `tutor.md` (Passo 4), `metodo.md` |
| Scaffolding / ZPD | O proprio termo "scaffold"; andaime calibrado ao substrato; "nem trivial nem impossivel" (`TODO(human)` dimensionado) | `reference.md` (formato do scaffold), `metodo.md` (calibragem) |
| Mastery Learning | Gate de "done"; "so depois de funcionar"; "passo N nunca pressupoe conceito nao introduzido"; criterio de fechamento verificavel | `fecha-marco.md` (Passo 1 verificacao do done), `reference.md` (verificacao de coesao) |
| Avaliacao Formativa | DONE / pergunta-guia / diario `APRENDIZADO.md` como instrumentos formativos (nao nota); check formativo no gate de curadoria | `reference.md` (templates), `metodo.md` (gate de curadoria) |
| Feedback Hattie | PERGUNTA-GUIA e PISTA do scaffold; protocolo de forense; "elogie o processo, nao so o acerto"; PISTA como feed-forward (nao da a resposta) | `reference.md` (campos PERGUNTA-GUIA/PISTA), `debug.md` (protocolo de forense) |
| Spacing | (LACUNA hoje — Fase 4) dividas de aprendizado em `PROGRESSO.md`; reuso cumulativo de conceitos antigos em marcos novos | hoje parcial (`PROGRESSO.md` dividas); aterrissagem em `fecha-marco.md`/`tutor.md` (Fase 4) |

## Campo "aplicado em <doc>" — destinos por framework (D-05)

> Combina o mapeamento Requirement->Phase da REQUIREMENTS.md (Traceability) com a build order.
> Status: `(ja presente)` quando a aplicacao ja existe implicitamente hoje; `(Fase N, pendente)`
> quando a aterrissagem acontece numa fase futura. O planner deve conferir paths reais ao redigir
> (todos verificados como existentes — ver secao "Docs-alvo"). `[VERIFIED: REQUIREMENTS.md Traceability + leitura dos docs]`

| Framework | Aplicado em (sugestao) | Status sugerido | Base |
|-----------|------------------------|-----------------|------|
| First Principles | `metodo.md`, `novo-projeto.md` | (ja presente) — estrutura a espinha hoje | SUMMARY: "ANCORA tudo, nenhuma lacuna" |
| Backward Design | `reference.md`, `novo-projeto.md` | (Fase 2/3, pendente) — EST-02/EST-03 nomeiam explicitamente | REQUIREMENTS EST-02 (Fase 2), EST-03 (Fase 3) |
| Constructive Alignment | `reference.md` | (Fase 2, pendente) — EST-01 (campo Objetivo) | EST-01 Fase 2 |
| Cognitive Load Theory | `reference.md`, `metodo.md` | (ja presente) regra de granularidade; (Fase 2, pendente) Mayer/CARGA-03 | CARGA-01/02/03 Fase 2 |
| Worked-Example + Expertise-Reversal | `reference.md` | (parcial hoje; Fase 2, pendente) CARGA-01 fading, CARGA-02 worked example, EST-04 GRR | CARGA-01/02, EST-04 Fase 2 |
| Retrieval Practice | `tutor.md` | (Fase 4, pendente) — AVAL-01 | AVAL-01 Fase 4 |
| SDT | `tutor.md`, `PROGRESSO.md` (via reference) | (Fase 4, pendente) — ENG-01 | ENG-01 Fase 4 |
| Scaffolding / ZPD | `reference.md`, `metodo.md` | (ja presente) — termo scaffold ja em uso | — |
| Mastery Learning | `fecha-marco.md` | (Fase 4, pendente) — AVAL-03 mastery gate | AVAL-03 Fase 4 |
| Avaliacao Formativa | `metodo.md` (gate de curadoria), `fecha-marco.md` | (Fase 5, pendente) — AVAL-05 | AVAL-05 Fase 5 |
| Feedback Hattie | `debug.md` | (Fase 5, pendente) — AVAL-06 feedback tri-partido | AVAL-06 Fase 5 |
| Spacing | `fecha-marco.md`, `PROGRESSO.md` | (Fase 4, pendente) — AVAL-02 | AVAL-02 Fase 4 |

> O planner deve tratar a coluna "Status sugerido" como rascunho rastreavel, nao verdade
> absoluta: para frameworks com mais de um destino, o executor escolhe a aterrissagem mais
> representativa OU lista as duas. O criterio de aceite da Fase 1 e: campo PREENCHIDO com um
> destino que EXISTE + status coerente com a build order. NAO e a aterrissagem verificada.

## Limites e ressalvas (D-03, Criterio #4) — redacao precisa, sem inflar

> Estas sao as DUAS ressalvas honestas que o doc DEVE registrar literalmente. A instrucao
> central e: registrar o limite SEM inflar o claim. `[CITED: SUMMARY.md Gaps + STACK.md]`

### Ressalva 1 — SDT relatedness em solo+IA

**Claim correto (nao inflar):** A SDT preve 3 necessidades — autonomia, competencia,
relacionamento (relatedness). Em estudo SOLO mediado por IA, sem interlocutor humano, a
necessidade de **relatedness e estruturalmente fraca**. Portanto o anti-evasao do metodo
deve ancorar em **autonomia + competencia** (as duas que o setup solo+IA atende bem), e NAO
prometer relatedness que o formato nao entrega.

**Redacao sugerida (sem acentos):**
> Ressalva SDT: a SDT preve 3 necessidades (autonomia, competencia, relatedness). Em estudo
> solo mediado por IA nao ha interlocutor humano real, entao relatedness e estruturalmente
> fraca. Ancoramos o anti-evasao em autonomia (o aluno escolhe o projeto real) e competencia
> (entregavel observavel por marco). NAO inflamos um claim de relatedness que o formato nao
> sustenta.

### Ressalva 2 — Mayer: so 3 de 12 principios em texto puro

**Claim correto (nao inflar):** Mayer descreve 12 principios multimidia. O metodo e texto
markdown SEM audio/video/animacao. Apenas **3 dos 12 transferem para texto puro**:
**coerencia** (cortar o superfluo), **sinalizacao** (destacar o essencial), **segmentacao**
(1 passo atomico). Os outros 9 dependem de midia que o metodo nao tem; nao se aplicam aqui.

**Redacao sugerida (sem acentos):**
> Ressalva Mayer: dos 12 principios multimidia de Mayer, so 3 transferem para texto puro
> (coerencia: corte o superfluo; sinalizacao: destaque o essencial; segmentacao: um passo
> atomico por vez). Os outros 9 tratam de audio/video/animacao que o metodo (markdown) nao
> tem, entao nao se aplicam. Citamos so os 3 aplicaveis; nao inflamos para "aplicamos Mayer".

> CRITICO: os 3 principios sao EXATAMENTE coerencia, sinalizacao e segmentacao. Nao trocar
> por outros (ex: "redundancia", "contiguidade") — esses sao dos 9 que NAO transferem.

## Mitos Refutados (FUND-02, D-03) — verbatim para a secao "O que NAO usamos e por que"

> 4 mitos obrigatorios (ROADMAP Criterio #2 + FUND-02), cada um com a razao da refutacao e
> a fonte. `[CITED: STACK.md "What NOT to Use" + SUMMARY.md Debunked + PITFALLS.md P11]`

| Mito (NAO usar) | Razao da refutacao (sem inflar) | Fonte de refutacao | Use no lugar |
|-----------------|--------------------------------|--------------------|--------------|
| Estilos de aprendizagem (VAK/VARK; "sou visual/auditivo") | A "meshing hypothesis" (ensinar no estilo preferido melhora aprendizado) foi testada e refutada repetidamente; e neuromito. 71 modelos revisados, nenhum se sustentou. | Pashler et al. (2008); BPS | Adaptar ao SUBSTRATO (conhecimento previo medido por sondagem), nao a "estilo" |
| "Nativos digitais" | Jovens nao tem proficiencia tecnologica inata; multitarefa e mito; design baseado nisso prejudica. | Kirschner & De Bruyckere (2017); Nature (2017) | Nao presumir competencia por idade; medir substrato sempre |
| Piramide de Aprendizagem / Cone de Dale com percentuais ("lembramos 10% do que lemos, 90% do que ensinamos") | Numeros fabricados, sem fonte/metodologia; corrupcao do Cone de Dale (1946, que nunca falou de retencao); rastreados a Treichler (1967, Mobil Oil). | Treichler (1967) corrompido; Thalheimer (worklearning.com); T&F (2018) | Para "ensinar e a melhor forma de aprender", citar protege effect / retrieval practice (efeito real, sem numeros inventados) |
| Taxonomia de Bloom como piramide rigida/sequencial ("dominar 'lembrar' antes de 'criar'") | Interpretacao equivocada; os niveis nao sao estritamente hierarquicos nem pre-requisitos lineares. Aprendizagem por projeto opera em "criar/aplicar" desde cedo. | Anderson & Krathwohl (2001, revisao) | Bloom so como banco de VERBOS para objetivos verificaveis, nao como sequencia obrigatoria |

## Preambulo de uso interno (D-04, FUND-03, Criterio #3) — redacao sugerida

> Posicionar como blockquote/cabecalho no TOPO do arquivo, antes do catalogo. Estilo: blockquote
> de "nota de contrato/aviso" (convencao do repo, ver CONVENTIONS.md).

**Redacao sugerida (sem acentos):**
> Este e um documento INTERNO do metodo. Ele existe para guiar a CONDUTA do agente — e a
> fonte unica do vocabulario teorico que os outros docs de `mentor/` citam. NUNCA e lido pelo
> aluno nem injetado na sessao: o aluno experimenta as boas praticas, jamais ouve os nomes
> dos frameworks. Despejar este conteudo na sessao recriaria o "paredao de teoria" que o
> metodo combate. Os outros docs CITAM este aqui por referencia; nenhum deles redefine a
> teoria localmente (design fonte-unica).

## Recommended Skeleton — `mentor/fundamentos.md`

> Skeleton consistente com D-01 (hibrido: tabela + notas onde precisa), D-02 (1-linha +
> mini-nota separada), D-03 (secoes dedicadas), D-04 (preambulo no topo), D-05 (forward-ref
> com status). O planner pode refinar nomes de secao; a ESTRUTURA e load-bearing.

```markdown
# Fundamentos — Frameworks de Ciencia da Aprendizagem

> [PREAMBULO DE USO INTERNO — D-04, ver redacao acima]

## Como ler este doc

(1-2 linhas: tabela-resumo por bloco da o relance; mini-notas "como usamos" aparecem so
onde o framework pede nuance; ressalvas e mitos tem secao propria.)

## Frameworks foundational (load-bearing)

[Tabela-resumo — D-01. Colunas sugeridas (specifics do CONTEXT):]
| Framework | Definicao (1 linha) | Fonte primaria | Termo no metodo | Aplicado em (doc + status) |

[Mini-notas "como usamos no metodo" — D-02, SO para os que pedem nuance. Candidatos:
 Worked-Example/Expertise-Reversal (fading vs drill condicional), CLT (a propria ironia
 do paredao de teoria), Retrieval (lacuna a aterrissar na Fase 4).]

## Frameworks supporting (ancoram um doc)

[Tabela-resumo — mesmas colunas.]

[Mini-notas "como usamos" — SO onde precisa. Candidato obrigatorio: SDT
 (apontar para a secao Limites e ressalvas).]

## Limites e ressalvas

### SDT relatedness em solo+IA
[redacao da Ressalva 1]

### Mayer: so 3 de 12 principios em texto puro
[redacao da Ressalva 2]

## O que NAO usamos e por que

[Tabela ou lista dos 4 mitos: mito | razao | fonte | use no lugar]
```

**Decisao de coluna (specifics do CONTEXT, confirmado):** a tabela-resumo usa
`Framework | Definicao (1 linha) | Fonte primaria | Termo no metodo | Aplicado em (doc + status)`.
As mini-notas "como usamos" (D-02) ficam ABAIXO da tabela, NAO numa coluna (senao a tabela
incha e quebra o relance escaneavel).

## Docs-alvo do campo "aplicado em" (paths verificados)

> `[VERIFIED: Glob mentor/**/*.md nesta sessao]` — TODOS os destinos existem hoje. O campo
> "aplicado em" pode apontar com seguranca; nenhum path quebrado.

| Doc-alvo | Existe? | Papel |
|----------|---------|-------|
| `mentor/metodo.md` | sim (165 linhas) | persona/conduta; ciclo por marco |
| `mentor/reference.md` | sim (419 linhas) | templates + regras (CAMINHO, PROGRESSO, aula, scaffold) |
| `mentor/novo-projeto.md` | sim | bootstrap (diagnostico->sondagem->caminho->marcos) |
| `mentor/tutor.md` | sim | copiloto de sessao |
| `mentor/fecha-marco.md` | sim | fechamento de marco |
| `mentor/debug.md` | sim | protocolo de forense (6 passos) |
| `mentor/spidr-split.md` | sim | decomposicao SPIDR (nao e destino dos 12 frameworks) |

> NAO ha um doc "dono" separado por framework: os destinos sao estes 6 docs de procedimento/
> referencia/persona. `fundamentos.md` e o 8o doc de `mentor/` (novo).

## Don't Hand-Roll

| Problema | Don't Build | Use Instead | Why |
|----------|-------------|-------------|-----|
| Definir um framework pedagogico | Reescrever a teoria com palavras proprias / fonte secundaria | Copiar a definicao de 1-linha e a fonte primaria de `STACK.md` (ja verificadas) | Re-derivar arrisca drift semantico e introducao acidental de mito (P11) |
| Inventar o "termo no metodo" | Cunhar jargao novo (ex: "fase de absorcao") | Mapear para o termo JA existente nos docs (secao Mapeamento acima) | Jargao novo quebra a fonte-unica e confunde os docs downstream (P8 cargo-cult) |
| Escolher os 3 principios de Mayer | Listar de memoria | coerencia, sinalizacao, segmentacao (exato) | Trocar por outros injeta um claim falso (os outros 9 nao transferem) |
| Redigir as ressalvas | Suavizar / inflar o claim | Usar a redacao "sem inflar" desta pesquisa | Criterio #4 exige honestidade explicita; inflar viola o objetivo |

**Key insight:** Esta fase e MONTAGEM, nao criacao. Todo conteudo factual ja existe em
`.planning/research/*` e nos docs `mentor/*.md`. O risco nao e "nao saber a resposta" — e
re-derivar e introduzir drift. Copie rastreavel; nao reinvente.

## Architecture Patterns

### Padrao 1: Fonte-unica (single source of truth)
**What:** A teoria mora SO em `fundamentos.md`; todos os outros docs citam por referencia.
**When to use:** sempre, neste milestone.
**Anti-pattern:** redefinir um framework dentro de `reference.md`/`metodo.md`, ou copiar
conteudo para os adaptadores (`.claude/`, `AGENTS.md`). Viola o design e garante drift (P12).

### Padrao 2: Forward-reference com marcador de status (D-05)
**What:** O campo "aplicado em" aponta o destino futuro + status `(Fase N, pendente)` ou
`(ja presente)`.
**When to use:** ao preencher o campo "aplicado em" de cada framework nesta fase.
**Why:** a build order e inegociavel (fundamentos.md primeiro, docs-alvo nas Fases 2-6); o
campo registra a INTENCAO rastreavel sem exigir a aterrissagem agora.

### Padrao 3: Hibrido tabela + mini-nota (D-01 + D-02)
**What:** tabela-resumo escaneavel no topo; mini-notas "como usamos" so onde ha nuance.
**Anti-pattern:** transformar cada entrada num paragrafo longo (vira o "paredao de teoria"
que o metodo combate — P2; ironia explicita em PITFALLS.md).

### Convencoes editoriais (CONVENTIONS.md) — `[VERIFIED: leitura]`
- Portugues SEM acentos (robustez de encoding). Inegociavel.
- Paths e identificadores SEMPRE em backticks (`mentor/tutor.md`, `TODO(human)`, `/tutor`).
- Negrito para conceitos-chave/regras inegociaveis; blockquote `>` para notas de contrato no topo.
- Tabelas para mapeamentos (e exatamente o formato deste catalogo).
- Tom: instrui o agente (o doc fala COM o agente, nao com o aluno).

## Common Pitfalls

### Pitfall 1: Cargo-cult — citar framework sem aterrissagem (P8)
**What goes wrong:** o doc cresce mas nenhum comportamento muda; "aplicado em" vazio ou falso.
**How to avoid:** todo framework tem "aplicado em <doc>" apontando destino REAL (todos verificados
como existentes). Nesta fase o aceite e o ponteiro preenchido + status; a Fase 6 audita a chegada.
**Warning sign:** campo "aplicado em" em branco, ou apontando doc inexistente.

### Pitfall 2: O proprio doc virar "paredao de teoria" (P2, ironia)
**What goes wrong:** entradas longas, enciclopedicas; o doc fica pesado de consultar.
**How to avoid:** definicao = EXATAMENTE 1 linha (D-02); mini-nota = 1-2 frases curtas; nuance
so onde precisa (D-01). A tabela carrega o relance.
**Warning sign:** uma definicao com 2+ linhas; mini-nota virando paragrafo.

### Pitfall 3: Citar mito como se fosse fundamento (P11)
**What goes wrong:** mencionar estilos de aprendizagem / cone de Dale / nativos digitais
positivamente, destruindo a credibilidade do doc.
**How to avoid:** os 4 mitos SO aparecem na secao "O que NAO usamos e por que", com a razao.
Fontes primarias/meta-analises, com nome — nada de blog de coaching.
**Warning sign:** percentual de retencao por modalidade; "estilo do aluno" fora da secao de mitos.

### Pitfall 4: Inflar as ressalvas (Criterio #4)
**What goes wrong:** "aplicamos SDT completo" / "seguimos Mayer" — claim maior que a realidade.
**How to avoid:** usar a redacao "sem inflar" desta pesquisa; nomear o limite explicitamente
(relatedness fraca; so 3 de 12).
**Warning sign:** ausencia da palavra "ressalva/limite"; SDT citado sem o caveat de relatedness;
Mayer citado sem "so 3 de 12".

### Pitfall 5: Drift fonte-unica ao escrever (P12)
**What goes wrong:** copiar definicao de framework para um adaptador "pra garantir".
**How to avoid:** nesta fase SO `mentor/fundamentos.md` e tocado. Nenhum adaptador, nenhum
outro doc de mentor. (A aterrissagem nos outros docs e Fases 2-6.)
**Warning sign:** qualquer edicao fora de `mentor/fundamentos.md` nesta fase.

### Pitfall 6: Inventar jargao novo no "termo no metodo" (P8 variante)
**What goes wrong:** cunhar termos que nao existem nos docs, criando vocabulario paralelo.
**How to avoid:** usar SO os termos do mapeamento verificado (espinha, passo, marco, substrato,
scaffold, `TODO(human)`, gate de curadoria, drill condicional, "eu faco -> voce faz", forense,
pergunta-guia, PISTA, DONE, sondagem, roadmap vivo, walking skeleton).
**Warning sign:** um termo na coluna "termo no metodo" que nao aparece em nenhum `mentor/*.md`.

## Code Examples

N/A — fase de autoria de documentacao, sem codigo. Os "exemplos" load-bearing sao as redacoes
sugeridas (preambulo, ressalvas) e o skeleton, todos acima.

## Runtime State Inventory

N/A — fase greenfield de UM arquivo novo (`mentor/fundamentos.md`). Nao e rename/refactor/
migracao; nao ha estado em runtime, datastores, servicos, OS-registrations, secrets ou build
artifacts envolvidos. Verificado: o unico efeito da fase e a criacao de um markdown novo +
(commit_docs=true) o commit. Nenhum doc existente e editado nesta fase.

## State of the Art

N/A para "tecnologia". Para o conteudo pedagogico: os frameworks sao consagrados e estaveis
(decadas). O unico "outdated vs current" relevante e o conjunto de MITOS a NAO usar — ja
capturado na secao de mitos (estilos de aprendizagem, cone de Dale, nativos digitais, Bloom-
piramide sao as nocoes "antigas/refutadas"; substrato medido / retrieval / multiplas
representacoes para todos sao o "atual correto").

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | GRR ("eu faco -> nos fazemos -> voce faz") NAO vira 13a entrada canonica; e coberto pela entrada Worked-Example e nomeado explicitamente na Fase 2 | Catalogo Canonico (nota) | Se o usuario quiser GRR como entrada propria, o catalogo tem 13 entradas, nao 12 — desalinha com FUND-01/ROADMAP que dizem "6+6". Baixo risco; recomendacao ja minimiza |
| A2 | Para frameworks com 2 destinos possiveis em "aplicado em", o executor escolhe o mais representativo OU lista os dois | Campo "aplicado em" | Se a Fase 6 esperar um destino especifico nao listado, a auditoria pode falhar. Mitigado: a Fase 6 audita aterrissagem real, nao a escolha exata do ponteiro |
| A3 | As mini-notas "como usamos" sao opcionais por entrada (so onde ha nuance), nao obrigatorias para os 12 | Recommended Skeleton / D-02 | D-02 diz "cada entrada tem... mini-nota". Se o usuario quis mini-nota para TODAS as 12, o skeleton precisa de 12 mini-notas, nao "so onde precisa". Ler D-01+D-02 juntos sugere "onde precisa" (D-01 diz "notas curtas apenas para os que pedem nuance"). Conflito aparente D-01 vs D-02 — planner deve resolver |

> A3 e o unico conflito real entre decisoes: D-01 diz mini-notas "apenas para os frameworks
> que pedem nuance"; D-02 diz "cada entrada tem... MAIS uma mini-nota". Resolucao recomendada:
> seguir D-01 (mini-nota so onde ha nuance) — D-02 estabelece o FORMATO da mini-nota (campo
> separado, curto) quando ela existe, nao a obrigatoriedade em todas as 12. O planner deve
> confirmar essa leitura ou perguntar ao usuario.

## Open Questions

1. **Mini-nota obrigatoria em todas as 12 entradas, ou so onde ha nuance? (D-01 vs D-02)**
   - What we know: D-01 diz "so onde pede nuance"; D-02 diz "cada entrada tem mini-nota".
   - What's unclear: se as 12 entradas precisam de mini-nota ou so um subconjunto.
   - Recommendation: seguir D-01 (subconjunto); ver A3. Confirmar com usuario se houver duvida.

2. **GRR como entrada canonica propria, nice-to-cite, ou aninhado em Worked-Example?**
   - What we know: aparece em EST-02/EST-04 e FEATURES.md, mas nao na lista de 12 de FUND-01.
   - What's unclear: onde o usuario quer ve-lo em fundamentos.md.
   - Recommendation: aninhar em Worked-Example (a sintaxe "eu faco -> voce faz" ja e GRR);
     nomeacao explicita fica para Fase 2 (dona de reference.md). Ver A1.

3. **Incluir o bloco "nice-to-cite" (Bloom-verbos, Mayer-contexto, ADDIE/linhagem) no doc?**
   - What we know: STACK.md lista; CONTEXT/ROADMAP nao exigem (so 6+6 + mitos + ressalvas).
   - What's unclear: se o usuario quer essa terceira camada no doc.
   - Recommendation: opcional; se incluir, manter MUITO curto (1 linha cada) para nao inchar.
     Bloom-verbos e util porque EST-01 vai usar (verbo de Bloom no campo Objetivo). Decisao do planner.

## Environment Availability

N/A — fase code/config-only (autoria de markdown). Nenhuma dependencia externa, tool, runtime
ou servico. Brave/Exa/Firecrawl desabilitados em config; nenhuma pesquisa web foi necessaria
(conteudo ja travado em `.planning/research/*`). Step 2.6: SKIPPED (no external dependencies).

## Validation Architecture

> `nyquist_validation: true` em config, mas esta e uma fase de AUTORIA DE DOC: nao ha codigo,
> nao ha framework de teste, nao ha comando automatizado de teste. A "validacao" e revisao do
> doc contra os criterios. Abaixo, o mapa de verificacao adaptado.

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Nenhum (doc-authoring) — verificacao por revisao manual / checklist |
| Config file | none — N/A |
| Quick run command | N/A (inspecao visual do doc + grep de paths) |
| Full suite command | N/A |

### Phase Requirements -> Verificacao
| Req ID | Behavior | Tipo | Como verificar (manual) |
|--------|----------|------|-------------------------|
| FUND-01 | 6 foundational + 6 supporting, cada um com def 1-linha + fonte + termo no metodo + aplicado-em | review | Contar 12 entradas; cada uma tem os 4 campos preenchidos; "aplicado em" aponta doc existente |
| FUND-02 | Secao "O que NAO usamos e por que" com 4 mitos + razao | review | Secao existe; lista estilos de aprendizagem, nativos digitais, Cone de Dale/percentuais, Bloom-piramide; cada um com razao |
| FUND-03 | Declaracao de uso interno (nunca lido pelo aluno / nunca injetado) | review | Preambulo no topo declara explicitamente o uso interno |
| Criterio #4 | Ressalvas SDT + Mayer sem inflar | review | Secao "Limites e ressalvas" registra relatedness fraca em solo+IA e Mayer 3-de-12 (coerencia/sinalizacao/segmentacao) |
| CONS-02 (prep) | "aplicado em" verificavel | review | Cada destino existe (`ls mentor/`); paths em backticks; status coerente com build order |

### Sampling Rate
- **Per task / por entrada:** revisar que a entrada tem os 4 campos e nao inflou a definicao.
- **Per doc:** rodar o checklist "Looks Done But Isn't" abaixo antes de fechar a fase.
- **Phase gate:** os 4 Criterios de Sucesso + FUND-01/02/03 verdadeiros por revisao.

### Checklist de aceite (adaptado de PITFALLS.md "Looks Done But Isn't")
- [ ] 12 entradas (6+6); cada uma com def 1-linha + fonte primaria + termo no metodo + aplicado-em.
- [ ] Nenhum "termo no metodo" e jargao novo (todos aparecem em algum `mentor/*.md`).
- [ ] Cada "aplicado em" aponta um doc que EXISTE; status `(Fase N, pendente)`/`(ja presente)` coerente.
- [ ] Secao "Limites e ressalvas": SDT relatedness fraca + Mayer 3-de-12 (coerencia/sinalizacao/segmentacao), sem inflar.
- [ ] Secao "O que NAO usamos e por que": os 4 mitos, cada um com razao + fonte.
- [ ] Preambulo de uso interno no topo (D-04).
- [ ] Nenhuma definicao com >1 linha; mini-notas curtas (anti-paredao).
- [ ] Portugues SEM acentos; paths em backticks.
- [ ] SO `mentor/fundamentos.md` foi criado/editado (nenhum adaptador, nenhum outro doc — anti-drift).

### Wave 0 Gaps
None — fase de autoria, sem infraestrutura de teste a montar. A verificacao e a revisao
do doc pelo checklist acima.

## Security Domain

N/A — autoria de documentacao markdown interna, sem autenticacao, entrada de usuario,
sessao, criptografia, ou superficie de ataque. Nenhuma categoria ASVS se aplica a um doc
de teoria pedagogica nao executavel. (security_enforcement nao aplicavel a doc-authoring.)

## Sources

### Primary (HIGH confidence) — artefatos do projeto
- `.planning/research/SUMMARY.md` — sintese decision-ready: listas canonicas, gaps SDT/Mayer, mitos.
- `.planning/research/STACK.md` — frameworks com fonte primaria + 1-linha + mapeamento; "What NOT to Use".
- `.planning/research/FEATURES.md` — tecnicas pedagogicas, GRR, pratica->doc.
- `.planning/research/PITFALLS.md` — P8 cargo-cult, P9 theory-leak, P11 mitos, P12 drift, checklist de aceite.
- `.planning/REQUIREMENTS.md` — FUND-01/02/03, CONS-02, Traceability (Requirement->Phase).
- `.planning/ROADMAP.md` — Phase 1 goal + 4 Success Criteria.
- `.planning/phases/01-.../01-CONTEXT.md` — D-01..D-05 (forma).
- `.planning/codebase/{ARCHITECTURE,STRUCTURE,CONVENTIONS}.md` — design fonte-unica, layout, estilo.

### Verified this session (HIGH confidence) — leitura direta dos docs
- `mentor/{metodo,reference,novo-projeto,tutor,fecha-marco,debug}.md` — fonte do vocabulario do metodo (campo "termo no metodo") e confirmacao de que os 6 docs-alvo existem.
- `Glob mentor/**/*.md` — confirma 7 docs existentes; `fundamentos.md` e o 8o (novo).

### Tertiary (LOW confidence)
- Nenhuma. Nenhuma pesquisa web nova foi necessaria; conteudo travado em artefatos do projeto.

## Metadata

**Confidence breakdown:**
- Conteudo (frameworks, mitos, ressalvas): HIGH — travado por pesquisa previa, fontes primarias rastreadas.
- Mapeamento framework->termo do metodo: HIGH — extraido por leitura direta dos docs reais.
- Paths dos docs-alvo: HIGH — verificados por Glob nesta sessao.
- Forma (skeleton, D-01..D-05): HIGH — travada por CONTEXT.md; unico ponto aberto e A3 (D-01 vs D-02 sobre mini-notas).

**Research date:** 2026-06-14
**Valid until:** estavel (conteudo pedagogico consagrado; docs do repo so mudam por este milestone) — revalidar so se `.planning/research/*` ou os docs `mentor/*.md` mudarem.
