---
name: converte-livro
description: Conversao de livro-base. Use quando o aluno tem um livro-base em PDF e quer converte-lo para markdown em .projetos/<slug>/livro/, ou quando o bootstrap pergunta "tem livro-base?". Aponta para o procedimento canonico no mentor.
---

# Converte Livro (adaptador Claude Code)

Leia `mentor/novo-projeto.md` (passo do livro-base, "Passo 3b") na raiz deste
repositorio e siga o procedimento exatamente: pergunte se o livro e PDF ou `.md`,
pre-avise que a conversao demora / nao consome tokens (roda local) / mostra o
progresso, e so consuma `livro/` depois.

Excecao de convencao: ao contrario das demais skills (que apontam para
`mentor/<comando>.md`), esta aponta para `mentor/novo-projeto.md` — o livro-base e um
PASSO do bootstrap, nao um procedimento proprio; nao existe `mentor/converte-livro.md`.
