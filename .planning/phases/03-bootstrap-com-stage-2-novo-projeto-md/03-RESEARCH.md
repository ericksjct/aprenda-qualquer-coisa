# Phase 3: Bootstrap com Stage 2 (novo-projeto.md) - Research

**Researched:** 2026-06-14
**Domain:** Edicao de procedimento markdown (design instrucional) lido pelo AGENTE -- nao codigo, nao teoria nova
**Confidence:** HIGH (teoria fixada; ancoras reais verificadas por leitura dos arquivos-fonte)

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01 (EST-03, posicionamento):** Stage 2 em DOIS niveis, sem renumerar o doc:
  - **Nivel macro (Passo 4):** o Passo 4 ja faz "engenharia reversa do output final ->
    capacidades necessarias". Apenas NOMEAR isso como backward design, com 1 frase +
    hyperlink para `fundamentos.md`. Nenhuma reescrita do mecanismo.
  - **Nivel marco (Passo 5):** quando cada marco ganha sua User Story na montagem
    (Passo 5), o agente escreve JUNTO a frase de capacidade daquele marco. As duas
    nascem coladas. Este e o "Stage 2" propriamente dito.
  - **Rejeitado:** passo separado novo entre 4 e 5; reembrulhar tudo em "Stages 1/2/3".
  - Registrar no plano a interpretacao do "entre caminho e marcos" (ver abaixo).

- **D-02 (EST-03, onde a frase mora):** A frase de capacidade por marco vai no
  `PROGRESSO.md`, colada na User Story de cada marco na arvore de marcos. Persistir e
  obrigatorio: o gate da Fase 4 (`fecha-marco.md`) vai PROCURAR essa frase ali.
  - `CAMINHO.md` mantem capacidade por PASSO (Fase 2); `PROGRESSO.md` ganha capacidade
    por MARCO. Nao misturar os dois.
  - Anti-leak: como `PROGRESSO.md` e lido pelo aluno, a frase usa o formato puro da
    Fase 2 ("ao terminar, voce consegue <verbo> <conceito>"), sem "Bloom", "maestria"
    ou "backward design".
  - **Dependencia de template:** o template do `PROGRESSO.md` mora em `reference.md`.
    Se a arvore de marcos do template nao tiver o campo de capacidade por marco, o plano
    da Fase 3 precisa adiciona-lo la. (Confirmado nesta pesquisa: NAO tem -- ver achado 2.)

- **D-03 (ENG-02, primeiro done leve):** Ancorar o principio no Passo 8 (Walking Skeleton).
  - **Passo 8:** nomear "primeiro done leve" + porque (reduzir time-to-first-success =
    anti-evasao do async) + hyperlink para `fundamentos.md`. ROTULAGEM de algo que ja
    existe, nao mecanismo novo.
  - **Passo 5:** reforco leve de 1 linha -- dimensionar o primeiro marco como o menor
    possivel, para a primeira vitoria vir rapido.
  - **Rejeitado:** principio geral no topo do doc.

- **D-04 (EST-03, leveza / anti over-formalizacao):** Stage 2 OBRIGATORIO por marco, com
  TETO RIGIDO de exatamente 1 frase no formato verbo-capacidade. Guardrail explicito no
  `novo-projeto.md`: "Stage 2 = exatamente 1 frase de capacidade por marco. Se virou
  lista, rubrica ou sub-doc, esta errado -- corte."
  - NAO opcional / NAO escalavel: rejeitada a opcao de pular em projetos com muitos
    marcos. O controle de leveza e o TAMANHO (1 frase), nao a opcionalidade.

### Claude's Discretion

- Texto exato das frases de nomeacao (backward design no Passo 4; primeiro done leve no
  Passo 8) e a posicao precisa das ancoras de hyperlink. O executor confere as ancoras
  reais ao linkar. (Esta pesquisa ja listou as ancoras reais -- ver achado 1.)

### Deferred Ideas (OUT OF SCOPE)

- Campo de agenda de retrieval/dividas no `PROGRESSO.md` -- pertence a Fase 4
  (ENG-01/AVAL-02), NAO a esta fase.
- Confirmacao final de que cada "(Fase 3, pendente)" do `fundamentos.md` virou aplicacao
  real -- auditoria da Fase 6 (CONS-02).
- Mitigacao "campo opcional para muitos marcos" sugerida na pesquisa de projeto --
  REJEITADA aqui (D-04).
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| EST-03 | O bootstrap (`novo-projeto.md`) insere um Stage 2 (evidencia de maestria por marco) entre o Passe 1 e a montagem de marcos, com ~1 frase de capacidade por marco | Achados 1, 2, 3 (pontos de insercao Passo 4 + Passo 5; campo no template `PROGRESSO.md`; ancoras de hyperlink) |
| ENG-02 | O metodo nomeia e reforca o "primeiro done leve" (reduzir time-to-first-success) como principio anti-evasao, conectado ao Walking Skeleton | Achados 1 (ancora de hyperlink -- LACUNA), 3 (ponto de insercao Passo 8 + reforco Passo 5) |
</phase_requirements>

