# Referencia — Mentor de Projeto

## Regra de granularidade

- Unidade = **1 capacidade coesa**, nao 1 atomo de conceito. Teste: ao fechar a unidade,
  o aluno consegue articular UM "porque" inteiro.
- **Criterio de fechamento verificavel**: cada unidade tem um "done" objetivo (algo roda,
  renderiza, passa num check visual). Check verde so vale se houve sintese.
- **Tamanho**: completavel numa sessao focada (~30-90 min). Maior -> quebre; menor -> funda.
- **Salto suave**: cada unidade introduz no maximo 1 conceito dominante novo e reusa os
  anteriores. Sem degraus.
- **Granularidade ~ 1/nivel**: iniciante -> unidades menores + mais andaime; avancado ->
  unidades maiores + mais buraco a preencher.
- **Substrato por assunto, nao por aluno**: o nivel GLOBAL engana. Um aluno pode ser
  avancado em logica/dados e ZERO-ABSOLUTO na sintaxe de um assunto novo (ex: HTML/JS de
  frontend). Calibre pelo substrato DO ASSUNTO em jogo, nao por uma media do aluno.
  Zero-absoluto != iniciante: zero nao tem materia-prima pra deduzir uma sintaxe que
  nunca viu, entao "descobrir sozinho" vira abismo, nao desafio (ver formato do scaffold).

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

A cada marco fechado, releia `PROGRESSO.md` e **recalibre os marcos restantes** (divida,
funda, ajuste granularidade) com base em como o aluno performou. O roadmap e uma espinha
estavel, mas as folhas adaptam.

## Marcos = git, nao pastas (para artefato unico)

Para um artefato unico que cresce (um app, um site), os marcos sao **estagios** marcados
com `git tag marco-NN-<slug>`, NAO pastas. `projeto/` tem UM conjunto de arquivos que
evolui marco a marco. Pastas-por-conceito existem apenas em `exercicios/` (drills isolados).

## Layout do repo do aluno

```text
<projeto>/
├── PROGRESSO.md          # fonte da verdade: perfil, DoD, marcos, dividas, log
├── APRENDIZADO.md        # diario de bordo: licoes, padroes de erro, decisoes
├── exercicios/           # drills ISOLADOS, gerados just-in-time
│   └── NN-<conceito>/     #   pasta-por-conceito so aqui
└── projeto/              # o ARTEFATO UNICO; cresce marco a marco (marcos = git tags)
```

## Template — PROGRESSO.md

```markdown
# PROGRESSO — <nome do projeto>

## Perfil do aluno
- Ja sabe: ...
- Objetivo: ...
- Nivel atual: ...
- Restricoes (stack/tempo/ferramentas): ...

## Output final
<descricao do que sera construido>

## Definition of Done
- [ ] <criterio objetivo 1>
- [ ] <criterio objetivo 2>

## Marcos

### 00 — <slug> (Walking Skeleton)
**User Story:** Como [usuario], eu quero [capacidade basica], para que [valor minimo].
- [ ] <criterio de done>

### 01 — <slug>
**User Story:** Como [usuario], eu quero [capacidade], para que [valor].
- [ ] <criterio de done>

### 02 — <slug>
**User Story:** Como [usuario], eu quero [capacidade], para que [valor].
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
  MARCO NN — <nome>
  META: <o que vai ficar pronto>
  PORQUE: <que capacidade isso destrava no projeto>
  DONE: <como o aluno sabe que terminou>
  PERGUNTA-GUIA: <pergunta socratica que o aluno responde ANTES de codar>
*/
// TODO(human): <o que o aluno deve implementar aqui>
// PISTA (revele so se ele travar): <pista gradual, comentada>
```

NUNCA preencha o `TODO(human)`. O scaffold e o esqueleto; a carne e do aluno.

### Como o aluno le o scaffold (explique na 1a entrega)

Os campos sao uma SEQUENCIA, nao um menu pra escolher "qual seguir". Na primeira vez que
entregar um scaffold, diga ao aluno a ordem de leitura — senao ele trava sem saber qual
campo executar:

- META -> onde voce quer chegar (o destino)
- PORQUE -> por que isso importa (motivacao, pra nao ser tarefa cega)
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
