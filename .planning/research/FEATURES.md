# Feature Research

**Domain:** Tecnicas de design instrucional para cursos assincronos baseados em projeto (aplicadas a um toolkit de mentor-IA em markdown — ensinar-construindo, `TODO(human)`, agnostico de LLM, fonte unica)
**Researched:** 2026-06-13
**Confidence:** HIGH (tecnicas ancoradas em literatura reconhecida: Wiggins/McTighe, Bloom revisado, Pearson/Gallagher, Fisher/Frey, Rosenshine, Sweller, Mayer, Hattie, Roediger/Butler, Deci/Ryan)

> **Nota de leitura.** Aqui "feature" = **tecnica pedagogica**, nao funcionalidade de software.
> Cada linha traz: descricao em 1 frase, complexidade de adicionar a ESTE metodo, e a tag
> **reinforce** (o metodo ja faz — so precisa ancorar/nomear) vs **new** (lacuna a preencher).
> "Complexity" = custo de tecer no markdown de `mentor/` (LOW = 1 frase/regra; MEDIUM = template
> ou checklist novo; HIGH = mexe na espinha/ordem do bootstrap). Mapeado as 4 dimensoes do milestone.

## Feature Landscape

### Table Stakes (Um metodo grounded e credivel TEM que ter)

Sem isto, o metodo nao passa como "ancorado em ciencia da aprendizagem". Penalizam pela ausencia.

#### Dimensao 1 — Estrutura & objetivos

| Tecnica | Por que esperada | Complexity | Tag / nota |
|---------|------------------|------------|------------|
| Objetivo de aprendizagem mensuravel por passo/marco (verbo observavel, nivel de Bloom) | Backward design exige outcome claro antes de qualquer conteudo; ancora "done" | MEDIUM | **new** — passos hoje tem "1 conceito dominante", falta o verbo de desempenho ("ao fim voce CONSEGUE explicar/estender X") |
| Backward design: definir evidencia de dominio ANTES de escrever a aula | Wiggins/McTighe: comeca pelo resultado, depois avaliacao, depois instrucao | MEDIUM | **reinforce** — o gate de curadoria so depois de funcionar ja e isto; falta nomear/ordenar explicitamente |
| Ordenacao por dependencia conceitual (passo N nunca pressupoe conceito nao introduzido) | Sequenciamento valido e pre-requisito de qualquer curso | LOW | **reinforce** — JA E o nucleo do Passe 1 ("caminho completo antes dos marcos") |
| Liberacao gradual de responsabilidade ("I do / we do / you do") | Pearson/Gallagher; Fisher/Frey; Rosenshine — scaffold que transfere carga do mentor ao aluno | MEDIUM | **reinforce** — aula (I do) + scaffold com `TODO(human)` (you do) ja existem; o "we do" (passo guiado conjunto) e implicito, vale tornar explicito |
| Checagem de pre-requisito antes de avancar de fase | Fisher/Frey: exigir evidencia de prontidao antes de transferir mais responsabilidade | LOW | **reinforce** — sondagem de substrato cobre a entrada; falta o micro-check entre passos |

#### Dimensao 2 — Engajamento & retencao

| Tecnica | Por que esperada | Complexity | Tag / nota |
|---------|------------------|------------|------------|
| Uma unica proxima acao clara a cada momento | Async morre no "e agora?"; o "cliff effect" em transicoes e a maior fonte de evasao | LOW | **reinforce** — `PROGRESSO.md` + roteamento por situacao ja dao isto; reforcar como regra explicita |
| Chunking / microlearning (passo = 1 unidade cognitiva, parar no fim do chunk) | Alinha com memoria de trabalho; permite parar sem "deixar pela metade" | LOW | **reinforce** — "Passo = unidade atomica, 1 conceito" ja e chunking; nomear a base |
| Reduzir time-to-first-success (walking skeleton entrega algo observavel cedo) | Primeiro sucesso rapido sustenta a motivacao inicial | LOW | **reinforce** — marco 00 walking skeleton ja faz exatamente isto |
| Visibilidade de progresso (onde estou / quanto falta) | Senso de avanco e correlato direto de persistencia em async | LOW | **reinforce** — `PROGRESSO.md` + marcos como git tags |
| Micro-vitorias por marco (fatia vertical = entrega celebravel) | Reforca competencia (SDT) sem recompensa extrinseca | LOW | **reinforce** — marcos verticais como User Story ja sao micro-vitorias |

#### Dimensao 3 — Avaliacao & feedback

