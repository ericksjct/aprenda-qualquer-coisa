# Phase 5: Persona e feedback (metodo.md + debug.md) - Context

**Gathered:** 2026-06-15
**Status:** Ready for planning

<domain>
## Phase Boundary

Editar DOIS docs EXISTENTES, ambos lidos pelo AGENTE (nunca pelo aluno):

1. **`mentor/metodo.md`** (a persona / conduta permanente). Tres fios:
   - **CONS-01 (anti theory-leak):** declarar a regra de que a fundamentacao guia o agente
     mas o jargao de framework nunca e citado ao aluno na sessao, com link para
     `fundamentos.md` como o "porque" + lembrete FUND-03 (doc interno).
   - **AVAL-05 (check formativo):** o gate de curadoria ganha um check formativo +
     prompt de auto-explicacao antes de avancar.
   - **Criterio 4 (ciclo nomeado):** a "Conduta por marco (ciclo)" cita as etapas
     nomeadas (gate, retrieval, GRR 3 fases) por referencia aos docs donos, sem duplicar
     teoria nem definicoes.
2. **`mentor/debug.md`** (o protocolo de forense, dono da definicao):
   - **AVAL-06 (feedback tri-partido):** reescrever a forense como feed-up / feed-back /
     feed-forward (Hattie & Timperley), com a PISTA enquadrada como feed-forward que
     preserva a reflexao (nao entrega a resposta).

Entrega AVAL-05, AVAL-06, CONS-01 e os 4 Criterios de Sucesso da Fase 5 no ROADMAP.

**O que NAO foi rediscutido:** o CONTEUDO teorico (Hattie tri-partido, avaliacao formativa,
auto-explicacao, anti-leak) ja esta fixado pela pesquisa (confianca HIGH nos frameworks).
As decisoes abaixo sao sobre a FORMA da costura nesses dois docs (a parte que a pesquisa
marcou LOW/MEDIUM).

**Nuance estrutural que governa as decisoes:** `metodo.md` e `debug.md` sao lidos pelo
AGENTE, nao pelo aluno. Logo a PROSA pode nomear frameworks e linkar `fundamentos.md`; o
anti-leak (CONS-01) restringe o que o agente FALA/ESCREVE ao aluno na sessao, nao a prosa
do procedimento (mesma logica da Fase 3).

</domain>

<decisions>
## Implementation Decisions

### Anti theory-leak — CONS-01 (Criterio 1) — em `metodo.md`
- **D-01:** A regra mora em DOIS lugares de `metodo.md`, sem redundancia de conteudo:
  - **Corpo (afirmativa):** uma regra curta declarando que a fundamentacao guia o agente,
    o jargao de framework NUNCA e citado ao aluno na sessao, COM o link para
    `fundamentos.md` como o "porque" teorico. Esta e a primeira referencia de `metodo.md`
    a `fundamentos.md` (hoje a persona nao o menciona).
  - **Espelho na lista:** 1 item correspondente na lista "Anti-padroes (NUNCA faca)" (que
    fecha o doc), pegando quem so bate o olho na checklist.
  - **Rejeitado:** so o item na lista (espreme o "porque"/link numa linha) e so a secao
    positiva (quem le so a checklist nao ve a regra).
- **D-02:** A mesma regra positiva carrega o lembrete FUND-03: `fundamentos.md` e doc
  interno, guia o agente, nunca e lido pelo aluno nem injetado na sessao. Anti-leak +
  FUND-03 num lugar so, sem duplicar.

### Check formativo no gate de curadoria — AVAL-05 (Criterio 2) — em `metodo.md`
- **D-03:** Inserir um NOVO passo na secao "Gate de curadoria - so depois de funcionar",
  ANTES de abrir as 1-3 melhorias: quando o codigo funciona, o agente faz 1 pergunta de
  auto-explicacao ("me explica por que isso funciona") antes de curar. So segue para a
  curadoria se o aluno consegue explicar; se nao, e sinal de lacuna -> volta ao conceito.
  Deixa o gatekeeping formativo explicito como etapa propria.
  - **Rejeitado:** dobrar a pergunta dentro do passo 2 atual (fica menos visivel como check).
