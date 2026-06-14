# Phase 3: Bootstrap com Stage 2 (novo-projeto.md) - Pattern Map

**Mapped:** 2026-06-14
**Files analyzed:** 2 editados (`mentor/novo-projeto.md`, `mentor/reference.md`)
**Analogs found:** 4 / 4 seams (todos com costura existente a imitar)

## Natureza desta fase (ler antes de tudo)

NAO ha codigo. Esta fase EDITA dois arquivos markdown ja existentes. "Padrao/analogo"
aqui = a COSTURA existente que a edicao deve IMITAR (tom da prosa, formato do hyperlink,
formato verbo-capacidade, estrutura do template), nunca codigo a replicar. Toda edicao
e ADITIVA: o mecanismo ja existe em cada seam; a costura ADICIONA nome + link + campo,
sem reescrever o mecanismo. Linhas-ancora abaixo foram RE-VERIFICADAS contra os arquivos
vivos (batem 1:1 com a 03-RESEARCH.md).

## File Classification

| Arquivo editado | Papel (role) | Fluxo (data flow) | Analogo a imitar | Match |
|-----------------|--------------|-------------------|------------------|-------|
| `mentor/novo-projeto.md` Passo 4 | procedimento (prosa lida pelo AGENTE) | nomear-framework + link | `reference.md:97-99` (link backward design) | exato |
| `mentor/novo-projeto.md` Passo 5 | procedimento (instrucao ao AGENTE) | gravar-campo + reforco | `reference.md:76,85` (formato verbo-capacidade) | exato |
| `mentor/novo-projeto.md` Passo 8 | procedimento (prosa lida pelo AGENTE) | rotular + link | `reference.md:97-99` (mesmo padrao de link) | role-match (ancora a definir) |
| `mentor/reference.md` template `PROGRESSO.md` | template (artefato do ALUNO) | adicionar-campo na arvore | `reference.md:227-229,235-237` (blocos de marco existentes) | exato |

## Pattern Assignments

### Seam 1 - `novo-projeto.md` Passo 4 (procedimento, nomear-framework + link) - D-01 macro

**Trecho-ancora REAL onde a costura entra** (`novo-projeto.md:52-57`):

```markdown
## Passo 4 — Passe 1: o caminho completo (`CAMINHO.md`)

Expanda o caminho de aprendizado INTEIRO antes de pensar em marcos:

- Engenharia reversa do output final -> capacidades necessarias -> conceitos
  necessarios -> ordene por dependencia (use a referencia do Passo 3 como guia).
```

