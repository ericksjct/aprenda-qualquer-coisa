---
phase: 03-bootstrap-com-stage-2-novo-projeto-md
plan: 02
subsystem: docs
tags: [novo-projeto, fundamentos, backward-design, sdt, anti-evasao, hyperlink, fonte-unica]

# Dependency graph
requires:
  - phase: 03-bootstrap-com-stage-2-novo-projeto-md (plan 01)
    provides: "campo **Capacidade:** no Passo 5 / template PROGRESSO.md (base da costura backward design)"
  - phase: 01 (fundamentos.md)
    provides: "headings-fonte #frameworks-foundational-load-bearing (linha 19) e #frameworks-supporting-ancoram-um-doc (linha 41) usados como alvos de link"
provides:
  - "Passo 4 de novo-projeto.md nomeia backward design via hyperlink (Seam 1 / D-01 macro)"
  - "Passo 8 de novo-projeto.md nomeia primeiro done leve / time-to-first-success / anti-evasao via hyperlink Opcao B (Seam 3 / D-03 / ENG-02)"
affects: [fase-6-auditoria-consistencia, CONS-02]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Hyperlink de framework inline (fonte-unica): nomear o framework + linkar fundamentos.md sem reescrever teoria, imitando reference.md:97-99"
    - "Edicao 100% aditiva: nomeacao/rotulagem sobre mecanismo pre-existente, sem reescrever o mecanismo nem criar headings de secao novos"

key-files:
  created:
    - .planning/phases/03-bootstrap-com-stage-2-novo-projeto-md/03-02-SUMMARY.md
  modified:
    - mentor/novo-projeto.md

key-decisions:
  - "Passo 8 usa Opcao B: link aponta para o heading-fonte da SDT (#frameworks-supporting-ancoram-um-doc), NAO para a ressalva #sdt-relatedness-em-soloia, pois nao existe heading dedicado a time-to-first-success em fundamentos.md"
  - "fundamentos.md NAO foi editado (build-order Fase 1); so foi usado como alvo de link"
  - "Descompasso de rastreabilidade aceito: o campo 'Aplicado em <doc>' da SDT (fundamentos.md:45) lista tutor.md e PROGRESSO.md mas NAO novo-projeto.md — reconciliacao na Fase 6 (CONS-02)"

patterns-established:
  - "Costura NOMEACAO + LINK: a prosa lida pelo AGENTE pode nomear o framework e linkar fundamentos.md (sem anti-leak, pois o aluno nao le novo-projeto.md)"

requirements-completed: [EST-03, ENG-02]

# Metrics
duration: 8min
completed: 2026-06-15
---

# Phase 03 Plan 02: Costuras backward design (Passo 4) e primeiro done leve (Passo 8) em novo-projeto.md Summary

**Passo 4 de novo-projeto.md agora nomeia backward design e Passo 8 nomeia primeiro done leve / time-to-first-success / anti-evasao, ambos por hyperlink fonte-unica para fundamentos.md, sem reescrever os mecanismos existentes (engenharia reversa e Walking Skeleton).**

## Performance

- **Duration:** ~8 min
- **Started:** 2026-06-15T09:30:00Z
- **Completed:** 2026-06-15T09:37:17Z
- **Tasks:** 2
- **Files modified:** 1 (mentor/novo-projeto.md)

## Accomplishments
- Passo 4 ganha um bullet aditivo que nomeia "backward design" logo apos a engenharia reversa, com hyperlink para `fundamentos.md#frameworks-foundational-load-bearing` (alvo canonico identico ao de `reference.md:98`).
- Passo 8 ganha um paragrafo aditivo que nomeia "primeiro done leve" (com "time-to-first-success" e "anti-evasao") conectado ao Walking Skeleton, com hyperlink Opcao B para `fundamentos.md#frameworks-supporting-ancoram-um-doc`.
- Ambos os mecanismos pre-existentes (engenharia reversa no Passo 4, Walking Skeleton no Passo 8) permaneceram intactos; edicao 100% aditiva.
- `fundamentos.md` nao foi editado (so alvo de link); nenhum heading de secao novo criado; diff toca apenas `mentor/novo-projeto.md`.

## Task Commits

Each task was committed atomically:

