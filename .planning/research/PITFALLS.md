# Pitfalls Research

**Domain:** Mentor de aprendizado por projeto (async, self-paced, text-based) — milestone de ancoragem em ciencia da aprendizagem
**Researched:** 2026-06-13
**Confidence:** HIGH (claims centrais verificados em literatura/meta-analises; aplicacao ao toolkit e MEDIUM por ser inferencia de design)

> Idioma sem acentos, por consistencia com o repo. Cada pitfall mapeia para uma das 4
> dimensoes do milestone (estrutura, engajamento, avaliacao, carga cognitiva) ou para a
> meta-categoria "ancoragem teorica" especifica deste milestone.

---

## Critical Pitfalls

### Pitfall 1: Evasao do async (a falha dominante)

**What goes wrong:**
O aluno some. Em educacao online assincrona a evasao e estruturalmente maior que no
presencial. As causas convergem em quatro vetores: (a) falta de accountability/cadencia
externa, (b) proximo passo nao obvio ao reabrir a sessao, (c) perda de momentum entre
sessoes, (d) overwhelm (marco grande ou teoria demais de uma vez). A literatura mostra
um pico desproporcional de "stopout" no **primeiro assessment avaliado** — o primeiro
ponto de friccao real e onde mais gente desiste.

**Why it happens:**
Self-control, gestao de tempo e auto-eficacia baixos disparam a saida; sem cadencia
imposta e sem um "next action" trivial, o custo de reentrada cresce a cada dia parado.

**How to avoid:**
- Cada artefato de estado (`PROGRESSO.md`) deve terminar com um **proximo passo unico e
  acionavel** ("ao voltar, abra X e faca Y") — nao um menu de opcoes.
- Walking skeleton como marco 00 ja existe: protege contra o overwhelm inicial. Manter.
- Marcos curtos e verticais (entregam algo observavel) dao senso de progresso frequente.
- Tornar o **primeiro "done" facil de alcancar** — reduzir friccao no primeiro assessment,
  o ponto historico de maior abandono.
- "Micro-vitorias" explicitas no fim de cada passo (ver Pitfall 5 para nao exagerar).

**Warning signs:**
PROGRESSO.md sem campo "proximo passo"; marcos com muitos passos; primeiro fechamento
de marco exigindo muita coisa antes de qualquer recompensa.

**Phase to address:**
Dim. Engajamento & retencao. Tecer em `mentor/reference.md` (template PROGRESSO) e
`mentor/fecha-marco.md`.

---

### Pitfall 2: Sobrecarga cognitiva — "paredao de teoria" e conceitos demais por passo

**What goes wrong:**
Despejar teoria antes da pratica, ou introduzir varios conceitos novos no mesmo passo.
A memoria de trabalho e limitada; passar de ~1 conceito dominante novo por passo
sobrecarrega e a aprendizagem despenca. O metodo ja nomeia o "paredao de teoria" e a
regra "1 conceito dominante por passo" — o risco e a regra ser enfraquecida ao tecer
teoria nova (ironia: o doc de fundamentos pode ele mesmo virar paredao).

**Why it happens:**
Autor quer ser completo; teoria "just in case" parece seguranca. Mas teoria fora do
ponto de uso e carga extranea pura.

**How to avoid:**
- Reforcar (nao afrouxar) a aula just-in-time: teoria minima **no passo onde sera usada**.
- Manter o invariante "1 conceito dominante novo por passo" como regra verificavel.
- Aplicar principios multimidia (Mayer) ao formato da aula: coerencia (cortar o
  supérfluo), sinalizacao, segmentacao. Texto enxuto, exemplo concreto, sem tangentes.
- `fundamentos.md` deve ser **referencia de fundo** (consultada), nunca conteudo
  injetado na sessao do aluno.

**Warning signs:**
Aula com >1 conceito novo central; teoria antes de qualquer `TODO(human)`; aulas
crescendo de tamanho; o agente "explicando o contexto todo" antes de deixar o aluno agir.

