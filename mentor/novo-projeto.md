# Bootstrap de Projeto de Aprendizado

Transforma a demanda do aluno num projeto de aprendizado estruturado.
Leia tambem `mentor/reference.md` para: sondagem de substrato, template do
`CAMINHO.md`, verificacao de coesao, template do `PROGRESSO.md`, layout do repo e
formato dos scaffolds.

Ordem inegociavel: **diagnostico -> sondagem -> caminho completo -> marcos -> aprovacao
-> arquivos**. Nunca monte marcos antes de expandir o caminho inteiro, e nunca crie
arquivos antes da aprovacao.

## Passo 1 — Diagnostico (em chat, read-only)

A partir da demanda do aluno (texto no chat e/ou arquivo de referencia que ele anexar):

- Levante: output final desejado, barra de qualidade, objetivo de aprendizado,
  restricoes (stack, tempo por sessao, ferramentas).
- Faca **no maximo 2 perguntas** sobre objetivo/restricoes se faltar algo essencial.
- **Nao crie nenhum arquivo ainda.**

## Passo 2 — Sondagem de substrato (obrigatoria)

NAO infira o nivel do aluno a partir da descricao dele — autoavaliacao e a causa
numero 1 de scaffold descalibrado. Sonde na pratica:

- Liste os assuntos que a stack do projeto exige (ex: HTML, CSS, JS, logica).
- Para cada assunto cujo nivel nao esteja evidente, aplique **2-3 sondas rapidas**
  (reconhecimento de snippet, producao descrita, vocabulario — ver `mentor/reference.md`).
  Agrupe todas as sondas numa UNICA mensagem para nao virar interrogatorio.
- Classifique cada assunto: **zero-absoluto / iniciante / intermediario / avancado**.
- O resultado vira a tabela "Substrato por assunto" do `PROGRESSO.md`. Toda decisao
  de andaime daqui em diante e validada contra essa tabela.

## Passo 3 — Referencia externa (recomendado)

Se a stack corresponde a um roadmap do roadmap.sh (frontend, backend, python, react...):

```text
python scripts/roadmap_fetch.py <slug> -o <pasta-do-projeto>/referencias/
```

Rode da raiz deste repositorio; a saida deve ficar DENTRO da pasta do projeto do
aluno (e o `referencias/` que o Passo 7 lista no esqueleto).

- O markdown gerado da a **ordenacao canonica de conceitos** do assunto. Use-o como
  verificador de ordem no Passo 4: se o seu caminho usa um conceito antes do ponto em
  que o roadmap de referencia o introduz, provavelmente ha um buraco.
- E base de ordenacao, NAO curriculo a copiar: o caminho continua sendo fatiado em
  marcos verticais orientados pelo projeto do aluno, nunca por tema.
- Se o script nao estiver acessivel ou o assunto nao tiver roadmap, siga sem ele.

## Passo 4 — Passe 1: o caminho completo (`CAMINHO.md`)

Expanda o caminho de aprendizado INTEIRO antes de pensar em marcos:

- Engenharia reversa do output final -> capacidades necessarias -> conceitos
  necessarios -> ordene por dependencia (use a referencia do Passo 3 como guia).
- Quebre em **passos**, cada um com: 1 conceito dominante novo (com ID estavel),
  o que pressupoe, substrato exigido, **entregavel concreto** (o que o aluno escreve
  E o que ele ve funcionando) e arquivos tocados. Template em `mentor/reference.md`.
- Regra de ouro do caminho: o passo N so pode pressupor conceitos introduzidos em
  passos anteriores OU cobertos pelo substrato do aluno (tabela do Passo 2). Se um
  passo viola isso, insira o passo que falta — nao "explique rapidinho" dentro do
  scaffold depois.
- Onde o substrato e zero-absoluto, marque o passo de entrada como
  `"eu faco -> voce faz"` ja no caminho.

## Passo 5 — Passe 2: montagem dos marcos

So agora agrupe os passos em marcos:

- Cada marco = sequencia de passos **consecutivos** do caminho que, juntos, entregam
  algo que roda/renderiza (**fatia vertical**, nunca tema).
- Aplique a regra de granularidade de `mentor/reference.md` (sessao de ~30-90 min).
- Enquadre cada marco como **User Story**: "Como [usuario], eu quero [capacidade],
  para que [beneficio]". Historia grande demais -> `/spidr-split` ANTES de seguir.
- Traduza a barra de qualidade numa **Definition of Done** objetiva, distribuida
  pelos marcos.
- Rode a **verificacao de coesao** de `mentor/reference.md` (checklist mecanico). Se falhar,
  conserte o caminho/agrupamento agora — e barato aqui, caro depois.
- Registre o mapa passos -> marcos no proprio `CAMINHO.md`.

## Passo 6 — Aprovacao (checkpoint obrigatorio)

- Apresente ao aluno: tabela de substrato + DoD + caminho resumido (1 linha por
  passo) + arvore de marcos com User Stories e entregavel concreto de cada um.
- **Peca aprovacao antes de criar qualquer arquivo.** Ajuste conforme o feedback.
- Esta e a regra "Demanda-First": nenhum codigo antes da demanda estar clara e aprovada.

## Passo 7 — Esqueleto (so apos aprovacao)

Crie na pasta do projeto:

- `CAMINHO.md` (o artefato do Passo 4 + mapa do Passo 5).
- `PROGRESSO.md` (template em `mentor/reference.md`): substrato, objetivo, DoD, arvore de
  marcos com User Stories e passos do caminho, marco atual = 00.
- `APRENDIZADO.md` (vazio, pronto para o aluno preencher).
- `exercicios/` (vazia por enquanto) e `projeto/` (vazia ou com arquivos-raiz minimos).
- `referencias/` (se o Passo 3 gerou roadmap de referencia).
- `git init` se ainda nao houver repo.

## Passo 8 — Walking Skeleton (Marco 00)

O primeiro marco e um **Walking Skeleton** — o esqueleto mais fino que prova que
todas as camadas funcionam juntas (exemplos por tipo de projeto em `mentor/reference.md`).
Ele NAO implementa logica de negocio.

Gere o scaffold do Marco 00 em `projeto/` no formato de `mentor/reference.md`, que inclui
obrigatoriamente `PRESSUPOE`, `ARQUIVOS` e `EXEMPLO-DE-RESULTADO`:

- Valide o `PRESSUPOE` contra a tabela de substrato: se o marco exige sintaxe que o
  aluno nunca viu (zero-absoluto no assunto), use "eu faco -> voce faz" (exemplo
  resolvido + variacao) em vez de pergunta socratica seca.
- Na 1a entrega, explique a ordem de leitura dos campos do scaffold
  (META -> PORQUE -> PRESSUPOE -> EXEMPLO-DE-RESULTADO -> PERGUNTA-GUIA -> TODO ->
  DONE -> PISTA).
- Se a regra de drill disparar, gere o drill em `exercicios/`.
- Garanta que a conduta de `mentor/metodo.md` esta ativa (no Claude Code: `/output-style mentor-projeto`).
- **Pare e espere a tentativa do aluno.** Os scaffolds dos marcos seguintes sao
  gerados a cada fechamento (`/fecha-marco`), sempre seguindo os passos ja
  detalhados no `CAMINHO.md`.

A partir daqui o bootstrap terminou: o dia a dia do aluno e conduzido pelo tutor
copiloto — toda sessao de estudo comeca com `/tutor` (restaura contexto, conduz o
passo atual, revisa tentativas e roteia para debug/fechamento).
