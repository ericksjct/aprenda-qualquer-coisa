# Architecture Research

**Domain:** Design instrucional de curso assincrono auto-guiado (estrutura + sequenciamento) aplicado a um toolkit de mentor em markdown
**Researched:** 2026-06-13
**Confidence:** HIGH (frameworks reconhecidos: Backward Design/UbD, Gradual Release of Responsibility, Bloom revisado, mastery/retrieval/spacing) — MEDIUM nas escolhas de costura (recomendacao de onde encaixar)

> Esta NAO e arquitetura de software. O "sistema" e a organizacao do conhecimento
> instrucional (frameworks reconhecidos) e como ela mapeia nos artefatos existentes do
> metodo (`mentor/*.md` + artefatos do aluno). O downstream desta pesquisa e a ordem de
> edicao dos docs no roadmap deste milestone.

## Resumo executivo (o que muda)

O metodo ja implementa, sem nomear, tres frameworks consagrados:

1. **Backward Design / Understanding by Design (UbD)** — o bootstrap faz engenharia
   reversa do output final ("desired results") antes de fatiar marcos. Ja e backward na
   intencao, mas pula o **Stage 2 (evidencia/avaliacao)** como etapa explicita: hoje vai
   de "output desejado" direto para "plano de passos", deixando o "como vou saber que
   aprendeu" implicito no DONE de cada scaffold.
2. **Gradual Release of Responsibility (GRR / "I do, we do, you do")** — o metodo tem
   "eu faco -> voce faz" so na **entrada zero-absoluto**. O GRR completo tem TRES fases
   (modelo -> pratica guiada -> pratica independente). O metodo colapsou a fase do meio
   ("we do" / pratica guiada) e so a tem implicita na pergunta-guia + PISTA.
3. **Objetivos mensuraveis (Bloom revisado)** — o "Entregavel" do CAMINHO e o "Objetivo
   do passo" da aula sao quase objetivos de aprendizagem, mas usam linguagem de **artefato
   observavel** ("os 3 cards ficam lado a lado"), nao de **capacidade verificavel do aluno**
   (verbo de Bloom: "o aluno consegue aplicar flexbox para alinhar N itens"). Os dois sao
   compativeis e devem coexistir — falta o verbo de capacidade ao lado do artefato.

A maior lacuna estrutural e **avaliacao distribuida**: o metodo tem forte avaliacao
**formativa dentro do passo** (sintese obrigatoria, protocolo de forense) e **summativa
implicita** (o projeto cumulativo = avaliacao autentica/transfer), mas **nao tem retrieval
espaçado entre marcos nem mastery gate explicito para avancar de marco**. A "divida de
aprendizado" e o gancho perfeito para retrieval espaçado, hoje subutilizado.

Recomendacao de identidade: **preservar a espinha** (marco vertical / passo / aula /
scaffold). Os frameworks nao pedem reestruturacao — pedem **nomeacao e completude** de
etapas que ja existem pela metade. `fundamentos.md` vira a fonte upstream que nomeia os
frameworks; os outros docs ganham 1 etapa/campo cada e referenciam `fundamentos.md`.

## Modelo de estrutura de curso alinhado (mapa explicito)

### Hierarquia: curso classico <-> espinha do metodo

```
DESIGN INSTRUCIONAL CLASSICO          ESPINHA DO METODO
─────────────────────────────         ─────────────────────────────
Curso                          <->     Projeto (.projetos/<slug>/)
  Resultado desejado (UbD S1)  <->       Output final + DoD (PROGRESSO.md)
  Evidencia/avaliacao (UbD S2) <->       [LACUNA PARCIAL — ver abaixo]
  Plano de aprendizagem (S3)   <->       CAMINHO.md (passos ordenados por dependencia)
Modulo / Unidade               <->     Marco (fatia vertical = User Story = git tag)
Licao                          <->     Passo (P0x: 1 conceito dominante novo)
  Objetivo da licao            <->       "Objetivo do passo" (aula) + "Entregavel" (CAMINHO)
  Conteudo/instrucao           <->       Aula (aulas/P0x.md): teoria minima just-in-time
  Atividade/pratica            <->       Scaffold (TODO human) + drill condicional
  Checagem formativa           <->       Sintese obrigatoria ("explique em 2 frases")
Avaliacao do modulo            <->       Verificacao de "done" (fecha-marco)
Avaliacao final (summativa)    <->       Projeto cumulativo (artefato unico que cresce)
```

