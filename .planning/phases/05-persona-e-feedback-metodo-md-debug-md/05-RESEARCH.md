# Phase 5: Persona e feedback (metodo.md + debug.md) - Research

**Researched:** 2026-06-15
**Domain:** Costura editorial de ciencia da aprendizagem em docs markdown de `mentor/` (NAO software)
**Confidence:** HIGH

## Summary

Esta e uma fase de TECEDURA DE DOCUMENTACAO, nao de software: nao ha runtime, codigo de
aplicacao nem testes-como-codigo. "Implementacao" = editar dois docs markdown existentes
(`mentor/metodo.md` e `mentor/debug.md`) lidos pelo AGENTE (nunca pelo aluno). O conteudo
teorico (avaliacao formativa, auto-explicacao, feedback tri-partido de Hattie, anti-leak)
ja esta FIXADO pela pesquisa de milestone (HIGH) e pelo catalogo `mentor/fundamentos.md`;
esta fase NAO re-pesquisa ciencia da aprendizagem. O trabalho do planner e: posicionar
cada decisao travada (D-01..D-09) na ancora certa dos dois docs, linkar os docs-donos
pelos slugs corretos, e provar cada um dos 4 Criterios de Sucesso por grep estatico.

A boa noticia operacional: as Fases 1-4 ja rodaram (ou rodarao antes da 5 pela ordem de
execucao inegociavel), e TODOS os docs-alvo de link ja existem no estado esperado.
Confirmei por leitura direta que `fundamentos.md` (Fase 1), `reference.md` (Fase 2),
`tutor.md` e `fecha-marco.md` (Fase 4) contem hoje as secoes/ancoras de que D-01/D-02/D-09
precisam. Nenhuma ancora de D-09 e uma forward-reference quebrada no estado atual do repo
(detalhe na tabela de ancoras). O executor ainda deve re-confirmar as ancoras no momento
de rodar a Fase 5, mas o risco de anchor-miss e BAIXO.

O harness de verificacao ja esta provado em 3 fases (Fase 2 `check-phase2.sh`, Fase 4
`check-phase4.sh`) usando o par `extract-fenced.sh` + `check-phase5.sh`. A Fase 5 deve
clonar esse padrao em Wave 0: checks positivos (`check_min`/`check_has`) para presenca de
regra/heading/link, `check_zero` para o anti-leak (CONS-01) DENTRO de blocos cercados, e
ANCHOR-RESOLVE para confirmar que cada `#slug` linkado casa um heading real no doc-dono.

**Primary recommendation:** Wave 0 clona `extract-fenced.sh` + autora `check-phase5.sh`
(checks V-01..V-NN abaixo); depois 2 planos de edicao — um para `metodo.md` (D-01/D-02
anti-leak + D-03/D-04 check formativo + D-07 ponteiro + D-08/D-09 ciclo nomeado) e um para
`debug.md` (D-05 overlay Hattie + D-06 PISTA=feed-forward). O anti-leak NAO se aplica a
prosa do procedimento (lida pelo agente) — so a blocos cercados que viram artefato do aluno.

## User Constraints (from CONTEXT.md)

### Locked Decisions

**Anti theory-leak — CONS-01 (Criterio 1) — em `metodo.md`**
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

**Check formativo no gate de curadoria — AVAL-05 (Criterio 2) — em `metodo.md`**
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
  passo, nao o mastery gate por marco.

**Feedback tri-partido na forense — AVAL-06 (Criterio 3) — em `debug.md`**
- **D-05:** OVERLAY, nao reestruturacao: manter os 6 passos existentes do `debug.md`
  (Observar, Isolar, Hipoteses, Testar, Corrigir, Documentar) e adicionar a lente de
  Hattie por cima, agrupando-os:
  - **feed-up (Aonde vou?)** = Observar (expectativa vs resultado / objetivo).
  - **feed-back (Como estou indo?)** = Isolar + Hipoteses + Testar (onde diverge).
  - **feed-forward (Para onde a seguir?)** = Corrigir + PISTA + Documentar (proximo passo).
  - **Rejeitado:** reescrever o doc inteiro nas 3 fases (mais invasivo, mais risco).
