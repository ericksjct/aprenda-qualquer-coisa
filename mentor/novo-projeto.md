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
python scripts/roadmap_fetch.py <slug> -o .projetos/<slug>/referencias/
```

Rode da raiz deste repositorio; a saida deve ficar DENTRO da pasta do projeto do
aluno (`.projetos/<slug>/referencias/`, que o Passo 7 lista no esqueleto).

- O markdown gerado da a **ordenacao canonica de conceitos** do assunto. Use-o como
  verificador de ordem no Passo 4: se o seu caminho usa um conceito antes do ponto em
  que o roadmap de referencia o introduz, provavelmente ha um buraco.
- E base de ordenacao, NAO curriculo a copiar: o caminho continua sendo fatiado em
  marcos verticais orientados pelo projeto do aluno, nunca por tema.
- Se o script nao estiver acessivel ou o assunto nao tiver roadmap, siga sem ele.

## Passo 3b — Livro-base (opcional)

Se o aluno tem um livro-base que quer usar como literatura de apoio, o mentor
PERGUNTA: "tem livro-base? (PDF ou `.md`)". Entao ramifique:

- Se `.md`: instrua o aluno a COLAR o arquivo (ou os capitulos) em
  `.projetos/<slug>/livro/`. Caminho sem nenhuma dependencia nova — nada de docling,
  nada de venv.
- Se PDF: o mentor mostra a linha de comando EXATA abaixo (ou dispara
  `/converte-livro`), sempre com o PRE-AVISO obrigatorio:
  "vai demorar, nao consome tokens (roda local), e mostra o progresso (pagina N de M)".
  A 1a execucao tambem baixa modelos (~2GB).

```text
python -m venv .venv-pdf
.\.venv-pdf\Scripts\activate
pip install -r requirements-pdf.txt
python scripts/converte_livro.py <pdf> --slug <slug>
```

Use o venv explicito (Python 3.10+) ativado acima — nunca o `python` global ambiguo.

- A saida (markdown do livro, **um arquivo por capitulo** com ancoras
  `<!-- page: N -->`) fica em `.projetos/<slug>/livro/`. E a literatura-base que o tutor
  consulta depois (detalhado em `mentor/tutor.md`).
- O mentor NUNCA roda docling silenciosamente: ele mostra o comando ou dispara a skill
  com o pre-aviso, e so segue quando `livro/` estiver populado.
- Se o aluno nao tem livro-base, ou o venv nao esta acessivel, siga sem ele — o livro e
  opcional; o contrato e apenas markdown em `livro/` quando existir.

## Passo 4 — Passe 1: o caminho completo (`CAMINHO.md`)

Expanda o caminho de aprendizado INTEIRO antes de pensar em marcos:

- Engenharia reversa do output final -> capacidades necessarias -> conceitos
  necessarios -> ordene por dependencia (use a referencia do Passo 3 como guia).
- Essa engenharia reversa (capacidade-alvo -> atividade) e o
  [backward design](fundamentos.md#frameworks-foundational-load-bearing): defina o
  resultado desejado (a capacidade) antes de desenhar os passos.
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
- Dimensione o **primeiro marco** (Walking Skeleton) como o MENOR possivel: a primeira
  vitoria precisa vir rapido (ver Passo 8, "primeiro done leve").
- Enquadre cada marco como **User Story**: "Como [usuario], eu quero [capacidade],
  para que [beneficio]". Historia grande demais -> `/spidr-split` ANTES de seguir.
- Junto da User Story, escreva no `PROGRESSO.md` a **frase de capacidade** daquele
  marco, no formato `ao terminar, voce consegue <verbo> <conceito>` (campo
  `**Capacidade:**` da arvore de marcos do template em `mentor/reference.md`). E a
  evidencia de maestria do marco (backward design: defina a capacidade-alvo antes de
  detalhar os passos). O que voce GRAVA no `PROGRESSO.md` e so o verbo de capacidade
  puro — sem nomes de framework (o aluno le esse arquivo).
- **Teto rigido:** exatamente 1 frase de capacidade por marco. Se virou lista, rubrica
  ou sub-doc, esta errado — corte. Obrigatorio por marco (o gate de fechamento depende
  dessa frase existir), nunca opcional.
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

Todo projeto mora em `.projetos/<slug>/` (a "raiz do projeto"; ver o layout em
`mentor/reference.md`). Escolha um `<slug>` curto em kebab-case e crie DENTRO de
`.projetos/<slug>/`:

- `CAMINHO.md` (o artefato do Passo 4 + mapa do Passo 5).
- `PROGRESSO.md` (template em `mentor/reference.md`): substrato, objetivo, DoD, arvore de
  marcos com User Stories e passos do caminho, marco atual = 00.
- `APRENDIZADO.md` (vazio, pronto para o aluno preencher).
- `aulas/` (sera preenchida no Passo 7b).
- `exercicios/` (vazia por enquanto) e `projeto/` (vazia ou com arquivos-raiz minimos).
- `referencias/` (se o Passo 3 gerou roadmap de referencia).
- `livro/` (se o Passo 3b converteu/colou o livro-base do aluno).

A pasta `.projetos/` esta no `.gitignore` do toolkit (projetos sao pessoais, nao sobem
pro github do toolkit). Cada projeto e seu PROPRIO repo git: rode `git init` dentro de
`.projetos/<slug>/`. Os marcos viram tags `marco-NN-<slug>` nesse repo; o aluno pusha
pra um github proprio se quiser.

## Passo 7b — Aulas (uma por passo do CAMINHO)

Gere uma aula por passo do `CAMINHO.md` em `aulas/P0x-<slug>.md`, no template de
`mentor/reference.md`. Esta e a correcao central do metodo: o aluno nunca deve precisar
adivinhar intuitivamente COMO fazer um passo — a aula e o insumo teorico confiavel,
lido antes do scaffold, suficiente para concluir o passo sem internet nem PISTA.

Cada aula traz: **objetivo do passo**, **o que o tutor espera do aluno**, **teoria
minima** (intuicao -> exemplo -> conceito formal), **exemplos de aplicacao** e **boas
praticas quando aplicavel**.

- Calibre a profundidade pelo substrato DO ASSUNTO do passo (tabela do Passo 2): assunto
  zero-absoluto -> exemplos de aplicacao no formato "eu faco" (resolvido e explicado);
  assunto avancado -> teoria enxuta, mais foco em trade-offs e boas praticas.
- **Contrato anti-gabarito**: os exemplos da aula usam instancia DIFERENTE da do
  `TODO(human)`. Se um exemplo, copiado, fecha o passo, a aula esta errada.
- As aulas sao geradas agora (todas), mas o tutor as revela **just-in-time** (a do passo
  atual, na hora do passo). Nao instrua o aluno a ler todas de uma vez.

## Passo 8 — Walking Skeleton (Marco 00)

O primeiro marco e um **Walking Skeleton** — o esqueleto mais fino que prova que
todas as camadas funcionam juntas (exemplos por tipo de projeto em `mentor/reference.md`).
Ele NAO implementa logica de negocio.

Esse e o **primeiro done leve**: o menor entregavel que ja "roda" reduz o
time-to-first-success e e a principal defesa contra a evasao do estudo assincrono
([anti-evasao da SDT](fundamentos.md#frameworks-supporting-ancoram-um-doc) —
competencia via micro-vitorias). Quanto antes a primeira vitoria, melhor.

Gere o scaffold do Marco 00 em `projeto/` no formato de `mentor/reference.md`, que inclui
obrigatoriamente `PRESSUPOE`, `ARQUIVOS` e `EXEMPLO-DE-RESULTADO`:

- Valide o `PRESSUPOE` contra a tabela de substrato: se o marco exige sintaxe que o
  aluno nunca viu (zero-absoluto no assunto), use "eu faco -> voce faz" (exemplo
  resolvido + variacao) em vez de pergunta socratica seca.
- Na 1a entrega, explique a ordem de leitura dos campos do scaffold
  (META -> PORQUE -> PRESSUPOE -> EXEMPLO-DE-RESULTADO -> PERGUNTA-GUIA -> TODO ->
  DONE -> PISTA).
- Se a regra de drill disparar, gere o drill em `exercicios/`.
- Garanta que a conduta de `mentor/metodo.md` esta ativa (no Claude Code: `/config` -> Output style -> `mentor-projeto`).
- **Pare e espere a tentativa do aluno.** Os scaffolds dos marcos seguintes sao
  gerados a cada fechamento (`/fecha-marco`), sempre seguindo os passos ja
  detalhados no `CAMINHO.md`.

A partir daqui o bootstrap terminou: o dia a dia do aluno e conduzido pelo tutor
copiloto — toda sessao de estudo comeca com `/tutor` (restaura contexto, conduz o
passo atual, revisa tentativas e roteia para debug/fechamento).
