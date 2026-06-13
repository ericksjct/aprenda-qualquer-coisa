# Referencia — Mentor de Projeto

## Sondagem de substrato

Autoavaliacao engana: "sei um pouco de JS" pode ser qualquer coisa entre zero-absoluto
e intermediario. Sonde na pratica, com 2-3 sondas rapidas por assunto duvidoso:

- **Reconhecimento**: mostre um snippet de 3-5 linhas do assunto e pergunte
  "o que esse trecho faz?". Quem nao reconhece a sintaxe e zero-absoluto.
- **Producao descrita**: "como voce faria X?" — descricao em palavras basta;
  nao exija codigo perfeito no chat.
- **Vocabulario**: "o que significa [termo central do assunto]?" — vocabulario
  avancado sinaliza profundidade desejada, nao maestria; confirme com as outras sondas.

Classificacao por assunto:

- **zero-absoluto** — nao reconhece a sintaxe; nao tem materia-prima pra deduzir.
  Andaime: "eu faco -> voce faz" obrigatorio na entrada do assunto.
- **iniciante** — reconhece e le, mas nao produz sem apoio. Andaime: pergunta-guia
  + scaffold detalhado.
- **intermediario** — produz com hesitacao. Andaime: pergunta-guia + scaffold padrao.
- **avancado** — produz e explica trade-offs. Andaime: mais buraco, menos pista.

Regras:

- Agrupe TODAS as sondas numa unica mensagem (nao vire interrogatorio).
- Registre nivel + evidencia na tabela do `PROGRESSO.md`. Evidencia importa: e o que
  permite recalibrar depois sem re-sondar do zero.
- O substrato e **por assunto, nao por aluno**: um aluno forte em logica/dados pode
  ser zero-absoluto em sintaxe de frontend. Calibre pelo substrato DO ASSUNTO em jogo.
- Re-sonde de leve quando o vocabulario do aluno mudar ou um marco fechar com folga
  ou com muito sofrimento.

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

## Template — CAMINHO.md

O `CAMINHO.md` e a expansao completa do caminho de aprendizado, gerada ANTES da
montagem dos marcos. E o documento de design; o `PROGRESSO.md` e o de acompanhamento.

```markdown
# CAMINHO — <nome do projeto>

> Regra de ouro: o passo N so pode pressupor conceitos introduzidos em P01..P(N-1)
> ou cobertos pelo substrato do aluno (tabela no PROGRESSO.md).

## Conceitos (indice)

- c01-<slug> — <definicao de 1 linha> (introduzido em P01)
- c02-<slug> — <definicao de 1 linha> (introduzido em P02)

## Passos

### P01 — <titulo curto>

- Conceito dominante (novo): c01-<slug>
- Pressupoe: (nenhum — entrada coberta pelo substrato)
- Substrato exigido: <assunto>: zero-absoluto ok ("eu faco -> voce faz")
- Entregavel: <o que o aluno ESCREVE> + <o que ele VE funcionando ao terminar>
- Arquivos: <paths em projeto/>

### P02 — <titulo curto>

- Conceito dominante (novo): c02-<slug>
- Pressupoe: c01-<slug>
- Substrato exigido: <assunto>: >= iniciante
- Entregavel: ...
- Arquivos: ...

## Mapa passos -> marcos

- Marco 00 (Walking Skeleton): P01-P02 — coeso porque <1 linha>
- Marco 01: P03-P05 — coeso porque <1 linha>
```

Regras do caminho:

- IDs de conceito sao estaveis (`c01-tags-html`); marcos e scaffolds referenciam por ID.
- "Entregavel" e sempre concreto e observavel: o que o aluno digita e o que aparece
  na tela/terminal quando da certo. "Aprender flexbox" NAO e entregavel;
  "os 3 cards ficam lado a lado e centralizados" e.
- Se um passo precisaria de 2 conceitos dominantes novos, sao 2 passos.
- Se a referencia do roadmap.sh (em `referencias/`) introduz um conceito antes do seu
  caminho, cheque se ha buraco de dependencia.

## Verificacao de coesao (rodar no Passe 2 e em toda recalibragem)

Checklist mecanico — falhou, conserta o caminho antes de qualquer scaffold:

- [ ] Todo conceito em "Pressupoe" de P(N) e dominante de algum P(<N), OU esta coberto
      pelo substrato em nivel >= iniciante.
- [ ] Cada passo introduz no maximo 1 conceito dominante novo.
- [ ] Todo passo cujo assunto esta zero-absoluto na tabela esta marcado
      "eu faco -> voce faz".