## Summary

Esta e uma fase de EDICAO cirurgica de um unico arquivo (`mentor/novo-projeto.md`) mais
uma adicao de campo no template de `mentor/reference.md`. Nenhum conteudo teorico novo: a
teoria (backward design/UbD Stage 2, time-to-first-success, Walking Skeleton) ja esta
catalogada em `mentor/fundamentos.md` (HIGH confidence) e e CITADA por hyperlink, nunca
redefinida (regra fonte-unica). As decisoes de FORMA (D-01..D-04) ja estao travadas. A
pesquisa fechou os 4 pontos MEDIUM/abertos que o planner precisava:

1. **Ancoras reais de `fundamentos.md`** confirmadas por leitura. O backward design e
   alcancavel hoje pela ancora `#frameworks-foundational-load-bearing` (ja usada por
   `reference.md`). **LACUNA CRITICA para ENG-02:** NAO existe heading dedicado para
   time-to-first-success / anti-evasao em `fundamentos.md`; o conceito mora na LINHA da
   tabela SDT e na ressalva SDT. O planner precisa decidir o alvo do link do Passo 8
   (ver achado 1 + Open Question 1).
2. **Template do `PROGRESSO.md` (`reference.md`) NAO tem campo de capacidade por marco.**
   A arvore de marcos hoje tem `User Story`, `Passos do caminho`, `Entregavel` e checkbox
   de done -- nenhum campo `Capacidade`. D-02 exige adiciona-lo la. Isto e uma tarefa
   concreta do plano, nao "pendente da Fase 2".
3. **Pontos de insercao em `novo-projeto.md` mapeados** com trechos-ancora exatos (Passo
   4 linhas 56-57; Passo 5 linhas 76-78; Passo 8 linhas 128-147) -- o planner escreve
   `<action>` por linha-alvo.
4. **Formato verbo-capacidade confirmado como canonico:** "ao terminar, voce consegue
   <verbo> <conceito>" e exatamente o que `reference.md` usa hoje no nivel de PASSO
   (linhas 76, 85, 294). Reusar identico no nivel de MARCO mantem coerencia total.

**Primary recommendation:** O plano e 3 edicoes em `novo-projeto.md` (Passo 4 nomeia
backward design + link; Passo 5 instrui gravar a frase de capacidade junto da User Story
+ reforco do primeiro marco menor; Passo 8 nomeia "primeiro done leve" + link) e 1 edicao
em `reference.md` (adicionar campo `Capacidade:` na arvore de marcos do template
`PROGRESSO.md`). Resolver primeiro o alvo do link do Passo 8 (Open Question 1).

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Nomear backward design (Stage 2 macro) | Procedimento (`novo-projeto.md` Passo 4) | Referencia teorica (`fundamentos.md` via link) | Prosa lida pelo AGENTE; pode nomear framework e linkar |
| Gravar frase de capacidade por marco (Stage 2 marco) | Procedimento (`novo-projeto.md` Passo 5) instrui; Template (`reference.md`) define o campo | Artefato do aluno (`PROGRESSO.md`) persiste | A instrucao mora no procedimento; o campo onde gravar mora no template; o dado final mora no artefato lido pelo aluno (anti-leak: verbo puro) |
| Nomear "primeiro done leve" (ENG-02) | Procedimento (`novo-projeto.md` Passo 8) | Referencia teorica (`fundamentos.md` via link) | Rotulagem de mecanismo ja existente (Walking Skeleton) |
| Guardrail de leveza (D-04) | Procedimento (`novo-projeto.md` Passo 5/Stage 2) | -- | Regra de conduta para o agente; texto de teto rigido inline na prosa |
| Definir a teoria citada | `mentor/fundamentos.md` (upstream) | -- | NUNCA editado nesta fase; so e alvo dos links (fonte-unica) |

**Boundary critica (anti-leak CONS-01):** ha DOIS publicos. A **prosa de
`novo-projeto.md`** e lida pelo AGENTE -> pode nomear "backward design", "Stage 2",
"primeiro done leve", "time-to-first-success" e linkar `fundamentos.md`. A **frase gravada
no `PROGRESSO.md`** e lida pelo ALUNO -> so o verbo de capacidade puro, zero jargao. O
plano precisa instruir os dois registros separadamente.

## Standard Stack

Nao se aplica (fase de edicao de markdown; sem libraries, sem instalacao). Os "componentes"
sao arquivos do toolkit:

| Arquivo | Papel nesta fase | Acao |
|---------|------------------|------|
| `mentor/novo-projeto.md` | UNICO procedimento editado | 3 edicoes (Passos 4, 5, 8) |
| `mentor/reference.md` | Dono do template `PROGRESSO.md` | 1 edicao (campo `Capacidade:` na arvore de marcos) |
| `mentor/fundamentos.md` | Upstream teorico | SO alvo de hyperlink; NAO editar |

