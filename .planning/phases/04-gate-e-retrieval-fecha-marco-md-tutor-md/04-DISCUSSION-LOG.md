# Phase 4: Gate e retrieval (fecha-marco.md + tutor.md) - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-15
**Phase:** 4-gate-e-retrieval-fecha-marco-md-tutor-md
**Areas discussed:** Retrieval na abertura (tutor), Mastery gate + sintese/transferencia (fecha-marco), Agenda de revisao espacada, Proxima acao unica + ancora SDT

> O usuario optou por "passar por cada item de forma simples e didatica" — todas as 4 areas
> foram discutidas (em vez de uma selecao parcial).

---

## Area 1 — Retrieval na abertura (tutor.md)

### Q: De onde o tutor tira a pergunta de recuperacao?

| Option | Description | Selected |
|--------|-------------|----------|
| Loop fechado com fallback | Prioriza agenda do PROGRESSO; fallback ad-hoc se vazia | |
| So loop fechado | Cobra estritamente o que o fecha-marco agendou | ✓ |
| Ad-hoc do ultimo conceito | Tutor gera na hora do CAMINHO.md | |

**User's choice:** So loop fechado.

### Q: Onde a recuperacao entra e o que acontece se o aluno nao lembra?

| Option | Description | Selected |
|--------|-------------|----------|
| Passo proprio antes do recap; nao-lembrar vira divida | Novo passo antes do recap; formativo | ✓ |
| Dobrar no ritual de abertura existente | Inserir no Passo 1 atual | |

**User's choice:** Passo proprio antes do recap; nao-lembrar vira divida (formativo).

### Q (follow-up): Quando a agenda esta vazia (antes do 1o fechamento)?

| Option | Description | Selected |
|--------|-------------|----------|
| Pula a recuperacao, segue pro recap | Sem conceito anterior = sem pergunta | ✓ |
| Fallback so nesse caso de borda | 1 pergunta ad-hoc na borda | |

**User's choice:** Pula a recuperacao, segue pro recap (sem fallback ad-hoc).

**Notes:** Edge case da 1a sessao / Marco 00 levantado pelo Claude apos a escolha "so loop
fechado"; resolvido sem reintroduzir logica ad-hoc.

---

## Area 2 — Mastery gate + sintese/transferencia (fecha-marco.md)

### Q: Qual a forma do componente de transferencia no gate?

| Option | Description | Selected |
|--------|-------------|----------|
| 1 pergunta de extensao oral/mental | "como voce mudaria para X?" sem andaime | ✓ |
| Mini-tarefa de extensao no codigo | Aluno faz extensao real no projeto | |
| So sintese (explicar) | Mantem so "explica em 2 frases" | |

**User's choice:** 1 pergunta de extensao oral/mental.

### Q: O mastery gate bloqueia o fechamento do marco?

| Option | Description | Selected |
|--------|-------------|----------|
| Bloqueante, mas formativo | Nao explica/estende -> nao fecha, volta ao ciclo, sem nota | ✓ |
| Consultivo (registra, nao trava) | Sinaliza fraqueza mas deixa fechar | |

**User's choice:** Bloqueante, mas formativo.

---

## Area 3 — Agenda de revisao espacada (fecha-marco.md + template PROGRESSO.md)

### Q: Onde a agenda de retrieval mora no PROGRESSO.md?

| Option | Description | Selected |
|--------|-------------|----------|
| Secao nova "## Agenda de retrieval" | Bloco dedicado, separado das dividas de curadoria | ✓ |
| Estender "## Dividas de aprendizado" | Reusa a secao com marcador de tipo | |

**User's choice:** Secao nova "## Agenda de retrieval".

### Q: O que o fecha-marco agenda, e quando revisitar?

| Option | Description | Selected |
|--------|-------------|----------|
| 1 conceito load-bearing -> revisitar no proximo marco | Agenda a frase de Capacidade; 1 entrada/fechamento | ✓ |
| Intervalo espacado crescente (1, depois 2 marcos) | Spacing expandido, multiplas datas | |
| Aluno escolhe o que agendar | Mais autonomia, mas arrisca esvaziar a agenda | |

**User's choice:** 1 conceito load-bearing -> revisitar no proximo marco.

---

## Area 4 — Proxima acao unica + ancora SDT (tutor.md + fecha-marco.md)

### Q: Como aterrissar ENG-01 (proxima acao unica + ancora SDT)?

| Option | Description | Selected |
|--------|-------------|----------|
| Reforco leve verificavel | Item de checklist (1 acao) + nomear SDT na prosa | ✓ |
| Reforco + guardrail anti-lista | Idem + regra escrita "se virou lista, escolha 1" | |
| So nomear a ancora SDT | Apenas mencionar SDT, sem verificabilidade | |

**User's choice:** Reforco leve verificavel.

---

## Claude's Discretion

- Texto exato das frases de nomeacao e dos prompts (recuperacao, extensao).
- Numeracao dos passos renumerados no tutor.md.
- Ancoras precisas de hyperlink no fundamentos.md.
- Formato exato da linha da agenda de retrieval.

## Deferred Ideas

- Intervalo espacado crescente (1+2 marcos) — rejeitado por leveza.
- Mini-tarefa de extensao no codigo — rejeitado por peso.
- Check formativo de curadoria / forense tri-partido — Fase 5.
- Auditoria de aterrissagem das praticas — Fase 6.
