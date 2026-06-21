# Referencia -- Mentor de Projeto

## Convencao de markdown (markdownlint)

Todo arquivo `.md` que as personas escreverem (`CAMINHO.md`, `PROGRESSO.md`,
`APRENDIZADO.md`, `aulas/P0x-<slug>.md`, e qualquer outro) deve obedecer as regras do
[markdownlint](https://github.com/DavidAnson/markdownlint) (David Anson). Em texto gerado
por LLM, as regras mais violadas -- e que voce DEVE respeitar -- sao:

- **MD022**: cabecalhos cercados por uma linha em branco antes e depois.
- **MD032**: listas cercadas por uma linha em branco antes e depois.
- **MD031**: blocos de codigo cercados (` ``` `) cercados por linha em branco.
- **MD040**: todo bloco de codigo cercado declara a linguagem (` ```python `, ` ```text `).
- **MD025**: um unico cabecalho de nivel 1 (`#`) por arquivo, no topo.
- **MD012**: nunca mais de uma linha em branco consecutiva.
- **MD009**: sem espacos no fim das linhas.
- **MD047**: o arquivo termina com exatamente uma quebra de linha.
- **MD034**: sem URL "nua" -- use `<https://...>` ou `[texto](url)`.

Regra: a saida ja nasce limpa. Nao escreva markdown torto pra "consertar depois".

## Idioma e acentuacao -- dois publicos, duas regras

O repo tem DOIS tipos de texto, e a regra de acentuacao depende de QUEM le:

- **Docs internos do agente** -- tudo em `mentor/`, `mentor/fundamentos.md`, `.planning/`,
  `AGENTS.md`, `README.md`: portugues **sem acentos** (ASCII puro). So a LLM (e o
  mantenedor) le; o ASCII evita problemas de encoding entre ferramentas, terminais e
  hooks. Mantenha assim. Esta e a regra que voce ja segue ao escrever conduta.
- **Artefatos que vao para o aluno** -- `CAMINHO.md`, `PROGRESSO.md`, `APRENDIZADO.md`,
  `aulas/P0x-<slug>.md`, os scaffolds em `projeto/`, os drills em `exercicios/` e
  qualquer outro texto que o ALUNO le: use a **ortografia correta do portugues** --
  acentos, cedilha, til ("voce" -> "você", "codigo" -> "código", "funcao" -> "função",
  "licao" -> "lição"). Material de estudo sem acento passa desleixo e atrapalha a
  leitura; o aluno merece texto bem escrito.

Regra pratica: **escrito PARA a LLM -> ASCII; escrito PARA o aluno -> portugues
acentuado.** O markdownlint acima vale nos dois casos. Salve sempre em UTF-8.

Atencao aos templates abaixo: o texto fixo em portugues dentro deles (titulos de secao,
frases-modelo) e copiado para o artefato do aluno -- ja vem acentuado de proposito.
Reproduza a acentuacao ao instanciar. As chaves estruturais em maiusculas do scaffold
(`META`, `PORQUE`, `PRESSUPOE`, `DONE`...) sao identificadores fixos e ficam em ASCII.

## Sondagem de substrato

Autoavaliacao engana: "sei um pouco de JS" pode ser qualquer coisa entre zero-absoluto
e intermediario. Sonde na pratica, com 2-3 sondas rapidas por assunto duvidoso:

- **Reconhecimento**: mostre um snippet de 3-5 linhas do assunto e pergunte
  "o que esse trecho faz?". Quem nao reconhece a sintaxe e zero-absoluto.
- **Producao descrita**: "como voce faria X?" -- descricao em palavras basta;
  nao exija codigo perfeito no chat.
- **Vocabulario**: "o que significa [termo central do assunto]?" -- vocabulario
  avancado sinaliza profundidade desejada, nao maestria; confirme com as outras sondas.

Classificacao por assunto:

- **zero-absoluto** -- nao reconhece a sintaxe; nao tem materia-prima pra deduzir.
  Andaime: "eu faco -> voce faz" obrigatorio na entrada do assunto.
- **iniciante** -- reconhece e le, mas nao produz sem apoio. Andaime: pergunta-guia
  + scaffold detalhado.
- **intermediario** -- produz com hesitacao. Andaime: pergunta-guia + scaffold padrao.
- **avancado** -- produz e explica trade-offs. Andaime: mais buraco, menos pista.

Regras:

- Agrupe TODAS as sondas numa unica mensagem (nao vire interrogatorio).
- Registre nivel + evidencia na tabela do `PROGRESSO.md`. Evidencia importa: e o que
  permite recalibrar depois sem re-sondar do zero.
- O substrato e **por assunto, nao por aluno**: um aluno forte em logica/dados pode
  ser zero-absoluto em sintaxe de frontend. Calibre pelo substrato DO ASSUNTO em jogo.
- Re-sonde de leve quando o vocabulario do aluno mudar ou um marco fechar com folga
  ou com muito sofrimento.
- **O andaime RECUA conforme a maestria sobe** -- e o
  [expertise-reversal effect](fundamentos.md#frameworks-foundational-load-bearing):
  suporte demais ATRAPALHA o avancado (vira ruido), enquanto o iniciante precisa do
  exemplo resolvido. Calibre a densidade de andaime + pista pelo substrato DO ASSUNTO:
  zero-absoluto/iniciante -> exemplo resolvido + pergunta-guia + pista detalhada;
  intermediario -> pergunta-guia + scaffold padrao; avancado -> mais buraco, menos pista
  (recue o andaime). E o mesmo principio do fading: mais maestria, menos suporte.

## Regra de granularidade

- Unidade = **1 capacidade coesa**, nao 1 atomo de conceito. Teste: ao fechar a unidade,
  o aluno consegue articular UM "porque" inteiro.
- **Criterio de fechamento verificavel**: cada unidade tem um "done" objetivo (algo roda,
  renderiza, passa num check visual). Check verde so vale se houve sintese.
- **Tamanho**: completavel numa sessao focada (~30-90 min). Maior -> quebre; menor -> funda.
- **Salto suave**: cada passo introduz no maximo 1 conceito dominante novo e reusa os
  anteriores. Sem degraus.
- **Granularidade ~ 1/nivel**: iniciante -> unidades menores + mais andaime; avancado ->
  unidades maiores + mais buraco a preencher.

## Template -- CAMINHO.md

O `CAMINHO.md` e a expansao completa do caminho de aprendizado, gerada ANTES da
montagem dos marcos. E o documento de design; o `PROGRESSO.md` e o de acompanhamento.

```markdown
# CAMINHO -- <nome do projeto>

> Regra de ouro: o passo N só pode pressupor conceitos introduzidos em P01..P(N-1)
> ou cobertos pelo substrato do aluno (tabela no PROGRESSO.md).

## Conceitos (índice)

- c01-<slug> -- <definição de 1 linha> (introduzido em P01)
- c02-<slug> -- <definição de 1 linha> (introduzido em P02)

## Passos

### P01 -- <título curto>

- Conceito dominante (novo): c01-<slug>
- Pressupõe: (nenhum -- entrada coberta pelo substrato)
- Substrato exigido: <assunto>: zero-absoluto ok ("eu faço -> você faz")
- Objetivo (capacidade): ao terminar, você consegue <verbo> <conceito>
- Entregável: <o que o aluno ESCREVE> + <o que ele VÊ funcionando ao terminar>
- Arquivos: <paths em projeto/>

### P02 -- <título curto>

- Conceito dominante (novo): c02-<slug>
- Pressupõe: c01-<slug>
- Substrato exigido: <assunto>: >= iniciante
- Objetivo (capacidade): ao terminar, você consegue <verbo> <conceito>
- Entregável: ...
- Arquivos: ...

## Mapa passos -> marcos

- Marco 00 (Walking Skeleton): P01-P02 -- coeso porque <1 linha>
- Marco 01: P03-P05 -- coeso porque <1 linha>
```

Regras do caminho:

- A ordem capacidade-primeiro, artefato-como-evidencia segue
  [backward design](fundamentos.md#frameworks-foundational-load-bearing): defina o
  resultado desejado (a capacidade) antes de desenhar a atividade.
- IDs de conceito sao estaveis (`c01-tags-html`); marcos e scaffolds referenciam por ID.
- "Entregavel" e sempre concreto e observavel: o que o aluno digita e o que aparece
  na tela/terminal quando da certo. "Aprender flexbox" NAO e entregavel;
  "os 3 cards ficam lado a lado e centralizados" e.
- Se um passo precisaria de 2 conceitos dominantes novos, sao 2 passos.
- Se a referencia do roadmap.sh (em `referencias/`) introduz um conceito antes do seu
  caminho, cheque se ha buraco de dependencia.

## Verificacao de coesao (rodar no Passe 2 e em toda recalibragem)

Checklist mecanico -- falhou, conserta o caminho antes de qualquer scaffold:

- [ ] Todo conceito em "Pressupoe" de P(N) e dominante de algum P(<N), OU esta coberto
      pelo substrato em nivel >= iniciante.
- [ ] Cada passo introduz no maximo 1 conceito dominante novo.
- [ ] Todo passo cujo assunto esta zero-absoluto na tabela esta marcado
      "eu faco -> voce faz".
- [ ] Cada marco agrupa passos CONSECUTIVOS do caminho (sem buracos nem saltos).
- [ ] Cada marco termina em algo que roda/renderiza (fatia vertical, nao tema).
- [ ] O primeiro marco e um Walking Skeleton.
- [ ] Todo entregavel e observavel (descreve o que o aluno VE, nao so o que "aprende").
- [ ] Todo passo tem uma aula (`aulas/P0x-<slug>.md`) com a teoria minima para conclui-lo
      sem internet nem PISTA, e nenhuma aula contem a solucao do `TODO(human)`.

## Marcos verticais, nunca temas

Nao organize por tema puro (`01-html/`, `02-css/`, `03-js/`). Isso recria o curso
tradicional: o aluno aprende um assunto inteiro antes de saber pra que -> salto de
motivacao e de integracao. Cada marco e uma **fatia vertical** que atravessa varios
assuntos mas sempre entrega algo visivel e funcional.

## Drill condicional (`exercicios/`)

- Gere SO quando: conceito novo x nao-trivial x acima do nivel atual.
- **Angulo diferente** da aplicacao: drill = intuicao do mecanismo isolado; aplicacao =
  decisao/integracao no artefato. O drill nunca deve entregar a resposta da aplicacao.
- **Just-in-time**: no comeco do marco que precisa, nao tudo upfront.
- Pasta por drill faz sentido aqui (drills sao isolados): `exercicios/NN-<conceito>/`.

## User Story por marco

Cada marco deve ter uma historia de usuario no formato:

```text
Como [tipo de usuario], eu quero [capacidade], para que [beneficio].
```

A historia e o norte do marco. Se o aluno nao consegue articular o "para que", o marco
esta mal definido ou muito grande. Use `/spidr-split` para decompor.

## SPIDR Splitting -- quando um marco e grande demais

Cinco eixos para decompor uma historia grande em fatias menores:

- **S**pike: investigacao rapida para reduzir incerteza (ex: "como funciona a API X?").
- **P**aths: caminhos alternativos de um fluxo (ex: checkout com cartao vs boleto).
- **I**nterfaces: diferentes superficies de interacao (ex: web vs mobile vs API).
- **D**ata: variacoes de dados (ex: formulario simples vs formulario com upload).
- **R**ules: regras de negocio que podem ser adiadas (ex: validacao basica vs validacao
  completa com regras de dominio).

Aplique 1 ou mais eixos ate que cada fatia caiba numa sessao (~30-90 min).

## Roadmap vivo

A cada marco fechado, releia `CAMINHO.md` e `PROGRESSO.md` e **recalibre** (divida,
funda, ajuste granularidade, atualize a tabela de substrato) com base em como o aluno
performou. Re-rode a verificacao de coesao apos qualquer mudanca. A espinha e estavel;
as folhas adaptam.

## Marcos = git, nao pastas (para artefato unico)

Para um artefato unico que cresce (um app, um site), os marcos sao **estagios** marcados
com `git tag marco-NN-<slug>`, NAO pastas. `projeto/` tem UM conjunto de arquivos que
evolui marco a marco. Pastas-por-conceito existem apenas em `exercicios/` (drills isolados).

As tags vivem no repo git do PROPRIO projeto (cada `.projetos/<slug>/` tem o seu, criado
com `git init` no bootstrap) -- independente do repo do toolkit, que ignora `.projetos/`.

## Layout do repo do aluno

Todo projeto mora em `.projetos/<slug>/` (a raiz do projeto). A pasta `.projetos/` esta
no `.gitignore` do toolkit: projetos sao pessoais (cada usuario tem os seus) e NAO sobem
pro github do toolkit. Cada projeto e seu PROPRIO repo git (`git init` no bootstrap).

```text
.projetos/<slug>/
|-- CAMINHO.md            # design: passos detalhados + mapa passos -> marcos
|-- PROGRESSO.md          # acompanhamento: substrato, DoD, marcos, dividas, log
|-- APRENDIZADO.md        # diario de bordo: licoes, padroes de erro, decisoes
|-- referencias/          # roadmaps de referencia (scripts/roadmap_fetch.py)
|-- aulas/                # teoria minima POR PASSO (P0x), lida ANTES do scaffold
|   `-- P0x-<slug>.md      #   uma aula por passo do CAMINHO.md
|-- exercicios/           # drills ISOLADOS, gerados just-in-time
|   `-- NN-<conceito>/     #   pasta-por-conceito so aqui
`-- projeto/              # o ARTEFATO UNICO; cresce marco a marco (marcos = git tags)
```

## Template -- PROGRESSO.md

```markdown
# PROGRESSO -- <nome do projeto>

## Substrato por assunto

| Assunto | Nível | Evidência da sondagem |
|---|---|---|
| <assunto> | zero-absoluto / iniciante / intermediário / avançado | <o que a sonda mostrou> |

## Objetivo

- Objetivo de aprendizado: ...
- Restrições (stack/tempo/ferramentas): ...

## Output final

<descrição do que será construído>

## Definition of Done

- [ ] <critério objetivo 1>
- [ ] <critério objetivo 2>

## Marcos

### 00 -- <slug> (Walking Skeleton)  <- ATUAL

**User Story:** Como [usuário], eu quero [capacidade básica], para que [valor mínimo].
**Capacidade:** ao terminar, você consegue <verbo> <conceito>
**Passos do caminho:** P01-P02 (ver CAMINHO.md)
**Entregável:** <o que o aluno VÊ funcionando ao fechar o marco>

- [ ] <critério de done>

### 01 -- <slug>

**User Story:** Como [usuário], eu quero [capacidade], para que [valor].
**Capacidade:** ao terminar, você consegue <verbo> <conceito>
**Passos do caminho:** P03-P05
**Entregável:** <concreto e observável>

- [ ] <critério de done>

## Dívidas de aprendizado

- (registradas na curadoria; revisitar quando fizer sentido)

## Agenda de retrieval

- <conceito> -- revisitar na abertura do marco <NN>

## Log

- AAAA-MM-DD -- marco-00 fechado: <o que ficou pronto>
```

## Template -- APRENDIZADO.md

```markdown
# Diário de Aprendizado -- <nome do projeto>

## Lições

- AAAA-MM-DD -- <conceito aprendido> (contexto: <em que marco/situação>)

## Padrões de erro

- AAAA-MM-DD -- <erro recorrente> -> <causa raiz> -> <como evitar da próxima vez>

## Decisões arquiteturais

- AAAA-MM-DD -- <decisão tomada> (contexto: <por que escolhemos isso>)

## Dívidas de aprendizado (da curadoria)

- <dívida> -- registrada em <data> -- revisitar no marco <NN>
```

## Template -- aula (`aulas/P0x-<slug>.md`)

Cada passo do `CAMINHO.md` tem uma aula: o **insumo teorico confiavel** que o aluno
le ANTES de encarar o scaffold. Ela existe para resolver a queixa central -- o aluno
nunca deve ter que adivinhar intuitivamente, buscar na internet ou depender da PISTA
para saber COMO fazer. A aula entrega a teoria minima; o scaffold pede a aplicacao.

Contrato inegociavel: **a aula ensina o mecanismo, nunca resolve o passo**. Os exemplos
da aula usam uma instancia DIFERENTE da do `TODO(human)` (mesma regra do drill: angulo
diferente da aplicacao). Se um exemplo da aula, copiado, fecha o `TODO`, a aula virou
gabarito -- esta errada.

```markdown
# Aula -- P0x: <título do passo>

> Leia ANTES de abrir o scaffold. Esta aula te dá a teoria mínima para concluir P0x
> sem buscar na internet nem descomentar a PISTA. Ela NÃO contém a solução do
> TODO(human): os exemplos usam uma instância diferente da do seu projeto; transferir
> para o seu artefato é a sua parte.

## Objetivo do passo

<capacidade: ao terminar, você consegue <verbo> <conceito>; e o artefato que prova isso:
o que vai ficar pronto, concreto e observável -- espelha o "Objetivo (capacidade)" e o
"Entregável" do CAMINHO.md, em 1-2 linhas>

## O que o tutor espera de você

<explícito: o que você precisa PRODUZIR e DEMONSTRAR. Ex: "escrever a função que
recebe X e devolve Y, e me explicar em 2 frases por que ela funciona". Conecta com
o DONE e a PERGUNTA-GUIA do scaffold.>

## Teoria mínima

Conceito dominante: c0x-<slug>.

- **Intuição**: <por que isso existe / analogia, 2-3 linhas>
- **Exemplo**: <um exemplo curto e concreto do mecanismo, instância DIFERENTE da do projeto>
- **Conceito formal**: <a definição precisa, a sintaxe e as regras que valem>

## Exemplos de aplicação

<1-2 exemplos resolvidos e explicados, SEMPRE em instância diferente do TODO(human).
Mostram como o conceito vira código sem entregar o código-alvo. Se o assunto está
zero-absoluto na tabela de substrato, este é o "eu faço" do "eu faço -> você faz".>

## Boas práticas (quando aplicável)

<guia idiomático do conceito: a forma convencional/elegante, armadilhas comuns, o que
evitar. Só inclua quando houver boa prática real a ensinar neste passo; não force seção
vazia. Mantenha curto e ancorado no que o passo exercita.>

## Para conferir antes de codar

- [ ] Consigo explicar <conceito> com minhas palavras.
- [ ] Sei qual é a entrada e a saída esperadas do que vou escrever.
- [ ] Se algo aqui é novidade total, avisei o tutor (o caminho ajusta, não eu).
```

Regras da aula:

- **Uma por passo** (`aulas/P0x-<slug>.md`), nomeada pelo ID do passo do `CAMINHO.md`.
- **Geradas no bootstrap** (`/novo-projeto`), mas **reveladas just-in-time**: o tutor
  aponta o aluno para a aula do passo ATUAL na hora do passo -- nunca manda ler todas de
  uma vez (isso recriaria o paredao de teoria que o metodo combate).
- **Recalibradas junto com o caminho**: ao recalibrar o `CAMINHO.md` no fechamento de
  marco, regenere as aulas dos passos que mudaram ou foram inseridos. Aula desatualizada
  e pior que aula nenhuma.
- **Teoria minima, nao enciclopedia**: o corte e "o suficiente para concluir ESTE passo".
  Conceito futuro entra na aula do passo futuro, nao aqui.
- **Boas praticas so quando aplicavel**: se o passo nao tem convencao relevante a ensinar,
  omita a secao em vez de inventar conteudo.
- **Apresentacao (texto puro):** aplique os 3 principios de Mayer que transferem para
  texto -- coerencia (corte o superfluo), sinalizacao (destaque o essencial), segmentacao
  (um passo atomico por vez) -- e linguagem simples/legivel. Os outros 9 tratam de
  audio/video e nao se aplicam: ver
  [so 3 de 12 principios transferem](fundamentos.md#mayer-so-3-de-12-principios-em-texto-puro).

## Formato do scaffold (TODO human)

Cada arquivo entregue ao aluno em `projeto/` recebe, no topo, um comentario assim
(adapte a sintaxe de comentario a linguagem):

```text
/*
  MARCO NN -- <nome>  (passos P0x-P0y do CAMINHO.md)
  META: <o que vai ficar pronto>
  PORQUE: <que capacidade isso destrava no projeto>
  PRESSUPOE: <conceitos ja introduzidos, por ID (ex: c01-tags-html). Se algum for
    novidade pra voce, AVISE antes de comecar -- o caminho e que ajusta, nao voce.>
  ARQUIVOS: <quais arquivos o aluno cria/edita neste marco>
  EXEMPLO-DE-RESULTADO: <o que o aluno VE quando der certo, concreto: "ao abrir
    index.html aparece uma lista com 3 itens; clicar num item risca o texto">
  PERGUNTA-GUIA: <pergunta socratica que o aluno responde ANTES de codar>
  DONE: <evidencia observavel de que voce JA CONSEGUE <a capacidade do passo>: o que roda/aparece quando voce a demonstra, nao so "o codigo compila">
*/
// TODO(human): <o que digitar, descrito como COMPORTAMENTO: "escreva a funcao que
//   recebe X e retorna Y", nunca "implemente a logica">
// PISTA (revele so se ele travar): <pista gradual, comentada>
```

NUNCA preencha o `TODO(human)`. O scaffold e o esqueleto; a carne e do aluno.

Validacao obrigatoria antes de entregar qualquer scaffold:

- Todo item de `PRESSUPOE` e conceito ja introduzido (passo anterior do CAMINHO.md
  fechado) OU coberto pelo substrato em nivel >= iniciante. Se nao for, o scaffold
  esta errado: conserte o caminho (insira passo / mude para "eu faco -> voce faz").
- `EXEMPLO-DE-RESULTADO` descreve algo observavel (tela, terminal, comportamento),
  nunca um conceito abstrato.
- O `TODO(human)` descreve comportamento (entrada -> saida / o que aparece), nunca
  "implemente X" seco.

### Como o aluno le o scaffold (explique na 1a entrega)

Os campos sao uma SEQUENCIA, nao um menu pra escolher "qual seguir". Na primeira vez que
entregar um scaffold, diga ao aluno a ordem de leitura -- senao ele trava sem saber qual
campo executar:

- META -> onde voce quer chegar (o destino)
- PORQUE -> por que isso importa (motivacao, pra nao ser tarefa cega)
- PRESSUPOE -> auto-checagem: se algo aqui e novidade, avise antes de comecar
- EXEMPLO-DE-RESULTADO -> visualize o resultado antes de pensar no codigo
- PERGUNTA-GUIA -> PENSE antes de digitar (constroi o entendimento)
- TODO(human) -> o que voce DIGITA (a unica acao a executar)
- DONE -> como saber que acertou (o teste final)
- PISTA -> rede de seguranca, so se travar de vez

### Sintaxe nova de verdade: "eu faco -> nos fazemos -> voce faz"

Descoberta socratica so funciona quando o aluno tem materia-prima pra raciocinar. Se o
TODO exige uma sintaxe que o aluno NUNCA viu (zero-absoluto no assunto), a pergunta-guia
vira abismo e a PISTA acaba sendo a unica saida -- o que forca copia cega, nao aprendizado.

A [liberacao gradual de responsabilidade](fundamentos.md#frameworks-foundational-load-bearing)
formaliza tres fases; o exemplo resolvido na fase "eu faco" e um worked example (instancia
diferente da do `TODO(human)`). As 3 fases, nomeadas e em ordem:

- **eu faco:** o agente MOSTRA um exemplo resolvido completo, explicando cada pedaco, numa
  instancia DIFERENTE da do `TODO(human)` (= worked example analogo). Para substrato
  zero-absoluto no conceito dominante, esse exemplo resolvido e OBRIGATORIO antes do solo.
- **nos fazemos:** pratica conjunta guiada -- o agente puxa cada micro-decisao, o aluno
  responde, o agente confirma -- numa instancia AINDA diferente da do `TODO(human)` solo.
  Esta e a ponte que faltava entre o exemplo e o solo.
- **voce faz:** o `TODO(human)` solo, o aluno aplica numa VARIACAO (outro nome, outro valor).
  Isso prova entendimento sem ser copia.

Gatilho CONDICIONAL do "nos fazemos": ligue a etapa quando o substrato no conceito dominante
e zero-absoluto/iniciante OU quando o salto do exemplo resolvido para o solo e grande. PULE
o "nos fazemos" em intermediario/avancado, onde a pratica conjunta vira atrito (conecta com
o fading da Sondagem: o andaime recua conforme a maestria sobe). A pergunta-guia socratica
seca volta a fazer sentido nos marcos seguintes, quando ja houver substrato acumulado.

A PISTA e rede de seguranca, NUNCA a ponte principal. Se o unico jeito de o aluno avancar
e descomentar a PISTA, o scaffold esta mal calibrado pro substrato dele -- conserte o
scaffold, nao culpe o aluno.

## Protocolo de forense (para erros)

Quando o aluno erra, conduza uma investigacao sistematica:

1. **Observar**: "O que voce esperava? O que aconteceu de fato?"
2. **Isolar**: "Qual e a menor parte do codigo que ainda reproduz o problema?"
3. **Hipoteses**: "O que poderia estar causando isso? Liste 2-3 possibilidades."
4. **Testar**: "Como voce poderia verificar qual hipotese esta certa?"
5. **Corrigir**: Aplique a correcao e verifique.
6. **Documentar**: Registre no `APRENDIZADO.md` o padrao de erro e a licao.

## Walking Skeleton

O primeiro marco (00) deve ser o esqueleto ambulante mais fino que prove que todas as
camadas funcionam juntas. Exemplos por tipo de projeto:

- **Web:** HTML basico + CSS basico + JS basico, conectados, renderizando algo na tela.
- **Backend:** Rota basica + resposta JSON + teste de ping.
- **Mobile:** Tela basica + navegacao + dados mock.
- **CLI:** Comando basico + argumento + output formatado.
- **Data/ML:** Leitura de dados + transformacao basica + output.

O Walking Skeleton NAO implementa logica de negocio. Ele prova que o pipeline funciona.