### Onde alinham (sem mudanca)

| Componente classico | Artefato do metodo | Status |
|---|---|---|
| Backward design (reverse engineering do output) | Passe 1 do `novo-projeto.md` (output -> capacidades -> conceitos -> ordem) | JA EXISTE, so falta nomear |
| Sequenciamento por dependencia / sem pre-requisito nao introduzido | Regra de ouro do CAMINHO + verificacao de coesao | JA EXISTE, mais forte que a media do mercado |
| Avaliacao autentica/transfer como summativa | Artefato unico que cresce marco a marco | JA EXISTE (e uma forca rara) |
| Formativa de baixo risco dentro da licao | Sintese obrigatoria + forense de erro | JA EXISTE |
| Just-in-time / nao despejar teoria | Aula revelada na hora do passo | JA EXISTE (anti-paredao) |
| Modelagem para iniciante absoluto | "eu faco -> voce faz" zero-absoluto | JA EXISTE (= fase "I do" do GRR) |

### Onde estao as lacunas (nomeadas)

| Lacuna | O que falta | Framework de ancoragem | Onde encaixar |
|---|---|---|---|
| **L1 — Stage 2 do UbD ausente como etapa** | Bootstrap vai de output -> passos sem desenhar "evidencia de aprendizado" explicitamente. DoD hoje e evidencia do ARTEFATO, nao da CAPACIDADE. | Backward Design / UbD Stage 2 | Novo Passo entre Passe 1 e marcos no `novo-projeto.md` |
| **L2 — Mastery gate de marco implicito** | "done" do marco checa "roda + explica", mas nao e enquadrado como **portao de maestria** (nao avanca enquanto nao demonstra). Falta o vocabulario e a explicitacao de que isso e um gate. | Mastery Learning | `fecha-marco.md` Passo 1 (renomear/enquadrar) |
| **L3 — Retrieval espaçado entre marcos** | Nada faz o aluno **recuperar ativamente** conceito de marco antigo num marco posterior. A "divida de aprendizado" e revisitada por conveniencia, nao por agenda de espaçamento. | Retrieval Practice + Spaced Repetition | `tutor.md` (abertura) + `PROGRESSO.md` (campo) + `fecha-marco.md` |
| **L4 — Fase "we do" (pratica guiada) colapsada** | GRR tem 3 fases; o metodo tem "I do" (zero-absoluto) e "you do" (TODO), mas a pratica guiada do meio so existe implicita (pergunta-guia/PISTA). Para iniciante (nao zero), o salto modelo->independente pode ser ingreme. | Gradual Release of Responsibility | `reference.md` (formalizar "nos fazemos") + `metodo.md` |
| **L5 — Objetivo de capacidade (verbo Bloom) vs entregavel de artefato** | "Entregavel" descreve o que aparece na tela; falta o **verbo de capacidade do aluno** (Bloom) que torna o objetivo avaliavel como aprendizado, nao so como output. | Bloom revisado / objetivos mensuraveis / alinhamento construtivo | `reference.md` (template CAMINHO + template aula) |

## Backward design: como reshapear o bootstrap (concreto)

O `novo-projeto.md` hoje:

```
diagnostico -> sondagem -> caminho completo (Passe 1) -> marcos (Passe 2)
   -> aprovacao -> arquivos
```

UbD pede TRES stages nesta ordem: **resultados desejados -> evidencia/avaliacao ->
plano**. O metodo tem Stage 1 (diagnostico + output final) e Stage 3 (CAMINHO), mas
**Stage 2 esta diluido**. Reshape recomendado (preserva a ordem inegociavel, insere 1
etapa de evidencia ANTES de detalhar passos):

