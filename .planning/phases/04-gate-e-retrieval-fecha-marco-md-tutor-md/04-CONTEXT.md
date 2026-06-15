# Phase 4: Gate e retrieval (fecha-marco.md + tutor.md) - Context

**Gathered:** 2026-06-15
**Status:** Ready for planning

<domain>
## Phase Boundary

Editar 3 alvos (todos EXISTENTES) para fechar as duas maiores lacunas de avaliacao do
metodo, mantendo a mecanica LEVE:

1. **`mentor/tutor.md`** — abrir a sessao com 1 pergunta de recuperacao ativa (retrieval
   practice) sobre conceito anterior, ANTES de qualquer aula (AVAL-01), e garantir uma
   "proxima acao unica" verificavel por sessao, ancorada em SDT (ENG-01).
2. **`mentor/fecha-marco.md`** — enquadrar o "done" do Passo 1 como mastery gate com
   criterio de capacidade (AVAL-03) + componente de sintese/transferencia (AVAL-04), e
   agendar revisao espacada de conceito do marco fechado (AVAL-02).
3. **template `PROGRESSO.md`** (em `mentor/reference.md`) — nova secao `## Agenda de
   retrieval` onde o `fecha-marco.md` grava a divida de revisao que o `tutor.md` cobra na
   abertura (fecha o loop AVAL-02 <-> AVAL-01).

Entrega ENG-01, AVAL-01, AVAL-02, AVAL-03, AVAL-04 e os 4 Criterios de Sucesso da Fase 4.

**O QUE citar ja esta fixado** pela Fase 1 (`fundamentos.md`): Retrieval Practice/Testing
Effect, Mastery Learning, Spacing Effect, SDT (autonomia+competencia, com ressalva de
relatedness). Esta discussao decidiu a FORMA da costura, nao o conteudo teorico.

**Nuance estrutural (herdada da Fase 3):** `tutor.md` e `fecha-marco.md` sao PROCEDIMENTOS
lidos pelo AGENTE (nao templates). O anti-theory-leak (CONS-01) se aplica ao que o aluno
LE (`PROGRESSO.md`, proxima acao no Log): zero jargao. A prosa do procedimento pode nomear
frameworks (SDT, mastery, retrieval, spacing) e linkar `fundamentos.md`.

**Contrato consumido da Fase 3 (D-02):** o campo `**Capacidade:**` por marco ja existe no
`PROGRESSO.md`. O mastery gate LE essa frase e a cobra literalmente; e tambem o conceito
load-bearing que a agenda de retrieval agenda.

</domain>

<decisions>
## Implementation Decisions

### Area 1 — Retrieval na abertura do tutor (AVAL-01, AVAL-02 lado tutor)
- **D-01:** Inserir um passo proprio de "Recuperacao ativa" ANTES do recap (Passo 1 atual),
  para a recuperacao acontecer sem o aluno consultar a aula (Criterio 1). 1 pergunta apenas.
  Renumera o ritual de abertura existente (decisao explicita sobre "dobrar no Passo 1":
  REJEITADA porque o recap revela "o que ja funciona" e poderia entregar a resposta).
- **D-02:** Fonte da pergunta = **SO loop fechado**. O tutor cobra ESTRITAMENTE o conceito
  agendado pelo `fecha-marco.md` na secao `## Agenda de retrieval` do `PROGRESSO.md`
  (ver D-09/D-10). Nao gera pergunta ad-hoc. Isso amarra o loop AVAL-02 -> AVAL-01 e
  cumpre o Criterio 3 ("a mesma divida que tutor.md vai cobrar na abertura").
- **D-03:** Recuperacao e FORMATIVA, nao teste. Se o aluno nao lembra: sem penalidade —
  vira/permanece divida de revisao e o tutor reaponta a aula do conceito. Nunca bloqueia
  a sessao.
