---
phase: 2
slug: templates-e-sintaxe-reference-md
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-06-14
---

# Phase 2 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.
>
> Esta fase e trabalho de doc/metodo (sem codigo executavel). A "validacao" e VERIFICACAO
> ESTATICA: presenca de strings, presenca de campos/secoes, e resolucao de hyperlinks contra
> os cabecalhos reais de `mentor/fundamentos.md`. Sem framework de teste de runtime.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Nenhum — verificacao estatica via `rg` (ripgrep) / `grep` + inspecao manual de link |
| **Config file** | none — ver Wave 0 (extrator de blocos cercados) |
| **Quick run command** | `rg -n "<padrao do criterio tocado>" mentor/reference.md` |
| **Full suite command** | Script de checagem estatica (Wave 0) rodado contra `mentor/reference.md` + `mentor/fundamentos.md` |
| **Estimated runtime** | ~2 segundos (grep direto) |

---

## Sampling Rate

- **After every task commit:** Run o `rg` do criterio tocado + o grep negativo anti-leak (CONS-01)
- **After every plan wave:** Run o script de checagem estatica completo (todos os comandos da tabela)
- **Before `/gsd-verify-work`:** Suite completa verde + resolucao manual de >= 1 hyperlink no renderizador-alvo
- **Max feedback latency:** ~5 segundos

---

## Per-Task Verification Map

| Req / SC | Behavior verificavel | Test Type | Automated Command (estatico) | File Exists | Status |
|----------|----------------------|-----------|------------------------------|-------------|--------|
| EST-01 / SC1 | Linha `Objetivo (capacidade):` DENTRO do bloco CAMINHO, ACIMA de `Entregavel:` | grep + ordem | `rg -n "Objetivo \(capacidade\):" mentor/reference.md` (confirmar antes de `Entregavel:` no mesmo passo) | ✅ | ⬜ pending |
| EST-01 / SC1 | `## Objetivo do passo` espelha capacidade + artefato | grep + inspecao | `rg -n "## Objetivo do passo" mentor/reference.md` + leitura do corpo | ✅ | ⬜ pending |
| EST-01 / SC1 | `DONE:` reenquadrado como evidencia de capacidade | grep | `rg -n "DONE:" mentor/reference.md` (inspecionar texto no bloco scaffold) | ✅ | ⬜ pending |
| EST-04 / SC2 | Corpo da secao L382 contem as 3 fases nomeadas (nao so o titulo) | grep | `rg -n "nos fazemos" mentor/reference.md` deve achar no CORPO | ✅ | ⬜ pending |
| EST-04 / SC2 | "nos fazemos" enquadrado como condicional (gatilho substrato/salto) | inspecao | leitura: gatilho zero-absoluto/iniciante OU salto exemplo->solo grande | ✅ | ⬜ pending |
| EST-02 / SC3 | Backward design e GRR nomeados + linkam `fundamentos.md` | grep link | `rg -n "\]\(fundamentos\.md#" mentor/reference.md` retorna >= 2 links | ✅ | ⬜ pending |
| CARGA-01 / SC4 | Fading nomeado (expertise-reversal) na secao de substrato (Z1/Z2) | grep | `rg -n "recua\|expertise-reversal\|suporte demais" mentor/reference.md` | ✅ | ⬜ pending |
| CARGA-02 / SC4 | Worked example analogo (instancia diferente) no "eu faco" (Z6/Z4) | grep | `rg -n "instancia diferente\|exemplo resolvido" mentor/reference.md` | ✅ | ⬜ pending |
| CARGA-03 / SC5 | 3 principios de Mayer + limite honesto + link, em "Regras da aula" | grep | `rg -n "coerencia\|sinalizacao\|segmentacao\|3 de 12" mentor/reference.md` | ✅ | ⬜ pending |
| CONS-01 (anti-leak) | NENHUM jargao de framework DENTRO de bloco cercado | grep negativo | extrair blocos ` ``` ` e confirmar 0 ocorrencias de `Bloom\|backward design\|GRR\|Mayer\|expertise-reversal\|constructive alignment\|cognitive load` | ✅ | ⬜ pending |
| EST-02 (link resolve) | Cada `fundamentos.md#ancora` aponta a um cabecalho real | resolucao de ancora | extrair ancoras e cruzar com `rg -n "^#" mentor/fundamentos.md` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky · File Exists ✅ porque a fase EDITA arquivos existentes (zero Wave 0 de criacao de codigo).*

---

## Wave 0 Requirements

- [ ] Nenhum arquivo de teste de runtime aplicavel (doc/metodo).
- [ ] **Extrator de blocos cercados** para a verificacao anti-leak (CONS-01): isolar o conteudo
  dentro de ` ``` ` e rodar o grep negativo so nesse subconjunto. Sem ele, o grep negativo daria
  falso-positivo (acharia "backward design" na prosa LEGITIMA do `reference.md`). Este e o unico
  utilitario nao-trivial da fase.
- [ ] Recomendado (opcional): consolidar os comandos da tabela num pequeno script `bash`/`rg` como
  "smoke test" reproduzivel do gate da fase.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Resolucao de hyperlink no renderizador-alvo | EST-02 / D-04 | Anchor slug depende do renderizador (GitHub web vs VS Code vs leitura raw do agente) | Abrir `mentor/reference.md` no renderizador-alvo e clicar em >= 1 link `fundamentos.md#...`; confirmar que salta ao cabecalho certo |
| "nos fazemos" como etapa REAL e condicional | EST-04 / SC2 | A condicionalidade (gatilho de substrato/salto) e semantica, nao grep-avel | Ler o corpo da secao L382 reescrita e confirmar que "nos fazemos" e pratica conjunta guiada, ligada por gatilho |

---

## Validation Sign-Off

- [ ] Todos os 5 Criterios de Sucesso tem comando `rg` automatizado OU verificacao manual mapeada
- [ ] Sampling continuity: grep negativo anti-leak roda a CADA commit que toca bloco cercado
- [ ] Wave 0 cobre o extrator de blocos cercados (unica dependencia de verificacao)
- [ ] Sem watch-mode flags (verificacao e one-shot)
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