| Tecnica | Por que esperada | Complexity | Tag / nota |
|---------|------------------|------------|------------|
| Checks formativos de baixo risco (sem nota, so diagnostico) | Formative assessment guia a proxima decisao do mentor | MEDIUM | **new** — falta um micro-check explicito "voce consegue explicar X?" antes de seguir |
| Gate de dominio antes de avancar (mastery learning) | Nao avancar sobre base fraca; pre-requisito do sequenciamento | LOW | **reinforce** — gate de curadoria "so depois de funcionar" ja e um mastery gate; estender ao entendimento |
| Feedback acionavel estruturado (Hattie: feed-up / feed-back / feed-forward) | Feedback so funciona se diz alvo, situacao atual e proximo passo | MEDIUM | **new** — forense de erro existe; falta o template tri-partido (onde vou / onde estou / como fechar a lacuna) |
| Forense Socratica de erro (perguntar, nao entregar a correcao) | Mantem a regra de ouro e gera retrieval; preserva autonomia | LOW | **reinforce** — protocolo de forense ja existe; ancorar em retrieval/SDT |
| Rubrica com criterios observaveis para "done"/curadoria | Criterio observavel evita "done" subjetivo | MEDIUM | **new** — curadoria hoje e gate de funcionamento; falta rubrica explicita de criterios |

#### Dimensao 4 — Carga cognitiva & acessibilidade

| Tecnica | Por que esperada | Complexity | Tag / nota |
|---------|------------------|------------|------------|
| Worked example para o novato (passo a passo resolvido antes de exigir producao) | Sweller: worked-example effect reduz carga extranea no iniciante | MEDIUM | **reinforce** — a aula just-in-time e um proto worked-example; falta o exemplo resolvido analogo antes do `TODO(human)` |
| Aula minima just-in-time (teoria so quando o passo precisa) | Evita despejo de teoria; respeita carga intrinseca | LOW | **reinforce** — aulas `aulas/P0x.md` reveladas por passo ja sao isto (forte diferencial) |
| Linguagem simples / jargao de framework escondido do aluno | Acessibilidade a iniciante absoluto (publico declarado) | LOW | **new** — risco de vazar termos de design instrucional/GSD para o aluno; precisa de regra explicita |
| Evitar split-attention (codigo + explicacao integrados, nao separados) | Mayer: referencias cruzadas longe uma da outra aumentam carga | LOW | **new** — formalizar: explicacao junto do scaffold, nao em doc distante |

### Differentiators (Elevam qualidade no nicho async + baseado-em-projeto)

Nao obrigatorios, mas onde o metodo compete. Devem alinhar ao Core Value (ensinar a construir, nunca resolver).

| Tecnica | Proposta de valor | Complexity | Tag / nota |
|---------|-------------------|------------|------------|
| Fading scaffolds conforme expertise cresce (mais `TODO(human)`, menos esqueleto) | Expertise reversal effect: guia que ajuda novato atrapalha o avancado; ajustar suporte | MEDIUM | **new** — hoje o scaffold tem densidade fixa; regra de afinar com base no substrato medido |
| Retrieval practice deliberada (relembrar antes de re-ler) | Roediger/Butler, Hattie: practice testing entre as tecnicas de maior efeito | MEDIUM | **reinforce/new** — forense ja puxa retrieval; falta prompt explicito "antes de abrir a aula, tente lembrar X" |
| Revisao espacada de conceitos anteriores ao iniciar novo marco | Distributed practice: top-tier no meta de Hattie; combate a curva do esquecimento | MEDIUM | **new** — `tutor.md` (volta a estudar) e o lugar natural para um micro-quiz de revisao espacada |
| Interleaving leve (reencontrar conceito antigo em contexto novo no projeto) | Melhora discriminacao e transferencia | MEDIUM | **new** — fatia vertical ja mistura camadas; tornar a reincidencia intencional |
| Prompts de auto-explicacao ("por que isto funciona?") | Self-explanation effect: explicar em voz alta cimenta o schema | LOW | **new** — encaixa direto no gate de curadoria como pergunta obrigatoria |
| Suporte a autonomia (desafio opcional / ordem de escolha) que preserva motivacao | SDT: autonomia + competencia sustentam motivacao melhor que recompensa | MEDIUM | **new** — drill condicional ja e um esboco; formalizar como "desafio opcional", iniciado pelo aluno (suporte solicitado preserva reflexao) |
| Sondagem de substrato por ASSUNTO (nao por aluno) calibrando profundidade da aula | Personaliza carga sem cair em "estilos de aprendizagem"; ajuste por prior knowledge real | MEDIUM | **reinforce** — ja existe; e diferencial forte, ancorar em expertise reversal |
| `fundamentos.md` rastreavel: cada pratica -> fonte -> vocabulario do metodo | Autoridade e completude (a dor relatada); mantem fonte-unica | MEDIUM | **new** — o entregavel central do milestone |