```
Stage 1 (resultados)   diagnostico + output final + objetivo de aprendizado
                          + sondagem de substrato
Stage 2 (evidencia)    >>> NOVO: definir a EVIDENCIA DE MAESTRIA por marco <<<
                          - "como vou saber que o aluno aprendeu, nao so que o codigo roda?"
                          - traduz a barra de qualidade em DoD de ARTEFATO **e**
                            criterio de CAPACIDADE (verbo Bloom) por marco
                          - isto vira o mastery gate de fecha-marco (L2) e os
                            criterios summativos do projeto cumulativo
Stage 3 (plano)        Passe 1 caminho completo + Passe 2 marcos
                          (cada passo herda um objetivo de capacidade do Stage 2)
aprovacao -> arquivos
```

Por que ANTES dos passos (e nao depois): se a evidencia de maestria for desenhada so no
fim, os passos viram "cobrir conteudo" e o DONE de cada scaffold vira improviso. Desenhar
a evidencia primeiro mantem cada passo **alinhado construtivamente** ao que sera avaliado.

Custo: +1 etapa no bootstrap (ja longo). Mitigacao: a etapa e LEVE — uma frase de
capacidade por marco, derivada da User Story que ja existe. Nao e um documento novo;
e uma coluna a mais no enquadramento de marcos e um campo no `PROGRESSO.md`.

## Onde a avaliacao vive (arquitetura de avaliacao distribuida)

```
┌──────────────────────────────────────────────────────────────────┐
│ DENTRO DO PASSO  (formativa, baixo risco)                          │
│   Sintese obrigatoria ("explique em 2 frases")  -> tutor.md P3     │
│   Protocolo de forense (erro = diagnostico)     -> metodo/debug    │
├──────────────────────────────────────────────────────────────────┤
│ FECHAMENTO DO MARCO  (mastery gate)                                │
│   Verificacao de "done": roda + explica + User Story satisfeita    │
│   >>> enquadrar como GATE: nao avanca sem demonstrar capacidade <<<│
│   -> fecha-marco.md P1  (L2)                                        │
├──────────────────────────────────────────────────────────────────┤
│ ENTRE MARCOS  (retrieval espaçado) — LACUNA L3                     │
│   >>> abertura de sessao recupera 1 conceito de marco anterior <<< │
│   >>> divida de aprendizado vira agenda de espaçamento <<<         │
│   -> tutor.md P1 (abertura) + PROGRESSO.md (campo) + fecha-marco   │
├──────────────────────────────────────────────────────────────────┤
│ FIM DO PROJETO  (summativa autentica) — JA EXISTE                  │
│   O artefato unico que cresce = avaliacao de transfer.             │
│   Aluno "explica e estende sozinho" = criterio summativo final.    │
└──────────────────────────────────────────────────────────────────┘
```

Detalhe das duas adicoes:

- **Mastery gate (L2):** `fecha-marco.md` Passo 1 ja checa os criterios certos. A mudanca
  e de ENQUADRAMENTO: nomear como "portao de maestria" e tornar explicito que o criterio
  de capacidade (do Stage 2) — nao so o codigo rodando — e o que libera o proximo marco.
  Custo quase zero; ganho de autoridade alto.
- **Retrieval espaçado (L3):** a unica adicao com peso real. Mecanica minima sugerida: na
  abertura de sessao (`tutor.md` Passo 1), o tutor faz **1 pergunta de recuperacao** sobre
  um conceito de marco ja fechado (sem consultar a aula), escolhido pela agenda de dividas/
  espaçamento registrada no `PROGRESSO.md`. Barato em tokens, alto retorno em retencao.
  Isto tambem ataca a evasao do async (dominio do pesquisador de engajamento) — coordenar.

## Objetivos: como o verbo de Bloom atravessa os artefatos (L5)

