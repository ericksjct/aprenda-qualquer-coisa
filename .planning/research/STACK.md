# Stack Research — Frameworks de Ciencia da Aprendizagem

**Domain:** Design instrucional para curso por projeto, auto-ritmado (assincrono), mediado por mentor de IA
**Researched:** 2026-06-13
**Confidence:** HIGH (frameworks consagrados, atribuicoes verificadas contra a literatura)

> Este "stack" NAO e software. Sao os frameworks/modelos/principios de ciencia da
> aprendizagem que devem virar a fundacao citada do metodo (novo `mentor/fundamentos.md`).
> O criterio de selecao e duplo: (1) o framework e real, bem atribuido e nao-debunkado;
> (2) ele ANCORA algo que o metodo ja faz, ou revela uma LACUNA que vale fechar.
> Frameworks que so "soariam eruditos" sem mapear para o metodo foram rebaixados ou cortados.

## Recommended Stack

Organizado em 3 camadas de carga. **Foundational (load-bearing)** = a espinha citavel; se
o `fundamentos.md` so puder citar 6, cite estes. **Supporting** = ancoram pratica concreta
num doc especifico. **Nice-to-cite** = reforco, nao estrutura.

### Core / Foundational (load-bearing)

Estes seis carregam a fundacao. Cada um ANCORA um pilar que o metodo ja tem.

| Framework | Autor / fonte | 1-linha | Por que aqui + mapeamento (ancora vs lacuna) | Conf |
|-----------|---------------|---------|----------------------------------------------|------|
| **First Principles of Instruction** | M. David Merrill (2002; livro 2013) | Aprendizagem e promovida por 5 fases: problema real -> ativacao do conhecimento previo -> demonstracao -> aplicacao -> integracao. | **A pedra angular.** Os 5 principios mapeiam quase 1:1 na espinha existente: problema real = marco como User Story / entregavel observavel; ativacao = sondagem de substrato; demonstracao = aula por passo; aplicacao = scaffold com `TODO(human)`; integracao = fecha-marco + roadmap vivo. **ANCORA a espinha inteira** e da a ela um nome consagrado. Recomendado como o esqueleto organizador do `fundamentos.md`. | HIGH |
| **Backward Design / Understanding by Design** | Wiggins & McTighe (1ed 1998, 2ed 2005, ASCD) | Projete de tras pra frente: resultados desejados -> evidencia de dominio -> atividades. Nunca atividade-primeiro. | **ANCORA o bootstrap.** A ordem inegociavel "caminho completo (resultados/dependencias) antes dos marcos" e literalmente backward design: define-se o destino e as dependencias antes de montar os modulos. Da autoridade ao Passe 1 -> Passe 2 de `novo-projeto.md`. | HIGH |
| **Constructive Alignment** | John Biggs (1996; Biggs & Tang) | Objetivos, atividades de ensino e avaliacao devem estar alinhados; o "done" deve medir exatamente o objetivo declarado. | **ANCORA o gate de curadoria + DONE do scaffold.** O campo `DONE` e o `entregavel observavel` so funcionam se alinharem ao objetivo do passo. Constructive alignment e o nome do principio de que `META` -> `DONE` nao podem divergir. Reforca o template fixo de scaffold. | HIGH |
| **Cognitive Load Theory** | John Sweller (1988; + Sweller, Ayres & Kalyuga 2011) | Memoria de trabalho e severamente limitada; instrucao deve cortar carga extranea e dosar a intrinseca. 3 cargas: intrinseca, extranea, germane. | **ANCORA "1 conceito dominante por passo", aula minima, walking skeleton.** A regra de granularidade (um conceito novo por passo) e gestao de carga intrinseca; "teoria minima just-in-time" corta carga extranea. Da fundacao a por que o passo e atomico. | HIGH |
| **Worked-Example Effect + Expertise-Reversal Effect** | Sweller & Cooper (1985); Kalyuga et al. (2003) | Novatos aprendem mais estudando exemplos resolvidos que resolvendo do zero; conforme a expertise sobe, esse apoio vira ESTORVO e deve recuar. | **ANCORA o scaffold E o drill condicional.** O scaffold com `TODO(human)` e um worked example parcial (completion problem). O expertise-reversal justifica POR QUE o apoio recua: o `drill condicional` e o fading do scaffold. **Tambem revela uma LACUNA**: o metodo deveria desvanecer scaffolds explicitamente conforme o substrato sobe, nao so "condicionalmente". | HIGH |
| **Retrieval Practice / Testing Effect** | Roediger & Karpicke (2006); Dunlosky et al. (2013) | Recuperar da memoria (vs reler) fortalece a retencao de longo prazo. Uma das 2 estrategias "alta utilidade" da revisao Dunlosky. | **Revela uma LACUNA parcial.** O metodo tem `tutor` (revisao) e `APRENDIZADO.md` (diario), mas nao formaliza recuperacao ativa: o aluno deveria ser pedido a EXPLICAR/reconstruir antes de reler a aula. Fechar isso e o maior ganho da dimensao avaliacao. Foundational porque a evidencia e robusta e o gap e real. | HIGH |

