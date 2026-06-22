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

<!-- Entregue no marco v1.0 (Ancoragem em ciencia da aprendizagem) — 21/21 requisitos. -->

- ✓ **Dim. Estrutura & objetivos** — verbo de capacidade (Objetivo) no CAMINHO, backward design
  e GRR de 3 fases nomeados em `reference.md`/`novo-projeto.md` — v1.0
- ✓ **Dim. Engajamento & retenção** — "próxima ação única" no `tutor.md`/`PROGRESSO.md` e
  "primeiro done leve" anti-evasão ligado ao Walking Skeleton — v1.0
- ✓ **Dim. Avaliação & feedback** — mastery gate com síntese/transferência, retrieval ativo na
  abertura, revisão espaçada e feedback tri-partido de Hattie no `debug.md` — v1.0
- ✓ **Dim. Carga cognitiva & acessibilidade** — fading por substrato, worked example análogo e
  os 3 princípios de Mayer que transferem para texto em `reference.md` — v1.0
- ✓ **Doc de fundação** — `mentor/fundamentos.md` catalogando 6+6 frameworks com fontes,
  vocabulário do método, "aplicado em <doc>" e mitos refutados — v1.0
- ✓ **Tecer nos docs existentes** — práticas embutidas em `metodo.md`, `reference.md`,
  `novo-projeto.md`, `tutor.md`, `fecha-marco.md`, `debug.md` — v1.0