**Phase to address:**
Dim. Carga cognitiva & acessibilidade. Tecer em `mentor/reference.md` (template aula) e
`mentor/metodo.md` (regra de granularidade).

---

### Pitfall 3: Expertise-reversal — over-scaffolding do aluno avancado

**What goes wrong:**
O scaffold e a aula otimizados para iniciante **prejudicam** quem ja tem schema. Guia
redundante + conhecimento proprio gera carga extra; worked examples atrasam quem ja
sabe. O efeito de reversao de expertise e bem estabelecido: o que ajuda novato e nocivo
ao avancado.

**Why it happens:**
O metodo mede substrato por assunto (nao por aluno), o que e bom — mas o risco e tratar
"substrato baixo" como default fixo e nunca recalibrar quando a sondagem indica dominio.

**How to avoid:**
- Usar a **sondagem de substrato** (ja existe) para modular o nivel de scaffold: substrato
  alto -> menos andaime, mais problema aberto; substrato baixo -> mais worked example.
- Tornar explicito no metodo que scaffold e **fade-out** conforme o aluno demonstra dominio,
  nao constante.

**Warning signs:**
Aluno reclamando que a aula e obvia/lenta; sondagem indicando dominio mas o passo ainda
entregando worked example detalhado; mesmo nivel de andaime do inicio ao fim do projeto.

**Phase to address:**
Dim. Carga cognitiva & acessibilidade + Estrutura. Tecer em `mentor/reference.md`
(regra de sondagem/scaffold) e `mentor/novo-projeto.md`.

---

### Pitfall 4: Avaliacao atomizada sem sintese + proxy completion

**What goes wrong:**
Checks pequenos e isolados ("rodou? passou?") sem nunca exigir que o aluno **integre** o
que aprendeu — o metodo ja nomeia "atomizacao". Some-se a isso o "proxy completion":
clicar/avancar sem aprender de fato. Resultado: o aluno "completa" sem capacidade de
explicar ou estender o projeto (que e exatamente o Core Value).

**Why it happens:**
Checks atomicos sao faceis de escrever e de passar. Sintese exige design deliberado.

**How to avoid:**
- Ancorar "done" em **avaliacao formativa + mastery learning**: o gate de fechamento de
  marco deve incluir uma tarefa de **sintese/transferencia** (explicar, estender,
  reaplicar), nao so "o codigo roda".
- Diario de APRENDIZADO como evidencia de compreensao, nao de conclusao.
- A regra de ouro (`TODO(human)`) ja combate proxy completion: se o agente preencher,
  o aluno "completa" sem fazer. Manter enforcement (ver Pitfall 9).

**Warning signs:**
Criterios de "done" so verificam execucao/output; nenhum passo pede para o aluno
explicar com as proprias palavras ou estender sem andaime; fechamento de marco sem
componente de sintese.

**Phase to address:**
Dim. Avaliacao & feedback. Tecer em `mentor/fecha-marco.md` e template APRENDIZADO em
`mentor/reference.md`.

---

### Pitfall 5: Sem retrieval/spacing — conhecimento evapora

**What goes wrong:**
Sem recuperacao ativa e revisao espacada, o conhecimento decai rapido (curva de
esquecimento: perda grande nas primeiras 24h sem reforco). Um curso por projeto linear,
onde cada conceito aparece uma vez e nunca mais, deixa o aluno "completar" o projeto e
nao reter quase nada.

**Why it happens:**
Aprendizado por projeto e naturalmente cumulativo (passos posteriores reusam anteriores),
o que ja da algum spacing implicito — mas sem retrieval deliberado isso e fraco.

**How to avoid:**
- Inserir **retrieval practice** leve: ao reabrir (tutor.md) ou fechar marco, pedir ao
  aluno para **recuperar de memoria** (sem olhar) um conceito anterior antes de seguir.
- Aproveitar a estrutura cumulativa: marcos posteriores devem **reusar e nomear**
  conceitos antigos (spacing intencional), nao reintroduzi-los do zero.