### Supporting (ancoram um doc/pratica especifica)

Cite onde forem aplicados, nao no esqueleto geral.

| Framework | Autor / fonte | 1-linha | Mapeamento (ancora vs lacuna) | Conf |
|-----------|---------------|---------|-------------------------------|------|
| **Self-Determination Theory (SDT)** | Deci & Ryan (1985; 2017) | Motivacao sustentavel exige 3 necessidades: autonomia, competencia, relacionamento. | **ANCORA o anti-evasao (dim. engajamento).** Autonomia = aluno escolhe o projeto real; competencia = entregavel observavel a cada marco (senso de progresso); relacionamento = o mentor como par dialogico. **LACUNA leve:** "relatedness" e fraca em estudo solo com IA — citar honestamente, nao inflar. | HIGH |
| **Scaffolding + Zona de Desenvolvimento Proximal (ZPD)** | Vygotsky (ZPD); Wood, Bruner & Ross (1976, scaffolding) | Ensine no espaco entre o que o aluno faz sozinho e o que faz com apoio; reduza o apoio gradualmente. | **ANCORA o proprio termo "scaffold".** O `TODO(human)` e dimensionado para cair na ZPD: nem trivial nem impossivel. Da raiz teorica ao vocabulario que o metodo ja usa. (Complementa worked-example: scaffolding = a metafora; CLT = o mecanismo.) | HIGH |
| **Mastery Learning** | Bloom (1968); Guskey | Avancar so apos dominio do pre-requisito; correcao antes de prosseguir. | **ANCORA "passo N nunca pressupoe conceito nao introduzido" + gate de aprovacao.** O `DONE` por passo e um check de mastery. **LACUNA:** o metodo nao define explicitamente o ciclo de correcao quando o `DONE` falha — o `protocolo de forense` cobre erros, mas nao "nao-dominio". | HIGH |
| **Avaliacao Formativa** | Black & Wiliam (1998) | Avaliacao a servico do aprendizado (durante), nao so do julgamento (depois). | **ANCORA o DONE, a pergunta-guia e o diario** como instrumentos formativos, nao notas. Reenquadra `fecha-marco` como check formativo. | HIGH |
| **Modelo de Feedback (Feed Up / Back / Forward)** | Hattie & Timperley (2007) | Bom feedback responde 3 perguntas: Aonde vou? Como estou indo? Para onde a seguir? | **ANCORA a PERGUNTA-GUIA e a PISTA do scaffold.** Da estrutura ao feedback do mentor: a PISTA nao deve dar a resposta (feed-forward, nao solucao). Reforca a regra de ouro `TODO(human)`. | HIGH |
| **Productive Failure** | Manu Kapur (2008; Sinha & Kapur 2021) | Deixar o aluno tentar/falhar ANTES da instrucao formal gera melhor conhecimento conceitual que instruir-primeiro. | **Tensao produtiva + LACUNA.** O metodo hoje e instrucao-primeiro (aula -> scaffold). Productive failure sugere, para conceitos selecionados, deixar o aluno tentar o `TODO(human)` e SO ENTAO revelar a aula. Nao reescreve a espinha, mas justifica um modo "tente antes" opcional. Citar com a nuance correta (nao e "deixar sofrer"; e tentativa estruturada). | MEDIUM |
| **ARCS Model** | John Keller (1987) | 4 alavancas de motivacao instrucional: Attention, Relevance, Confidence, Satisfaction. | **ANCORA o anti-evasao, vetor operacional.** Onde SDT explica "por que", ARCS da o checklist de "como": relevancia = projeto real do aluno; confidence = walking skeleton cedo (vitoria rapida); satisfaction = entregavel observavel. Bom para o checklist de `novo-projeto`. | MEDIUM |
| **Spacing Effect / Pratica Distribuida** | Ebbinghaus; Cepeda et al. (2006); Dunlosky (2013) | Estudo espalhado no tempo retem mais que massado. Segunda estrategia "alta utilidade" de Dunlosky. | **LACUNA real.** O metodo nao agenda revisitas espacadas de conceitos antigos. `tutor` poderia reintroduzir conceitos de marcos anteriores em intervalos. Ganho de retencao alto, custo baixo. | HIGH |