1. **Task 1: Nomear backward design no Passo 4 (Seam 1 / D-01 macro)** - `8cefc43` (feat)
2. **Task 2: Nomear primeiro done leve no Passo 8 (Seam 3 / D-03 / ENG-02)** - `bf28fee` (feat)

**Plan metadata:** committed separately with this SUMMARY (docs).

## Files Created/Modified
- `mentor/novo-projeto.md` - Passo 4 nomeia backward design (linha ~58-60); Passo 8 nomeia primeiro done leve / time-to-first-success / anti-evasao (linha ~148-151), ambos por hyperlink para fundamentos.md.
- `.planning/phases/03-bootstrap-com-stage-2-novo-projeto-md/03-02-SUMMARY.md` - este resumo.

## Decisions Made
- **Opcao B para o link do Passo 8:** como nao existe heading dedicado a "time-to-first-success" / "primeiro done leve" em `fundamentos.md`, o conceito mora na linha SDT (`fundamentos.md:45`) sob `## Frameworks supporting (ancoram um doc)`. O link aponta para esse heading-fonte (`#frameworks-supporting-ancoram-um-doc`), NAO para a ressalva `#sdt-relatedness-em-soloia` (rejeitada). Decisao herdada da pesquisa (Open Question 1, RESOLVIDA).
- **Nao editar `fundamentos.md`:** build-order da Fase 1 manda que `fundamentos.md` seja a fonte; aqui ele e so alvo de link.
- **Ancorar a nomeacao onde o mecanismo mora** (no Passo, nao num principio geral no topo do doc) — coerente com D-03 (rejeicao de principio geral).

## Deviations from Plan

None - plan executed exactly as written. Ambas as edicoes foram aplicadas com o texto exato especificado nas tasks; todas as ancoras-alvo foram verificadas como headings reais em `fundamentos.md` antes da edicao (linhas 19 e 41).

## Issues Encountered
- A verificacao `grep` via Bash falhou inicialmente com padroes contendo `(load-bearing)` por interferencia de quoting/hook do shell (exit 1 falso-negativo). Resolvido usando a tool Grep (ripgrep) diretamente, que confirmou ambos os headings como reais (`fundamentos.md:19` e `:41`). Nenhuma alteracao de conteudo necessaria.

## Threat Surface / Rastreabilidade a Reconciliar

**Descompasso "aplicado em <doc>" da SDT (CONS-02, Fase 6):** o campo "Aplicado em (doc + status)" da linha SDT em `fundamentos.md:45` lista hoje `mentor/tutor.md`, `PROGRESSO.md` (via `mentor/reference.md`) (Fase 4, pendente) — mas NAO lista `mentor/novo-projeto.md`, apesar de o Passo 8 agora linkar e nomear o conceito da SDT. Esse descompasso e CONSCIENTE e ACEITO neste plano (a build-order proibe editar `fundamentos.md` aqui). Deve ser reconciliado na auditoria de consistencia da Fase 6 (CONS-02): incluir `mentor/novo-projeto.md` na lista "aplicado em" da SDT (e, se desejado, da entrada de backward design em `#frameworks-foundational-load-bearing`).

Sem nova superficie de seguranca: edicao de documentacao markdown estatica, sem entrada nao-confiavel, codigo, rede ou dados de usuario (consistente com o threat_model do plano — disposicoes accept/mitigate ja honradas: ancoras verificadas via grep).

## Self-Check

- FOUND: mentor/novo-projeto.md (Passo 4 backward design + Passo 8 primeiro done leve)
- FOUND: commit 8cefc43 (Task 1)
- FOUND: commit bf28fee (Task 2)
- FOUND: fundamentos.md headings #frameworks-foundational-load-bearing (linha 19) e #frameworks-supporting-ancoram-um-doc (linha 41)
- CONFIRMED: fundamentos.md nao modificado; diff toca apenas mentor/novo-projeto.md

## Next Phase Readiness
- EST-03 (Passo 4 / backward design) e ENG-02 (Passo 8 / primeiro done leve — Criterio 3 do ROADMAP) cobertos.
- Pendencia rastreada para a Fase 6 (CONS-02): atualizar o campo "aplicado em" da SDT em `fundamentos.md` para incluir `novo-projeto.md`.

---
*Phase: 03-bootstrap-com-stage-2-novo-projeto-md*
*Completed: 2026-06-15*

## Self-Check: PASSED
