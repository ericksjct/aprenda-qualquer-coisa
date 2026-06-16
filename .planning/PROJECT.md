# Mentor de Aprendizado por Projeto

## What This Is

Um toolkit agnóstico de LLM que faz um agente de IA atuar como **mentor de aprendizado
por projeto**: em vez de escrever o código pelo aluno, ele projeta um caminho de curso,
escreve a teoria mínima de cada passo e conduz o aluno a preencher lacunas `TODO(human)`.
O método vive em markdown neutro (`mentor/`) consumido por Claude Code, Codex CLI, Kimi,
Cursor e outros via adaptadores finos. O público é qualquer pessoa — inclusive iniciante
absoluto — que queira aprender a construir algo real.

## Core Value

O agente deve **ensinar a construir** (aluno sai capaz de explicar e estender o projeto
sozinho), nunca resolver pelo aluno — agora **ancorado em ciência da aprendizagem
reconhecida**, não em método caseiro.

## Requirements

### Validated

<!-- Inferido do mapa de codebase (.planning/codebase/) — o toolkit já existe e funciona. -->

- ✓ Arquitetura fonte-única + adaptadores finos: método em `mentor/`, adaptadores em
  `.claude/` e `AGENTS.md` que só apontam (sem duplicar conteúdo) — existing
- ✓ Persona/conduta permanente com regra de ouro `TODO(human)` (`mentor/metodo.md`) — existing
- ✓ Roteamento por situação → procedimento (`AGENTS.md`: novo-projeto/tutor/fecha-marco/
  debug/spidr-split) — existing
- ✓ Bootstrap em 2 passes (caminho completo → marcos) com sondagem de substrato e gate
  de aprovação (`mentor/novo-projeto.md`) — existing
- ✓ Espinha pedagógica: substrato por assunto, marcos verticais, walking skeleton, drill
  condicional, aula por passo, protocolo de forense — existing
- ✓ Templates e regras centralizados (`mentor/reference.md`) — existing
- ✓ Agnosticismo de LLM (mesmo método em múltiplas ferramentas) — existing
- ✓ Script opcional de referência de roadmap (`scripts/roadmap_fetch.py`, stdlib) — existing

### Active

<!-- Milestone atual: ancorar o método em fundação reconhecida de design instrucional
     e boas práticas de cursos online assíncronos, nas 4 dimensões. Hipóteses até
     entregues; escopo concreto será recortado em REQUIREMENTS.md após a pesquisa. -->

- [ ] **Dim. Estrutura & objetivos** — o método ancora estrutura/sequenciamento em design
  instrucional reconhecido (ex: backward design, objetivos de aprendizagem mensuráveis,
  Bloom) e aplica isso ao CAMINHO/marcos
- [ ] **Dim. Engajamento & retenção** — o método trata a evasão característica do async
  (motivação, microlearning, ritmo, senso de progresso) com práticas fundamentadas
- [ ] **Dim. Avaliação & feedback** — o método ancora "done"/curadoria/diário em
  avaliação formativa, mastery learning, retrieval practice e repetição espaçada
- [ ] **Dim. Carga cognitiva & acessibilidade** — apresentação de aula/scaffold ancorada
  em Cognitive Load Theory, princípios multimídia (Mayer) e design inclusivo
- [ ] **Doc de fundação** — novo `mentor/fundamentos.md` catalogando as práticas adotadas
  com fontes, traduzidas para o vocabulário do método
- [ ] **Tecer nos docs existentes** — aplicações concretas das práticas embutidas em
  `metodo.md`, `reference.md`, `novo-projeto.md`, `tutor.md`, `fecha-marco.md`, `debug.md`
  (checklists e templates atualizados)

### Out of Scope

- **Código de aplicação / runtime novo** — o toolkit é markdown + 1 script; este milestone
  não cria software executável
- **Quebrar o agnosticismo de LLM** — nada que acople o método a um provedor específico
- **Duplicar conteúdo nos adaptadores** — o design fonte-única é inegociável; práticas
  entram em `mentor/`, não copiadas em `.claude/` ou `AGENTS.md`
- **Plataforma/LMS, vídeo, hospedagem de curso** — "curso online assíncrono" aqui é a
  fonte de boas práticas pedagógicas, não a construção de uma plataforma

## Context

- Toolkit brownfield já mapeado em `.planning/codebase/` (7 docs). Releia
  `ARCHITECTURE.md` e `STRUCTURE.md` antes de planejar mudanças.
- Idioma do repo: português, predominantemente **sem acentos** (escolha de robustez de
  encoding). Manter o padrão ao editar.
- Concern aberto do mapa (#1): **drift** entre `mentor/` e adaptadores não tem verificação
  automatizada — relevante porque este milestone vai mexer em vários docs de `mentor/`.
- Risco de execução: o agente pode não aplicar o método (persona não ativada). Reforçar
  boas práticas como instruções verificáveis ajuda a mitigar.

## Constraints

- **Tech stack**: Markdown neutro em `mentor/` é a fonte única; adaptadores apontam por
  caminho relativo — não mover pastas de topo sem atualizar ponteiros
- **Arquitetura**: preservar fonte-única + adaptadores finos + agnosticismo de LLM
- **Idioma/estilo**: português sem acentos; paths e identificadores em backticks
- **Processo**: nenhuma mudança em arquivos antes da pesquisa + requisitos aprovados

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Ancorar o método em fundação reconhecida (vs. método caseiro) | Dor principal relatada: falta autoridade e completude | — Pending |
| Cobrir as 4 dimensões (estrutura, engajamento, avaliação, carga cognitiva) | Usuário marcou todas como relevantes | — Pending |
| Aberto a reestruturar a espinha se a pesquisa justificar | Usuário não quer travar conceitos centrais se houver organização melhor | ⚠️ Revisit (proteger identidade do produto: ensinar-construindo, agnóstico de LLM) |
| Forma: `mentor/fundamentos.md` novo + tecer nos docs existentes | Mantém fonte-única e dá um catálogo rastreável de fontes | — Pending |
| Pesquisa-primeiro antes de definir requisitos/"done" | "Done" indefinido; práticas de mercado guiam o recorte | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-06-16 — Phase 5 complete (persona/feedback: `metodo.md` fixa a regra anti-theory-leak + check formativo de auto-explicacao no gate de curadoria e nomeia gate/retrieval/GRR por link aos docs donos; `debug.md` ganhou overlay tri-partido de Hattie (feed-up/back/forward) sobre os 6 passos preservados, com a PISTA enquadrada como feed-forward que nao entrega a resposta). Satisfaz AVAL-05, AVAL-06, CONS-01 — avanca a dim. Avaliacao & feedback. Verifier 4/4 + aval humano (navegacao dos links + tom editorial). Resta so a Phase 6 (auditoria de consistencia) para fechar o milestone v1.0. Antes: Phase 3 complete (bootstrap em `novo-projeto.md` ganhou evidencia de maestria por marco: campo `**Capacidade:**` no template PROGRESSO.md + instrucao no Passo 5, e nomeacao de backward design (Passo 4) e "primeiro done leve" anti-evasao (Passo 8), ambos linkando `fundamentos.md`). Avanca as dims. Estrutura & objetivos e Engajamento & retencao; `novo-projeto.md` feito dentro de "Tecer nos docs existentes". Antes: Phase 2 complete (templates de `reference.md` — verbo de capacidade, GRR 3 fases, fading/worked-example, Mayer).*