O mecanismo de backward design JA esta na linha 56 ("engenharia reversa do output final
-> capacidades"). A edicao e ADITIVA: 1 frase logo apos a linha 57 que NOMEIA isso como
backward design + hyperlink. NAO reescrever o bullet existente.

**Analogo a imitar - hyperlink de framework canonico do toolkit** (`reference.md:97-99`):

```markdown
- A ordem capacidade-primeiro, artefato-como-evidencia segue
  [backward design](fundamentos.md#frameworks-foundational-load-bearing): defina o
  resultado desejado (a capacidade) antes de desenhar a atividade.
```

Reusar EXATAMENTE este alvo de link: `fundamentos.md#frameworks-foundational-load-bearing`
(ancora VERIFICADA em uso em `reference.md:34,98,406`). Tom: 1 frase declarativa, nomeia
o framework via link inline, completa com uma clausula que explica a aplicacao ("defina o
resultado desejado antes de..."). O Passo 4 deve casar este tom.

**Publico:** prosa lida pelo AGENTE -> PODE nomear "backward design" e linkar. Sem anti-leak aqui.

---

### Seam 2 - `novo-projeto.md` Passo 5 (instrucao ao AGENTE, gravar-campo + reforco) - D-01 marco + D-03 reforco + D-04 guardrail

**Trecho-ancora REAL da User Story** (`novo-projeto.md:72-78`):

```markdown
- Cada marco = sequencia de passos **consecutivos** do caminho que, juntos, entregam
  algo que roda/renderiza (**fatia vertical**, nunca tema).
- Aplique a regra de granularidade de `mentor/reference.md` (sessao de ~30-90 min).
- Enquadre cada marco como **User Story**: "Como [usuario], eu quero [capacidade],
  para que [beneficio]". Historia grande demais -> `/spidr-split` ANTES de seguir.
- Traduza a barra de qualidade numa **Definition of Done** objetiva, distribuida
  pelos marcos.
```

Tres costuras entram aqui (estilo de bullet imperativo, ja usado nas linhas 72-81):

1. **D-01 marco (Stage 2):** bullet novo logo APOS o bullet da User Story (linha 76) -
   "as duas nascem coladas". Instruir o agente a gravar, junto da User Story, a frase de
   capacidade do marco no `PROGRESSO.md` no formato verbo-capacidade (ver analogo abaixo).
2. **D-04 guardrail:** incluir o teto rigido de 1 frase (texto literal na secao Shared Patterns).
3. **D-03 reforco (ENG-02):** 1 linha dimensionando o primeiro marco como o menor possivel
   (primeira vitoria rapida). Encaixe natural junto da regra de granularidade (linha 74) ou
   da DoD (linha 77-78).

**Analogo a imitar - formato verbo-capacidade canonico** (`reference.md:76` e `:85`, identicos):

```markdown
- Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>
```

Tambem em `reference.md:294` (template aula):

```markdown
<capacidade: ao terminar, voce consegue <verbo> <conceito>; ...>
```

A frase resultante gravada no `PROGRESSO.md` usa EXATAMENTE "ao terminar, voce consegue
<verbo> <conceito>". Diferenca de nivel: o `CAMINHO.md` usa o rotulo "Objetivo (capacidade)"
por PASSO; o `PROGRESSO.md` usa "Capacidade" por MARCO. Manter os dois rotulos distintos
(D-02: nao misturar niveis).

**Publico DUPLO (Pattern 3 - anti-leak CONS-01):** a INSTRUCAO ao agente (no Passo 5) PODE
dizer "Stage 2 / backward design / frase de capacidade"; a frase RESULTANTE no `PROGRESSO.md`
(lido pelo aluno) so diz "ao terminar, voce consegue...". O plano precisa instruir os dois
registros separadamente.

---

### Seam 3 - `novo-projeto.md` Passo 8 (procedimento, rotular + link) - D-03 / ENG-02

**Trecho-ancora REAL** (`novo-projeto.md:128-132`):

```markdown
## Passo 8 — Walking Skeleton (Marco 00)

O primeiro marco e um **Walking Skeleton** — o esqueleto mais fino que prova que
todas as camadas funcionam juntas (exemplos por tipo de projeto em `mentor/reference.md`).
Ele NAO implementa logica de negocio.
```

O mecanismo (vitoria rapida) JA existe. A edicao e ROTULAGEM: nomear "primeiro done leve"
+ o porque (reduzir time-to-first-success = anti-evasao do async) + hyperlink. Encaixe:
1 frase apos a linha 132, OU junto de "Pare e espere a tentativa do aluno" (linha 145).

**Analogo a imitar:** mesmo padrao de hyperlink inline do Seam 1 (`reference.md:97-99`).

**LACUNA CRITICA (Open Question 1 da RESEARCH - planner deve resolver):** NAO existe
heading dedicado a "time-to-first-success" / "anti-evasao" / "primeiro done leve" em
`fundamentos.md`. O conceito mora na linha SDT (`fundamentos.md:45`) e na ressalva SDT.
Opcoes (recomendada = B):
- A: linkar `#sdt-relatedness-em-soloia` (especifica mas e a *ressalva*, pode confundir).
- B (recomendada): linkar `#frameworks-supporting-ancoram-um-doc` (linha-fonte da SDT,
  sem ser a ressalva).
- C (REJEITADA): criar heading novo em `fundamentos.md` - viola build-order (Fase 1) e o
  escopo travado. NAO editar `fundamentos.md` nesta fase.

Ambas A e B sao slugs INFERIDOS (convencao GitHub), nao confirmados por link existente
(Assumption A1). Verificar o heading-alvo existe antes de escrever o link. Registrar no
plano que o status "aplicado em <doc>" da SDT sera reconciliado na auditoria da Fase 6.

**Publico:** prosa lida pelo AGENTE -> PODE nomear "primeiro done leve / time-to-first-success".

---

### Seam 4 - `reference.md` template `PROGRESSO.md` (template, adicionar-campo) - D-02 [PAR ACOPLADO com Seam 2]

**Estado REAL dos dois blocos de marco no template** (`reference.md:223-239`):

```markdown
## Marcos

### 00 -- <slug> (Walking Skeleton)  <- ATUAL

**User Story:** Como [usuario], eu quero [capacidade basica], para que [valor minimo].
**Passos do caminho:** P01-P02 (ver CAMINHO.md)
**Entregavel:** <o que o aluno VE funcionando ao fechar o marco>

- [ ] <criterio de done>

### 01 -- <slug>

**User Story:** Como [usuario], eu quero [capacidade], para que [valor].
**Passos do caminho:** P03-P05
**Entregavel:** <concreto e observavel>

- [ ] <criterio de done>
```

**CONFIRMADO por leitura: NAO existe campo `Capacidade:`.** O plano PRECISA adiciona-lo
em AMBOS os blocos (marco 00 nas linhas 227-229 E marco 01 nas linhas 235-237). Forma a
imitar - inserir uma linha `**Capacidade:**` LOGO ABAIXO da `**User Story:**`, no mesmo
estilo de campo em negrito do bloco existente:

```markdown
### 00 -- <slug> (Walking Skeleton)  <- ATUAL

**User Story:** Como [usuario], eu quero [capacidade basica], para que [valor minimo].
**Capacidade:** ao terminar, voce consegue <verbo> <conceito>
**Passos do caminho:** P01-P02 (ver CAMINHO.md)
**Entregavel:** <o que o aluno VE funcionando ao fechar o marco>

- [ ] <criterio de done>
```

**Anti-leak no campo (CONS-01):** o valor de `**Capacidade:**` e lido pelo ALUNO -> so o
verbo de capacidade puro. Zero "Bloom", "Stage 2", "maestria", "backward design". O rotulo
"Capacidade" e neutro e ja faz parte do vocabulario do metodo (`CAMINHO.md` usa "Objetivo
(capacidade)") - sem vazamento.

---

## PAR DE EDICAO ACOPLADA (dependencia critica)

Seam 2 (`novo-projeto.md` Passo 5) e Seam 4 (`reference.md` template) sao UM PAR. Um sem
o outro deixa a feature manca:

| Edicao | Define | Sem o par |
|--------|--------|-----------|
| Seam 4 (`reference.md`) | O CAMPO onde gravar (`**Capacidade:**`) | template com campo vazio que o agente nunca preenche |
| Seam 2 (`novo-projeto.md` Passo 5) | A INSTRUCAO que manda o agente preencher | agente sem lugar canonico para gravar a frase |

**Acao para o planner:** as duas devem ir juntas (mesmo plano ou plans com dependencia
explicita marcada). Downstream: a Fase 4 (`fecha-marco.md`) CONSOME a frase gravada - o
mastery gate PROCURA `**Capacidade:**` no `PROGRESSO.md`. A leveza (D-04, 1 frase) e o
contrato que a Fase 4 espera encontrar.

## Shared Patterns

### Hyperlink de framework (fonte-unica via link)
**Fonte/analogo:** `reference.md:97-99`
**Aplicar a:** Seam 1 (Passo 4) e Seam 3 (Passo 8)
**Regra:** teoria nova NUNCA escrita em `novo-projeto.md`; cita-se `fundamentos.md` por link
markdown relativo `fundamentos.md#ancora`. Ancora de backward design CONFIRMADA:
`#frameworks-foundational-load-bearing`. Ancora do Passo 8: a definir (Open Question 1).
```markdown
[backward design](fundamentos.md#frameworks-foundational-load-bearing): <clausula de aplicacao>
```

### Formato verbo-capacidade canonico
**Fonte/analogo:** `reference.md:76`, `:85`, `:294` (identico em 3 lugares)
**Aplicar a:** Seam 2 (instrucao) e Seam 4 (campo no template)
```markdown
ao terminar, voce consegue <verbo> <conceito>
```

### Dois registros, dois publicos (anti-leak CONS-01 - Pattern 3)
**Aplicar a:** Seam 2 + Seam 4 (qualquer coisa que toque o `PROGRESSO.md`)
**Regra:** prosa/instrucao do procedimento (AGENTE) PODE nomear o framework; o valor gravado
no artefato do ALUNO (`PROGRESSO.md`, campo `**Capacidade:**`) usa SO o verbo de capacidade
puro. Warning sign: jargao de framework dentro de bloco `PROGRESSO.md`.

### Guardrail de leveza D-04 (texto literal a inserir no Passo 5)
**Fonte:** 03-CONTEXT.md Specific Ideas
**Aplicar a:** Seam 2 (prosa do procedimento)
```markdown
Stage 2 = exatamente 1 frase de capacidade por marco. Se virou lista, rubrica ou
sub-doc, esta errado — corte.
```

### Edicao aditiva, nunca reescrita do mecanismo
**Aplicar a:** TODOS os 4 seams
**Regra:** cada seam ja contem o mecanismo (Passo 4 = engenharia reversa; Passo 8 = Walking
Skeleton; template = blocos de marco). A costura ADICIONA nome + link + campo. Reescrever
inflaria o doc (Pitfall 10) e arriscaria quebrar o procedimento. Warning sign: bullet
existente reescrito, ou nova secao "## Stage 2" criada.

### Drift fonte-unica (NAO tocar adaptadores)
**Aplicar a:** todo o diff da fase
**Regra:** editar SO `mentor/`. NAO copiar conteudo para `.claude/skills/` ou `AGENTS.md`
(eles apontam, nao duplicam). Warning sign: diff tocando `.claude/` ou `AGENTS.md`.

## No Analog Found

Nenhum seam ficou sem analogo. Unica incerteza e a ANCORA do hyperlink do Passo 8 (Seam 3):
nao ha heading dedicado em `fundamentos.md` para time-to-first-success; o planner escolhe
entre A/B (slugs SDT inferidos) ou nomeia sem link. Isso e uma decisao de ancora, nao uma
ausencia de padrao de costura - o PADRAO de hyperlink (Shared Patterns) continua valendo.

## Metadata

**Escopo de busca de analogo:** `mentor/novo-projeto.md`, `mentor/reference.md` (leitura
direta dos seams). `mentor/fundamentos.md` consultado via RESEARCH (NAO editado nesta fase).
**Arquivos escaneados:** 2 editados + 1 alvo-de-link (read-only).
**Linhas-ancora re-verificadas:** `novo-projeto.md:52-57,72-78,128-147`;
`reference.md:76,85,97-99,223-239,294`. Batem 1:1 com 03-RESEARCH.md.
**Data:** 2026-06-14