### Nice-to-cite (reforco, nao estrutura)

Cite de passagem; nao construa secao em torno deles.

| Framework | Autor | Por que so reforco |
|-----------|-------|--------------------|
| **Taxonomia de Bloom revisada** | Anderson & Krathwohl (2001) | Util como vocabulario de verbos para objetivos mensuraveis (lembrar->criar). Mas e taxonomia, nao metodo; risco de virar jargao decorativo. Use so para redigir objetivos de passo verificaveis. Conf HIGH. |
| **Principios Multimidia de Mayer** | Richard Mayer (2001; 2021) | 12 principios (coerencia, sinalizacao, redundancia, segmentacao...). **Aplicabilidade limitada:** o metodo e texto markdown, sem audio/video/animacao. So 3 transferem: coerencia (corte o supérfluo), sinalizacao (destaque o essencial), segmentacao (1 passo atomico). Citar so esses; o resto e sobre multimidia que o metodo nao tem. Conf HIGH. |
| **Microlearning** | (pratica de industria, sem autor canonico) | Descreve bem "passo atomico = 1 conceito". Mas e termo de mercado, nao teoria validada; CLT + Mastery ja cobrem o mesmo com mais autoridade. Mencionar, nao ancorar. Conf MEDIUM. |
| **Interleaving** | Rohrer & Taylor (2007) | Intercalar tipos de problema ajuda discriminacao. **Encaixe fraco aqui:** curso por projeto e naturalmente sequencial/vertical, nao um conjunto de tipos de exercicio para embaralhar. Util so se um marco tiver varios sub-skills praticaveis. Conf MEDIUM. |
| **Goal-setting** | Locke & Latham (1990) | Metas especificas e desafiadoras elevam desempenho. Ja implicito no marco como User Story. Reforco para o engajamento. Conf HIGH. |
| **ADDIE / SAM / Gagne (9 Eventos)** | Florida State / Allen / Gagne | Modelos de PROCESSO de design de curso (para quem CONSTROI cursos), nao de experiencia de aprendizagem. O mentor de IA ja faz design dinamico (bootstrap em 2 passes ~ SAM iterativo). Citar 1x para situar a linhagem; nao estruturar o metodo neles — seriam burocracia. Gagne tem sobreposicao com Merrill (este e mais moderno e enxuto, prefira Merrill). Conf HIGH. |

## Alternatives Considered