- ✓ **Anti-drift mecânico** — `scripts/check-consistencia.sh` verifica anti-cargo-cult +
  anti-drift dos adaptadores a cada execução (fecha o concern #1 do mapa de codebase) — v1.0

<!-- Entregue no marco v2.0 (em andamento) -->

- ✓ **Ingestao de livro-base (PDF -> markdown)** — CLI Python opt-in `scripts/converte_livro.py`
  (docling) converte o PDF do livro do aluno em markdown por capitulo, page-anchored
  (`<!-- page: N -->`), sob `.projetos/<slug>/livro/`; deps isoladas (`requirements-pdf.txt`),
  slug sanitizado anti-traversal, suite pytest. O mentor consome `livro/` como literatura-base
  no bootstrap (`novo-projeto.md` Passo 3b) e na tutoria (`tutor.md`: baseline + referencia de
  pagina + protocolo de divergencia datado em `APRENDIZADO.md`). Skill `/converte-livro` e
  harness reconciliado — Validado na Phase 7 — v2.0

### Active

<!-- Proximo marco v2.0: localizacao / i18n do toolkit (pre-escopado). Escopo concreto
     sera recortado em REQUIREMENTS.md via /gsd-new-milestone apos a pesquisa. -->

- [ ] **v2.0 — Localização (i18n)** — tornar o método/adaptadores utilizáveis em mais de um
  idioma sem quebrar fonte-única nem agnosticismo de LLM (escopo a definir)
- [ ] **FUT-04 carregado** — o anti-drift mecânico (`check-consistencia.sh`) já cobre o concern
  #1; avaliar estendê-lo conforme novos docs/idiomas entrarem
- [ ] **Backlog v2 (FUT-01/02/03/05)** — interleaving, modo "tente antes" (Productive Failure,
  validar evidência), desafio opcional (SDT) e rubrica reutilizável de curadoria

### Out of Scope

- **Código de aplicação / runtime novo** — o toolkit é markdown + 1 script; este milestone
  não cria software executável
- **Quebrar o agnosticismo de LLM** — nada que acople o método a um provedor específico
- **Duplicar conteúdo nos adaptadores** — o design fonte-única é inegociável; práticas
  entram em `mentor/`, não copiadas em `.claude/` ou `AGENTS.md`
- **Plataforma/LMS, vídeo, hospedagem de curso** — "curso online assíncrono" aqui é a
  fonte de boas práticas pedagógicas, não a construção de uma plataforma

## Context

- **Estado pós-v1.0:** toolkit brownfield (markdown + scripts), ~1.412 linhas em `mentor/`,
  método ancorado em ciência da aprendizagem em todos os 7 docs. Mapa em `.planning/codebase/`
  (7 docs) — releia `ARCHITECTURE.md`/`STRUCTURE.md` antes de mudanças.
- Idioma do repo: **docs internos do agente** (`mentor/`, `fundamentos.md`, `.planning/`,
  `AGENTS.md`, `README.md`) em português **sem acentos** (robustez de encoding); manter o
  padrão ao editá-los. **Artefatos que vão para o aluno** (`.projetos/<slug>/`: `CAMINHO.md`,
  `PROGRESSO.md`, `APRENDIZADO.md`, aulas, scaffolds) usam **português acentuado correto**
  (ver "Idioma e acentuacao" em `mentor/reference.md`).
- Concern #1 do mapa (drift `mentor/`↔adaptadores) **RESOLVIDO** em v1.0:
  `scripts/check-consistencia.sh` é o gate mecânico permanente (anti-cargo-cult + anti-drift).
- Risco de execução: o agente pode não aplicar o método (persona não ativada). Reforçar
  boas práticas como instruções verificáveis ajuda a mitigar.

## Constraints

- **Tech stack**: Markdown neutro em `mentor/` é a fonte única; adaptadores apontam por
  caminho relativo — não mover pastas de topo sem atualizar ponteiros
- **Arquitetura**: preservar fonte-única + adaptadores finos + agnosticismo de LLM
- **Idioma/estilo**: docs internos do agente em português sem acentos; artefatos do aluno
  (`.projetos/`) em português acentuado correto; paths e identificadores em backticks
- **Processo**: nenhuma mudança em arquivos antes da pesquisa + requisitos aprovados

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Ancorar o método em fundação reconhecida (vs. método caseiro) | Dor principal relatada: falta autoridade e completude | ✓ Good — entregue em v1.0 (`fundamentos.md` + tecido nos docs) |
| Cobrir as 4 dimensões (estrutura, engajamento, avaliação, carga cognitiva) | Usuário marcou todas como relevantes | ✓ Good — todas as 4 validadas em v1.0 |
| Aberto a reestruturar a espinha se a pesquisa justificar | Usuário não quer travar conceitos centrais se houver organização melhor | ✓ Good — identidade preservada (ensinar-construindo, agnóstico de LLM); ancoragem feita por overlay, sem reescrever a espinha |
| Forma: `mentor/fundamentos.md` novo + tecer nos docs existentes | Mantém fonte-única e dá um catálogo rastreável de fontes | ✓ Good — fonte-única preservada; auditoria de consistência verde |
| Pesquisa-primeiro antes de definir requisitos/"done" | "Done" indefinido; práticas de mercado guiam o recorte | ✓ Good — pesquisa guiou os 21 requisitos v1, todos satisfeitos |
| Harness mecânico permanente (`check-consistencia.sh`) como gate anti-drift | Concern #1 do mapa de codebase: drift `mentor/`↔adaptadores não tinha verificação | ✓ Good — codifica anti-cargo-cult + anti-drift; roda da raiz, exit 0 |

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
*Last updated: 2026-06-22 — Phase 7 (Ingestao de PDF via docling) COMPLETE (3/3 planos, 19/19 must-haves): o aluno converte um PDF do livro-base em markdown por capitulo page-anchored sob `.projetos/<slug>/livro/` via CLI opt-in, e o mentor consome `livro/` no bootstrap e na tutoria. Primeira entrega do marco v2.0. — v1.0 "Ancoragem em ciencia da aprendizagem" SHIPPED. 6 fases, 16 planos, 21/21 requisitos satisfeitos (auditoria 3 fontes). O método deixou de ser caseiro: ganhou `fundamentos.md` (catálogo de frameworks com fontes) tecido em todos os docs de `mentor/`, mais um harness mecânico permanente (`check-consistencia.sh`) que fecha o concern #1 de drift. Próximo marco: v2.0 (localização/i18n) — definir via `/gsd-new-milestone`.*
