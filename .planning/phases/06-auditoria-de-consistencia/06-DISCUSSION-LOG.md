# Phase 6: Auditoria de consistencia - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-16
**Phase:** 06-auditoria-de-consistencia
**Areas discussed:** Forma da auditoria, Politica de correcao, Rigor CONS-02, Rigor CONS-03, Local da verificacao CONS-02, IN-01 acentos

**Nota de comunicacao:** o usuario passou `--prd @instrucoes-fase-6.md`, mas o arquivo
era guia de COMO conversar (explicar didaticamente; distinguir fase de CONSTRUCAO do
toolkit vs etapa DIDATICA do aluno; contextualizar jargao), nao um PRD de criterios.
Rodou-se a discussao normal aplicando esse estilo.

---

## Forma da auditoria

| Option | Description | Selected |
|--------|-------------|----------|
| Relatorio unico, sem script | Agente le, roda greps na hora, produz relatorio; nada permanente. Mais leve. | |
| Script leve permanente | Script commitado (check-consistencia.sh) + relatorio; re-rodavel; ataca Risco #1 parcial. | ✓ |

**User's choice:** Script leve permanente
**Notes:** Mudanca de padrao deliberada vs Fases 2/4/5 (harness descartaveis). NAO e o FUT-04 (v2).

---

## Politica de correcao ao achar problema

| Option | Description | Selected |
|--------|-------------|----------|
| Corrige trivial inline, escala estrutural | Conserto mecanico seguro dentro da fase; estrutural vira achado mostrado antes. | ✓ |
| So reporta, nao corrige | Lista achados; fixes viram planos separados. Mais cerimonioso. | |

**User's choice:** Corrige trivial inline, escala estrutural

---

## Rigor CONS-02 (anti-cargo-cult)

| Option | Description | Selected |
|--------|-------------|----------|
| Verificacao profunda + atualizar status | Confirmar que o termo prometido aparece no doc citado; so entao flip de status. | ✓ |
| Verificacao rasa | So confirmar que o doc existe e trocar a marca. | |

**User's choice:** Verificacao profunda + atualizar status

---

## Rigor CONS-03 (anti-drift / conjunto de procedimentos)

| Option | Description | Selected |
|--------|-------------|----------|
| Igualdade de conjunto, AGENTS.md como fonte | Lista canonica = tabela AGENTS.md; README/metodo.md citam o mesmo conjunto exato. | ✓ |
| So ausencia de contradicao | Mais frouxo; cada doc pode enfatizar/omitir. | |

**User's choice:** Igualdade de conjunto, AGENTS.md como fonte

---

## Local da verificacao profunda do CONS-02 (follow-up, resolvido por token economy)

| Option | Description | Selected |
|--------|-------------|----------|
| Script faz o grep, agente confirma o sentido | Grep por teoria no script (rede mecanica) + agente confirma 1x o sentido no relatorio. | ✓ |
| Script so faz os 3 checks do CONS-03; CONS-02 e do agente | Script menor; CONS-02 so no relatorio, sem grep permanente. | |

**User's choice:** Script faz o grep, agente confirma o sentido
**Notes:** Pergunta original rejeitada pelo usuario ("quero esclarecer"); reenquadrada como
"qual decisao entrega mais com menor impacto (token economy)". Resolvido: encodar o check no
script tem custo unico baixo e torna a re-auditoria ~0 token (vs agente reler 8 docs sempre).

---

## IN-01 acentos (follow-up)

| Option | Description | Selected |
|--------|-------------|----------|
| Sim, corrigir inline (one-off) | Tirar acentos de debug.md:31-32 na Fase 6; NAO virar linter permanente. | ✓ |
| Nao, deixar de fora | Fica advisory nao-resolvido; milestone fecha com a inconsistencia. | |

**User's choice:** Sim, corrigir inline (one-off)

---

## Claude's Discretion

- Nome exato do script, estrutura de saida, texto do novo status que substitui "(Fase N, pendente)",
  e se o relatorio e arquivo proprio ou cabe na VERIFICATION.

## Deferred Ideas

- FUT-04 (verificador de drift completo) — v2.
- Linter de acentos permanente (Risco #5) — fora de escopo.
- Parametrizar raiz do repo (Risco #2) — fora de escopo.