- **D-04:** Guardrail de leveza RIGIDO escrito no doc: "check formativo = exatamente 1
  pergunta de auto-explicacao; se virou checklist ou rubrica, esta errado". MAIS uma nota
  de fronteira: o gate de DOMINIO por marco (sintese/transferencia) mora em
  `fecha-marco.md` (Fase 4), nao aqui — este e o micro-check do gate de curadoria por
  passo, nao o mastery gate por marco. Evita duplicar a Fase 4 e a confusao entre os dois
  gates. (Pesquisa: AVAL-05 e LOW reinforce, "1 pergunta, nao vire quiz".)

### Feedback tri-partido na forense — AVAL-06 (Criterio 3) — em `debug.md`
- **D-05:** OVERLAY, nao reestruturacao: manter os 6 passos existentes do `debug.md`
  (Observar, Isolar, Hipoteses, Testar, Corrigir, Documentar) e adicionar a lente de
  Hattie por cima, agrupando-os:
  - **feed-up (Aonde vou?)** = Observar (expectativa vs resultado / objetivo).
  - **feed-back (Como estou indo?)** = Isolar + Hipoteses + Testar (onde diverge).
  - **feed-forward (Para onde a seguir?)** = Corrigir + PISTA + Documentar (proximo passo).
  - **Rejeitado:** reescrever o doc inteiro nas 3 fases (mais invasivo, reescreve protocolo
    que ja funciona, mais risco).