Hoje o "objetivo" vive como **artefato observavel** em tres lugares e perde a dimensao de
**capacidade do aluno**. Recomendacao: cada nivel carrega objetivo de capacidade (verbo
Bloom) AO LADO do entregavel de artefato — nao substitui, complementa.

```
CAMINHO.md  "Entregavel"        : artefato observavel  ("os 3 cards lado a lado")
            + NOVO "Objetivo"   : capacidade (Bloom)   ("aplicar flexbox p/ alinhar N itens")
   v herda
aula  "Objetivo do passo"        : espelha capacidade + artefato em 1-2 linhas
   v aterrissa
scaffold  "DONE"                 : a EVIDENCIA de que a capacidade foi demonstrada
                                   (nao so "codigo roda", mas "alinhou e explicou por que")
```

Threading: o **mesmo verbo de Bloom** aparece no objetivo do CAMINHO, na aula e vira o
criterio de DONE. Isso e **alinhamento construtivo**: objetivo -> instrucao (aula) ->
avaliacao (DONE) em acordo. Hoje o trio existe mas sem o fio do verbo conectando os tres.

Cuidado de identidade: NAO transformar o metodo num gerador de objetivos academicos
("ao final desta unidade o discente sera capaz de..."). O verbo de Bloom entra como
**1 frase enxuta de capacidade**, na voz do projeto, nao jargao pedagogico.

## Gradual Release: completar a fase "we do" (L4)

```
GRR completo            Metodo hoje                 Recomendacao
──────────              ───────────                 ────────────
I do   (modelo)         "eu faco" (so zero-absoluto)  manter; e a fase I do
We do  (pratica guiada) [colapsado em pergunta+PISTA]  formalizar "nos fazemos"
You do (independente)   TODO(human)                    manter; e a fase You do
```

"eu faco -> voce faz" e na verdade "I do -> You do" com a fase do meio suprimida. Para
zero-absoluto isso pode ser ingreme. Recomendacao: nomear a sintaxe completa
**"eu faco -> nos fazemos -> voce faz"** (ja insinuada no titulo de uma secao do
`reference.md:382`, mas o corpo so descreve duas fases). O "nos fazemos" = uma variacao
RESOLVIDA EM CONJUNTO (tutor conduz, aluno completa pedacos pequenos) entre o exemplo
do tutor e o TODO solo. Aplicar **condicionalmente** (so quando o salto modelo->solo for
grande), espelhando a logica condicional do drill — nao virar obrigatorio em todo passo.

## Ownership por conceito (fonte unica, sem drift)

Regra de ouro do toolkit: cada conceito mora em UM arquivo; os outros **referenciam**, nao
duplicam. Atribuicao recomendada (com `fundamentos.md` como upstream teorico):

| Conceito instrucional | Arquivo DONO | Os outros so referenciam |
|---|---|---|
| Catalogo de frameworks + fontes + traducao p/ vocabulario do metodo | **`fundamentos.md` (NOVO)** | todos apontam pra ca p/ o "porque" teorico |
| Backward design como ordem do bootstrap | `novo-projeto.md` | `fundamentos.md` explica; `novo-projeto` aplica |
| Stage 2 / evidencia de maestria (etapa nova) | `novo-projeto.md` | DoD/campo no `PROGRESSO.md` template |
| Templates (CAMINHO, aula, scaffold, PROGRESSO) + verbo de Bloom no template | `reference.md` | procedimentos usam o template |
| Regra de granularidade / coesao / sequenciamento | `reference.md` | `novo-projeto`/`fecha-marco` rodam o checklist |
| Sintaxe GRR completa ("eu faco -> nos fazemos -> voce faz") | `reference.md` | `metodo.md` cita a regra; `tutor` aplica |
| Persona / regra de ouro / ciclo por marco | `metodo.md` | adaptadores apontam |
| Mastery gate (enquadramento do "done") | `fecha-marco.md` | `metodo.md` resume o ciclo |
| Retrieval espaçado (abertura de sessao) | `tutor.md` | `PROGRESSO.md` guarda a agenda; `fecha-marco` agenda |
| Avaliacao formativa dentro do passo (sintese/forense) | `metodo.md` + `debug.md` | `tutor` aplica |
| Curadoria (make-it-right) | `fecha-marco.md` + `metodo.md` | — |