- **D-06:** A regra "PISTA = feed-forward que aponta a direcao sem entregar a resposta"
  vive em `debug.md`, no ponto onde a PISTA e invocada (passo Corrigir / "travado ha 10
  min"). A definicao do scaffold em `metodo.md`/`reference.md` NAO muda.
- **D-07:** O resumo de forense DENTRO de `metodo.md` continua um PONTEIRO CURTO para
  `/debug` (fonte-unica: a definicao tri-partida mora so em `debug.md`). Pode ganhar no
  maximo 1 linha nomeando "feedback tri-partido" + link, sem copiar a definicao.
  - **Rejeitado:** espelhar a reescritura tri-partida no `metodo.md` tambem.

**Ciclo nomeado — Criterio 4 — em `metodo.md`**
- **D-08:** ANOTAR OS 5 PASSOS INLINE (sem bloco de visao geral novo): manter os 5 itens
  da "Conduta por marco (ciclo)" e, em cada ponto onde a etapa ja ocorre, nomear o
  framework + linkar o doc dono. Minima cirurgia num doc ja longo.
  - **Rejeitado:** adicionar um paragrafo de visao geral no topo do ciclo.
- **D-09:** Escopo = exatamente as 3 etapas do criterio, cada uma por link ao dono:
  - **GRR 3 fases** ("eu faco -> nos fazemos -> voce faz") no passo 3 do ciclo -> link
    `reference.md` (dono da sintaxe GRR, Fase 2).
  - **retrieval** (recuperacao ativa) na abertura -> link `tutor.md` (Fase 4).
  - **gate** (mastery gate de fechamento) -> link `fecha-marco.md` (Fase 4).
  - **Rejeitado:** nomear tambem backward design / "primeiro done leve" (Fase 3).

### Claude's Discretion
- Texto exato das frases de nomeacao/regra e a posicao precisa das ancoras de hyperlink
  dependem da estrutura de cabecalhos dos docs-donos. O executor confere as ancoras reais
  ao linkar (Fase 4 ja estara feita quando a Fase 5 rodar).
- Mapeamento exato passo-a-fase de Hattie no `debug.md` (D-05) pode ser ajustado pelo
  executor desde que preserve os 6 passos e as 3 perguntas.

### Deferred Ideas (OUT OF SCOPE)
- Rubrica reutilizavel de criterios observaveis para curadoria de marco — v2 (FUT-05).
  AVAL-05 aqui e deliberadamente 1 pergunta, nao rubrica (D-04).
- Nomear backward design / "primeiro done leve" no ciclo de `metodo.md` — REJEITADO (D-09).
- Verificacao final de que "(Fase 5, pendente)" em `fundamentos.md` virou "aplicado em"
  verificavel — auditoria da Fase 6 (CONS-02).

## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| AVAL-05 | O gate de curadoria (`metodo.md`) inclui um check formativo + prompt de auto-explicacao antes de avancar | Gancho pronto: secao "Gate de curadoria - so depois de funcionar" ja tem 3 passos numerados (metodo.md:64-75). D-03 insere novo passo ANTES das 1-3 melhorias; D-04 escreve o guardrail "exatamente 1 pergunta" + nota de fronteira para `fecha-marco.md`. Padrao de guardrail rigido herda da Fase 4 (`fecha-marco.md` "Mantenha leve... Nao vire quiz nem checklist gigante", linha 31-32). |
| AVAL-06 | O protocolo de forense (`debug.md`) reescrito como feedback tri-partido (feed-up/back/forward, Hattie & Timperley), com a PISTA enquadrada como feed-forward que preserva a reflexao | `debug.md` ja tem os 6 passos (linhas 16-87) + ponto da PISTA (linha 73, passo Corrigir "travado ha mais de 10 minutos"). D-05 e overlay (agrupar os 6 em 3 lentes); D-06 nomeia a PISTA como feed-forward no ponto onde ela e invocada. Owner do framework: `fundamentos.md` linha 49 (Hattie & Timperley 2007). |
| CONS-01 | `metodo.md` declara como regra/anti-padrao que a fundamentacao guia o agente mas o jargao de framework nunca e citado ao aluno na sessao (anti theory-leak) | `metodo.md` HOJE nao referencia `fundamentos.md` em lugar nenhum — D-01 cria a 1a ponte. Regra positiva no corpo + espelho na lista "Anti-padroes (NUNCA faca)" (metodo.md:141-165). Carrega FUND-03 (D-02). Anti-leak governa o que o agente DIZ AO ALUNO, nao a prosa do procedimento. |

## Architectural Responsibility Map

> "Tier" aqui = camada de doc no design fonte-unica (ARCHITECTURE.md), nao tier de software.

| Capability | Primary Tier (dono) | Secondary Tier (cita por link) | Rationale |
|------------|---------------------|--------------------------------|-----------|
| Regra anti theory-leak (CONS-01) | `metodo.md` (persona/conduta) | `fundamentos.md` (o "porque" + FUND-03) | Conduta permanente do agente mora na persona; o porque teorico mora no catalogo upstream, citado por link |
| Check formativo + auto-explicacao (AVAL-05) | `metodo.md` (gate de curadoria) | `fecha-marco.md` (nota de fronteira: mastery gate por marco vive la) | O micro-check por passo e conduta de curadoria; o gate de dominio por marco e outro lugar (evita duplicar Fase 4) |
| Feedback tri-partido / forense (AVAL-06) | `debug.md` (dono da definicao da forense) | `fundamentos.md` (Hattie, opcional) | Fonte-unica: a definicao tri-partida mora SO em `debug.md`; `metodo.md` so aponta |
| PISTA = feed-forward (D-06) | `debug.md` (no ponto da PISTA) | `reference.md` (dono do scaffold/PISTA — NAO muda) | `debug.md` nomeia o PAPEL da PISTA quando a usa; a sintaxe/definicao da PISTA continua em `reference.md` |
| Ciclo por marco nomeado (Criterio 4) | `metodo.md` (a secao "Conduta por marco (ciclo)") | `reference.md` (GRR), `tutor.md` (retrieval), `fecha-marco.md` (gate) | A persona resume o ciclo; cada etapa e definida no doc-dono e so citada por link |
| Ponteiro de forense em metodo (D-07) | `metodo.md` (secao "Protocolo de forense") | `debug.md` (dono) | Resumo curto que aponta `/debug`; nao duplica a reescritura tri-partida |

## Standard Stack

Esta fase NAO usa bibliotecas de software. O "stack" e o ferramental editorial + de
verificacao estatica ja estabelecido no repo:

### Core
| Ferramenta | Versao | Proposito | Por que padrao |
|------------|--------|-----------|----------------|
| `rg` (ripgrep) | ja presente | Grep estatico de presenca/ausencia de padroes nos docs | [VERIFIED: codebase] Usado em `check-phase2.sh`, `check-phase4.sh` |
| `awk` | ja presente | Isolar conteudo de blocos cercados (` ``` `) para o grep anti-leak | [VERIFIED: codebase] `extract-fenced.sh` usa `inside = !inside` |
| `sh` (POSIX) | ja presente | Wrapper do harness PASS/FAIL | [VERIFIED: codebase] `check-phase{2,4}.sh` |

### Supporting (artefatos a clonar de Wave 0)
| Artefato | Origem | Proposito | Quando usar |
|----------|--------|-----------|-------------|
| `extract-fenced.sh` | clone verbatim da Fase 4 (`.planning/phases/04-.../scripts/extract-fenced.sh`) | Isola SO o texto dentro de blocos cercados, para o anti-leak nao dar falso-positivo na prosa legitima | Wave 0; consumido por `check-phase5.sh` (CONS-01) |
| `check-phase5.sh` | autorar a partir de `check-phase4.sh` (template de `count`/`check_min`/`check_zero`/`check_has`/ANCHOR-RESOLVE) | Gate estatico PASS/FAIL dos criterios da Fase 5 | Wave 0; rodado por task/wave/gate |

**Installation:** Nenhuma. `rg`, `awk`, `sh` ja provados por 3 fases. Sem npm/pip.

## Architecture Patterns

### System Architecture Diagram (fluxo editorial + verificacao)

```
                   FASE 5 — edita 2 docs lidos pelo AGENTE (nunca pelo aluno)
                   ┌──────────────────────────────────────────────────────┐
   D-01/D-02 ───►  │ mentor/metodo.md  (persona / conduta permanente)      │
   D-03/D-04 ───►  │   - corpo: regra anti-leak + link fundamentos.md      │ ──link──►  fundamentos.md
   D-07      ───►  │   - "Gate de curadoria": novo passo formativo + guard │            (#frameworks-supporting...)
   D-08/D-09 ───►  │   - "Anti-padroes (NUNCA faca)": espelho 1 item       │            (FUND-03 preambulo)
                   │   - "Protocolo de forense": ponteiro curto p/ /debug   │ ──link──►  reference.md (GRR slug)
                   │   - "Conduta por marco (ciclo)": GRR/retrieval/gate    │ ──link──►  tutor.md (retrieval slug)
                   └──────────────────────────────────────────────────────┘ ──link──►  fecha-marco.md (gate slug)
                                                                                          ▲
   D-05/D-06 ───►  ┌──────────────────────────────────────────────────────┐             │ (link de D-09)
                   │ mentor/debug.md  (dono da forense — definicao unica)   │             │
                   │   - overlay Hattie sobre os 6 passos (feed-up/back/fwd)│             │
                   │   - PISTA = feed-forward (no ponto Corrigir/10min)     │             │
                   └──────────────────────────────────────────────────────┘             │
                                                                                          │
   VERIFICACAO ►   check-phase5.sh ──┬── check_min/check_has (presenca de regra/heading/link)
   (Wave 0)                          ├── ANCHOR-RESOLVE (cada #slug casa heading real no dono)
                                     └── extract-fenced.sh | rg -c (anti-leak: 0 jargao em blocos cercados)
```

### Recommended Plan Structure (3 planos)

```
05-01-PLAN.md  # Wave 0: clonar extract-fenced.sh + autorar check-phase5.sh (todos os checks)
05-02-PLAN.md  # metodo.md: D-01/D-02 (anti-leak+FUND-03) + D-03/D-04 (formativo) + D-07 (ponteiro) + D-08/D-09 (ciclo)
05-03-PLAN.md  # debug.md: D-05 (overlay Hattie) + D-06 (PISTA=feed-forward)
```

`05-02` e `05-03` editam arquivos disjuntos (`metodo.md` vs `debug.md`) — podem rodar em
paralelo apos Wave 0. D-07 (ponteiro em `metodo.md`) so nomeia "feedback tri-partido" + link
para `/debug`; nao depende do conteudo exato de `debug.md`, so do nome do conceito (ja
travado em D-05). Sem dependencia de conteudo cruzado entre os dois planos de edicao.

### Pattern 1: Regra em dois lugares sem duplicar conteudo (D-01)
**What:** A regra anti-leak tem UMA fonte de verdade (a afirmativa no corpo, com o link e o
porque); o item na lista "Anti-padroes" e um ESPELHO curto (1 linha imperativa), nao uma
re-explicacao. Mesmo padrao que o repo ja usa: a Regra de ouro mora no corpo (metodo.md:12)
e e espelhada como "Preencher o `TODO(human)` pelo aluno" na lista (metodo.md:143).
**When to use:** Sempre que uma regra precisa pegar tanto o leitor linear quanto o que so
bate o olho na checklist final.
**Example (forma, nao texto literal — Claude's discretion):**
```markdown
<!-- no corpo, primeira referencia de metodo.md a fundamentos.md -->
A fundamentacao guia a sua conduta, nunca vira conteudo: voce APLICA as boas praticas,
mas NUNCA cita o nome do framework ao aluno na sessao. O "porque" teorico (interno) esta
em [fundamentos.md](fundamentos.md) — doc do agente, jamais lido pelo aluno nem injetado
na sessao.

<!-- espelho na lista "Anti-padroes (NUNCA faca)" -->
- Citar jargao de framework (Bloom, CLT, retrieval...) ao aluno na sessao — a teoria guia voce, nao e despejada nele.
```

### Pattern 2: Overlay nao-destrutivo (D-05)
**What:** Adicionar uma lente conceitual (os 3 rotulos de Hattie) SEM reescrever os 6 passos
que ja funcionam. Os passos permanecem; os rotulos agrupam-nos. Mesmo espirito do D-08
(anotar inline, nao adicionar bloco novo).
**When to use:** Quando o procedimento existente esta correto e so falta nomear a estrutura.
**Example (forma):**
```markdown
## O protocolo (6 passos)

> Os 6 passos sao um ciclo de feedback acionavel em 3 lentes (Hattie & Timperley):
> feed-up (Aonde vou?) = Observar · feed-back (Como estou?) = Isolar+Hipoteses+Testar ·
> feed-forward (Para onde a seguir?) = Corrigir+PISTA+Documentar.

### 1. Observar   <!-- (feed-up: Aonde vou?) -->
...
```

### Anti-Patterns to Avoid
- **Duplicar a definicao da forense entre `metodo.md` e `debug.md`:** D-07 e PONTEIRO, nao
  copia. Se a reescritura tri-partida aparecer nos dois docs, viola fonte-unica -> drift
  (PITFALLS P12). `metodo.md` ganha no maximo 1 linha + link.
- **Mover a definicao da PISTA para `debug.md`:** D-06 so NOMEIA o papel da PISTA; a sintaxe
  da PISTA continua em `reference.md` (Formato do scaffold) e a regra "PISTA nao e a unica
  ponte" continua em `metodo.md`/`reference.md`. Nao recortar.
- **Transformar o check formativo em rubrica/quiz:** D-04 exige guardrail literal "exatamente
  1 pergunta". O risco e o LOW-confidence da pesquisa (AVAL-05) — over-formalizacao (P10).
- **Nomear etapas alem das 3 de D-09 no ciclo:** backward design / primeiro done leve foram
  REJEITADOS para nao virar indice. Escopo fechado.
- **Aplicar o anti-leak a PROSA do procedimento:** a prosa de `metodo.md`/`debug.md` PODE
  nomear frameworks e linkar `fundamentos.md` (e lida pelo agente). O anti-leak so se aplica
  ao que vira artefato do aluno — operacionalmente, ao conteudo de blocos cercados.

## Don't Hand-Roll

| Problema | Nao construa | Use no lugar | Por que |
|----------|--------------|--------------|---------|
| Verificar presenca de regra/heading/link | Checklist manual / revisao a olho | `check-phase5.sh` (clone de `check-phase4.sh`) | Harness provado em 3 fases; PASS/FAIL deterministico em ~2s |
| Anti-leak sem falso-positivo na prosa | grep cru no doc inteiro | `extract-fenced.sh \| rg -c` (so blocos cercados) | A prosa do agente PODE citar frameworks; so o conteudo cercado vira artefato do aluno |
| Resolver slug de ancora markdown | Adivinhar o `#slug` | ANCHOR-RESOLVE (grep do heading literal no doc-dono) + 1 conferencia manual no renderer | Slugs de GitHub tem regras (lowercase, espacos->hifen, pontuacao caai, `+` some); grep do heading prova que o alvo existe |

**Key insight:** O unico "codigo" desta fase sao 2 scripts shell de verificacao estatica,
clonados de um padrao ja provado. Tudo o mais e edicao de prosa. Nao reinvente o harness
nem o extrator — clone verbatim e so troque os checks.

## Mapa dos 4 Criterios de Sucesso -> ancora exata + acao

> Quotes de heading sao o texto LITERAL atual dos docs (use-os como ancora de edicao).

### Criterio 1 (CONS-01) — anti theory-leak em `metodo.md`
**Alvo A (corpo, regra positiva + D-02 FUND-03):** inserir como nova regra curta. Posicao
sugerida: logo apos a "## Regra de ouro" (metodo.md:12-16) OU como nova subsecao perto do
topo da conduta — onde o agente le cedo. HOJE `metodo.md` nao cita `fundamentos.md`: esta
e a 1a ponte.
**Alvo B (espelho):** lista "## Anti-padroes (NUNCA faca)" — heading literal na linha 141.
Adicionar 1 item imperativo curto.
**Acao:** corpo = afirmativa com `[fundamentos.md](fundamentos.md)` + lembrete FUND-03 (doc
interno, nunca lido pelo aluno); lista = espelho de 1 linha. NAO duplicar o "porque".

### Criterio 2 (AVAL-05) — check formativo em `metodo.md`
**Alvo:** secao "## Gate de curadoria — "so depois de funcionar"" — heading literal na
linha 64. Hoje tem 3 passos numerados (linhas 66-72) + "Ordem sagrada" (74-75).
**Acao:** D-03 = inserir NOVO passo (auto-explicacao "me explica por que isso funciona")
ENTRE o passo 2 (codigo funciona) e o passo 3 (curadoria/melhorias) — ou seja, ANTES de
abrir as 1-3 melhorias. D-04 = escrever o guardrail literal "exatamente 1 pergunta... se
virou checklist/rubrica, esta errado" + nota de fronteira apontando `fecha-marco.md`
(mastery gate por marco mora la, nao aqui).

### Criterio 3 (AVAL-06) — feedback tri-partido em `debug.md`
**Alvo overlay (D-05):** secao "## O protocolo (6 passos)" — heading literal na linha 14;
os 6 sub-headings `### 1. Observar` ... `### 6. Documentar` (linhas 16, 31, 42, 53, 64, 77).
**Alvo PISTA (D-06):** dentro de "### 5. Corrigir" — a linha "Se estiver travado ha mais de
10 minutos, ofereca a pista gradual..." (linha 73). (Tambem ha o gancho equivalente em
`metodo.md:88-89` no resumo, mas D-06 trava em `debug.md`.)
**Acao:** D-05 = blockquote/nota de mapeamento Hattie sobre os 6 passos + (opcional)
rotulo `(feed-up/back/forward)` em cada sub-heading. D-06 = no ponto da PISTA, enquadrar
"PISTA = feed-forward: aponta a direcao do proximo passo SEM entregar a resposta".

### Criterio 4 — ciclo nomeado em `metodo.md`
**Alvo:** secao "## Conduta por marco (ciclo)" — heading literal na linha 32; 5 itens
numerados (linhas 34-62). Ganchos prontos:
- **GRR (D-09):** passo 3 (linha 48) ja descreve "inverta para 'eu faco -> voce faz'" —
  ancora natural para nomear GRR 3 fases + link `reference.md`.
- **retrieval (D-09):** a abertura do ciclo / passo 1 (conceito antes da tentativa) +
  o "Onde voce esta no fluxo" (linha 22 menciona `/tutor`) — ancora para nomear retrieval
  + link `tutor.md`.
- **gate (D-09):** a secao "## Fechamento de marco" (linha 132, menciona `/fecha-marco`
  linha 139) — ancora para nomear mastery gate + link `fecha-marco.md`.
- **forense (D-07):** passo 4 (linha 59) ja aponta o protocolo de forense; e a secao
  "## Protocolo de forense" (linha 77). D-07 mantem curto + 1 linha "feedback tri-partido"
  + link `/debug`.
**Acao:** anotar INLINE (D-08) nos pontos onde a etapa ja ocorre; nao adicionar bloco de
visao geral. Exatamente 3 nomeacoes com link (GRR, retrieval, gate).

## Mapa de ancoras de hyperlink (slugs reais nos docs-donos)

> Slug = GitHub-flavored: minusculas, espacos->hifen, pontuacao/`()`/`:`/`"` caem, `+`
> some, acentos ja ausentes (docs sem acento). Todos VERIFICADOS por leitura do heading
> literal no estado ATUAL do repo. O executor re-confirma ao linkar (rode o ANCHOR-RESOLVE).

| Link de | Conceito | Doc-dono | Heading literal atual | Slug a usar | Existe hoje? |
|---------|----------|----------|------------------------|-------------|--------------|
| D-01/D-02 | anti-leak "porque" / FUND-03 | `fundamentos.md` | (preambulo no topo, linhas 3-8 — doc interno) + linha "Avaliacao Formativa" e "Modelo de Feedback" na tabela "## Frameworks supporting (ancoram um doc)" (linha 41) | `fundamentos.md` (link simples ao doc basta para D-01; se quiser ancora de secao: `#frameworks-supporting-ancoram-um-doc`) | SIM |
| D-09 GRR | GRR 3 fases (dono da sintaxe) | `reference.md` | `### Sintaxe nova de verdade: "eu faco -> nos fazemos -> voce faz"` (linha 406) | `reference.md#sintaxe-nova-de-verdade-eu-faco---nos-fazemos---voce-faz` | SIM — CONFERIR slug (caracteres `:`/`"`/`->` no heading complicam; ver nota abaixo) |
| D-09 retrieval | recuperacao ativa na abertura | `tutor.md` | `## Passo 1 — Recuperacao ativa (antes do recap)` (linha 37) | `tutor.md#passo-1--recuperacao-ativa-antes-do-recap` | SIM (Fase 4 ja rodou) |
| D-09 gate | mastery gate de fechamento | `fecha-marco.md` | `## Passo 1 — Mastery gate: verificacao do "done"` (linha 12) | `fecha-marco.md#passo-1--mastery-gate-verificacao-do-done` | SIM (Fase 4 ja rodou) |
| D-04 fronteira | mastery gate por marco vive la | `fecha-marco.md` | idem acima (`## Passo 1 — Mastery gate...`) | `fecha-marco.md#passo-1--mastery-gate-verificacao-do-done` | SIM |
| D-07 ponteiro | forense tri-partida | `debug.md` (mesmo milestone, editado nesta fase) | `# Protocolo de Debug / Forense` (titulo) — o ponteiro usa o comando `/debug`, nao precisa de #ancora | `/debug` (convencao de roteamento) ou `debug.md` | SIM |

**Nota critica sobre o slug GRR (D-09):** o heading `### Sintaxe nova de verdade: "eu faco
-> nos fazemos -> voce faz"` contem `:`, aspas e `->`. O renderer (GitHub) gera o slug
removendo pontuacao e colapsando hifens — o resultado exato e fragil de prever a olho.
**Recomendacao para o planner:** (a) o executor deve confirmar o slug abrindo o
`reference.md` renderizado e clicando, OU (b) — preferivel e mais robusto — linkar GRR ao
heading mais estavel `### Sintaxe nova de verdade...` mas tambem aceitar como alternativa o
link ja existente que o proprio `reference.md` usa para GRR: a ancora de fundamentos
`fundamentos.md#frameworks-foundational-load-bearing` (reference.md:412). POReM D-09 trava o
dono como `reference.md` (a SINTAXE GRR), nao `fundamentos.md` (a teoria). Mantenha o link
para `reference.md`; o ANCHOR-RESOLVE do `check-phase5.sh` deve grepar o HEADING LITERAL
(`^### Sintaxe nova de verdade`) em vez de tentar reconstruir o slug — isso prova que o
alvo existe sem depender da regra de slug. O slug exato fica como verificacao manual
(1 clique no renderer) no gate, igual a Fase 4 fez para `#sdt-relatedness-em-solo-ia`.

**Forward-reference status:** NENHUMA ancora de D-09 esta quebrada hoje. `tutor.md` e
`fecha-marco.md` ja estao no estado pos-Fase-4 (li ambos: contem os headings `## Passo 1 —
Recuperacao ativa...` e `## Passo 1 — Mastery gate...`). Como a Fase 4 executa antes da
Fase 5 (ordem 1->...->6), o risco de anchor-miss e BAIXO. O executor ainda re-confirma no
gate (ANCHOR-RESOLVE).

## Runtime State Inventory

> Fase de edicao de doc — sem datastore, servico, OS-state, secret ou build artifact que
> carregue strings renomeadas. Esta fase ADICIONA prosa/links; nao renomeia identificadores.

| Categoria | Itens encontrados | Acao |
|-----------|-------------------|------|
| Stored data | Nenhum — verificado: a fase nao toca `.projetos/` nem nenhum datastore | nenhuma |
| Live service config | Nenhum — sem servico externo; docs markdown estaticos | nenhuma |
| OS-registered state | Nenhum — sem tasks/daemons | nenhuma |
| Secrets/env vars | Nenhum — sem secrets envolvidos | nenhuma |
| Build artifacts | Nenhum — sem compilacao; os 2 scripts shell de Wave 0 sao novos, nao artefatos stale | nenhuma |

**Risco de drift especifico desta fase (PITFALLS P12):** editar `metodo.md` + `debug.md`
pode introduzir conteudo nos adaptadores (`.claude/`, `AGENTS.md`) por engano. NAO copie a
regra anti-leak nem a forense tri-partida para os adaptadores — eles so apontam. A auditoria
da Fase 6 (CONS-03) checa isso, mas o `check-phase5.sh` pode incluir um check defensivo
(jargao novo NAO aparece em `AGENTS.md`/`.claude/`).

## Common Pitfalls

### Pitfall 1: Duplicar a definicao da forense (drift fonte-unica)
**What goes wrong:** D-07 vira uma copia da reescritura tri-partida dentro de `metodo.md`.
**Why it happens:** Tentacao de "deixar completo" no doc que o agente le primeiro.
**How to avoid:** D-07 e PONTEIRO — no maximo 1 linha + link `/debug`. A definicao mora SO
em `debug.md`. Check: a string "feed-up"/"feed-back"/"feed-forward" aparece em `debug.md`,
mas em `metodo.md` so como nome "feedback tri-partido" + link (nao a definicao dos 3).
**Warning signs:** Os 3 rotulos de Hattie definidos em dois docs; `metodo.md` ganhando
mais de ~1-2 linhas no resumo de forense.

### Pitfall 2: Check formativo virando rubrica (over-formalizacao)
**What goes wrong:** O "novo passo" de D-03 cresce numa lista de criterios / quiz.
**Why it happens:** AVAL-05 e LOW-confidence; a tentacao de "robustecer" e forte.
**How to avoid:** Guardrail literal de D-04 escrito NO doc: "exatamente 1 pergunta de
auto-explicacao; se virou checklist ou rubrica, esta errado". O `check-phase5.sh` grepa
esse guardrail.
**Warning signs:** Mais de 1 pergunta no passo formativo; aparicao de palavra "rubrica"
ou "criterios" como instrucao (nao como guardrail negativo).

### Pitfall 3: Anti-leak mal-escopo (falso-positivo na prosa)
**What goes wrong:** O verificador grepa o doc inteiro e acusa "Bloom"/"retrieval" na prosa
legitima (que o agente PODE ler), ou o autor remove nomes de framework da prosa por medo.
**Why it happens:** Confundir "o que o agente le" com "o que o aluno ve".
**How to avoid:** O anti-leak (V-anti-leak) roda SO sobre `extract-fenced.sh` (blocos
cercados). A prosa pode nomear frameworks e linkar `fundamentos.md`. CONS-01 restringe o
que o agente DIZ AO ALUNO na sessao, nao a prosa do procedimento (nuance da Fase 3).
**Warning signs:** Check anti-leak falhando por causa de prosa; regra anti-leak removendo
o proprio link para `fundamentos.md` que D-01 exige.

### Pitfall 4: Slug de ancora quebrado (especialmente GRR)
**What goes wrong:** O `#slug` linkado nao casa o heading real (heading do GRR tem `:`/`"`/`->`).
**Why it happens:** Regra de slug do GitHub e dificil de prever a olho.
**How to avoid:** ANCHOR-RESOLVE grepa o HEADING LITERAL (`^### Sintaxe nova de verdade`),
nao o slug reconstruido — prova que o alvo existe. O slug exato e verificacao manual de 1
clique no gate (igual Fase 4 fez para SDT). Manter o dono = `reference.md` (D-09).
**Warning signs:** Link 404 no renderer; ANCHOR-RESOLVE passando mas o clique nao salta.

### Pitfall 5: Reescrever em vez de overlay (D-05/D-08)
**What goes wrong:** Os 6 passos do `debug.md` ou os 5 itens do ciclo sao reescritos.
**Why it happens:** "Fica mais limpo reorganizar."
**How to avoid:** D-05 e D-08 sao explicitamente OVERLAY/INLINE — adicione rotulos e links,
nao reestruture. Check: `count` dos 6 sub-headings de `debug.md` e dos 5 itens do ciclo
permanece igual ao baseline (nenhum passo some).
**Warning signs:** Numero de passos/itens muda; o protocolo de 6 passos vira 3 secoes.

## Code Examples

> "Code" aqui = padroes de verificacao estatica (shell) + forma de edicao markdown.

### Anti-leak check (CONS-01) — clone do padrao V-15 da Fase 4
```sh
# Source: .planning/phases/04-.../scripts/check-phase4.sh:120-126 (VERIFIED)
LEAK_PAT='SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect|feed-up|feed-back|feed-forward|Hattie|formativ|auto-explicacao'
leak=$(sh "$DIR/extract-fenced.sh" "mentor/metodo.md" | rg -c "$LEAK_PAT" 2>/dev/null || echo 0)
check_zero "ANTI-LEAK-METODO" "$leak"
# idem para mentor/debug.md
```
**Nota:** ajustar o `LEAK_PAT` para incluir os termos novos da Fase 5 (Hattie/feed-*/
formativo/auto-explicacao) — eles podem aparecer na PROSA (ok) mas NAO em blocos cercados
que viram artefato do aluno. Use a forma de FRASE quando o token isolado for ambiguo (ex:
`retrieval practice`, nao `retrieval` solto — `## Agenda de retrieval` e rotulo legitimo).

### ANCHOR-RESOLVE — confirma que cada link D-09 casa heading real
```sh
# Source: padrao V-14 de check-phase4.sh:111-118 (VERIFIED)
if rg -q '^### Sintaxe nova de verdade' mentor/reference.md 2>/dev/null && \
   rg -q '^## Passo 1 — Recuperacao ativa' mentor/tutor.md 2>/dev/null && \
   rg -q '^## Passo 1 — Mastery gate' mentor/fecha-marco.md 2>/dev/null; then
  printf 'PASS  %-16s as 3 ancoras D-09 resolvem\n' "V-ANCHOR"
else
  printf 'FAIL  %-16s ancora D-09 ausente\n' "V-ANCHOR"; fails=$((fails+1))
fi
```

### Presenca de regra/link (check_min) — exemplos por criterio
```sh
# CONS-01: metodo.md cita fundamentos.md (1a ponte) + tem o espelho na lista
check_min "CONS-01-link"  "$(count 'fundamentos\.md' mentor/metodo.md)" 1
check_min "CONS-01-corpo" "$(count 'jargao|nunca .*ao aluno|nunca .*citad' mentor/metodo.md)" 1
# AVAL-05: guardrail literal "exatamente 1 pergunta"
check_min "AVAL-05-guard" "$(count 'exatamente 1|1 pergunta de auto-explicacao' mentor/metodo.md)" 1
check_min "AVAL-05-fronteira" "$(count 'fecha-marco' mentor/metodo.md)" 1
# AVAL-06: debug.md nomeia as 3 lentes + PISTA=feed-forward
check_min "AVAL-06-lentes" "$(count 'feed-up|feed-back|feed-forward' mentor/debug.md)" 3
check_min "AVAL-06-pista"  "$(count 'PISTA.*feed-forward|feed-forward.*PISTA|PISTA.*sem .*resposta' mentor/debug.md)" 1
# Criterio 4: ciclo nomeia GRR/retrieval/gate por link
check_min "C4-grr"       "$(count 'reference\.md' mentor/metodo.md)" 1
check_min "C4-retrieval" "$(count 'tutor\.md|/tutor' mentor/metodo.md)" 1
check_min "C4-gate"      "$(count 'fecha-marco\.md|/fecha-marco' mentor/metodo.md)" 1
```

## State of the Art

Nao se aplica (sem ecossistema de software em movimento). O "estado da arte" relevante e o
harness de verificacao do proprio repo, que evoluiu Fase 2 -> Fase 4:

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Revisao manual de doc | `check-phase2.sh` (grep estatico PASS/FAIL) | Fase 2 | Verificacao deterministica de propriedades de doc |
| grep cru no doc inteiro | `extract-fenced.sh` isola blocos cercados p/ anti-leak | Fase 2 | Anti-leak sem falso-positivo na prosa |
| slug adivinhado | ANCHOR-RESOLVE (grep do heading literal) + 1 clique manual | Fase 4 | Prova que o alvo do link existe sem depender da regra de slug |

**Deprecated/outdated:** nada. Clone o padrao da Fase 4 verbatim.

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | O slug exato do heading GRR em `reference.md` (com `:`/`"`/`->`) nao foi confirmado num renderer — so o heading literal foi verificado por grep | Mapa de ancoras / Pitfall 4 | Link D-09 pode 404 no renderer; mitigado por ANCHOR-RESOLVE no heading literal + 1 clique manual no gate |
| A2 | A posicao ideal da regra anti-leak no corpo (apos "Regra de ouro") e sugestao; o executor tem discricao de posicionar onde o agente le cedo | Criterio 1 mapa | Baixo — qualquer posicao cedo no doc satisfaz CONS-01; e Claude's Discretion |
| A3 | 3 planos (Wave 0 + metodo + debug) e a granularidade recomendada; o planner pode fundir metodo+debug num so se preferir | Recommended Plan Structure | Baixo — disjuntos por arquivo, paralelizaveis; fundir nao quebra nada |
| A4 | A inclusao de um check defensivo "jargao novo nao vaza para adaptadores" no `check-phase5.sh` e sugestao (a auditoria formal e Fase 6/CONS-03) | Runtime State Inventory | Baixo — defensivo; ausencia nao bloqueia a fase |

## Open Questions

1. **Slug exato do heading GRR em `reference.md`**
   - What we know: o heading literal e `### Sintaxe nova de verdade: "eu faco -> nos fazemos -> voce faz"` (verificado por leitura).
   - What's unclear: o `#slug` gerado pelo renderer (pontuacao/aspas/`->`).
   - Recommendation: ANCHOR-RESOLVE grepa o heading literal; slug confirmado por 1 clique
     manual no gate (mesma estrategia da Fase 4 para SDT). Manter dono = `reference.md`.

2. **`metodo.md` deve linkar a ancora de secao de `fundamentos.md` ou so o doc?**
   - What we know: D-01 exige "link para `fundamentos.md` como o porque". O preambulo de
     `fundamentos.md` (linhas 3-8) ja declara FUND-03; a tabela "Frameworks supporting"
     (linha 41) lista Avaliacao Formativa e Hattie.
   - What's unclear: granularidade do link (doc inteiro vs `#frameworks-supporting...`).
   - Recommendation: link simples ao doc (`fundamentos.md`) satisfaz D-01/D-02/CONS-01 e e
     mais robusto (sem dependencia de slug). Ancora de secao e opcional/Claude's discretion.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| `rg` (ripgrep) | `check-phase5.sh` | ✓ | provado por Fase 2/4 | — |
| `awk` | `extract-fenced.sh` | ✓ | POSIX, provado | — |
| `sh` (POSIX) | harness wrapper | ✓ | provado | — |

**Missing dependencies with no fallback:** Nenhum.
**Missing dependencies with fallback:** Nenhum.

## Validation Architecture

> `nyquist_validation: true` em config.json — secao incluida. DOC-EDITING phase: sem
> runtime/framework de teste. Validacao = grep estatico (presenca/ausencia + ANCHOR-RESOLVE
> + anti-leak em blocos cercados), modelado verbatim no harness das Fases 2 e 4.

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Nenhum — `rg`/`awk`/`sh` via `check-phase5.sh` + `extract-fenced.sh` |
| Config file | Nenhum — `extract-fenced.sh` clonado verbatim no scripts dir da Fase 5 (Wave 0) |
| Quick run command | `rg -n "<padrao do criterio tocado>" mentor/<file>.md` |
| Full suite command | `sh .planning/phases/05-persona-e-feedback-metodo-md-debug-md/scripts/check-phase5.sh` |

### Phase Requirements -> Test Map
| Check ID | Req / SC | Behavior | Test Type | Automated Command (static) | File Exists? |
|----------|----------|----------|-----------|----------------------------|--------------|
| V-01 | CONS-01 / SC1 | corpo de `metodo.md` declara regra anti-leak + link `fundamentos.md` (1a ponte) | grep | `rg -n "fundamentos\.md" mentor/metodo.md` | ❌ Wave 0 |
| V-02 | CONS-01 / SC1 | regra nomeia "nunca ao aluno / jargao" no corpo | grep | `rg -n "jargao\|nunca .*ao aluno\|nunca .*citad" mentor/metodo.md` | ❌ Wave 0 |
| V-03 | CONS-01 / D-02 | FUND-03 (doc interno, nunca lido pelo aluno) no mesmo lugar | grep | `rg -n "interno\|nunca .*lido pelo aluno\|injetad" mentor/metodo.md` | ❌ Wave 0 |
| V-04 | CONS-01 / D-01 | espelho na lista "Anti-padroes (NUNCA faca)" | grep | `rg -n "jargao.*aluno\|framework.*aluno" mentor/metodo.md` (apos linha do heading 141) | ❌ Wave 0 |
| V-05 | AVAL-05 / SC2 | novo passo de auto-explicacao no gate de curadoria | grep | `rg -n "auto-explicacao\|me explica por que\|explicar.*antes de curar" mentor/metodo.md` | ❌ Wave 0 |
| V-06 | AVAL-05 / D-04 | guardrail literal "exatamente 1 pergunta / nao rubrica" | grep | `rg -n "exatamente 1\|checklist ou rubrica\|esta errado" mentor/metodo.md` | ❌ Wave 0 |
| V-07 | AVAL-05 / D-04 | nota de fronteira aponta `fecha-marco.md` (mastery gate por marco la) | grep | `rg -n "fecha-marco" mentor/metodo.md` | ❌ Wave 0 |
| V-08 | AVAL-06 / SC3 | as 3 lentes de Hattie nomeadas em `debug.md` | grep | `rg -c "feed-up\|feed-back\|feed-forward" mentor/debug.md` (>= 3) | ❌ Wave 0 |
| V-09 | AVAL-06 / D-06 | PISTA enquadrada como feed-forward (sem entregar a resposta) | grep | `rg -n "PISTA.*feed-forward\|feed-forward.*PISTA\|PISTA.*sem .*resposta" mentor/debug.md` | ❌ Wave 0 |
| V-10 | AVAL-06 / D-05 | os 6 passos PRESERVADOS (overlay, nao reescrita) | grep order | `rg -c "^### [1-6]\." mentor/debug.md` (== 6) | ❌ Wave 0 |
| V-11 | C4 / D-09 | ciclo linka GRR -> `reference.md` | grep | `rg -n "reference\.md" mentor/metodo.md` | ❌ Wave 0 |
| V-12 | C4 / D-09 | ciclo linka retrieval -> `tutor.md` | grep | `rg -n "tutor\.md\|/tutor" mentor/metodo.md` | ❌ Wave 0 |
| V-13 | C4 / D-09 | ciclo linka gate -> `fecha-marco.md` | grep | `rg -n "fecha-marco\.md\|/fecha-marco" mentor/metodo.md` | ❌ Wave 0 |
| V-14 | C4 / D-08 | os 5 itens do ciclo PRESERVADOS (inline, nao bloco novo) | grep | `rg -c "^[1-5]\." dentro da secao "Conduta por marco (ciclo)"` (== 5) | ❌ Wave 0 |
| V-15 | D-07 | `metodo.md` mantem ponteiro curto p/ /debug nomeando "feedback tri-partido" | grep | `rg -n "feedback tri-partido" mentor/metodo.md` + `rg -n "/debug\|debug\.md" mentor/metodo.md` | ❌ Wave 0 |
| V-16 | ANCHOR-RESOLVE | cada `#`/doc linkado por D-09 casa heading real no dono | anchor | `rg -q '^### Sintaxe nova de verdade' reference.md` AND `rg -q '^## Passo 1 — Recuperacao ativa' tutor.md` AND `rg -q '^## Passo 1 — Mastery gate' fecha-marco.md` | ❌ Wave 0 |
| V-17 | CONS-01 (anti-leak) | nenhum jargao de framework DENTRO de bloco cercado de `metodo.md` nem `debug.md` | grep negative | `sh scripts/extract-fenced.sh mentor/metodo.md \| rg -c "<LEAK_PAT>"` -> 0; idem `debug.md` | ❌ Wave 0 |
| V-18 (defensivo) | P12 anti-drift | jargao novo (Hattie/feed-*/formativo) NAO vaza para adaptadores | grep negative | `rg -c "feed-up\|feed-back\|Hattie" AGENTS.md .claude/` -> 0 | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** `rg` do criterio tocado + anti-leak grep quando um bloco cercado for tocado
- **Per wave merge:** `sh scripts/check-phase5.sh` + a CONTRACT/ANCHOR-RESOLVE
- **Phase gate:** suite verde + 1 clique manual no link GRR (confirma slug A1) antes de `/gsd-verify-work`

### Wave 0 Gaps
- [ ] `.planning/phases/05-persona-e-feedback-metodo-md-debug-md/scripts/extract-fenced.sh` — clone verbatim da Fase 4
- [ ] `.planning/phases/05-persona-e-feedback-metodo-md-debug-md/scripts/check-phase5.sh` — autorar de `check-phase4.sh`, codificar V-01..V-18
- [ ] Sem framework install — `rg`/`awk`/`sh` ja presentes (provado por Fase 2/4)

*Baseline antes das edicoes: checks positivos FALHAM (esperado); V-16 (ANCHOR-RESOLVE) e
V-17/V-18 (anti-leak, baseline 0) PASSAM — mesma convencao das Fases 2 e 4.*

## Security Domain

> N/A — justificado. Fase de edicao de documentacao markdown + 2 scripts shell de
> verificacao estatica que rodam SO localmente sobre arquivos versionados do repo. Sem
> autenticacao, rede, parsing de input nao-confiavel, cripto ou manuseio de dados. Nenhuma
> categoria ASVS se aplica (mesma conclusao das Fases 2 e 4). A unica preocupacao de
> integridade e editorial (anti-drift P12 / anti-leak CONS-01), ja coberta pela Validation
> Architecture (V-17 anti-leak, V-18 anti-drift defensivo, V-16 anchor-resolve).

| Trust Boundary | Description |
|----------------|-------------|
| N/A | Sem boundary de runtime — scripts shell locais sobre arquivos do repo |

## Sources

### Primary (HIGH confidence)
- `mentor/metodo.md` (lido integral) — secoes-alvo: Regra de ouro (12-16), Conduta por marco (32-62), Gate de curadoria (64-75), Protocolo de forense (77-89), Anti-padroes (141-165)
- `mentor/debug.md` (lido integral) — 6 passos (14-87), ponto da PISTA (passo 5, linha 73)
- `mentor/fundamentos.md` (lido integral) — preambulo FUND-03 (3-8), Avaliacao Formativa + Hattie na tabela Frameworks supporting (41-50)
- `mentor/reference.md` (lido integral) — heading GRR "Sintaxe nova de verdade" (406), Protocolo de forense duplicado (435-444 — nota de drift potencial), Formato do scaffold/PISTA (356-433)
- `mentor/tutor.md` (lido integral) — `## Passo 1 — Recuperacao ativa (antes do recap)` (37)
- `mentor/fecha-marco.md` (lido integral) — `## Passo 1 — Mastery gate: verificacao do "done"` (12)
- `.planning/phases/04-.../scripts/check-phase4.sh` + `04-VALIDATION.md` + `04-01-PLAN.md` — harness de verificacao a clonar (VERIFIED)
- `.planning/codebase/ARCHITECTURE.md` (fonte-unica + adaptadores finos) e `CONVENTIONS.md` (pt sem acento, backticks)

### Secondary (MEDIUM confidence)
- `.planning/research/SUMMARY.md` §Avaliacao & feedback; `FEATURES.md` (check formativo LOW, Hattie MEDIUM, auto-explicacao LOW); `PITFALLS.md` (P9 teoria vazando, P12 drift, P6 feedback acionavel)

### Tertiary (LOW confidence)
- Nenhuma fonte externa consultada — fase de costura editorial sobre conteudo ja decidido.

## Metadata

**Confidence breakdown:**
- Mapa de criterios -> ancora: HIGH — headings literais verificados por leitura direta dos 6 docs
- Ancoras de hyperlink (D-09): HIGH para tutor/fecha (Fase 4 ja rodou); MEDIUM para o slug exato do GRR (heading verificado; slug fragil — A1)
- Verificacao (Validation Architecture): HIGH — clone de harness provado em 3 fases
- Pitfalls: HIGH — derivados de PITFALLS.md + nuance anti-leak ja confirmada na Fase 3/4

**Research date:** 2026-06-15
**Valid until:** estavel (sem dependencia de ecossistema externo); re-confirmar ancoras de
D-09 no momento da execucao da Fase 5 (apos a Fase 4) via ANCHOR-RESOLVE.