- **D-04:** Borda "agenda vazia" (1a sessao do projeto e sessoes dentro do Marco 00, antes
  do 1o fechamento): nao existe conceito anterior agendado -> o tutor PULA a recuperacao e
  segue direto pro recap. Sem fallback ad-hoc (coerente com D-02 e com "retrieval sobre
  conceito ANTERIOR"). O passo de recuperacao so dispara quando ha entrada na agenda.

### Area 2 — Mastery gate em fecha-marco.md (AVAL-03, AVAL-04)
- **D-05:** Renomear/enquadrar o "Verificacao do done" (Passo 1) explicitamente como
  **mastery gate** — avancar so apos dominio, nao so "o codigo roda". Mantem leve: e o
  done-check existente renomeado + os criterios abaixo (Criterio 4).
- **D-06:** Adicionar criterio de capacidade: o gate LE o campo `**Capacidade:**` do marco
  no `PROGRESSO.md` (gravado na Fase 3) e cobra literalmente aquela capacidade ("ao
  terminar, voce consegue <verbo> <conceito>"). Contrato ja existente — so consumir.
- **D-07:** Componente de transferencia (AVAL-04) = **1 pergunta de extensao oral/mental**
  ("como voce mudaria isso para fazer X?"); o aluno descreve ou faz um ajuste minusculo
  da variacao SEM andaime. Combina sintese + transferencia num passo so. REJEITADO:
  mini-tarefa de extensao no codigo (pesa o gate, conflita com leveza) e "so sintese"
  (nao cumpre o "estende" de AVAL-04).
- **D-08:** Gate **bloqueante mas formativo**: se o aluno nao consegue explicar/estender, o
  marco NAO fecha — volta ao ciclo de ensino no ponto fraco (igual ao "volte ao ciclo" que
  o Passo 1 ja faz hoje). Sem nota, sem punicao: e diagnostico. REJEITADO: gate consultivo
  (deixaria passar proxy-completion, exatamente o que AVAL-03/04 barram).

### Area 3 — Agenda de revisao espacada (AVAL-02; fecha-marco.md + template PROGRESSO.md)
- **D-09:** Nova secao **`## Agenda de retrieval`** no template `PROGRESSO.md` (em
  `mentor/reference.md`), SEPARADA de `## Dividas de aprendizado` (que sao dividas de
  curadoria, coisa diferente). Fonte inequivoca que o tutor cobra (D-02 exige fonte limpa).
  Cada entrada e enxuta: 1 linha (conceito + em qual marco revisitar).
- **D-10:** Ao fechar um marco, o `fecha-marco.md` agenda **1 conceito load-bearing** do
  marco (essencialmente a frase de `**Capacidade:**`) para revisitar na ABERTURA do proximo
  marco. 1 entrada por fechamento (leveza). REJEITADO: intervalo espacado crescente (1+2
  marcos — arrisca leveza) e "aluno escolhe" (esvazia a agenda, quebra o loop).
- **D-11:** Essa entrada da agenda e a fonte UNICA que o tutor cobra na abertura (D-02) —
  o loop: fecha-marco escreve -> tutor le e cobra -> aluno recupera -> se falha, vira
  divida formativa (D-03).

### Area 4 — Proxima acao unica + ancora SDT (ENG-01; tutor.md + fecha-marco.md)
- **D-12:** Reforco leve VERIFICAVEL: tornar "exatamente 1 proxima acao" um item de
  checklist explicito no fechamento de sessao do tutor (Passo 4 atual) e no Checkpoint
  final do `fecha-marco.md`. Nao opcional, exatamente 1 (nao uma lista). Reusa o que ja
  existe (tutor Passo 4 "despeca com proxima acao"; fecha-marco Passo 6 "aluno sabe o
  proximo passo") — so amarra como contrato verificavel.
- **D-13:** Nomear a ancora SDT (autonomia + competencia, COM a ressalva honesta de
  relatedness em solo+IA) na PROSA dos procedimentos + link para `fundamentos.md`. A
  proxima acao que o aluno LE no Log do `PROGRESSO.md` fica sem jargao (anti-leak CONS-01).

### Claude's Discretion
- Texto exato das frases de nomeacao (mastery gate, retrieval, SDT) e dos prompts (pergunta
  de extensao, pergunta de recuperacao).
- Numeracao exata dos passos renumerados no `tutor.md` apos inserir o passo de recuperacao.
- Posicao precisa das ancoras de hyperlink — conferir os headings reais do `fundamentos.md`
  ("Frameworks foundational (load-bearing)", "Frameworks supporting (ancoram um doc)",
  "Limites e ressalvas" > "SDT relatedness em solo+IA") ao linkar.
- Forma exata da linha da `## Agenda de retrieval` no template (sugestao: `- <conceito> --
  revisitar na abertura do marco <NN>`).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Docs EDITADOS nesta fase
- `mentor/tutor.md` — inserir passo de Recuperacao ativa antes do recap (D-01..D-04);
  reforco da proxima acao unica no Passo 4 de fechamento (D-12); ancora SDT na prosa (D-13).
- `mentor/fecha-marco.md` — Passo 1 vira mastery gate (D-05..D-08); agendar retrieval ao
  fechar (D-10); proxima acao unica no Checkpoint final (D-12); ancora SDT/mastery na prosa.
- `mentor/reference.md` §"Template -- PROGRESSO.md" (~linhas 198-250) — nova secao
  `## Agenda de retrieval` (D-09), distinta de `## Dividas de aprendizado` (~linha 243).

### Docs CITADOS / consumidos (upstream — nunca redefinir)
- `mentor/fundamentos.md` — saida da Fase 1; alvo dos hyperlinks. Linhas/rows relevantes:
  - "Frameworks foundational (load-bearing)" -> row **Retrieval Practice / Testing Effect**
    (Roediger & Karpicke 2006; Dunlosky 2013), status "Fase 4, pendente".
  - "Frameworks supporting (ancoram um doc)" -> rows **Mastery Learning** (Bloom 1968),
    **Spacing Effect / Pratica Distribuida** (Cepeda 2006; Dunlosky 2013), **SDT**
    (Deci & Ryan), todos status "Fase 4, pendente".
  - "Limites e ressalvas" > "SDT relatedness em solo+IA" — usar ao ancorar ENG-01 (D-13).
  - Nota explicita: "Spacing e uma LACUNA hoje; a aterrissagem real ... e prevista para a
    Fase 4" — esta fase aterrissa.
- `mentor/reference.md` — dono do template `PROGRESSO.md` (campo `**Capacidade:**` por
  marco, `## Dividas de aprendizado`, `## Log`) que D-06/D-09/D-10/D-12 consomem.

### Contexto das fases anteriores (decisoes que esta fase herda)
- `.planning/phases/03-bootstrap-com-stage-2-novo-projeto-md/03-CONTEXT.md` — D-02 (campo
  `**Capacidade:**` por marco gravado no `PROGRESSO.md`; o gate desta fase cobra exatamente
  essa frase) e a nota de Integration Points que ja antecipa este consumo. Tambem flagou em
  Deferred que "agenda de retrieval/dividas no PROGRESSO" pertence a esta fase.
- `.planning/phases/02-templates-e-sintaxe-reference-md/02-CONTEXT.md` — formato verbo-
  capacidade puro (anti-leak) reusado na proxima acao e na frase de capacidade.

### Contrato da fase (o que tem de ficar VERDADEIRO)
- `.planning/REQUIREMENTS.md` — ENG-01 (proxima acao unica + SDT), AVAL-01 (retrieval na
  abertura), AVAL-02 (spacing + campo de agenda no PROGRESSO), AVAL-03 (mastery gate +
  criterio de capacidade), AVAL-04 (sintese/transferencia); CONS-01 (anti-leak).
- `.planning/ROADMAP.md` §"Phase 4" — os 4 Criterios de Sucesso.

### Conteudo teorico (o QUE citar — ja decidido pela pesquisa)
- `.planning/research/SUMMARY.md`, `.planning/research/FEATURES.md`,
  `.planning/research/PITFALLS.md` — retrieval practice, spacing, mastery learning, SDT;
  "uma unica proxima acao"; ressalvas de leveza (1 pergunta na abertura; gate leve).

### Convencoes e arquitetura (COMO editar sem quebrar o design)
- `.planning/codebase/ARCHITECTURE.md` — fonte-unica: teoria so em `mentor/`, citada por
  link, nunca duplicada nos adaptadores.
- `.planning/codebase/STRUCTURE.md` — lugar de `tutor.md`/`fecha-marco.md`/`reference.md` e
  dos artefatos do aluno (`PROGRESSO.md`).
- `.planning/codebase/CONVENTIONS.md` — portugues SEM acentos; paths/identificadores em
  backticks.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets (ganchos prontos — a fase EDITA, nao cria do zero)
- `mentor/tutor.md`:
  - **Passo 1** ja anuncia "se ha divida marcada para revisitar neste marco, anuncie" —
    gancho do loop de retrieval; o novo passo (D-01) formaliza isso ANTES do recap.
  - **Passo 3** ja pede "a sintese antes de comemorar" / "me explica em 2 frases" — base de
    sintese que o gate (D-07) estende para transferencia.
  - **Passo 4** ja "despeca com a proxima acao explicita" e loga `proxima acao: <acao>` —
    gancho de ENG-01 (D-12), so falta torna-lo verificavel/unico + ancora SDT.
- `mentor/fecha-marco.md`:
  - **Passo 1** ("Verificacao do done", 3 checkboxes incluindo "o aluno consegue explicar")
    e o alvo do mastery gate (D-05/D-06/D-07/D-08); o "Se algum criterio falhar ... Volte ao
    ciclo" ja e o comportamento bloqueante-formativo (D-08).
  - **Passo 4** (Atualizar PROGRESSO.md) e o lugar natural de escrever a agenda de retrieval
    (D-10), junto com dividas e log.
  - **Checkpoint final** (lista de checkboxes) — onde entra o item "1 proxima acao" (D-12).
- `mentor/reference.md` §"Template -- PROGRESSO.md" — ja tem `**Capacidade:**` por marco
  (Fase 3), `## Dividas de aprendizado` e `## Log`; D-09 adiciona `## Agenda de retrieval`.

### Established Patterns
- Fonte-unica: teoria nova nao e escrita aqui; procedimentos citam `fundamentos.md` por
  hyperlink. Inegociavel.
- Anti-theory-leak (CONS-01): prosa do procedimento (agente) pode nomear frameworks; o que
  o aluno le (PROGRESSO.md, proxima acao, agenda) usa linguagem sem jargao.
- Guardrail de leveza estilo Fase 3 (D-04 da Fase 3): teto explicito ("1 pergunta",
  "1 entrada", "exatamente 1 proxima acao") escrito no proprio doc.
- Estilo: portugues SEM acentos; paths/identificadores em backticks.

### Integration Points
- Upstream consumido: `**Capacidade:**` por marco e template `PROGRESSO.md` (Fase 3/2);
  `fundamentos.md` (Fase 1) como alvo dos links.
- Loop interno desta fase: `fecha-marco.md` (D-10) escreve em `## Agenda de retrieval` ->
  `tutor.md` (D-02) le e cobra na abertura. Os dois docs tem de concordar no formato da
  entrada e no nome da secao — contrato a fixar no plano.
- Downstream: Fase 5 (`metodo.md` + `debug.md`) resume estas etapas na persona e adiciona o
  check formativo de curadoria; Fase 6 audita que nenhuma teoria ficou sem aterrissagem
  (os "(Fase 4, pendente)" do `fundamentos.md` viram "ja presente").

</code_context>

<specifics>
## Specific Ideas

- Pergunta de extensao do gate (exemplo, a refinar): "como voce mudaria isso para fazer X?".
- Linha da agenda (exemplo): `- <conceito> -- revisitar na abertura do marco <NN>`.
- Pergunta de recuperacao na abertura: 1 so, sobre o conceito agendado, antes de qualquer
  aula; sem penalidade se o aluno nao lembrar (vira divida).
- Guardrails de leveza a escrever nos docs: "1 pergunta de recuperacao na abertura",
  "1 entrada de agenda por fechamento", "exatamente 1 proxima acao (se virou lista, corte)".

</specifics>

<deferred>
## Deferred Ideas

- Intervalo espacado crescente (revisitar em 1 e depois 2 marcos) — REJEITADO nesta fase
  (D-10) por leveza; poderia voltar como evolucao futura se a pratica mostrar necessidade.
- Mini-tarefa de extensao no codigo como transferencia — REJEITADO (D-07) por peso; fica
  como possivel reforco futuro, nao nesta fase.
- Check formativo de curadoria e protocolo de forense como feedback tri-partido —
  pertencem a Fase 5 (`metodo.md` + `debug.md`), nao a esta.
- Auditoria final de que cada "(Fase 4, pendente)" do `fundamentos.md` virou aplicacao real
  — Fase 6 (CONS-02 / anti-cargo-cult).

</deferred>

---

*Phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md*
*Context gathered: 2026-06-15*