## Achado 1: Ancoras reais de `fundamentos.md` (para os hyperlinks D-01/D-03)

**Verificado por leitura de `mentor/fundamentos.md` e dos links existentes em
`mentor/reference.md`.** O toolkit usa ancoras GitHub-style derivadas do heading
(minusculas, espacos -> hifen, pontuacao removida). Ancoras CONFIRMADAS em uso hoje:

| Heading real em `fundamentos.md` | Ancora (slug) | Ja usada por |
|----------------------------------|---------------|--------------|
| `## Frameworks foundational (load-bearing)` (linha 19) | `#frameworks-foundational-load-bearing` | `reference.md:34,98,406` [VERIFIED: grep] |
| `### Mayer: so 3 de 12 principios em texto puro` (linha 70) | `#mayer-so-3-de-12-principios-em-texto-puro` | `reference.md:348` [VERIFIED: grep] |
| `### SDT relatedness em solo+IA` (linha 62) | `#sdt-relatedness-em-soloia` | (nenhum link ainda; ressalva existente) [VERIFIED: leitura] |

### Backward design (D-01, Passo 4) -- ancora PRONTA

A linha da tabela de Backward Design / UbD vive sob `## Frameworks foundational
(load-bearing)` (`fundamentos.md:24`). O link canonico ja existe e e exatamente o que
`reference.md:98` usa para "backward design":

```markdown
[backward design](fundamentos.md#frameworks-foundational-load-bearing)
```

**Recomendacao:** o Passo 4 reusa esse MESMO alvo de link. Coerencia com `reference.md`
garantida. A linha da tabela ja diz, no campo "Aplicado em": "`mentor/novo-projeto.md`
(Fase 2/3, pendente)" (`fundamentos.md:24`) -- esta fase materializa o "Fase 3, pendente".
[VERIFIED: leitura fundamentos.md:24]

### Primeiro done leve / time-to-first-success (D-03, Passo 8) -- LACUNA

**NAO existe heading dedicado a "time-to-first-success", "anti-evasao", "Walking Skeleton"
ou "primeiro done leve" em `fundamentos.md`.** [VERIFIED: grep por todos esses termos
retornou so a tabela SDT e a ressalva]. O conceito mais proximo catalogado e o **SDT**, cuja
linha de tabela (`fundamentos.md:45`) lista no campo "Termo no metodo":

> "Anti-evasao; 'proxima acao unica' ...; autonomia (aluno escolhe o projeto real) +
> competencia (entregavel observavel por marco / micro-vitorias)"

Ou seja, o ANCORADOURO teorico de "reduzir time-to-first-success como anti-evasao" e a
**competencia/anti-evasao da SDT**, nao um heading proprio. Opcoes para o planner (ver
Open Question 1):

- **Opcao A (recomendada, menor atrito):** linkar para a ancora da SDT. O heading
  mais especifico e `### SDT relatedness em solo+IA` -> `#sdt-relatedness-em-soloia`.
  Risco: essa secao e a *ressalva* (relatedness fraca), nao a afirmacao positiva de
  anti-evasao -- pode confundir o leitor-agente.
- **Opcao B:** linkar para `## Frameworks supporting (ancoram um doc)`
  (`fundamentos.md:41`), onde a linha SDT vive. Slug provavel:
  `#frameworks-supporting-ancoram-um-doc`. Aponta para a linha-fonte da SDT.
- **Opcao C (mais invasiva, fora do escopo travado):** adicionar um heading/ressalva nova
  em `fundamentos.md` para time-to-first-success. **Conflita com a regra de que
  `fundamentos.md` NAO e editado nesta fase** e com a build-order (fundamentos = Fase 1).
  NAO recomendada sem re-discussao.

**Nota sobre status "aplicado em":** a SDT em `fundamentos.md:45` lista "aplicado em
`mentor/tutor.md`, `PROGRESSO.md` ... (Fase 4, pendente)" -- NAO lista `novo-projeto.md`.
Se o Passo 8 linkar SDT para ENG-02, ha um leve descompasso de rastreabilidade que a
auditoria da Fase 6 (CONS-02) pode apontar. O planner deve decidir conscientemente
(o ajuste do campo "aplicado em" de `fundamentos.md` seria, a rigor, Fase 6, nao Fase 3).

## Achado 2: Estado real do template `PROGRESSO.md` em `reference.md` (D-02)

**Verificado por leitura de `mentor/reference.md:198-248`.** A arvore de marcos do template
`PROGRESSO.md` HOJE e:

```markdown
### 00 -- <slug> (Walking Skeleton)  <- ATUAL

**User Story:** Como [usuario], eu quero [capacidade basica], para que [valor minimo].
**Passos do caminho:** P01-P02 (ver CAMINHO.md)
**Entregavel:** <o que o aluno VE funcionando ao fechar o marco>

- [ ] <criterio de done>
```

