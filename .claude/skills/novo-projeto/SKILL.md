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
- **Nao crie nenhum arquivo ainda.**

## Passo 2 — Roadmap (a espinha)
- Engenharia reversa do output final -> capacidades necessarias -> ordene por dependencia.
- Fatie em **marcos verticais (MVPs)**: cada marco entrega algo que roda/renderiza. NAO
  fatie por tema.
- Aplique a regra de granularidade de `reference.md`.
- Traduza a barra de qualidade numa **Definition of Done** com criterios objetivos,
  distribuidos pelos marcos (estetica, impressao, responsividade tem marco proprio).

## Passo 3 — Aprovacao (checkpoint obrigatorio)
- Apresente ao aluno: diagnostico + DoD + arvore de marcos (1 linha de meta cada).
- **Peca aprovacao antes de criar qualquer arquivo.** Ajuste conforme o feedback.

## Passo 4 — Esqueleto (so apos aprovacao)
Crie na pasta do projeto:
- `PROGRESSO.md` (use o template de `reference.md`): perfil, objetivo, DoD, arvore de
  marcos, marco atual = 00.
- `exercicios/` (vazia por enquanto).
- `projeto/` (vazia, ou com os arquivos-raiz minimos do artefato unico).
- `git init` se ainda nao houver repo.

## Passo 5 — Scaffold do Marco 00 (somente esse)
- Gere o scaffold do primeiro marco em `projeto/` no formato de `reference.md`:
  `TODO(human)` + pergunta-guia.
- Se a regra de drill disparar, gere o drill em `exercicios/`.
- Lembre o aluno de ativar a persona: `/output-style mentor-projeto`.
- **Pare e espere a tentativa do aluno.** Os marcos seguintes sao gerados on-the-go, sob a
  conduta do output style `mentor-projeto`.
