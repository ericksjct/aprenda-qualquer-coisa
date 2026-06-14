# Phase 3: Bootstrap com Stage 2 (novo-projeto.md) - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-14
**Phase:** 3-bootstrap-com-stage-2-novo-projeto-md
**Areas discussed:** A. Posicao/ordenacao do Stage 2, B. Onde a evidencia mora, C. Primeiro done leve, D. Leveza/guardrails

> **Formato da sessao:** o usuario pediu discussao conversacional ponto-a-ponto
> ("vai me falando ponto a ponto e a gente vai decidindo junto"), com re-explicacao
> didatica dos termos (backward design, Stage 2). O multiSelect inicial foi recusado.

---

## A. Posicao do Stage 2 + ovo-e-galinha da ordenacao

| Option | Description | Selected |
|--------|-------------|----------|
| Reordenar dentro do Passo 5 (capacidade colada na User Story) + nomear backward design no Passo 4 | Mantem numeracao; resolve o ovo-galinha (User Story so existe no Passo 5) | ✓ |
| Passo proprio entre 4 e 5, movendo a User Story pra ele | Fiel ao literal "entre", mas mais invasivo | |
| Reembrulhar tudo em Stages 1/2/3 explicitos (UbD) | Alinha vocabulario, mas reorganizacao grande + conflita com ordem do ROADMAP | |

**User's choice:** Opcao 1 ("pode ser"), apos confirmar a leitura de que o Passo 4 ja
deriva capacidades do output (backward design ja presente) e o novo e a frase por marco.
**Notes:** Usuario formulou o backward design com palavras proprias ("o agente estrutura
quais sao as capacidades necessarias para atingir o X e ai monta as aulas"). Interpretacao
do "entre caminho e marcos" do ROADMAP registrada como conceitual, nao fisica.

---

## B. Onde a frase de capacidade fica guardada

| Option | Description | Selected |
|--------|-------------|----------|
| `PROGRESSO.md`, colada na User Story de cada marco | Mesmo lugar da User Story; separa nivel marco (PROGRESSO) de nivel passo (CAMINHO); e onde o gate da Fase 4 procura | ✓ |
| `CAMINHO.md` | Misturaria com a capacidade por PASSO ja decidida na Fase 2 | |
| Inline so na prosa do procedimento | Sumiria; gate da Fase 4 ficaria sem chao | |

**User's choice:** `PROGRESSO.md` ("pode ser!").
**Notes:** Frase em linguagem simples (anti-leak), sem jargao. CAMINHO = capacidade por
passo; PROGRESSO = capacidade por marco.

---

## C. "Primeiro done leve" (ENG-02)

| Option | Description | Selected |
|--------|-------------|----------|
| Ancorar no Passo 8 (Walking Skeleton) + reforco no Passo 5 (primeiro marco menor) | Nomeia onde o mecanismo ja mora; rotulagem, nao mecanismo novo | ✓ |
| Principio geral no topo do doc | Mais destaque, mas longe de onde materializa | |

**User's choice:** Opcao 1 ("pode ser").
**Notes:** Explicado que Walking Skeleton (Marco 00) ja entrega vitoria rapida; a fase so
nomeia a intencao anti-evasao + link para `fundamentos.md`.

---

## D. Leveza / guardrail anti over-formalizacao

| Option | Description | Selected |
|--------|-------------|----------|
| Obrigatoria por marco + teto rigido de 1 frase | Mantem leve pelo TAMANHO; gate da Fase 4 sempre encontra a frase | ✓ |
| Opcional/escalavel (pular em projetos com muitos marcos) | Agente pularia sob atrito; gate ficaria sem chao | |

**User's choice:** Opcao 1 ("concordo, opcao 1").
**Notes:** Leveza vem do teto de 1 frase, nao da opcionalidade. Guardrail literal a
escrever no doc contra virar lista/rubrica/sub-doc.

## Claude's Discretion

- Texto exato das frases de nomeacao e posicao das ancoras de hyperlink (dependem da
  estrutura real de `fundamentos.md` e do template `PROGRESSO.md`).

## Deferred Ideas

- Campo de agenda de retrieval/dividas no `PROGRESSO.md` — Fase 4.
- Confirmacao "aplicado em <doc>" das praticas — auditoria da Fase 6.
- Mitigacao "campo opcional para muitos marcos" — rejeitada (D-04).