**Conclusao:** NAO existe campo `Capacidade:` por marco. [VERIFIED: leitura reference.md:225-239]
A decisao D-02 marcou isso como "confirmar no planning" -- esta confirmado: **o plano da
Fase 3 PRECISA adicionar o campo no template de `reference.md`**, em AMBOS os blocos de
exemplo (marco 00 e marco 01, linhas 225-239).

Forma recomendada (coerente com o exemplo do CONTEXT.md e com o formato da Fase 2):

```markdown
### 00 -- <slug> (Walking Skeleton)  <- ATUAL

**User Story:** Como [usuario], eu quero [capacidade basica], para que [valor minimo].
**Capacidade:** ao terminar, voce consegue <verbo> <conceito>
**Passos do caminho:** P01-P02 (ver CAMINHO.md)
**Entregavel:** <o que o aluno VE funcionando ao fechar o marco>

- [ ] <criterio de done>
```

**Atencao a duas edicoes acopladas:** alterar o template em `reference.md` (define o
campo) E instruir o preenchimento em `novo-projeto.md` Passo 5 (manda o agente escrever a
frase). Uma sem a outra deixa a feature manca: template sem instrucao = campo vazio
ignorado; instrucao sem template = agente sem lugar canonico para gravar.

**Anti-leak (CONS-01) no campo:** o conteudo do campo `Capacidade:` e lido pelo ALUNO
(`PROGRESSO.md` e artefato do aluno -- `ARCHITECTURE.md:45`, `reference.md:188-189`).
Logo o valor e SO o verbo de capacidade puro -- nada de "Bloom", "Stage 2", "maestria".
O rotulo do campo ("Capacidade") tambem e neutro e ja faz parte do vocabulario do metodo
(o `CAMINHO.md` usa "Objetivo (capacidade)") -- sem vazamento.

## Achado 3: Pontos de insercao exatos em `novo-projeto.md`

**Verificado por leitura de `mentor/novo-projeto.md`.** Trechos-ancora onde a costura
entra:

### Passo 4 -- "Passe 1: o caminho completo" (D-01 macro: nomear backward design)

Trecho-ancora (`novo-projeto.md:56-57`):

```markdown
- Engenharia reversa do output final -> capacidades necessarias -> conceitos
  necessarios -> ordene por dependencia (use a referencia do Passo 3 como guia).
```

