---
phase: 3
slug: bootstrap-com-stage-2-novo-projeto-md
status: approved
nyquist_compliant: true
wave_0_complete: false
created: 2026-06-14
---

# Phase 3 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.
> Dominio = edicao de prosa markdown (`mentor/novo-projeto.md` + `mentor/reference.md`).
> Nao ha suite de testes unitarios; a validacao e revisao de propriedades verificaveis
> por `grep`/leitura, mais o smoke-test estatico anti-leak herdado da Fase 2.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Nenhum framework de teste de markdown no repo (so `scripts/roadmap_fetch.py`, Python stdlib) |
| **Config file** | none |
| **Quick run command** | `grep -n "<termo-alvo>" mentor/novo-projeto.md` + checar ancora de link existe em `fundamentos.md` |
| **Full suite command** | Revisao dos 3 Criterios de Sucesso do ROADMAP contra o doc editado + extrator de blocos cercados / smoke-test anti-leak da Fase 2 sobre `reference.md` |
| **Estimated runtime** | ~30 segundos (grep + leitura) |

---

## Sampling Rate

- **After every task commit:** `grep` dos termos-alvo da Req->Test Map + checar que as ancoras de link existem em `fundamentos.md`.
- **After every plan wave:** Revisao dos 3 Criterios de Sucesso do ROADMAP contra o doc editado.
- **Before `/gsd-verify-work`:** Os 3 criterios do ROADMAP verdadeiros + nenhum jargao no bloco lido pelo aluno (smoke-test anti-leak verde).
- **Max feedback latency:** 30 segundos.

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 3-template | 01 | 1 | EST-03 | — / — | N/A | grep | `grep -n "Capacidade:" mentor/reference.md` | ❌ W0 | ⬜ pending |
| 3-passo4 | — | — | EST-03 | — / — | N/A | grep | `grep -n "backward design" mentor/novo-projeto.md` + ancora existe em `fundamentos.md` | ❌ W0 | ⬜ pending |
| 3-passo5 | — | — | EST-03 | — / — | N/A | leitura | revisao manual: Passo 5 instrui gravar frase de capacidade por marco | ❌ W0 | ⬜ pending |
| 3-guardrail | — | — | EST-03 | — / — | N/A | grep | `grep -n "exatamente 1 frase" mentor/novo-projeto.md` | ❌ W0 | ⬜ pending |
| 3-passo8 | — | — | ENG-02 | — / — | N/A | grep | `grep -n "primeiro done leve" mentor/novo-projeto.md` | ❌ W0 | ⬜ pending |
| 3-antileak | — | — | CONS-01 | — / — | Nenhum jargao de framework no template/exemplo de `PROGRESSO.md` (frase = verbo puro) | smoke-test estatico (Fase 2) | extrator de blocos cercados sobre `reference.md` | ✅ (reusa Fase 2) | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

*Task IDs definitivos serao atribuidos pelo planner; a coluna mapeia a propriedade verificavel, nao a numeracao final.*

---

## Wave 0 Requirements

- [ ] Nenhum teste automatizado NOVO necessario (dominio de prosa).
- [ ] O smoke-test anti-leak da Fase 2 (extrator de blocos cercados sobre `reference.md`) ja existe e cobre o risco principal: jargao em bloco lido pelo aluno.
- [ ] Opcional (se o planner quiser automacao): um `grep`-check dos 6 termos-alvo da Per-Task Verification Map — nao requer framework.

*Existing infrastructure (smoke-test Fase 2) cobre o requisito anti-leak; demais requisitos sao verificaveis por `grep`/leitura sem novo Wave 0.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Passo 5 instrui gravar a frase de capacidade por marco no `PROGRESSO.md`, colada a User Story | EST-03 | Semantica de prosa — `grep` confirma presenca do texto mas nao a coerencia da instrucao | Ler Passo 5: a instrucao manda o agente escrever 1 frase de capacidade junto da User Story de cada marco, no formato verbo-capacidade |
| Stage 2 e visivelmente leve (1 frase/marco, nao sub-doc) | EST-03 (Criterio 2) | Julgamento de leveza nao e grep-avel | Conferir que nenhuma rubrica/lista/sub-doc foi introduzida; guardrail D-04 presente |
| Link do Passo 8 (ENG-02) aponta para ancora real em `fundamentos.md` | ENG-02 | Decisao de alvo (Open Question 1 da pesquisa) resolvida no plano | Confirmar a ancora escolhida existe como heading em `fundamentos.md`; se "so nomear sem link", registrar |

---

## Validation Sign-Off

- [x] Todas as tarefas tem verificacao `grep`/leitura (auto-contidas; nao dependem da Fase 2 ter rodado)
- [x] Sampling continuity: cada tarefa tem ao menos um criterio verificavel por leitura
- [x] Wave 0 cobre o requisito anti-leak via grep scoped na secao `## Marcos` — sem gaps MISSING
- [x] Nenhuma ancora de link quebrada em `fundamentos.md` (ambas verificadas pelo plan-checker: linhas 19 e 41)
- [x] Feedback latency < 30s
- [x] `nyquist_compliant: true` set in frontmatter

**Approval:** approved 2026-06-14 (plan-checker PASSED; warnings 1-3 resolvidas no plano)