- [ ] Cada marco agrupa passos CONSECUTIVOS do caminho (sem buracos nem saltos).
- [ ] Cada marco termina em algo que roda/renderiza (fatia vertical, nao tema).
- [ ] O primeiro marco e um Walking Skeleton.
- [ ] Todo entregavel e observavel (descreve o que o aluno VE, nao so o que "aprende").

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

## SPIDR Splitting — quando um marco e grande demais

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

## Layout do repo do aluno

```text
<projeto>/
├── CAMINHO.md            # design: passos detalhados + mapa passos -> marcos
├── PROGRESSO.md          # acompanhamento: substrato, DoD, marcos, dividas, log
├── APRENDIZADO.md        # diario de bordo: licoes, padroes de erro, decisoes
├── referencias/          # roadmaps de referencia (scripts/roadmap_fetch.py)
├── exercicios/           # drills ISOLADOS, gerados just-in-time
│   └── NN-<conceito>/     #   pasta-por-conceito so aqui
└── projeto/              # o ARTEFATO UNICO; cresce marco a marco (marcos = git tags)
```

## Template — PROGRESSO.md

```markdown
# PROGRESSO — <nome do projeto>

## Substrato por assunto

| Assunto | Nivel | Evidencia da sondagem |
|---|---|---|
| <assunto> | zero-absoluto / iniciante / intermediario / avancado | <o que a sonda mostrou> |

## Objetivo

- Objetivo de aprendizado: ...
- Restricoes (stack/tempo/ferramentas): ...

## Output final

<descricao do que sera construido>

## Definition of Done

- [ ] <criterio objetivo 1>
- [ ] <criterio objetivo 2>

## Marcos

### 00 — <slug> (Walking Skeleton)  <- ATUAL

**User Story:** Como [usuario], eu quero [capacidade basica], para que [valor minimo].
**Passos do caminho:** P01-P02 (ver CAMINHO.md)
**Entregavel:** <o que o aluno VE funcionando ao fechar o marco>

- [ ] <criterio de done>

### 01 — <slug>

**User Story:** Como [usuario], eu quero [capacidade], para que [valor].
**Passos do caminho:** P03-P05
**Entregavel:** <concreto e observavel>

- [ ] <criterio de done>

## Dividas de aprendizado

- (registradas na curadoria; revisitar quando fizer sentido)

## Log

- AAAA-MM-DD — marco-00 fechado: <o que ficou pronto>
```

## Template — APRENDIZADO.md

```markdown
# Diario de Aprendizado — <nome do projeto>

## Licoes

- AAAA-MM-DD — <conceito aprendido> (contexto: <em que marco/situacao>)

## Padroes de erro

- AAAA-MM-DD — <erro recorrente> → <causa raiz> → <como evitar da proxima vez>

## Decisoes arquiteturais

- AAAA-MM-DD — <decisao tomada> (contexto: <por que escolhemos isso>)

## Dividas de aprendizado (da curadoria)

- <divida> — registrada em <data> — revisitar no marco <NN>
```

## Formato do scaffold (TODO human)

Cada arquivo entregue ao aluno em `projeto/` recebe, no topo, um comentario assim
(adapte a sintaxe de comentario a linguagem):

```text
/*
  MARCO NN — <nome>  (passos P0x-P0y do CAMINHO.md)
  META: <o que vai ficar pronto>
  PORQUE: <que capacidade isso destrava no projeto>
  PRESSUPOE: <conceitos ja introduzidos, por ID (ex: c01-tags-html). Se algum for
    novidade pra voce, AVISE antes de comecar — o caminho e que ajusta, nao voce.>
  ARQUIVOS: <quais arquivos o aluno cria/edita neste marco>
  EXEMPLO-DE-RESULTADO: <o que o aluno VE quando der certo, concreto: "ao abrir
    index.html aparece uma lista com 3 itens; clicar num item risca o texto">
  DONE: <como o aluno sabe que terminou>
  PERGUNTA-GUIA: <pergunta socratica que o aluno responde ANTES de codar>
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
entregar um scaffold, diga ao aluno a ordem de leitura — senao ele trava sem saber qual
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
vira abismo e a PISTA acaba sendo a unica saida — o que forca copia cega, nao aprendizado.

Nesse caso, inverta a ordem: MOSTRE um exemplo resolvido primeiro (o "eu faco"), explique
cada pedaco, e so entao peca ao aluno pra APLICAR numa VARIACAO (outro nome, outro valor —
o "voce faz"). Isso prova entendimento sem ser copia. A pergunta-guia socratica seca volta
a fazer sentido nos marcos seguintes, quando ja houver substrato acumulado.

A PISTA e rede de seguranca, NUNCA a ponte principal. Se o unico jeito de o aluno avancar
e descomentar a PISTA, o scaffold esta mal calibrado pro substrato dele — conserte o
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
