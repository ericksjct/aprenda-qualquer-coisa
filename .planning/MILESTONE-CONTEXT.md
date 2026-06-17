---
source: pre-scoped via conversa 2026-06-17 (decisoes travadas pelo usuario antes de fechar v1.0)
suggested_version: v2.0
prerequisite: fechar v1.0 com /gsd-complete-milestone ANTES de rodar /gsd-new-milestone
status: pending
---

# Milestone proposto: Localizacao para ingles (i18n do toolkit)

## Goal (uma frase)

Localizar o toolkit "Mentor de Aprendizado por Projeto" para ingles no nivel INTERNO
(docs, nomes de comando, adaptadores, harness) preservando todas as conexoes/invariantes,
e desacoplar a lingua interna da lingua de ENSINO -- a persona passa a ensinar o aluno em
qualquer lingua, nao so portugues.

## Versao sugerida

v2.0 (major): muda a lingua interna e RENOMEIA comandos (breaking change para quem ja usa
os comandos PT). Numeracao de fases continua a partir da 6 (proxima = Fase 7).

## Decisoes travadas pelo usuario (2026-06-17)

1. **Traduzir os nomes de comando** (SIM): `/novo-projeto` -> `/new-project`,
   `/fecha-marco` -> ex. `/close-milestone`, `/tutor` -> `/tutor` (ou `/mentor`),
   `/debug` -> `/debug`, `/spidr-split` -> `/spidr-split`. Nomes finais a definir no discuss.
   Cada renome = cascata: arquivo `mentor/<cmd>.md` + pasta `.claude/skills/<cmd>/` + tabela
   de roteamento em AGENTS.md + README + metodo.md + allowlist V-12 e set-equality V-15 do
   harness -- tudo em lockstep (medido: ~119 ocorrencias textuais dos 5 nomes fora de .planning/).

2. **Traduzir os artefatos de runtime do aluno** (SIM): `CAMINHO.md` -> `PATH.md`,
   `PROGRESSO.md` -> `PROGRESS.md`, `APRENDIZADO.md` -> ex. `LEARNINGS.md`, `aulas/` -> `lessons/`,
   `exercicios/` -> `exercises/`. Atualizar todas as citacoes nos docs + as SKIP regex do
   harness (V-13) que isentam esses nomes.

3. **Arquitetura de idioma: internos EN + ensino em QUALQUER lingua** (escolha A do usuario).
   - Lingua interna (A) = ingles: docs de `mentor/`, comandos, AGENTS.md, output-style,
     ancoras do harness viram EN (e ASCII).
   - Lingua de ensino (B) = a do aluno: a persona DETECTA/ACEITA a lingua do aluno e ensina
     nela (PT, EN, qualquer). Exige um mecanismo de "lingua do aluno" na persona/AGENTS.md
     (parametro ou deteccao na 1a interacao). Decisao de design da persona -- nova capacidade.

4. **Convencao "sem acentos" fica obsoleta para os internos** (SIM): ingles e ASCII, entao
   o check V-16 do harness passa trivialmente. NUANCE: artefatos de runtime do aluno gerados
   na lingua dele (ex.: PROGRESS.md de um aluno PT com acentos) sao OK -- vivem gitignored em
   `.projetos/<slug>/`, nao sao codigo-fonte do toolkit. O V-16 so audita `mentor/`.

## Invariantes a preservar (o que NAO pode quebrar)

- As 11 ancoras semanticas em `scripts/check-consistencia.sh` sao strings PT hardcoded
  (`backward design`, `Objetivo (capacidade)`, `auto-explicacao`, `feed-forward`,
  `mastery learning`, `Agenda de retrieval`, etc.). Traduzir um doc SEM traduzir sua ancora
  -> check vermelho. O harness e ao mesmo tempo o-que-atualizar E a rede-de-seguranca:
  apos traduzir, rodar `sh scripts/check-consistencia.sh` e consertar ate `0 fail(s)`.
- Set-equality V-15: AGENTS.md / README.md / metodo.md tem de citar EXATAMENTE o mesmo
  conjunto de 5 nomes (apos renome).
- Design fonte-unica (anti-drift) da Fase 6: adaptadores so APONTAM para `mentor/`, sem
  duplicar metodo. Manter.

## Forma sugerida (3-4 fases / waves)

1. Travar nomes finais dos comandos + artefatos + mecanismo de "lingua do aluno" (discuss).
2. Traduzir os 8 docs de `mentor/` + re-traduzir as 11 ancoras do harness em lockstep.
3. Cascata de renomeacao (comandos + artefatos: arquivos, pastas de skill, ~119 refs, harness).
4. Mecanismo de lingua de ensino na persona + re-verde do harness + relatorio de auditoria.

## Fora de escopo (candidatos)

- Manter copias bilingues PT+EN dos docs (DESCARTADO pelo usuario: dobra o drift, contradiz
  fonte-unica).
- FUT-04 (drift checker completo) continua para depois.