O mecanismo de backward design JA esta aqui ("engenharia reversa do output final ->
capacidades"). [VERIFIED: leitura] A edicao e ADITIVA: inserir 1 frase que NOMEIA isso
como backward design + hyperlink. Encaixe natural: como nova frase logo apos a linha 57,
ou como inciso na propria linha. Nao reescrever o bullet existente.

### Passo 5 -- "Passe 2: montagem dos marcos" (D-01 marco + D-03 reforco)

Trecho-ancora da User Story (`novo-projeto.md:76-78`):

```markdown
- Enquadre cada marco como **User Story**: "Como [usuario], eu quero [capacidade],
  para que [beneficio]". Historia grande demais -> `/spidr-split` ANTES de seguir.
```

Aqui entram DUAS costuras:
1. **D-01 marco (Stage 2):** instruir o agente a escrever, JUNTO da User Story, a frase de
   capacidade do marco no `PROGRESSO.md`, no formato verbo-capacidade. Encaixe: bullet novo
   logo apos o bullet da User Story (linha 78) -- "as duas nascem coladas" (CONTEXT).
   Incluir aqui o guardrail D-04 (teto de 1 frase).
2. **D-03 reforco (ENG-02):** 1 linha dimensionando o primeiro marco como o menor possivel.
   Encaixe natural junto da regra de granularidade ja citada (`novo-projeto.md:74`, "regra
   de granularidade ... sessao de ~30-90 min") ou junto da Definition of Done (linha 78-79).

Nota: a verificacao de coesao (`reference.md:108-123`) e o checklist mecanico do Passe 2.
Se a frase de capacidade por marco virar item verificavel, o planner PODE (opcional)
adicionar 1 linha de checklist la -- mas D-04 pede leveza; avaliar se vale.

### Passo 8 -- "Walking Skeleton (Marco 00)" (D-03: nomear primeiro done leve)

Trecho-ancora (`novo-projeto.md:128-132`):

```markdown
## Passo 8 -- Walking Skeleton (Marco 00)

O primeiro marco e um **Walking Skeleton** -- o esqueleto mais fino que prova que
todas as camadas funcionam juntas (exemplos por tipo de projeto em `mentor/reference.md`).
Ele NAO implementa logica de negocio.
```

O mecanismo (vitoria rapida) JA existe. [VERIFIED: leitura] A edicao e ROTULAGEM: nomear
"primeiro done leve" + o porque (reduzir time-to-first-success = anti-evasao) + hyperlink
para `fundamentos.md` (alvo a definir -- Open Question 1). Encaixe: 1 frase apos a linha
132, ou junto da instrucao de "Pare e espere a tentativa do aluno" (linha 145-147) que ja
fala do ritmo do aluno.

## Achado 4: Coerencia do formato verbo-capacidade (PASSO -> MARCO)

**Verificado por leitura.** O formato canonico ja vive em `reference.md` no nivel de PASSO,
identico em 3 lugares:

| Local | Texto | Linha |
|-------|-------|-------|
| Template `CAMINHO.md`, P01 | `Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>` | `reference.md:76` |
| Template `CAMINHO.md`, P02 | `Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>` | `reference.md:85` |
| Template aula | `<capacidade: ao terminar, voce consegue <verbo> <conceito>; ...>` | `reference.md:294` |

**Confirmado:** "ao terminar, voce consegue <verbo> <conceito>" e o formato CANONICO da
Fase 2. [VERIFIED: leitura] Reusa-lo identico no nivel de MARCO (campo `Capacidade:` do
`PROGRESSO.md`) mantem coerencia total e e exatamente o exemplo dado no CONTEXT.md
(D-02). A unica diferenca de nivel: o `CAMINHO.md` usa o rotulo "Objetivo (capacidade)"
por PASSO; o `PROGRESSO.md` usa "Capacidade" por MARCO. Manter os dois rotulos distintos
evita confundir os niveis (D-02: "nao misturar os dois no mesmo arquivo").

## Architecture Patterns

### System Architecture Diagram (fluxo da costura)

```
                 mentor/fundamentos.md  (teoria -- NAO editado; so alvo de link)
                   |  backward design (#frameworks-foundational-load-bearing)
                   |  SDT/anti-evasao  (ancora a definir -- Open Question 1)
                   v  (hyperlink, fonte-unica)
   +----------------------------------------------------------+
   |  mentor/novo-projeto.md  (procedimento lido pelo AGENTE) |
   |                                                          |
   |  Passo 4 --[nomeia backward design + link]               |
   |  Passo 5 --[instrui gravar Capacidade por marco]---------+--> grava em
   |          --[reforca: primeiro marco menor]               |    PROGRESSO.md
   |  Passo 8 --[nomeia "primeiro done leve" + link]          |    (artefato do
   +----------------------------------------------------------+     ALUNO: verbo puro)
                   |  usa o template de
                   v
   +----------------------------------------------------------+
   |  mentor/reference.md  (template PROGRESSO.md)            |
   |  arvore de marcos += campo "Capacidade:"  <-- ADICIONAR  |
   +----------------------------------------------------------+
                   |
                   v  (Fase 4 consome)
   mentor/fecha-marco.md  -- mastery gate PROCURA a frase Capacidade gravada
```

### Pattern 1: Edicao aditiva, nunca reescrita do mecanismo
**What:** Os 3 ganchos (Passo 4, 5, 8) ja contem o mecanismo. A costura ADICIONA nome +
link, nao reescreve a logica existente.
**When to use:** Sempre nesta fase. Reescrever inflaria o doc (Pitfall 10) e arriscaria
quebrar o procedimento existente.

### Pattern 2: Fonte-unica via hyperlink
**What:** Teoria nova NUNCA e escrita em `novo-projeto.md`. Cita-se `fundamentos.md` por
link markdown relativo (`fundamentos.md#ancora`). [CITED: ARCHITECTURE.md:29-34]
**Example (padrao ja em uso):**
```markdown
// Source: mentor/reference.md:98
A ordem capacidade-primeiro segue
[backward design](fundamentos.md#frameworks-foundational-load-bearing): defina o
resultado desejado (a capacidade) antes de desenhar a atividade.
```

### Pattern 3: Dois registros, dois publicos (anti-leak)
**What:** A prosa do procedimento (agente) nomeia o framework; o valor gravado no
artefato do aluno usa so o verbo de capacidade puro.
**When to use:** No Passo 5 -- a instrucao ao agente pode dizer "Stage 2 / backward
design"; a frase resultante no `PROGRESSO.md` so diz "ao terminar, voce consegue...".

### Anti-Patterns to Avoid
- **Reembrulhar o doc em "Stages 1/2/3" explicitos:** rejeitado (D-01) -- reorganizacao
  grande de doc longo + conflito com a ordem do ROADMAP.
- **Frase de capacidade so inline na prosa:** sumiria; o gate da Fase 4 nao a acharia
  (D-02). Tem de persistir no `PROGRESSO.md`.
- **Editar `fundamentos.md` para criar ancora de time-to-first-success:** viola a
  build-order (fundamentos = Fase 1) e o escopo travado. Ver Open Question 1.
- **Campo `Capacidade:` com jargao ("nivel Bloom Analisar"):** vaza teoria para o aluno
  (Pitfall 9 / CONS-01).

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Definir o formato da frase de capacidade | Inventar formato novo no nivel de marco | Reusar `ao terminar, voce consegue <verbo> <conceito>` da Fase 2 (`reference.md:76`) | Coerencia entre niveis; o gate da Fase 4 espera esse formato |
| Definir a teoria de backward design / anti-evasao | Escrever explicacao em `novo-projeto.md` | Hyperlink para `fundamentos.md` | Fonte-unica (`ARCHITECTURE.md:29-34`); duplicar = drift (Pitfall 12) |
| Estrutura da arvore de marcos | Criar nova secao no `PROGRESSO.md` | Adicionar 1 campo na arvore existente do template em `reference.md` | Template ja existe; so falta o campo |

**Key insight:** tudo nesta fase ja existe em alguma forma. O trabalho e NOMEAR e LINKAR,
nao criar. A maior tentacao de erro e formalizar demais (criar sub-docs, rubricas, stages
numerados) -- D-04 existe exatamente para barrar isso.

## Runtime State Inventory

> Fase de edicao de docs. Itens abaixo sao "estado" no sentido de artefatos gerados/
> consumidos, nao runtime de OS.

| Category | Items Found | Action Required |
|----------|-------------|------------------|
| Stored data | `PROGRESSO.md` de projetos JA existentes em `.projetos/<slug>/` (gitignored) nao terao o novo campo `Capacidade:` por marco | Nenhuma migracao no toolkit: `.projetos/` e gitignored e pessoal (`ARCHITECTURE.md:45`). O novo campo so afeta projetos criados APOS esta edicao. Nao ha dado do toolkit a migrar. |
| Live service config | Nenhum (toolkit e markdown estatico) | None -- verificado: sem servicos externos |
| OS-registered state | Nenhum | None -- verificado: sem tasks/daemons |
| Secrets/env vars | Nenhum | None -- verificado |
| Build artifacts | Adaptadores `.claude/skills/novo-projeto/`, `AGENTS.md` apontam para `mentor/novo-projeto.md` mas NAO duplicam conteudo (`ARCHITECTURE.md:29-32`) | Nenhuma: como nao duplicam, a edicao em `mentor/` propaga sozinha. NAO copiar conteudo para adaptadores (Pitfall 12 / CONS-03). |

**Canonical:** Apos editar `novo-projeto.md` e `reference.md`, nenhum sistema externo
guarda copia da string editada. Os adaptadores so apontam. A auditoria da Fase 6 (CONS-03)
confirma que nenhum conteudo vazou para adaptadores.

## Common Pitfalls

### Pitfall 1: Over-formalizacao do Stage 2 (Pitfall 10 da pesquisa de projeto)
**What goes wrong:** Stage 2 vira lista, rubrica, sub-doc ou um "Stage" numerado proprio,
inchando o bootstrap ja longo.
**Why it happens:** Backward design "pede" estrutura; o autor quer ser completo.
**How to avoid:** Guardrail literal D-04 escrito no `novo-projeto.md`: "Stage 2 = exatamente
1 frase de capacidade por marco. Se virou lista, rubrica ou sub-doc, esta errado -- corte."
Teto rigido de 1 frase.
**Warning signs:** Campo `Capacidade:` com mais de 1 frase; nova secao "## Stage 2" no doc;
checklist de maestria por marco.

### Pitfall 2: Teoria vazando para o aluno (Pitfall 9 / CONS-01)
**What goes wrong:** A frase gravada no `PROGRESSO.md` (lido pelo aluno) cita "Bloom",
"Stage 2", "backward design", "maestria".
**Why it happens:** Apos nomear o framework na prosa do agente, confunde-se os dois
publicos.
**How to avoid:** Separar os registros (Pattern 3). A instrucao no Passo 5 deve ser
explicita: o que o agente ESCREVE no `PROGRESSO.md` e SO "ao terminar, voce consegue
<verbo> <conceito>".
**Warning signs:** Jargao de framework no template `PROGRESSO.md` ou no exemplo de frase.

### Pitfall 3: Drift fonte-unica (Pitfall 12 / CONS-03)
**What goes wrong:** Conteudo da edicao copiado para `.claude/` ou `AGENTS.md`; ou teoria
escrita inline em `novo-projeto.md` em vez de linkada.
**Why it happens:** Conveniencia; "garantir" que o adaptador tenha o texto.
**How to avoid:** Editar SO `mentor/`. Teoria so por hyperlink. Adaptadores so apontam.
**Warning signs:** Diff tocando `.claude/` ou `AGENTS.md`; paragrafo de teoria novo em
`novo-projeto.md` sem link.

### Pitfall 4: Hyperlink quebrado / ancora errada
**What goes wrong:** Link para `fundamentos.md#ancora-inexistente`.
**Why it happens:** Slug calculado errado (pontuacao, acentos, parenteses).
**How to avoid:** Reusar ancoras JA verificadas (Achado 1). Para o Passo 8, resolver
Open Question 1 antes de escrever o link. Verificar que o heading-alvo existe em
`fundamentos.md` (achados 1 lista os 3 confirmados).
**Warning signs:** Ancora nova nao listada no Achado 1.

## Code Examples

> "Codigo" aqui = trechos markdown de referencia. Padroes verificados nos arquivos-fonte.

### Hyperlink de framework (padrao canonico do toolkit)
```markdown
// Source: mentor/reference.md:98 [VERIFIED]
[backward design](fundamentos.md#frameworks-foundational-load-bearing): defina o
resultado desejado (a capacidade) antes de desenhar a atividade.
```

### Frase de capacidade por marco (formato canonico, nivel marco)
```markdown
// Source: formato em reference.md:76 + exemplo em 03-CONTEXT.md
**Capacidade:** ao terminar, voce consegue percorrer uma lista de dados e gerar HTML por item
```

### Guardrail de leveza (D-04, texto sugerido para novo-projeto.md)
```markdown
// Source: 03-CONTEXT.md (Specific Ideas)
Stage 2 = exatamente 1 frase de capacidade por marco. Se virou lista, rubrica ou
sub-doc, esta errado -- corte.
```

## State of the Art

Nao se aplica: dominio teorico estavel (frameworks de 1996-2013), ja catalogado em
`fundamentos.md` com HIGH confidence pela pesquisa de projeto. Nenhuma mudanca de
"estado da arte" relevante para uma edicao de procedimento.

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Slugs GitHub-style de `fundamentos.md` (ex: `#sdt-relatedness-em-soloia`, `#frameworks-supporting-ancoram-um-doc`) seguem a convencao GitHub padrao (minusculas, hifens, pontuacao removida, `+` removido) | Achado 1 | Link do Passo 8 pode quebrar se o renderizador-alvo usar regra de slug diferente. Mitigado: a ancora do backward design (`#frameworks-foundational-load-bearing`) JA esta confirmada em uso, validando a convencao. As demais sao a MESMA regra. |
| A2 | O publico de cada arquivo (agente le `novo-projeto.md`; aluno le `PROGRESSO.md`) e como descrito em ARCHITECTURE.md e CONTEXT.md | Architecture Map, anti-leak | Se o aluno lesse `novo-projeto.md`, a estrategia anti-leak (nomear na prosa) vazaria. Risco baixo: ARCHITECTURE.md:45 e o preambulo de `fundamentos.md` confirmam a separacao de publicos. |

## Open Questions

1. **Alvo do hyperlink do Passo 8 (ENG-02 / primeiro done leve).**
   - What we know: NAO ha heading dedicado a time-to-first-success/anti-evasao em
     `fundamentos.md`; o conceito mora na linha SDT (`fundamentos.md:45`) e na ressalva
     SDT (`#sdt-relatedness-em-soloia`). [VERIFIED]
   - What's unclear: qual ancora linkar -- SDT-ressalva (especifica mas e ressalva),
     heading de supporting frameworks (linha-fonte), ou nenhuma (so nomear sem link).
     E se o campo "aplicado em" da SDT deveria passar a listar `novo-projeto.md`
     (a rigor, ajuste de Fase 6, nao Fase 3).
   - Recommendation: **Opcao A/B do Achado 1** -- linkar para a SDT (preferir o heading
     de supporting frameworks, `#frameworks-supporting-ancoram-um-doc`, que aponta para a
     linha-fonte sem ser "a ressalva"). NAO editar `fundamentos.md` nesta fase. Registrar
     no plano que o status "aplicado em <doc>" da SDT/anti-evasao sera reconciliado na
     auditoria da Fase 6 (CONS-02). Decisao final cabe ao planner/discuss.

2. **Checklist de coesao deve ganhar item para a frase de capacidade?**
   - What we know: a verificacao de coesao (`reference.md:108-123`) e o gate mecanico do
     Passe 2.
   - What's unclear: adicionar "[ ] cada marco tem uma frase Capacidade" la ajuda o
     enforcement OU fere a leveza (D-04).
   - Recommendation: provavelmente NAO adicionar (D-04 prioriza leveza; o teto de 1 frase
     ja e o controle). Deixar a decisao para o planner; se adicionar, que seja 1 linha so.

## Environment Availability

Sem dependencias externas: fase de edicao de markdown. Nenhuma ferramenta/runtime/servico
necessario alem de um editor de texto. (Achado adicional: nao ha framework de teste
automatizado no repo para markdown -- ver Validation Architecture.)

## Validation Architecture

> `.planning/config.json` foi consultado; nyquist_validation nao esta explicitamente
> `false` no bloco workflow, entao a secao e incluida. O dominio (edicao de prosa
> markdown) nao tem suite de testes unitarios -- a "validacao" e revisao de propriedades
> verificaveis por leitura, mais o smoke-test estatico anti-leak herdado da Fase 2.

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Nenhum framework de teste de markdown no repo (so `scripts/roadmap_fetch.py` em Python stdlib) |
| Config file | none |
| Quick run command | revisao manual: abrir `mentor/novo-projeto.md` e conferir os 3 criterios do ROADMAP |
| Full suite command | Fase 2 criou um "extrator de blocos cercados + smoke-test estatico anti-leak" (`.planning/ROADMAP.md:56`, plano 02-01) -- reutilizar se aplicavel para checar que nenhum jargao vazou para blocos `PROGRESSO.md` |

### Phase Requirements -> Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| EST-03 | `novo-projeto.md` Passo 4 nomeia backward design + link valido para `fundamentos.md` | grep/leitura | `grep -n "backward design" mentor/novo-projeto.md` e checar ancora existe | manual |
| EST-03 | `novo-projeto.md` Passo 5 instrui gravar frase de capacidade por marco no `PROGRESSO.md` | leitura | revisao manual do Passo 5 | manual |
| EST-03 | Template `PROGRESSO.md` em `reference.md` tem campo `Capacidade:` na arvore de marcos | grep | `grep -n "Capacidade:" mentor/reference.md` | manual |
| EST-03 | Guardrail D-04 (1 frase) escrito no `novo-projeto.md` | grep | `grep -n "exatamente 1 frase" mentor/novo-projeto.md` | manual |
| ENG-02 | Passo 8 nomeia "primeiro done leve" + link | grep | `grep -n "primeiro done leve" mentor/novo-projeto.md` | manual |
| CONS-01 | Nenhum jargao de framework no template/exemplo de `PROGRESSO.md` (frase = verbo puro) | smoke-test estatico (Fase 2) | extrator de blocos cercados sobre `reference.md` | reutilizar Fase 2 |

### Sampling Rate
- **Per task commit:** grep dos termos-alvo + checar ancoras de link existem em `fundamentos.md`.
- **Per wave merge:** revisao dos 3 criterios de sucesso do ROADMAP contra o doc editado.
- **Phase gate:** os 3 criterios do ROADMAP verdadeiros + nenhum jargao no bloco lido pelo aluno.

### Wave 0 Gaps
- Nenhum teste automatizado novo necessario (dominio de prosa). O smoke-test anti-leak
  da Fase 2 ja existe e cobre o risco principal (jargao em bloco lido pelo aluno).
- Se o planner quiser automacao: um grep-check dos 6 termos-alvo da Req->Test Map seria
  suficiente; nao requer framework.

## Security Domain

Nao aplicavel a esta fase. `security_enforcement` nao introduz superficie nova: nenhuma
autenticacao, entrada de usuario, cripto ou rede. A unica preocupacao "de seguranca"
analoga e o anti-leak (CONS-01) -- nao expor jargao teorico ao aluno -- tratado nos
Pitfalls 2 e na Architecture Map. ASVS V2-V6 nao se aplicam a edicao de documentacao
markdown.

## Sources

### Primary (HIGH confidence)
- `mentor/novo-projeto.md` (leitura integral) -- pontos de insercao Passo 4/5/8
- `mentor/reference.md` (leitura integral) -- template `PROGRESSO.md`, formato verbo-capacidade, ancoras de link existentes
- `mentor/fundamentos.md` (leitura integral) -- headings reais e ancoras-alvo
- `.planning/phases/03-bootstrap-com-stage-2-novo-projeto-md/03-CONTEXT.md` -- decisoes D-01..D-04
- `.planning/REQUIREMENTS.md` -- EST-03, ENG-02, CONS-01, CONS-02
- `.planning/ROADMAP.md` -- 3 criterios de sucesso da Fase 3
- `.planning/codebase/ARCHITECTURE.md` -- fonte-unica + adaptadores; publicos por arquivo
- `.planning/codebase/CONVENTIONS.md` -- markdown, backticks, sem acentos
- grep verificado: `fundamentos.md#` em `mentor/` (ancoras em uso); termos anti-evasao em `fundamentos.md`

### Secondary (MEDIUM confidence)
- `.planning/research/SUMMARY.md`, `FEATURES.md`, `PITFALLS.md` -- teoria fixada (HIGH no dominio, MEDIUM na costura especifica que esta fase resolve)

### Tertiary (LOW confidence)
- Slug do heading `### SDT relatedness em solo+IA` (`#sdt-relatedness-em-soloia`) e de
  `## Frameworks supporting (ancoram um doc)` -- inferidos pela convencao GitHub; nao ha
  link existente para eles confirmar (ver Assumption A1).

## Metadata

**Confidence breakdown:**
- Pontos de insercao (`novo-projeto.md`): HIGH -- leitura direta dos trechos-ancora.
- Estado do template `PROGRESSO.md`: HIGH -- confirmado que NAO tem campo Capacidade.
- Formato verbo-capacidade canonico: HIGH -- identico em 3 lugares de `reference.md`.
- Ancora de backward design (Passo 4): HIGH -- ja em uso em `reference.md:98`.
- Ancora do "primeiro done leve" (Passo 8): MEDIUM -- nao ha heading dedicado; decisao
  aberta (Open Question 1).

**Research date:** 2026-06-14
**Valid until:** estavel (~30 dias). Invalida se `fundamentos.md` ou `reference.md` forem
re-editados antes do plano da Fase 3 (re-conferir ancoras e template).