| Recomendado (load-bearing) | Alternativa | Quando a alternativa seria melhor |
|----------------------------|-------------|-----------------------------------|
| **Merrill (First Principles)** como esqueleto | Gagne (9 Eventos de Instrucao) | Se o publico fosse designers de e-learning corporativo formal. Gagne e mais granular/sequencial por licao; Merrill e mais alinhado a aprendizagem por problema/projeto e mais moderno. Para "ensinar construindo", Merrill vence. |
| **Backward Design** para o bootstrap | ADDIE / SAM | Se o foco fosse o PROCESSO de produzir o curso (analise->design->dev->impl->avaliacao). Mas o curso aqui e gerado dinamicamente pelo mentor, entao o valor citavel esta no principio (backward), nao no pipeline de producao. |
| **CLT + Worked Example** para apresentacao | Cognitive Apprenticeship (Collins) | Se quisesse enfatizar modelagem/coaching/articulacao explicitos. Tem boa sobreposicao com scaffolding; CLT da mecanismo mais testavel. Considerar so se o `fundamentos.md` quiser aprofundar a metafora mentor-aprendiz. |
| **Productive Failure** (modo opcional) | Inquiry/Discovery learning puro | Discovery puro sem suporte e MENOS eficaz que instrucao guiada (Kirschner, Sweller & Clark 2006). Productive failure e a forma ESTRUTURADA e suportada — fique nela, nunca em "descoberta livre". |

## What NOT to Use (debunkado — exclua e, se util, sinalize ativamente)

| Evitar | Problema especifico | Use no lugar |
|--------|---------------------|--------------|
| **Estilos de aprendizagem** (VAK/VARK; "sou visual/auditivo") | A "meshing hypothesis" (ensinar no estilo preferido melhora aprendizado) foi testada e refutada repetidamente; classificado como neuromito. 71 modelos revisados, nenhum se sustentou. Citar isso destruiria a credibilidade do `fundamentos.md`. | Adapte ao SUBSTRATO (conhecimento previo medido), nao a "estilo". O metodo ja faz a coisa certa via sondagem. |
| **"Nativos digitais"** | Refutado: jovens nao tem proficiencia tecnologica inata; multitarefa e mito; design baseado nisso prejudica. (Nature 2017; Kirschner & De Bruyckere). | Nao presumir competencia por idade. Medir substrato sempre. Reforca o publico "ate iniciante absoluto". |
| **Piramide de Aprendizagem / Cone de Dale com %** ("lembramos 10% do que lemos, 90% do que ensinamos") | Numeros fabricados, sem fonte. Rastreados a Treichler (1967, Mobil Oil) sem metodologia; corrupcao do Cone de Dale (1946, que nunca falou de retencao). Pura invencao. | Para "ensinar e a melhor forma de aprender", cite o **protégé effect** / retrieval practice — efeito real, sem numeros inventados. |
| **"Aprenda fazendo" sem suporte = descoberta livre** | Descoberta minimamente guiada e menos eficaz para novatos (Kirschner, Sweller & Clark 2006). "Ensinar construindo" do metodo NAO e isso — e construir COM scaffold/aula. | Mantenha a distincao: o metodo e aprendizagem por projeto GUIADA (worked example + scaffolding + productive failure estruturado), nao "se vira ai". |
| **Taxonomia de Bloom como piramide rigida/sequencial** ("tem que dominar 'lembrar' antes de 'criar'") | Interpretacao equivocada; os niveis nao sao estritamente hierarquicos nem pre-requisitos lineares. Aprendizagem por projeto opera em "criar/aplicar" desde cedo. | Use Bloom so como banco de VERBOS para redigir objetivos verificaveis, nao como sequencia obrigatoria. |

## Stack Patterns by Variant — como tecer no metodo

**Para `mentor/fundamentos.md` (o catalogo novo):**
- Estruture o doc nas 4 dimensoes do milestone, mas use **Merrill como espinha transversal** (os 5 principios costuram as dimensoes).
- Para cada framework foundational: 1-linha + fonte + "no nosso vocabulario isto e ___" (a coluna de mapeamento acima e o rascunho).
- Inclua uma secao curta "O que NAO usamos e por que" — sinaliza rigor e protege a credibilidade.

**Para `metodo.md` (persona/conduta):**
- Ancore a regra de ouro `TODO(human)` em **Hattie & Timperley** (feed-forward, nao dar a resposta) + **worked-example/scaffolding**.
- Ancore "erro nao e fracasso / protocolo de forense" em **productive failure** (falha estruturada e dado de aprendizado).