### Anti-Features (Pedidas/tentadoras, mas a NAO construir) -> Out of Scope em REQUIREMENTS.md

| Tecnica | Por que parece boa | Por que e problematica | Alternativa adotada |
|---------|--------------------|------------------------|---------------------|
| Pontos / badges / leaderboards (gamificacao extrinseca) | "Engaja"; comum em apps de curso | Recompensa tangivel mina motivacao intrinseca; leaderboard desmotiva quem fica para tras; conflita com SDT | Competencia via micro-vitorias reais (marco entregue) + autonomia (desafio opcional) |
| Streak/ofensiva obrigatoria estilo manipulativo | "Cria habito" | Pressao culposa; quebra o tom de mentor; nao cabe em async auto-ritmado | Momentum vem da proxima-acao-clara e do progresso visivel, sem punir ausencia |
| Adaptacao por "estilos de aprendizagem" (visual/auditivo/cinestesico) | Soa personalizado | Mito sem base empirica; desperdica esforco | Adaptar por SUBSTRATO/prior knowledge medido (expertise reversal), nao por "estilo" |
| ADDIE em cascata como processo obrigatorio do bootstrap | Modelo "oficial" classico | Linear, dificil de retroceder; avaliacao so no fim; choca com o ciclo iterativo do metodo | Backward design (define outcome+evidencia) com iteracao por marco (espirito SAM/agil), sem impor fases ADDIE |
| Despejo de teoria upfront antes de construir | "Da a base toda primeiro" | Sobrecarga intrinseca; mata o time-to-first-success; oposto do just-in-time | Aula minima por passo, revelada quando o passo precisa |
| Jargao de framework/design instrucional exposto ao aluno | "Mostra rigor" | Confunde iniciante absoluto; quebra acessibilidade | Vocabulario do metodo no doc interno (`fundamentos.md`); aluno so ve linguagem simples |
| Mentor escrevendo o codigo-alvo / "so desta vez" | "Destrava mais rapido" | Destroi o Core Value (aluno nao aprende a construir) | Regra de ouro `TODO(human)` inviolavel + forense Socratica |
| Quiz somativo com nota / certificacao | "Mede aprendizado" | Vira high-stakes; gera ansiedade; nao e o objetivo | Checks formativos de baixo risco + gate de dominio observavel |
| Plataforma/LMS, video, hospedagem | "Curso de verdade tem isso" | Fora do escopo: o produto e markdown + 1 script, agnostico de LLM | "Curso async" e a FONTE de boas praticas, nao um artefato a construir |

## Feature Dependencies

```
Objetivo mensuravel por passo
    └──requires──> Backward design (define evidencia de dominio)
                       └──requires──> Rubrica de criterios observaveis ("done")
                                          └──enables──> Gate de dominio (mastery)

Liberacao gradual (I do / we do / you do)
    └──requires──> Worked example (I do) ──fades-into──> Scaffold TODO(human) (you do)
    └──tuned-by──> Fading scaffolds ──requires──> Sondagem de substrato

Retrieval practice ──must-combine-with──> Revisao espacada   (Roediger: so juntas rendem)
    └──hosted-in──> tutor.md (volta a estudar) + gate de curadoria

Prompt de auto-explicacao ──enhances──> Gate de dominio / forense Socratica

Reducao de time-to-first-success
    └──requires──> Walking skeleton (marco 00) + chunking (passo atomico)
```

### Dependency Notes

- **Objetivo mensuravel requer backward design:** sem outcome observavel nao da para derivar a evidencia de "done"; por isso ambos entram cedo na ordem de tecedura (afetam `novo-projeto.md` e `reference.md`).
- **Worked example funde em scaffold:** o "I do" (exemplo resolvido) e o degrau ANTES do `TODO(human)` ("you do"); juntos materializam a liberacao gradual no markdown de aula+scaffold.
- **Retrieval + revisao espacada sao inseparaveis:** a literatura (Roediger/Butler) so credita o efeito quando combinadas; tecer ambas em `tutor.md`, nunca uma so.
- **Fading scaffolds conflita com scaffold de densidade fixa:** exige a sondagem de substrato como entrada para decidir quanto esqueleto remover — nao combinar "fading" sem o sinal de expertise.
- **Gamificacao extrinseca conflita com SDT/autonomia:** pontos/leaderboard e suporte-a-autonomia sao mutuamente excludentes no mesmo fluxo; escolher autonomia.

