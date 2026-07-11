---
name: converte-livro
description: Conversao de livro-base. Use quando o aluno tem um livro-base em PDF e quer converte-lo para markdown em .projetos/<slug>/livro/, ou quando o bootstrap pergunta "tem livro-base?". Aponta para o procedimento canonico no mentor.
---

# Converte Livro (adaptador Claude Code)

Leia `mentor/novo-projeto.md` (passo do livro-base, "Passo 3b") na raiz deste
repositorio e siga o procedimento exatamente: pergunte se o livro e PDF ou `.md`,
pre-avise que a conversao demora / nao consome tokens (roda local) / mostra o
progresso, e so consuma `livro/` depois.

Dois requisitos NAO-NEGOCIAVEIS deste fluxo:

1. **CRIE os diretorios automaticamente.** Antes de pedir o arquivo, rode
   `New-Item -ItemType Directory -Force` para `.projetos/<slug>/livro-fonte/` (PDF
   cru) e `.projetos/<slug>/livro/` (saida). Nunca deixe o aluno adivinhar onde por
   o livro.
2. **ENTREGUE um script, nao um passo-a-passo no chat.** Para PDF, aponte o aluno
   para `scripts/converte-livro.ps1` (versionado) e de UMA linha pra rodar no
   terminal: `.\scripts\converte-livro.ps1 -Slug <slug>`. O `.ps1` cria as pastas,
   ESCOLHE o motor sozinho (GPU -> VLM com formulas em LaTeX + indice de consulta
   `livro/.index/`; sem GPU -> docling texto), provisiona o venv do motor e instala
   deps na 1a vez, descobre o PDF em `livro-fonte/` e converte. Nunca peca pro
   aluno colar `python -m venv ...` linha a linha.

Excecao de convencao: ao contrario das demais skills (que apontam para
`mentor/<comando>.md`), esta aponta para `mentor/novo-projeto.md` — o livro-base e um
PASSO do bootstrap, nao um procedimento proprio; nao existe `mentor/converte-livro.md`.