Anti-drift: NENHUM destes conceitos deve aparecer escrito por extenso em dois donos. Ex:
a definicao de "mastery gate" mora em `fecha-marco.md`; `metodo.md` so diz "o done e um
portao de maestria (ver `/fecha-marco`)". O teor TEORICO (o que e mastery learning, fonte)
mora so em `fundamentos.md`.

## Build order das edicoes (dependencias)

`fundamentos.md` e o **upstream**: define o vocabulario que os outros vao referenciar.
Escrever os outros primeiro arrisca cada doc cunhar termos diferentes para a mesma coisa.

```
FASE 0 — Fundacao (upstream, bloqueia o resto)
  [1] fundamentos.md (NOVO)
      Cataloga: Backward Design/UbD, GRR, Bloom revisado, mastery learning,
      retrieval practice, spaced repetition. Cada um: definicao + fonte +
      traducao p/ o vocabulario do metodo (marco/passo/aula/scaffold).
      Define os TERMOS canonicos que os outros docs citam.

FASE 1 — Templates e regras (dependem do vocabulario de [1])
  [2] reference.md
      - template CAMINHO: campo "Objetivo (capacidade, verbo Bloom)" ao lado de "Entregavel"
      - template aula: "Objetivo do passo" espelha capacidade + artefato
      - template scaffold: DONE como evidencia de capacidade
      - formalizar "eu faco -> nos fazemos -> voce faz" (3 fases GRR)
      - template PROGRESSO: campo de agenda de retrieval/dividas espaçadas
      Bloqueia [3],[4],[5] porque eles consomem estes templates.

FASE 2 — Procedimentos (dependem dos templates [2] e do vocabulario [1])
  [3] novo-projeto.md
      - inserir Stage 2 (evidencia de maestria) entre Passe 1 e marcos
      - enquadrar a ordem como backward design (citar fundamentos.md)
  [4] fecha-marco.md
      - enquadrar Passo 1 como mastery gate (citar fundamentos.md)
      - agendar retrieval espaçado da divida no PROGRESSO
  [5] tutor.md
      - abertura de sessao: 1 pergunta de retrieval de marco anterior
      - aplicar "nos fazemos" condicional quando salto for grande

FASE 3 — Persona (amarra tudo, depende de [1]..[5] estarem nomeados)
  [6] metodo.md
      - ciclo por marco cita as etapas nomeadas (gate, retrieval, GRR 3 fases)
      - anti-padroes novos (ex: "avancar marco sem passar no gate de maestria")
      - 1 linha apontando fundamentos.md como o "porque" teorico

FASE 4 — Verificacao de drift (transversal, dominio fora desta dimensao)
  [7] conferir que nenhum conceito ficou duplicado entre donos;
      adaptadores (.claude/, AGENTS.md) continuam so apontando (nao tocar conteudo).
```

Dependencias resumidas: **[1] antes de tudo** (vocabulario). **[2] antes de [3][4][5]**
(templates consumidos). **[6] por ultimo** (resume o que os outros definiram). `debug.md`
provavelmente nao muda nesta dimensao (forense ja e formativa boa) — flag para a dimensao
de avaliacao confirmar.

## Anti-padroes (especificos deste milestone)

### AP1 — Reescrever a espinha em vez de nomear o que ja existe
**O que se faz:** trocar marco/passo por "modulo/licao", reorganizar tudo em torno do UbD.
**Por que e errado:** destroi a identidade (teach-by-building, marco vertical) e a forca
rara do projeto cumulativo como summativa. Os frameworks validam a espinha, nao a substituem.
**Em vez disso:** nomear etapas existentes, completar as 2-3 lacunas reais (Stage 2,
retrieval, gate), preservar nomes do metodo.