- **D-06:** A regra "PISTA = feed-forward que aponta a direcao sem entregar a resposta"
  vive em `debug.md`, no ponto onde a PISTA e invocada (passo Corrigir / "travado ha 10
  min"). A definicao do scaffold em `metodo.md`/`reference.md` NAO muda — `debug.md` so
  nomeia o papel da PISTA quando a usa. (Evita espalhar a mesma regra em 2 docs.)
- **D-07:** O resumo de forense DENTRO de `metodo.md` continua um PONTEIRO CURTO para
  `/debug` (fonte-unica: a definicao tri-partida mora so em `debug.md`). Pode ganhar no
  maximo 1 linha nomeando "feedback tri-partido" + link, sem copiar a definicao.
  - **Rejeitado:** espelhar a reescritura tri-partida no `metodo.md` tambem (duplicaria
    conteudo dono do `debug.md` -> risco de drift).

### Ciclo nomeado — Criterio 4 — em `metodo.md`
- **D-08:** ANOTAR OS 5 PASSOS INLINE (sem bloco de visao geral novo): manter os 5 itens da
  "Conduta por marco (ciclo)" e, em cada ponto onde a etapa ja ocorre, nomear o framework
  + linkar o doc dono. Minima cirurgia num doc ja longo.
  - **Rejeitado:** adicionar um paragrafo de visao geral no topo do ciclo (bloco a mais).
- **D-09:** Escopo = exatamente as 3 etapas do criterio, cada uma por link ao dono:
  - **GRR 3 fases** ("eu faco -> nos fazemos -> voce faz") no passo 3 do ciclo (onde o
    "eu faco -> voce faz" ja ocorre) -> link `reference.md` (dono da sintaxe GRR, Fase 2).
  - **retrieval** (recuperacao ativa) na abertura -> link `tutor.md` (Fase 4).
  - **gate** (mastery gate de fechamento) -> link `fecha-marco.md` (Fase 4).
  - **Rejeitado:** nomear tambem backward design / "primeiro done leve" (Fase 3) — risco de
    o ciclo virar indice.

### Claude's Discretion
- Texto exato das frases de nomeacao/regra e a posicao precisa das ancoras de hyperlink
  dependem da estrutura de cabecalhos de `fundamentos.md` (Fase 1) e dos docs da Fase 4
  (`tutor.md` retrieval, `fecha-marco.md` mastery gate). O executor confere as ancoras
  reais ao linkar (a Fase 4 ja estara feita quando a Fase 5 rodar, por ordem de execucao).
- Mapeamento exato passo-a-fase de Hattie no `debug.md` (D-05) pode ser ajustado pelo
  executor desde que preserve os 6 passos e as 3 perguntas.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Docs EDITADOS nesta fase
- `mentor/metodo.md` — persona/conduta. Secoes-chave:
  - "Anti-padroes (NUNCA faca)" (D-01 espelho) e corpo do doc (D-01 regra positiva +
    D-02 FUND-03).
  - "Gate de curadoria - so depois de funcionar" (D-03 novo passo + D-04 guardrail/fronteira).
  - "Protocolo de forense" (D-07 fica ponteiro curto).
  - "Conduta por marco (ciclo)" (D-08/D-09 nomear GRR/retrieval/gate inline).
- `mentor/debug.md` — dono da forense. Os 6 passos + ponto da PISTA (D-05 overlay Hattie,
  D-06 PISTA=feed-forward).

### Docs CITADOS / donos (upstream — nunca redefinir, so linkar)
- `mentor/fundamentos.md` — saida da Fase 1; alvo do link de D-01/D-02. Ancoras relevantes:
  "Frameworks supporting" (linha "Avaliacao Formativa" Black & Wiliam; linha "Modelo de
  Feedback (Feed Up/Back/Forward)" Hattie & Timperley). Conferir os cabecalhos reais ao linkar.
- `mentor/reference.md` — dono da sintaxe GRR (Fase 2); alvo do link de D-09 (GRR 3 fases)
  e dono da definicao do scaffold/PISTA que D-06 NAO altera.
- `mentor/tutor.md` — dono do retrieval na abertura (Fase 4); alvo do link de D-09. Ancora
  so existe apos a Fase 4 (forward-reference seguro: Fase 4 roda antes da 5).
- `mentor/fecha-marco.md` — dono do mastery gate por marco (Fase 4); alvo do link de D-09 e
  referencia da nota de fronteira de D-04. Ancora idem (Fase 4 primeiro).

### Contexto das fases anteriores (decisoes herdadas)
- `.planning/phases/03-bootstrap-com-stage-2-novo-projeto-md/03-CONTEXT.md` — a distincao
  anti-leak "prosa do agente PODE nomear frameworks; so o que vai pro aluno e jargao-zero"
  governa D-01/D-02; e o padrao de guardrail rigido de leveza (D-04 aqui ecoa o D-04 de la).
- `.planning/phases/02-templates-e-sintaxe-reference-md/02-CONTEXT.md` — citacao por
  hyperlink (nunca reescrever teoria) e a sintaxe GRR cuja DEFINICAO mora em `reference.md`
  (D-09 so linka, nao redefine).

### Conteudo teorico (o QUE citar — ja decidido pela pesquisa)
- `.planning/research/SUMMARY.md` §"Avaliacao & feedback" — avaliacao formativa
  (Black & Wiliam 1998) reenquadra DONE/curadoria; feedback Feed-Up/Back/Forward
  (Hattie & Timperley 2007) ancora PISTA como feed-forward; check formativo +
  auto-explicacao (LOW); feedback tri-partido (MEDIUM).
- `.planning/research/FEATURES.md` — linhas de "checks formativos de baixo risco" (new,
  LOW), "feedback acionavel estruturado (Hattie)" (new, MEDIUM), "prompts de
  auto-explicacao" (new, LOW); mapa pratica -> doc (gate de curadoria; debug.md).
- `.planning/research/PITFALLS.md` — P9 (teoria vazando = base de CONS-01), e a nota de
  ancorar "done" em avaliacao formativa + mastery learning.

### Contrato da fase (o que tem de ficar VERDADEIRO)
- `.planning/REQUIREMENTS.md` §AVAL (AVAL-05, AVAL-06), §CONS (CONS-01).
- `.planning/ROADMAP.md` §"Phase 5" — os 4 Criterios de Sucesso.

### Convencoes e arquitetura do toolkit (COMO editar sem quebrar o design)
- `.planning/codebase/ARCHITECTURE.md` — fonte-unica: teoria so em `mentor/`, citada por
  link, nunca duplicada nos adaptadores (`.claude/`, `AGENTS.md`).
- `.planning/codebase/STRUCTURE.md` — lugar de `metodo.md`/`debug.md` e a relacao
  persona <-> procedimentos.
- `.planning/codebase/CONVENTIONS.md` — portugues SEM acentos; paths/identificadores em
  backticks.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `mentor/metodo.md` ja contem todas as secoes-alvo; a fase EDITA, nao cria:
  - "Gate de curadoria - so depois de funcionar" ja tem 3 passos numerados — gancho pronto
    para inserir o check formativo como novo passo (D-03).
  - "Conduta por marco (ciclo)" ja tem 5 itens; o passo 3 ja descreve "eu faco -> voce faz"
    (gancho do GRR, D-09) e o item 4 ja aponta a forense (gancho do ponteiro D-07).
  - "Protocolo de forense" ja e um resumo de 6 passos que aponta `/debug` — D-07 so o
    mantem curto.
  - "Anti-padroes (NUNCA faca)" ja e uma lista longa — gancho para o espelho de D-01.
  - HOJE `metodo.md` NAO referencia `fundamentos.md` em lugar nenhum; D-01 cria a 1a ponte.
- `mentor/debug.md` ja tem os 6 passos (Observar...Documentar) + variacoes + anti-padroes —
  D-05 aplica overlay sem reescrever; o ponto "travado ha 10 min -> pista gradual" e o
  gancho de D-06 (PISTA = feed-forward).

### Established Patterns
- Fonte-unica: teoria nova nao e escrita aqui; `metodo.md`/`debug.md` citam os donos
  (`fundamentos.md`, `reference.md`, `tutor.md`, `fecha-marco.md`) por hyperlink.
- Anti-theory-leak: a prosa lida pelo agente pode nomear frameworks; o anti-leak governa o
  que o agente diz ao aluno na sessao.
- Estilo: portugues SEM acentos; paths/identificadores em backticks.

### Integration Points
- Upstream consumido: `fundamentos.md` (Fase 1) como alvo dos links; sintaxe GRR de
  `reference.md` (Fase 2); retrieval/`tutor.md` e mastery gate/`fecha-marco.md` (Fase 4).
- Downstream: a Fase 6 (auditoria de consistencia) verifica que (a) CONS-01 esta declarado,
  (b) cada "(Fase 5, pendente)" de `fundamentos.md` (Avaliacao Formativa, Hattie) virou
  aplicacao real e (c) nada de teoria/definicao foi duplicado nos adaptadores.

</code_context>

<specifics>
## Specific Ideas

- Mapa Hattie -> 6 passos do `debug.md` (D-05): feed-up = Observar; feed-back =
  Isolar+Hipoteses+Testar; feed-forward = Corrigir+PISTA+Documentar.
- Guardrail literal sugerido para o gate de curadoria (D-04): "check formativo = exatamente
  1 pergunta de auto-explicacao; se virou checklist ou rubrica, esta errado".
- Nota de fronteira a registrar (D-04): "o gate de dominio por marco (sintese/transferencia)
  mora em `fecha-marco.md`; aqui e o micro-check formativo do gate de curadoria por passo".
- Forma da regra anti-leak (D-01/D-02): afirmativa no corpo com link, espelhada como 1
  "NUNCA faca", carregando o lembrete de doc interno (FUND-03).

</specifics>

<deferred>
## Deferred Ideas

- Rubrica reutilizavel de criterios observaveis para curadoria de marco — e v2 (FUT-05),
  fora do escopo; AVAL-05 aqui e deliberadamente 1 pergunta, nao rubrica (D-04).
- Nomear backward design / "primeiro done leve" no ciclo de `metodo.md` — REJEITADO aqui
  (D-09) para nao inchar o ciclo; aterrissagem desses ja foi feita na Fase 3.
- Verificacao final de que "(Fase 5, pendente)" em `fundamentos.md` (Avaliacao Formativa,
  Hattie) virou "aplicado em" verificavel — auditoria da Fase 6 (CONS-02).

</deferred>

---

*Phase: 05-persona-e-feedback-metodo-md-debug-md*
*Context gathered: 2026-06-15*