## MVP Definition

### Launch With (v1) — o milestone "ancorar o metodo"

Nucleo para o metodo passar como grounded sem inchar a espinha.

- [ ] `mentor/fundamentos.md` — catalogo pratica -> fonte -> vocabulario do metodo (o entregavel-ancora; **new**)
- [ ] Objetivo mensuravel por passo/marco com verbo observavel — tecer em `reference.md`/`novo-projeto.md` (**new**, MEDIUM)
- [ ] Nomear backward design + liberacao gradual nos docs onde ja acontecem (**reinforce**, LOW/MEDIUM)
- [ ] Check formativo de baixo risco + prompt de auto-explicacao no gate de curadoria (**new**, LOW)
- [ ] Feedback tri-partido de Hattie no protocolo de forense (`debug.md`) (**new**, MEDIUM)
- [ ] Regra explicita: linguagem simples / jargao escondido do aluno (**new**, LOW)
- [ ] Lista de anti-features registrada (gamificacao, estilos, ADDIE, teoria-upfront, jargao) (**new**, LOW)

### Add After Validation (v1.x)

Tecnicas de retencao/transferencia que dependem do nucleo assentado.

- [ ] Retrieval practice deliberada + revisao espacada em `tutor.md` — gatilho: nucleo aprovado e em uso (**new**, MEDIUM)
- [ ] Fading scaffolds por substrato — gatilho: regra de objetivo+sondagem estavel (**new**, MEDIUM)
- [ ] Rubrica de criterios observaveis para curadoria — gatilho: gate de dominio definido (**new**, MEDIUM)

### Future Consideration (v2+)

- [ ] Interleaving intencional de conceitos antigos no projeto — adiar: exige maturidade do catalogo de passos por projeto (**new**)
- [ ] Desafio opcional formalizado (autonomia/SDT) — adiar: o drill condicional ja cobre o caso minimo (**new**)
- [ ] Verificacao automatizada de drift `mentor/` vs adaptadores — adiar: concern arquitetural #1, fora da pesquisa pedagogica

## Feature Prioritization Matrix

| Tecnica | User Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| `fundamentos.md` (catalogo grounded) | HIGH | MEDIUM | P1 |
| Objetivo mensuravel por passo/marco | HIGH | MEDIUM | P1 |
| Nomear backward design + liberacao gradual | HIGH | LOW | P1 |
| Check formativo + auto-explicacao no gate | HIGH | LOW | P1 |
| Feedback tri-partido (Hattie) na forense | MEDIUM | MEDIUM | P1 |
| Regra de linguagem simples / anti-jargao | MEDIUM | LOW | P1 |
| Worked example antes do `TODO(human)` | HIGH | MEDIUM | P2 |
| Retrieval + revisao espacada em `tutor.md` | HIGH | MEDIUM | P2 |
| Fading scaffolds por substrato | MEDIUM | MEDIUM | P2 |
| Rubrica de criterios observaveis | MEDIUM | MEDIUM | P2 |
| Interleaving intencional | MEDIUM | MEDIUM | P3 |
| Desafio opcional formalizado (SDT) | LOW | MEDIUM | P3 |

**Priority key:** P1 = nucleo do milestone | P2 = adicionar apos nucleo validado | P3 = considerar depois.

## Competitor Feature Analysis

Comparacao com como o ecossistema costuma resolver cada tecnica (e a escolha deste metodo).

| Tecnica | Pratica academica (Wiggins, Bloom, Sweller, Mayer) | Pratica de mercado eLearning (LMS/MOOC) | Nossa abordagem |
|---------|----------------------------------------------------|-----------------------------------------|-----------------|
| Sequenciamento | Backward design + Bloom | Modulos lineares fixos | Passe 1 dependency-first, ja existente, agora nomeado |
| Liberacao de responsabilidade | I do / we do / you do (Fisher/Frey) | Video -> quiz | Aula -> worked example -> scaffold `TODO(human)` |
| Avaliacao | Formative + mastery (Bloom/Hattie) | Quiz somativo com nota | Check formativo + gate de dominio observavel, sem nota |
| Retencao | Retrieval + spacing (Roediger/Hattie) | Recap em texto / re-leitura | Retrieval no gate + revisao espacada em `tutor.md` |
| Motivacao | SDT: autonomia/competencia (Deci/Ryan) | Pontos/badges/leaderboards | Micro-vitorias reais + desafio opcional; sem gamificacao extrinseca |
| Carga cognitiva | Worked examples + multimidia (Sweller/Mayer) | Teoria upfront em slides | Aula minima just-in-time + linguagem simples |
| Personalizacao | Expertise reversal (prior knowledge) | "Estilos de aprendizagem" (mito) | Sondagem de substrato por assunto |

