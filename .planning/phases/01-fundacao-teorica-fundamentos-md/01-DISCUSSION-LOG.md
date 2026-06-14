# Phase 1: Fundacao teorica (fundamentos.md) - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-14
**Phase:** 1-Fundacao teorica (fundamentos.md)
**Areas discussed:** "Aplicado em" antecipado, Formato do catalogo, Profundidade por entrada, Ressalvas e mitos

---

## "Aplicado em <doc>" antecipado

| Option | Description | Selected |
|--------|-------------|----------|
| Forward-reference com marcador de status | Campo aponta o destino futuro com status (ex: `tutor.md (Fase 4, pendente)`); auditoria da Fase 6 confirma a aterrissagem | ✓ (via discricao) |
| So o que ja aterrissa hoje | Preenche so para frameworks ja presentes implicitamente; resto em branco ate a fase deles | |
| Tudo TBD | Todos os campos "TBD" na Fase 1; cada fase posterior volta e preenche | |

**User's choice:** "voce decide" — delegado a Claude. Abordagem adotada: forward-reference com marcador de status (D-05).
**Notes:** E a unica decisao com acoplamento cross-phase. O "done" da Fase 1 fica sendo o campo PREENCHIDO com destino+status, nao a aterrissagem verificada (essa e a Fase 6 / CONS-02). Frameworks ja presentes hoje (ex: First Principles) marcam `(ja presente)`.

---

## Formato do catalogo

| Option | Description | Selected |
|--------|-------------|----------|
| Tabela unica | Uma tabela markdown com todas as colunas; compacto e escaneavel, mas aperta as ressalvas | |
| Subsecao por framework | Cada framework e um `### Nome` em prosa; respira mais, porem mais longo | |
| Hibrido | Tabela-resumo no topo + notas curtas so onde precisa de nuance | ✓ |

**User's choice:** Hibrido (D-01).
**Notes:** Junta "escaneavel" com "espaco pra nuance onde precisa". Combina bem com a decisao de profundidade (mini-notas abaixo da tabela).

---

## Profundidade por entrada

| Option | Description | Selected |
|--------|-------------|----------|
| So o catalogo | Definicao de 1 linha + campos, nada mais; fiel ao FUND-01 | |
| Linha + mini-nota "como usamos" | Cada entrada ganha 1-2 frases de "no nosso metodo isso vira X" | ✓ |

**User's choice:** Linha + mini-nota + "como usamos" (D-02).
**Notes:** Reconciliacao registrada: a definicao continua sendo exatamente 1 linha (campo distinto, cumpre FUND-01); a mini-nota e um campo adicional curto, nao um inchaco da definicao. Doc e interno, entao um pouco mais de contexto ajuda o agente a aplicar — mas a mini-nota tem de ficar curta (anti "paredao de teoria").

---

## Ressalvas e mitos (posicionamento)

| Option | Description | Selected |
|--------|-------------|----------|
| Secoes dedicadas | "Limites e ressalvas" (SDT/Mayer) + "O que NAO usamos e por que" (mitos), separadas do catalogo | ✓ |
| Ressalvas inline, mitos em secao | Ressalva colada no framework que limita; so os mitos em secao propria | |

**User's choice:** Secoes dedicadas (D-03).
**Notes:** Usuario pediu esclarecimento sobre o que sao ressalvas vs mitos antes de decidir. Esclarecido: ressalva = limite de coisa que USAMOS (SDT relatedness fraca em solo+IA; Mayer 3-de-12 em texto puro); mito = coisa que NAO usamos por ser refutada (estilos de aprendizagem, nativos digitais, Cone de Dale, Bloom-piramide-rigida). Apos esclarecimento, escolheu secoes dedicadas.

## Claude's Discretion

- Campo "aplicado em <doc>" antecipado — delegado; resolvido como forward-reference com marcador de status (ver acima e D-05).

## Deferred Ideas

- Aterrissagem real das praticas nos docs-alvo — Fases 2-6.
- Verificacao automatizada de drift mentor/ <-> adaptadores — FUT-04 (v2).
- Productive Failure como modo opcional — FUT-02 (v2).
