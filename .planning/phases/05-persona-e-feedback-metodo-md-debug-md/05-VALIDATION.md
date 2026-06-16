---
phase: 5
slug: persona-e-feedback-metodo-md-debug-md
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-06-15
---

# Phase 5 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.
> DOC-EDITING phase: no runtime / no test framework. Validation = static grep
> (presence / absence + ANCHOR-RESOLVE + anti-leak on fenced blocks), cloned
> verbatim from the Phase 2 and Phase 4 harness. Full check map in 05-RESEARCH.md
> §Validation Architecture (V-01..V-18).

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | None — `rg`/`awk`/`sh` via `check-phase5.sh` + `extract-fenced.sh` |
| **Config file** | None — `extract-fenced.sh` cloned into Phase 5 `scripts/` dir (Wave 0) |
| **Quick run command** | `rg -n "<padrao do criterio tocado>" mentor/<file>.md` |
| **Full suite command** | `sh .planning/phases/05-persona-e-feedback-metodo-md-debug-md/scripts/check-phase5.sh` |
| **Estimated runtime** | ~2 seconds |

---

## Sampling Rate

- **After every task commit:** Run `rg` for the touched criterion + anti-leak grep when a fenced block is touched
- **After every plan wave:** Run `sh scripts/check-phase5.sh` + the ANCHOR-RESOLVE checks
- **Before `/gsd-verify-work`:** Full suite green + 1 manual click on the GRR link (confirms fragile slug A1)
- **Max feedback latency:** ~2 seconds

---

## Per-Task Verification Map

| Check ID | Req / SC | Behavior | Test Type | Automated Command (static) | File Exists |
|----------|----------|----------|-----------|----------------------------|-------------|
| V-01 | CONS-01 / SC1 | corpo de `metodo.md` declara regra anti-leak + link `fundamentos.md` | grep | `rg -n "fundamentos\.md" mentor/metodo.md` | ❌ W0 |
| V-02 | CONS-01 / SC1 | regra nomeia "nunca ao aluno / jargao" no corpo | grep | `rg -n "jargao\|nunca .*ao aluno\|nunca .*citad" mentor/metodo.md` | ❌ W0 |
| V-03 | CONS-01 / D-02 | FUND-03 (doc interno, nunca lido pelo aluno) no mesmo lugar | grep | `rg -n "interno\|nunca .*lido pelo aluno\|injetad" mentor/metodo.md` | ❌ W0 |
| V-04 | CONS-01 / D-01 | espelho na lista "Anti-padroes (NUNCA faca)" | grep | `rg -n "jargao.*aluno\|framework.*aluno" mentor/metodo.md` | ❌ W0 |
| V-05 | AVAL-05 / SC2 | novo passo de auto-explicacao no gate de curadoria | grep | `rg -n "auto-explicacao\|me explica por que" mentor/metodo.md` | ❌ W0 |
| V-06 | AVAL-05 / D-04 | guardrail literal "exatamente 1 pergunta / nao rubrica" | grep | `rg -n "exatamente 1\|checklist ou rubrica\|esta errado" mentor/metodo.md` | ❌ W0 |
| V-07 | AVAL-05 / D-04 | nota de fronteira aponta `fecha-marco.md` | grep | `rg -n "fecha-marco" mentor/metodo.md` | ❌ W0 |
| V-08 | AVAL-06 / SC3 | 3 lentes de Hattie nomeadas em `debug.md` | grep | `rg -c "feed-up\|feed-back\|feed-forward" mentor/debug.md` (>= 3) | ❌ W0 |
| V-09 | AVAL-06 / D-06 | PISTA enquadrada como feed-forward (sem dar a resposta) | grep | `rg -n "PISTA.*feed-forward\|feed-forward.*PISTA" mentor/debug.md` | ❌ W0 |
| V-10 | AVAL-06 / D-05 | os 6 passos PRESERVADOS (overlay, nao reescrita) | grep order | `rg -c "^### [1-6]\." mentor/debug.md` (== 6) | ❌ W0 |
| V-11 | C4 / D-09 | ciclo linka GRR -> `reference.md` | grep | `rg -n "reference\.md" mentor/metodo.md` | ❌ W0 |
| V-12 | C4 / D-09 | ciclo linka retrieval -> `tutor.md` | grep | `rg -n "tutor\.md\|/tutor" mentor/metodo.md` | ❌ W0 |
| V-13 | C4 / D-09 | ciclo linka gate -> `fecha-marco.md` | grep | `rg -n "fecha-marco\.md\|/fecha-marco" mentor/metodo.md` | ❌ W0 |
| V-14 | C4 / D-08 | os 5 itens do ciclo PRESERVADOS (inline, nao bloco novo) | grep | `rg -c` na secao "Conduta por marco (ciclo)" (== 5) | ❌ W0 |
| V-15 | D-07 | `metodo.md` mantem ponteiro curto p/ /debug nomeando "feedback tri-partido" | grep | `rg -n "feedback tri-partido" mentor/metodo.md` + `rg -n "/debug\|debug\.md"` | ❌ W0 |
| V-16 | ANCHOR-RESOLVE | cada doc linkado por D-09 casa heading real no dono | anchor | `rg -q '^### Sintaxe nova de verdade' mentor/reference.md` AND `rg -q '^## Passo 1 — Recuperacao ativa' mentor/tutor.md` AND `rg -q '^## Passo 1 — Mastery gate' mentor/fecha-marco.md` | ❌ W0 |
| V-17 | CONS-01 (anti-leak) | nenhum jargao DENTRO de bloco cercado de `metodo.md`/`debug.md` | grep negative | `sh scripts/extract-fenced.sh mentor/metodo.md \| rg -c "<LEAK_PAT>"` -> 0; idem `debug.md` | ❌ W0 |
| V-18 | P12 anti-drift | jargao novo (Hattie/feed-*/formativo) NAO vaza p/ adaptadores | grep negative | `rg -c "feed-up\|feed-back\|Hattie" AGENTS.md .claude/` -> 0 | ❌ W0 |

*Status: ⬜ pending · ✅ green · ❌ red*

---

## Wave 0 Requirements

- [ ] `scripts/extract-fenced.sh` — clonado verbatim do harness das Fases 2/4 (extrai blocos cercados ``` para rodar o anti-leak so no conteudo do aluno)
- [ ] `scripts/check-phase5.sh` — runner estatico que executa V-01..V-18 e sai 0/1

*Sem framework de teste a instalar — a fase nao tem runtime.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Link GRR resolve para o heading certo em `reference.md` | C4 / D-09 | Slug A1 fragil (`:`, aspas, `->` no heading) — o `#slug` exato do renderer nao e previsivel por grep | Abrir `metodo.md` renderizado, clicar no link do GRR, confirmar que aterrissa na secao "Sintaxe nova de verdade" de `reference.md` |

---

## Validation Sign-Off

- [ ] Todas as tarefas tem verify estatico (`rg`) ou dependencia de Wave 0
- [ ] Continuidade de amostragem: sem 3 tarefas seguidas sem verify automatizado
- [ ] Wave 0 cobre os scripts MISSING (`extract-fenced.sh`, `check-phase5.sh`)
- [ ] Sem flags de watch-mode
- [ ] Latencia de feedback < 5s
- [ ] `nyquist_compliant: true` no frontmatter

**Approval:** pending