## Sources

Estrutura & objetivos:
- [Backward Design: Aligning learning objectives and assessments — elearn Magazine (ACM)](https://elearnmag.acm.org/archive.cfm?aid=3704734)
- [Backward Design and Learning Objectives — University of Vermont CTL](https://www.uvm.edu/ctl/backward-design-and-learning-objectives)
- [Revised Bloom's Taxonomy for Writing Learning Objectives — FHSU TigerLearn](https://tigerlearn.fhsu.edu/the-revised-blooms-taxonomy-as-a-framework-for-writing-learning-objectives/)
- [Gradual Release of Responsibility — Wisconsin DPI](https://dpi.wi.gov/excforall/effective-instruction/gradual-release-of-responsibility)
- [I Do, We Do, You Do: Gradual Release of Responsibility — Structural Learning](https://www.structural-learning.com/post/i-do-we-do-you-do)

Engajamento & retencao:
- [Why Learners Drop Off, and How to Stop It (cliff/pile-up effect) — BrainCert](https://blog.braincert.com/why-learners-drop-off-and-how-to-stop-it/)
- [Content Chunking: Enhancing Retention in Bite-Sized Learning — eLearning Industry](https://elearningindustry.com/content-chunking-enhancing-retention-in-bite-sized-learning)
- [The Role of Microlearning and Andragogy in Enhancing Online Student Engagement — Faculty Focus](https://www.facultyfocus.com/articles/online-education/the-role-of-microlearning-and-andragogy-in-enhancing-online-student-engagement/)

Avaliacao & feedback:
- [The Testing Effect: Why Retrieval Practice Works — Structural Learning](https://www.structural-learning.com/post/testing-effect-retrieval-practice)
- [Retrieval and Spaced Practice: Strategies That Must Be Combined — Evidence Based Education](https://evidencebased.education/resource/retrieval-and-spaced-practice-study-strategies-that-must-be-combined/)
- [Strategies for Making Learning Last (retrieval, spacing, interleaving) — Eton CIRL](https://cirl.etoncollege.com/strategies-for-making-learning-last-retrieval-practice-spaced-practice-and-interleaving/)
- [Effectiveness of Spaced Learning, Interleaving, and Retrieval Practice — ScienceDirect (systematic review)](https://www.sciencedirect.com/science/article/pii/S1546144023006464)

Carga cognitiva & acessibilidade:
- [Cognitive Load Theory: 12 Strategies to Reduce Overload — Structural Learning](https://www.structural-learning.com/post/cognitive-load-theory-a-teachers-guide)
- [Enhancing Teaching Strategies through CLT: Worked Examples — MDPI Education Sciences (2024)](https://www.mdpi.com/2227-7102/14/8/813)
- [Expertise Reversal Effect — Wikipedia (entry to primary literature)](https://en.wikipedia.org/wiki/Expertise_reversal_effect)
- [Cognitive Load Theory: Research teachers need to understand — NSW CESE](https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf)

Anti-features (motivacao, ADDIE, estilos):
- [Do points, levels and leaderboards harm intrinsic motivation? — ResearchGate](https://www.researchgate.net/publication/264310429_Do_points_levels_and_leaderboards_harm_intrinsic_motivation_An_empirical_analysis_of_common_gamification_elements)
- [Motivation through gamification: a Self-Determination Theory lens — Utrecht (CHI 2022)](https://webspace.science.uu.nl/~veltk101/publications/art/chi2022-sdtws.pdf)
- [Self-Determination Theory and Online Education: A Primer — Oregon State Ecampus](https://blogs.oregonstate.edu/inspire/2019/06/10/self-determination-theory-and-online-education-a-primer/)
- [Methodology Wars: ADDIE vs. SAM vs. AGILE — ATD](https://www.td.org/content/atd-blog/methodology-wars-addie-vs-sam-vs-agile)
- [ADDIE vs SAM (waterfall criticism, iterative alternative) — eLearning Industry](https://elearningindustry.com/addie-vs-sam-model-best-for-next-elearning-project)

---
*Feature research for: tecnicas pedagogicas de cursos async baseados em projeto, aplicadas ao toolkit mentor-IA*
*Researched: 2026-06-13*
