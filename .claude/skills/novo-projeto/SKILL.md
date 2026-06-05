---
name: novo-projeto
description: Bootstrap de um projeto de aprendizado. Use quando o aluno chega com uma demanda ou projeto que quer aprender a construir. Faz diagnostico, gera um roadmap de marcos (PROGRESSO.md) e, apos aprovacao, monta o esqueleto do repo e o scaffold do primeiro marco.
---

# Bootstrap de Projeto de Aprendizado

Transforma a demanda do aluno num projeto de aprendizado estruturado.
Leia tambem `reference.md` (nesta pasta) para: regra de granularidade, template do
`PROGRESSO.md`, layout do repo e formato dos scaffolds.

## Passo 1 — Diagnostico (em chat, read-only)

A partir da demanda do aluno (texto no chat e/ou arquivo de referencia que ele anexar):
- Levante: output final desejado, barra de qualidade, perfil (o que ja sabe, objetivo,
  nivel atual), restricoes (stack, tempo por sessao, ferramentas).
- Faca **no maximo 2 perguntas** se faltar algo essencial. Nao presuma o nivel.
- Mapeie o **substrato por assunto**, nao so o nivel global: para cada assunto que a stack
  do projeto exige (ex: HTML, CSS, JS), o aluno e avancado, iniciante ou zero-absoluto?
  Zero-absoluto num assunto muda o andaime (exige "eu faco -> voce faz", nao pergunta
  socratica seca). Um aluno forte num dominio pode ser zero-absoluto noutro.
- **Nao crie nenhum arquivo ainda.**

## Passo 2 — Roadmap (a espinha)

- Engenharia reversa do output final -> capacidades necessarias -> ordene por dependencia.
- Fatie em **marcos verticais (MVPs)**: cada marco entrega algo que roda/renderiza. NAO
  fatie por tema.
- Aplique a regra de granularidade de `reference.md`.
- Traduza a barra de qualidade numa **Definition of Done** com criterios objetivos,
  distribuidos pelos marcos (estetica, impressao, responsividade tem marco proprio).

## Passo 3 — User Stories (uma por marco)

Para cada marco, enquadre como uma historia de usuario no formato:

```text
Como [tipo de usuario], eu quero [capacidade], para que [beneficio].
```

- O "Como" define quem usa o que sera construido.
- O "quero" define a capacidade entregue no marco.
- O "para que" define o valor — e e o criterio de "done" do marco.

Se uma historia for grande demais para um marco, use **SPIDR Splitting** (veja
`/spidr-split`) para quebrar em fatias menores antes de prosseguir.

## Passo 4 — Aprovacao (checkpoint obrigatorio)

- Apresente ao aluno: diagnostico + DoD + arvore de marcos (1 linha de meta cada) +
  as User Stories de cada marco.
- **Peca aprovacao antes de criar qualquer arquivo.** Ajuste conforme o feedback.
- Esta e a regra "Demanda-First": nenhum codigo antes da demanda estar clara e aprovada.

## Passo 5 — Esqueleto (so apos aprovacao)

Crie na pasta do projeto:
- `PROGRESSO.md` (use o template de `reference.md`): perfil, objetivo, DoD, arvore de
  marcos com User Stories, marco atual = 00.
- `APRENDIZADO.md` (vazio, pronto para o aluno preencher): diario de licoes, padroes
  de erro, decisoes arquiteturais.
- `exercicios/` (vazia por enquanto).
- `projeto/` (vazia, ou com os arquivos-raiz minimos do artefato unico).
- `git init` se ainda nao houver repo.

## Passo 6 — Walking Skeleton (Marco 00)

O primeiro marco deve ser um **Walking Skeleton** — o esqueleto ambulante mais fino
que prove que todas as camadas funcionam juntas:

- Se for web: HTML basico + CSS basico + JS basico, tudo conectado, renderizando algo.
- Se for backend: rota basica + resposta JSON + teste de ping.
- Se for mobile: tela basica + navegacao + dados mock.

O Walking Skeleton NAO implementa logica de negocio. Ele prova que o pipeline
funciona. Isso da ao aluno confianca de que o projeto "respira" desde o dia 1.

Gere o scaffold do Marco 00 em `projeto/` no formato de `reference.md`:
`TODO(human)` + pergunta-guia.

- Calibre o scaffold ao **substrato** (ver `reference.md`): se o Marco 00 exige sintaxe
  que o aluno nunca viu, use "eu faco -> voce faz" (exemplo resolvido + variacao) em vez
  de pergunta-guia seca. Na 1a entrega, explique a ordem de leitura dos campos do scaffold
  (META -> PORQUE -> PERGUNTA-GUIA -> TODO -> DONE -> PISTA).

- Se a regra de drill disparar, gere o drill em `exercicios/`.
- Lembre o aluno de ativar a persona: `/output-style mentor-projeto`.
- **Pare e espere a tentativa do aluno.** Os marcos seguintes sao gerados on-the-go, sob a
  conduta do output style `mentor-projeto`.