- Diferenciar "recordar com esforco" de "reler" — reler nao e retrieval.

**Warning signs:**
`tutor.md` (volta a estudar) so resume o estado sem pedir recuperacao ativa; conceitos
nunca revisitados apos o passo de introducao.

**Phase to address:**
Dim. Avaliacao & feedback. Tecer em `mentor/tutor.md` e `mentor/fecha-marco.md`.

---

### Pitfall 6: Feedback como elogio/culpa em vez de acionavel

**What goes wrong:**
Feedback vago ("Mandou bem!", "Ficou otimo!") ou de pessoa ("voce e bom nisso") em vez de
feedback de tarefa orientado a "where to next". Meta-analises mostram que elogio e o tipo
**menos eficaz**; elogio a habilidade inata ("voce e bom em X") chega a minar performance
futura. O mais eficaz e o feedback sobre o proximo passo.

**Why it happens:**
Elogio e barato e parece motivador. Um mentor de IA tende a default "encorajador".

**How to avoid:**
- Padronizar feedback do agente como: (1) o que esta especifico, (2) por que importa,
  (3) o proximo passo concreto. Cortar elogio generico e julgamento de pessoa.
- Foco no processo/estrategia, nao no talento do aluno.

**Warning signs:**
Respostas do agente cheias de "perfeito/otimo/mandou bem" sem acao; feedback que avalia
o aluno ("voce e rapido") em vez da tarefa.

**Phase to address:**
Dim. Avaliacao & feedback. Tecer em `mentor/metodo.md` (conduta) e `mentor/debug.md`.

---

### Pitfall 7: Falso "voce conseguiu!" + gamificacao extrinseca minando motivacao intrinseca

**What goes wrong:**
Celebracao prematura ("Voce dominou!") quando o aluno so passou por cima, e recompensas
extrinsecas (badges, pontos, XP) que **crowd-out** a motivacao intrinseca (efeito de
sobrejustificacao, Deci/Lepper). A engagement vira fragil: tirou a recompensa, sumiu o
esforco; e o aluno passa a caçar badge em vez de dominio.

**Why it happens:**
Gamificacao parece engajar (e engaja no curto prazo, efeito novidade), mas degrada
quando vira o motivo de aprender.

**How to avoid:**
- **NAO** introduzir badges/pontos/leaderboards/XP. Marcar como anti-feature explicito.
- Motivacao deve vir de **autonomia, competencia e relacionamento** (autodeterminacao):
  o aluno constroi algo real e seu (autonomia), ve progresso verificavel (competencia),
  e o mentor responde a ele (relacionamento). O proprio projeto e a recompensa.
- Celebracao so apos evidencia de sintese real (ligado ao Pitfall 4), nunca por avancar.

**Warning signs:**
Qualquer proposta de pontuacao/medalha; mensagens de "parabens" desconectadas de
evidencia de dominio; "streaks" ou contadores de conclusao.

**Phase to address:**
Dim. Engajamento & retencao. Decisao de escopo (anti-feature) + conduta em `mentor/metodo.md`.

---

### Pitfall 8: Cargo-culting de frameworks (jargao ADDIE/Bloom sem mudar comportamento)

**What goes wrong:**
Colar terminologia ("aplicamos ADDIE", "objetivos no nivel Analisar de Bloom") por cima do
metodo **sem nenhuma mudanca de comportamento do agente**. O `fundamentos.md` vira uma
vitrine de autoridade que ninguem usa; os procedimentos seguem identicos. Isso e o oposto
do objetivo do milestone (ancorar de verdade), e ainda incha o repo.

**Why it happens:**
E mais facil citar do que reprojetar. A "dor" relatada (falta de autoridade) tenta uma
solucao cosmetica.

**How to avoid:**
- Para cada pratica catalogada em `fundamentos.md`, exigir uma **aplicacao concreta e
  verificavel** tecida num doc existente (checklist, template, regra). Se nao muda nenhum
  comportamento, nao entra.