### AP2 — Duplicar teoria nos procedimentos
**O que se faz:** explicar "o que e mastery learning" dentro de `fecha-marco.md` E de `metodo.md`.
**Por que e errado:** drift garantido (o concern #1 do mapa); duas definicoes divergem com o tempo.
**Em vez disso:** teoria so em `fundamentos.md`; procedimentos citam por referencia.

### AP3 — Objetivo academico jargonizado
**O que se faz:** "ao final o discente sera capaz de..." em todo passo.
**Por que e errado:** quebra o tom acessivel para leigos (publico do toolkit).
**Em vez disso:** verbo de Bloom em 1 frase enxuta na voz do projeto, ao lado do entregavel concreto.

### AP4 — Retrieval/gate como obrigacao pesada
**O que se faz:** quiz formal toda sessao, checklist de maestria gigante.
**Por que e errado:** vira friccao, contradiz o "ritual de 30s" e o async leve.
**Em vez disso:** 1 pergunta de recuperacao na abertura; gate = a verificacao de done ja
existente, so renomeada e com 1 criterio de capacidade.

## Integration points (coordenacao entre dimensoes)

| Fronteira | Coordenacao | Notas |
|---|---|---|
| Esta dim. (estrutura) <-> Avaliacao & feedback | Mastery gate, retrieval, formativa sao compartilhados | Decidir DONO unico: enquadramento estrutural aqui, profundidade de tecnica la |
| Esta dim. <-> Engajamento & retencao | Retrieval espaçado tambem combate evasao async; senso de progresso = marcos/tags | Evitar dois docs prescrevendo a abertura de sessao em conflito |
| Esta dim. <-> Carga cognitiva | Just-in-time (aula) e segmentacao (1 conceito/passo) ja sao CLT; GRR reduz carga | A fase "we do" e justificada por working memory — citar so em `fundamentos.md` |

## Sources

- [Understanding by Design / Backward Design — 3 stages (ASCD white paper)](https://files.ascd.org/staticfiles/ascd/pdf/siteASCD/publications/UbD_WhitePaper0312.pdf)
- [UbD & Backward Design (Open Guide to Teaching, ETSU)](https://pressbooks.pub/etsu/chapter/understanding-by-design-ubd-and-the-backward-design-framework/)
- [Wiggins & McTighe, Understanding by Design (PDF)](https://educationaltechnology.net/wp-content/uploads/2016/01/backward-design.pdf)
- [Gradual Release of Responsibility (Wikipedia)](https://en.wikipedia.org/wiki/Gradual_release_of_responsibility)
- [The "I Do, We Do, You Do" Model Explained (Evidence-Based Teaching)](https://evidencebasedteaching.org/the-i-do-we-do-you-do-model-explained/)
- [Gradual Release of Responsibility (LINCS / TEAL, US Dept of Education)](https://lincs.ed.gov/state-resources/federal-initiatives/teal/guide/gradrelease)
- [Bloom's Taxonomy & measurable objectives (UIC Center for Advancement of Teaching)](https://teaching.uic.edu/cate-teaching-guides/syllabus-course-design/blooms-taxonomy-of-educational-objectives/)
- [Constructive alignment with Bloom's Digital Taxonomy (University of Limerick)](https://www.ul.ie/def/articles/quick-tips-for-teaching-online-constructive-alignment-using-blooms-digital-taxonomy-in)
- [Master list of action verbs for Bloom's Taxonomy (Frontiers in Education)](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2020.00107/full)
- [Retrieval, spaced practice and interleaving (Eton College CIRL)](https://cirl.etoncollege.com/strategies-for-making-learning-last-retrieval-practice-spaced-practice-and-interleaving/)
- [Spaced repetition evidence overview (UPchieve)](https://upchieve.org/blog/spaced-repetition)

---
*Architecture research for: instructional design structure/sequencing mapped onto a markdown mentor toolkit*
*Researched: 2026-06-13*
