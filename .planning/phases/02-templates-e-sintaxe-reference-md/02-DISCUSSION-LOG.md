# Phase 2: Templates e sintaxe (reference.md) - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-14
**Phase:** 2-Templates e sintaxe (reference.md)
**Areas discussed:** Campo Objetivo (capacidade), Sintaxe GRR 3 fases, Carga (fading + worked example), Mayer + citacao de fundamentos.md

---

## Campo "Objetivo" (capacidade) — EST-01

| Option | Description | Selected |
|--------|-------------|----------|
| Linha por passo | Linha `Objetivo (capacidade)` por passo no CAMINHO.md | ✓ (Claude, delegado) |
| Coluna | Coluna numa tabela de passos | |
| So no DONE | So reenquadrar o DONE do scaffold | |

**User's choice:** "1. decida por mim." — delegado a Claude.
**Notes:** Claude escolheu linha nova `Objetivo (capacidade):` ACIMA de `Entregavel:`
(ordem backward design), espelhada na aula e no DONE do scaffold. Anti-leak: dentro dos
templates so o verbo puro, sem rotulo "Bloom".

---

## Sintaxe GRR de 3 fases — EST-04

| Option | Description | Selected |
|--------|-------------|----------|
| Reescrever secao existente | Reescrever "Sintaxe nova de verdade" (titulo ja tem 3 fases, corpo so 2) | ✓ |
| Campo novo no scaffold | Adicionar campo "nos fazemos" separado no formato do scaffold | |

**User's choice:** "2. reescreva"
**Notes:** "nos fazemos" vira etapa real e CONDICIONAL (pratica conjunta guiada) entre o
exemplo resolvido e o TODO solo. Gatilho: zero-absoluto/iniciante OU salto grande; pula
para intermediario/avancado.

---

## Carga cognitiva: fading + worked example — CARGA-01, CARGA-02

| Option | Description | Selected |
|--------|-------------|----------|
| Forma de agente (regra mecanica) | Regras de calibragem otimizadas para o agente consumir | ✓ |
| Forma de aluno (prosa) | Texto explicativo voltado ao aluno | |

**User's choice:** "3. isso e mais importante para o tutor do que o aluno certo?
instrucao pra ele ne? portanto escolha o que funcionar melhor com agentes."
**Notes:** Confirmado: e instrucao de agente. Fading = tabela substrato->densidade de
andaime (expertise-reversal nomeado). Worked example FUNDE no "eu faco" do GRR (D-02),
sem duplicar.

---

## Mayer + citacao de fundamentos.md — CARGA-03, EST-02

| Option | Description | Selected |
|--------|-------------|----------|
| Hyperlink markdown | `[framework](fundamentos.md#ancora)` na prosa | ✓ |
| Parentese inline plain | `(backward design — ver fundamentos.md)` | |
| Secao-rodape | Bloco "Fundamentos aplicados" no fim do doc | |

**User's choice:** "4. cita em hyperlink do markdown, desse jeito fica mais facil para
humanos navegarem tambem"
**Notes:** Hyperlink relativo (mesmo diretorio mentor/). Mayer: 3 principios
(coerencia/sinalizacao/segmentacao) + linguagem simples como regra de agente nas "Regras
da aula", com ressalva honesta 3-de-12 e link para fundamentos.md.

## Claude's Discretion

- D-01 (campo Objetivo) delegado integralmente.
- Ancoras exatas dos hyperlinks dependem da estrutura de cabecalhos do fundamentos.md da Fase 1.

## Deferred Ideas

- Campo de agenda de retrieval no PROGRESSO.md (pertence a Fase 4, nao a Fase 2).
- Confirmacao final do status "(Fase 2, pendente)" no fundamentos.md (auditoria Fase 6).
- Productive Failure / modo tente-antes (FUT-02, v2).