- Traduzir cada framework para o **vocabulario do metodo** (passo, marco, substrato,
  aula) — nao adotar o jargao cru.

**Warning signs:**
`fundamentos.md` cresce mas `metodo.md`/`reference.md` nao mudam; pratica listada sem um
"aplicado em X" correspondente; nomes de frameworks aparecendo nos docs de procedimento.

**Phase to address:**
Meta: Ancoragem teorica. Gate de aceitacao do `mentor/fundamentos.md`.

---

### Pitfall 9: Agente citando teoria PARA o aluno (em vez de so aplicar)

**What goes wrong:**
O agente comeca a explicar a teoria pedagogica ao aluno: "Vou usar retrieval practice
agora, segundo Roediger...". Isso (a) e meta-distracao/carga extranea, (b) quebra a
lightness do metodo, (c) confunde o aluno que veio aprender a *construir*, nao a estudar
design instrucional. A ciencia da aprendizagem e para o **autor do metodo e o
comportamento do agente**, invisivel ao aluno.

**Why it happens:**
Apos tecer fundamentos nos docs, o agente pode tratar a teoria como conteudo a ensinar.

**How to avoid:**
- Regra explicita em `metodo.md`: **a fundamentacao guia a conduta do agente; nunca e
  citada ao aluno**. O aluno experimenta boas praticas, nao ouve seus nomes.
- `fundamentos.md` enderecado ao autor/mantenedor, marcado como nao-injetavel na sessao.

**Warning signs:**
Agente mencionando "carga cognitiva", "Bloom", "spacing", "formative assessment" nas
respostas ao aluno; aulas explicando *por que* o ensino esta estruturado assim.

**Phase to address:**
Meta: Ancoragem teorica. Regra de conduta em `mentor/metodo.md` + nota de escopo em
`mentor/fundamentos.md`.

---

### Pitfall 10: Conflito de framework (ADDIE linear vs "roadmap vivo") e over-formalizacao

**What goes wrong:**
ADDIE classico e sequencial/waterfall (Analise->Design->Dev->Implement->Avalia). O metodo
ja opera como **roadmap vivo** que recalibra (sondagem, drill condicional, espinha
ajustavel). Importar ADDIE linear cru conflita com isso e pode endurecer o processo;
mais amplamente, formalizar demais mata a leveza que e identidade do produto.

**Why it happens:**
Frameworks de design instrucional foram criados para cursos estaticos pre-produzidos, nao
para mentoria adaptativa em tempo real.

**How to avoid:**
- Preferir modelos **iterativos/adaptativos** (SAM, backward design como lente, design
  rapido) sobre ADDIE waterfall; usar ADDIE so como vocabulario de fases, nao como
  cadeia obrigatoria.
- Tratar backward design como **lente** (resultado desejado -> evidencia -> atividades)
  que ja casa com a espinha existente (caminho completo antes dos marcos), nao como nova
  burocracia.
- Regra de "minimo viavel teorico": adicionar so o que muda comportamento (liga ao P8).

**Warning signs:**
Procedimentos ganhando etapas/gates novos que nao servem ao aluno; linguagem de fases
rigidas; perda da reversibilidade "roadmap vivo".

**Phase to address:**
Dim. Estrutura & objetivos + Meta. Tecer com cuidado em `mentor/novo-projeto.md`.

---

### Pitfall 11: Citar ideias desmascaradas (myths)

**What goes wrong:**
Ancorar o metodo em conceitos populares **ja refutados**, destruindo a credibilidade que o
milestone busca. Os principais a NUNCA citar como fundamento:
- **Learning styles** (visual/auditivo/cinestesico + "meshing hypothesis") — refutado
  repetidamente; ~76% dos educadores ainda acreditam, o que torna o erro tentador.
- **"Digital natives"** — nocao de que jovens "ja sabem" tecnologia por geracao; sem base.
- **Neuro-myths** em geral ("usamos 10% do cerebro", "hemisferio esquerdo/direito",
  estilos como neuromito).
