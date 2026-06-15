---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: executing
last_updated: "2026-06-15T22:25:30.714Z"
last_activity: 2026-06-15
progress:
  total_phases: 6
  completed_phases: 3
  total_plans: 6
  completed_plans: 6
  percent: 100
---

# Project State

## Current Position

Phase: 4
Plan: Not started
Status: Executing Phase 03
Last activity: 2026-06-15

## Project Reference

See: `.planning/PROJECT.md` (updated 2026-06-13)

**Core value:** O agente ensina a construir (aluno sai capaz de explicar e estender o projeto sozinho), ancorado em ciência da aprendizagem reconhecida — nunca resolve pelo aluno.
**Current focus:** Phase 03 — bootstrap-com-stage-2-novo-projeto-md

## Accumulated Context

- Projeto brownfield: o toolkit "Mentor de Aprendizado por Projeto" já existe e está
  mapeado em `.planning/codebase/`. Este milestone edita docs de `mentor/`, não cria
  software.

- **Build order inegociável** (fonte-única → evita drift semântico):
  `fundamentos.md` → `reference.md` → `novo-projeto.md` → (`fecha-marco.md` + `tutor.md`)
  → (`metodo.md` + `debug.md`) → auditoria de consistência. Reflete nos Depends-on do roadmap.

- **Decisão de setup:** NÃO foi gerado `CLAUDE.md` de instrução GSD. O repo ignora
  `CLAUDE.md` no `.gitignore` e usa `AGENTS.md` para a persona mentor; um CLAUDE.md GSD
  aplicaria regras de workflow a sessões de tutoria (conflito). Contexto GSD vive só em
  `.planning/`.

- **Estilo dos deliverables:** arquivos de `mentor/` em português SEM acentos (robustez de
  encoding); paths/identificadores em backticks. Manter o padrão ao editar.

- **Anti-drift / anti-cargo-cult:** toda prática nova em `fundamentos.md` precisa de
  "aplicado em <doc>" verificável; teoria nunca vaza para a sessão do aluno; nada de
  conteúdo de método duplicado nos adaptadores (`.claude/`, `AGENTS.md`).

- Pesquisa em `.planning/research/` (SUMMARY.md é o doc decision-ready). Confiança HIGH
  nos frameworks; MEDIUM nas escolhas exatas de costura — validar leveza na execução
  (esp. Stage 2 do bootstrap e a pergunta de retrieval no tutor).