**Para `reference.md` (templates):**
- Campo `DONE` -> **Constructive Alignment + Mastery + Avaliacao Formativa**.
- Campo `PISTA` / `PERGUNTA-GUIA` -> **Hattie & Timperley** (feed-forward).
- Regra "1 conceito dominante por passo" -> **CLT (carga intrinseca)**.

**Para `novo-projeto.md` (bootstrap):**
- Passe 1 -> Passe 2 -> gate -> **Backward Design**.
- Sondagem de substrato -> **Mastery (pre-requisitos) + ativacao de Merrill**; explicitar que NAO e estilo de aprendizagem.
- Checklist anti-evasao -> **SDT (autonomia/competencia/relatedness) + ARCS**.

**Para `tutor.md` (revisao) — onde estao as maiores LACUNAS a fechar:**
- Adicionar **retrieval practice**: pedir o aluno a reconstruir/explicar ANTES de reabrir a aula.
- Adicionar **spacing**: reintroduzir conceitos de marcos anteriores em intervalos.

**Para `debug.md`:**
- Protocolo de forense -> **productive failure + feedback feed-forward**.

## Sources

- Wiggins & McTighe, *Understanding by Design* (ASCD, 1ed 1998 / 2ed 2005) — backward design; via ASCD UbD White Paper e MIT TLL. HIGH.
- Biggs (1996), *Enhancing teaching through constructive alignment* — alinhamento construtivo; via Suffolk CTSE. HIGH.
- Merrill (2002), *First Principles of Instruction*, ETR&D; livro 2013/2024 — Wikipedia + mdavidmerrill.wordpress.com + Springer. HIGH.
- Sweller (1988); Sweller, Ayres & Kalyuga (2011), *Cognitive Load Theory* — NSW CESE review; education hub. HIGH.
- Sweller & Cooper (1985) worked-example; Kalyuga et al. (2003) expertise-reversal — Cambridge Handbook ch.40; Wikipedia (expertise reversal). HIGH.
- Roediger & Karpicke (2006), *Test-Enhanced Learning*, Psych Science — PMC + Matuschak notes. HIGH.
- Dunlosky et al. (2013), *Improving Students' Learning* — practice testing + distributed practice = unicas "alta utilidade". HIGH.
- Deci & Ryan, SDT (1985; 2017 Guilford) — APA SDT overview; PMC e-learning study; TheoryHub. HIGH.
- Vygotsky ZPD; Wood, Bruner & Ross (1976) scaffolding — SimplyPsychology; Open.edu Vygotskian principles. HIGH.
- Bloom (1968) Mastery Learning; Guskey — Kappan/Guskey. HIGH.
- Black & Wiliam (1998) formative assessment — referencia consagrada (training + corroboracao). HIGH.
- Hattie & Timperley (2007), *The Power of Feedback*, RER — ScienceDirect (revisitas 2022). HIGH.
- Kapur (2008); Sinha & Kapur (2021), *When Problem Solving Followed by Instruction Works*, RER — boldscience PDF + SAGE. MEDIUM (eficacia depende de design).
- Keller (1987) ARCS — referencia consagrada. MEDIUM.
- Cepeda et al. (2006) spacing; Rohrer & Taylor (2007) interleaving — via Dunlosky. HIGH/MEDIUM.
- Anderson & Krathwohl (2001) Bloom revisada; Mayer (2001/2021) multimedia — DLI Mayer principles. HIGH.
- **Debunked:** Pashler et al. (2008) e BPS — estilos de aprendizagem (PMC "Learning Styles Myth Thriving"; Frontiers 2020). Kirschner & De Bruyckere (2017) + Nature (2017) — nativos digitais. Treichler (1967) / corrupcao do Cone de Dale — Will Thalheimer (worklearning.com); T&F "Excavating the origins of the learning pyramid myths" (2018). Kirschner, Sweller & Clark (2006) — contra descoberta nao-guiada. HIGH.

---
*Stack research for: design instrucional de curso por projeto auto-ritmado mediado por IA*
*Researched: 2026-06-13*