- Aplicacoes frouxas de "pirâmides de retencao" (cone de Aprendizagem / numeros "lembramos
  10%/20%...") que sao fabricados.

**Why it happens:**
Sao ideias intuitivas e onipresentes em material de "como aprender"; entram por osmose.

**How to avoid:**
- O que substitui learning styles: **multiplas representacoes para todos** (Mayer), nao
  casar com "estilo" do aluno.
- `fundamentos.md` deve citar **fontes primarias/meta-analises**, com data; nada de blog
  de coaching. Um mini "anti-myths" interno ajuda o mantenedor a nao reintroduzir.

**Warning signs:**
Qualquer mencao a "estilo de aprendizagem do aluno", "nativo digital", percentuais de
retencao por modalidade, ou adaptar o ensino ao "tipo" do aluno.

**Phase to address:**
Meta: Ancoragem teorica. Curadoria de fontes em `mentor/fundamentos.md`.

---

### Pitfall 12: Drift fonte-unica <-> adaptadores (CONCERNS #1) amplificado por editar muitos docs

**What goes wrong:**
Este milestone edita varios docs de `mentor/` (metodo, reference, novo-projeto, tutor,
fecha-marco, debug) + cria fundamentos.md. O design "fonte unica + adaptadores finos" nao
tem verificacao automatizada. Renomear um procedimento, mudar um nome de template, ou
introduzir conteudo num adaptador (violando fonte-unica) passa silenciosamente.

**Why it happens:**
Mudanca em lote + disciplina 100% manual = janela maxima para inconsistencia.

**How to avoid:**
- **Regra inegociavel**: praticas entram so em `mentor/`; nunca copiar para `.claude/` ou
  `AGENTS.md` (eles so apontam). Ja esta no Out of Scope do PROJECT — manter.
- Apos as edicoes, conferir que todo `/comando` citado tem `mentor/<comando>.md`, que os
  paths em backticks existem, e que README/AGENTS/metodo descrevem o mesmo conjunto.
- Considerar (fora deste milestone, mas anotar) o script de verificacao de ponteiros
  sugerido em CONCERNS #1 como follow-up.

**Warning signs:**
Conteudo novo aparecendo num adaptador; nome de procedimento mudado em um lugar so;
paths em backticks que nao resolvem; README e metodo divergindo na lista de procedimentos.

**Phase to address:**
Transversal a todas as fases de edicao. Checklist de consistencia no fim do milestone.

---

## Technical Debt Patterns

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|----------|-------------------|----------------|-----------------|
| Citar framework sem mudar comportamento (cargo-cult) | Parece "ancorado", rapido | Repo incha, zero ganho pedagogico, falsa autoridade | Never |
| Copiar pratica nova nos adaptadores "pra garantir" | Conveniencia local | Quebra fonte-unica, drift garantido | Never |
| Despejar fundamentos.md inteiro na sessao do aluno | "Transparencia" | Carga extranea, mata leveza, confunde | Never |
| Badges/pontos pra engajar | Engagement curto prazo (novidade) | Crowd-out de motivacao intrinseca | Never |
| Scaffold fixo nivel-iniciante o projeto todo | Simples de escrever | Expertise-reversal pune o avancado | So MVP, com plano de fade-out |
| Aula com 2-3 conceitos pra "andar mais rapido" | Menos passos | Sobrecarga, regra de granularidade quebra | Never (e a regra central) |

## Integration Gotchas

| Integration | Common Mistake | Correct Approach |
|-------------|----------------|------------------|
| ADDIE como modelo | Importar a cadeia waterfall linear | Usar so como vocabulario de fases; preferir iterativo/backward design como lente |
| Bloom's taxonomy | Rotular passos com niveis ("nivel Analisar") visivel ao aluno | Usar internamente p/ escrever objetivos mensuraveis e sequenciar; invisivel ao aluno |
| Mayer / multimidia | Virar regra de "estilos" | Multiplas representacoes para TODOS; coerencia/segmentacao na aula |
| fundamentos.md -> docs existentes | Listar pratica sem aplicacao | Toda pratica precisa de um "aplicado em <doc/template>" verificavel |

## UX Pitfalls

| Pitfall | User Impact | Better Approach |
|---------|-------------|-----------------|
| Proximo passo ambiguo ao reabrir | Custo de reentrada alto -> evasao | PROGRESSO termina com 1 next-action |
| Primeiro "done" pesado | Pico de abandono no 1o assessment | Primeiro marco/done facil e recompensador |
| Agente citando teoria ao aluno | Confusao, perda de leveza | Aplicar a teoria; nunca nomear ao aluno |
| Elogio vago / julgamento de pessoa | Motivacao fragil, sem direcao | Feedback de tarefa: especifico + "where to next" |
| Celebracao prematura | Falsa sensacao de dominio | So celebrar apos evidencia de sintese |
| Texto longo sem segmentacao (acessibilidade) | Carga e exclusao | Aula curta, sinalizada, segmentada; linguagem simples |

## Accessibility / Inclusion (mentoria text-based self-paced)

- **Linguagem simples** e definicao de jargao no ponto de uso — publico inclui iniciante
  absoluto; nao presumir vocabulario tecnico nem cultural.
- **Estrutura legivel**: headings, passos curtos, segmentacao (alinha com carga cognitiva).
- **Sem pressupor velocidade/ritmo unico** — self-paced de verdade; nada de "voce ja
  devia...".
- **Sem pressupor contexto** (ferramentas pagas, hardware potente, ingles fluente). O
  metodo e PT sem acentos justamente por robustez — manter acessivel.
- **NAO adaptar por "estilo de aprendizagem"** (mito); adaptar por **substrato medido**
  e por multiplas representacoes para todos.

## "Looks Done But Isn't" Checklist

- [ ] **fundamentos.md:** parece completo, mas cada pratica tem um "aplicado em <doc>"
  verificavel? (senao e cargo-cult)
- [ ] **Tecedura nos docs:** mudou comportamento real (checklist/template/regra) ou so
  adicionou jargao?
- [ ] **Conduta do agente:** existe regra explicita de NAO citar teoria ao aluno?
- [ ] **Avaliacao:** o "done" de marco inclui sintese/transferencia, nao so "roda"?
- [ ] **Retrieval:** tutor.md/fecha-marco pedem recuperacao ativa de conceito anterior?
- [ ] **Feedback:** padrao e tarefa+next-step, sem elogio vago?
- [ ] **Anti-myths:** nenhum learning style / digital native / cone de retencao citado?
- [ ] **Fonte-unica:** nada novo vazou para `.claude/` ou `AGENTS.md`?
- [ ] **Ponteiros:** todo `/comando` citado tem `mentor/<comando>.md`; paths resolvem?
- [ ] **Leveza:** os procedimentos nao ganharam gates burocraticos que nao servem ao aluno?

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| Cargo-cult (jargao sem comportamento) | MEDIUM | Auditar fundamentos.md; cada item sem "aplicado em X" vira aplicacao concreta ou e cortado |
| Teoria citada ao aluno | LOW | Adicionar regra de conduta em metodo.md; revisar aulas |
| Mito citado | LOW | Remover, substituir por fonte primaria + nota anti-myth |
| Drift adaptadores | MEDIUM | Diff manual mentor/<->README/AGENTS; remover conteudo vazado; (follow-up: script) |
| Over-formalizacao | MEDIUM | Remover gates que nao servem ao aluno; restaurar leveza |
| Gamificacao extrinseca introduzida | LOW | Remover; redirecionar para autonomia/competencia/relacionamento |

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase / Dim. | Verification |
|---------|-------------------------|--------------|
| 1 Evasao async | Engajamento & retencao | PROGRESSO tem next-action unico; 1o done leve |
| 2 Sobrecarga / paredao | Carga cognitiva | Aula = 1 conceito, just-in-time, segmentada |
| 3 Expertise-reversal | Carga cognitiva + Estrutura | Scaffold modula por substrato + fade-out |
| 4 Avaliacao atomizada / proxy | Avaliacao & feedback | Done de marco inclui sintese; TODO(human) enforced |
| 5 Sem retrieval/spacing | Avaliacao & feedback | tutor/fecha-marco pedem recuperacao ativa |
| 6 Feedback elogio/culpa | Avaliacao & feedback | Feedback = tarefa + next-step |
| 7 Falso "conseguiu" / gamif. extrinseca | Engajamento (anti-feature) | Sem badges/pontos; celebra so com evidencia |
| 8 Cargo-cult de frameworks | Meta: ancoragem | Cada pratica tem "aplicado em X" |
| 9 Citar teoria ao aluno | Meta: ancoragem | Regra de conduta em metodo.md |
| 10 Conflito framework / over-formalizacao | Estrutura + Meta | Preferir iterativo; leveza preservada |
| 11 Myths (learning styles etc.) | Meta: ancoragem | Curadoria de fontes; nenhum mito citado |
| 12 Drift fonte<->adaptadores | Transversal | Checklist de ponteiros no fim do milestone |

## Flags para REQUIREMENTS.md "Out of Scope" (anti-features)

- **Badges / pontos / XP / leaderboards / streaks** — crowd-out de motivacao intrinseca.
- **Jargao de framework visivel ao aluno** (ADDIE/Bloom/CLT citados na sessao).
- **fundamentos.md injetado na sessao do aluno** — e referencia do mantenedor.
- **Adaptacao por "estilo de aprendizagem"** — mito refutado.
- **ADDIE waterfall como processo obrigatorio** — conflita com roadmap vivo.
- **Duplicar praticas nos adaptadores** — viola fonte-unica (ja no Out of Scope do PROJECT).

## Sources

- Dropout in online higher education: systematic literature review (2024) — https://educationaltechnologyjournal.springeropen.com/articles/10.1186/s41239-024-00450-9
- Factors affecting completion in asynchronous courses — http://itdl.org/Journal/Dec_07/article03.htm
- Stopout no primeiro assessment / dropout longitudinal (PMC, 2024) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12024346/
- Learning styles myth thriving in higher education (PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC4678182/
- Debunking the neuromyth of learning style (PubMed) — https://pubmed.ncbi.nlm.nih.gov/34973019/
- The stubborn myth of learning styles (Education Next) — https://www.educationnext.org/stubborn-myth-learning-styles-state-teacher-license-prep-materials-debunked-theory/
- Overjustification effect (Wikipedia / Deci & Lepper) — https://en.wikipedia.org/wiki/Overjustification_effect
- Dark side of gamification — https://www.growthengineering.co.uk/dark-side-of-gamification/
- Gamification meta-analysis (Springer ETR&D) — https://link.springer.com/article/10.1007/s11423-023-10337-7
- Expertise reversal effect (Wikipedia + InnerDrive) — https://en.wikipedia.org/wiki/Expertise_reversal_effect ; https://www.innerdrive.co.uk/blog/expertise-reversal-effect-scaffolding/
- Forgetting curve & spacing/retrieval — https://observatory.tec.mx/edu-news/how-the-forgetting-curve-affects-educational-teaching-and-assessment/
- Power of Feedback revisited: meta-analysis (Frontiers) — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.03087/full
- Beyond praise: meaningful feedback — https://www.guroo.academy/post/beyond-praise-meaningful-feedback-that-drives-learning-outcomes
- Backward design + Bloom + instructional design models — https://digital.dcie.miami.edu/learn-with-us/additional-resources/blooms-taxonomy/index.html ; https://www.shiftelearning.com/blog/top-instructional-design-models-explained
- Codebase CONCERNS #1 (drift fonte<->adaptadores) — `.planning/codebase/CONCERNS.md`

---
*Pitfalls research for: mentor de aprendizado por projeto (async) — milestone de ancoragem teorica*
*Researched: 2026-06-13*
