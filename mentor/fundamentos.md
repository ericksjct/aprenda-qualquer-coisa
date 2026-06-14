# Fundamentos -- Frameworks de Ciencia da Aprendizagem

> Este e um documento INTERNO do metodo. Ele existe para guiar a CONDUTA do agente -- e a
> fonte unica do vocabulario teorico que os outros docs de `mentor/` citam. NUNCA e lido pelo
> aluno nem injetado na sessao: o aluno experimenta as boas praticas, jamais ouve os nomes
> dos frameworks. Despejar este conteudo na sessao recriaria o "paredao de teoria" que o
> metodo combate. Os outros docs CITAM este aqui por referencia; nenhum deles redefine a
> teoria localmente (design fonte-unica).

## Como ler este doc

A **tabela-resumo** de cada bloco da o relance de todas as entradas. As **mini-notas "como
usamos no metodo"** aparecem SO abaixo da tabela e SO para os frameworks que pedem nuance --
nao ha mini-nota para todas as entradas. **Limites e ressalvas** e **o que NAO usamos** tem
secao propria, fora do catalogo. Cada entrada do catalogo traz 4 campos: definicao de 1 linha,
fonte primaria, termo no metodo e "aplicado em `<doc>`" com status (`(Fase N, pendente)` para
destinos futuros, `(ja presente)` onde a aplicacao ja existe hoje).

## Frameworks foundational (load-bearing)

| Framework | Definicao (1 linha) | Fonte primaria | Termo no metodo | Aplicado em (doc + status) |
|-----------|---------------------|----------------|-----------------|----------------------------|
| First Principles of Instruction | Aprendizagem e promovida por 5 fases: problema real -> ativacao do conhecimento previo -> demonstracao -> aplicacao -> integracao. | Merrill (2002; livro 2013) | A espinha inteira: marco como entregavel observavel (problema) -> sondagem de substrato (ativacao) -> aula por passo (demonstracao) -> scaffold com `TODO(human)` (aplicacao) -> fecha-marco + roadmap vivo (integracao) | `mentor/metodo.md`, `mentor/novo-projeto.md` (ja presente) |
| Backward Design / Understanding by Design | Projete de tras pra frente: resultados desejados -> evidencia de dominio -> atividades. Nunca atividade-primeiro. | Wiggins & McTighe (1ed 1998, 2ed 2005, ASCD) | Ordem inegociavel "caminho completo antes dos marcos"; Passe 1 -> Passe 2 (engenharia reversa do output final) | `mentor/reference.md`, `mentor/novo-projeto.md` (Fase 2/3, pendente) |
| Constructive Alignment | Objetivos, atividades de ensino e avaliacao devem estar alinhados; o "done" deve medir exatamente o objetivo declarado. | Biggs (1996; Biggs & Tang) | Par "META -> DONE" do scaffold; gate de curadoria "so depois de funcionar"; entregavel observavel alinhado ao objetivo | `mentor/reference.md` (Fase 2, pendente) |
| Cognitive Load Theory | Memoria de trabalho e severamente limitada; instrucao deve cortar carga extranea e dosar a intrinseca (3 cargas: intrinseca, extranea, germane). | Sweller (1988; + Sweller, Ayres & Kalyuga 2011) | "1 conceito dominante (novo) por passo"; aula minima just-in-time; "salto suave / sem degraus"; paredao de teoria (anti-padrao) | `mentor/reference.md`, `mentor/metodo.md` (ja presente; Mayer/CARGA-03 Fase 2, pendente) |
| Worked-Example Effect + Expertise-Reversal Effect | Novatos aprendem mais estudando exemplos resolvidos; conforme a expertise sobe, esse apoio vira estorvo e deve recuar. | Sweller & Cooper (1985); Kalyuga et al. (2003) | "eu faco -> voce faz" (worked example); `TODO(human)` como completion problem; calibragem por substrato; drill condicional; fading do andaime conforme substrato sobe | `mentor/reference.md` (parcial hoje; Fase 2, pendente) |
| Retrieval Practice / Testing Effect | Recuperar da memoria (vs reler) fortalece a retencao de longo prazo; uma das 2 estrategias "alta utilidade" de Dunlosky. | Roediger & Karpicke (2006); Dunlosky et al. (2013) | "pedir a sintese antes de comemorar" / "me explica em 2 frases por que isso funciona" (embriao da recuperacao ativa) | `mentor/tutor.md` (Fase 4, pendente) |

**Worked-Example + Expertise-Reversal:** a sintaxe "eu faco -> voce faz" entrega o exemplo
resolvido; o `fading` do andaime e condicional ao substrato (drill so quando a expertise ainda
nao subiu) -- nao aplicar o mesmo nivel de apoio a todos.

**Cognitive Load Theory:** ha uma ironia load-bearing aqui -- este proprio doc combate o
"paredao de teoria"; por isso definicoes de 1 linha e mini-notas curtas, nunca despejar a
teoria na sessao do aluno.

**Retrieval Practice:** e uma LACUNA hoje (so parcial em `mentor/tutor.md`); a abertura do tutor
com recuperacao ativa e a aterrissagem prevista para a Fase 4.

## Frameworks supporting (ancoram um doc)

| Framework | Definicao (1 linha) | Fonte primaria | Termo no metodo | Aplicado em (doc + status) |
|-----------|---------------------|----------------|-----------------|----------------------------|
| Self-Determination Theory (SDT) | Motivacao sustentavel exige 3 necessidades: autonomia, competencia, relacionamento. | Deci & Ryan (1985; 2017) | Anti-evasao; "proxima acao unica" (Log do `PROGRESSO.md` + despedida do tutor); autonomia (aluno escolhe o projeto real) + competencia (entregavel observavel por marco / micro-vitorias) | `mentor/tutor.md`, `PROGRESSO.md` (via `mentor/reference.md`) (Fase 4, pendente) |
| Scaffolding + Zona de Desenvolvimento Proximal (ZPD) | Ensine no espaco entre o que o aluno faz sozinho e o que faz com apoio; reduza o apoio gradualmente. | Vygotsky (ZPD); Wood, Bruner & Ross (1976) | O proprio termo "scaffold"; andaime calibrado ao substrato; "nem trivial nem impossivel" (`TODO(human)` dimensionado) | `mentor/reference.md`, `mentor/metodo.md` (ja presente) |
| Mastery Learning | Avancar so apos dominio do pre-requisito; correcao antes de prosseguir. | Bloom (1968); Guskey | Gate de "done"; "so depois de funcionar"; "passo N nunca pressupoe conceito nao introduzido"; criterio de fechamento verificavel | `mentor/fecha-marco.md` (Fase 4, pendente) |
| Avaliacao Formativa | Avaliacao a servico do aprendizado (durante), nao so do julgamento (depois). | Black & Wiliam (1998) | DONE / pergunta-guia / diario `APRENDIZADO.md` como instrumentos formativos (nao nota); check formativo no gate de curadoria | `mentor/metodo.md`, `mentor/fecha-marco.md` (Fase 5, pendente) |
| Modelo de Feedback (Feed Up / Back / Forward) | Bom feedback responde 3 perguntas: Aonde vou? Como estou indo? Para onde a seguir? | Hattie & Timperley (2007) | PERGUNTA-GUIA e PISTA do scaffold; protocolo de forense; "elogie o processo, nao so o acerto"; PISTA como feed-forward (nao da a resposta) | `mentor/debug.md` (Fase 5, pendente) |
| Spacing Effect / Pratica Distribuida | Estudo espalhado no tempo retem mais que massado; segunda estrategia "alta utilidade" de Dunlosky. | Cepeda et al. (2006); Dunlosky (2013) | Dividas de aprendizado em `PROGRESSO.md`; reuso cumulativo de conceitos antigos em marcos novos | `mentor/fecha-marco.md`, `PROGRESSO.md` (Fase 4, pendente) |

**SDT:** ancore o anti-evasao em **autonomia + competencia**, nao em relatedness -- ver a secao
"Limites e ressalvas" (em estudo solo+IA a relatedness e estruturalmente fraca).

**Spacing:** e uma LACUNA hoje (so parcial via dividas em `PROGRESSO.md`); a aterrissagem real
(reuso cumulativo, revisao espacada) e prevista para a Fase 4.

## Limites e ressalvas

Registre o limite SEM inflar o claim. Estas duas ressalvas sao honestas e inegociaveis.

### SDT relatedness em solo+IA

> Ressalva SDT: a SDT preve 3 necessidades (autonomia, competencia, relatedness). Em estudo
> solo mediado por IA nao ha interlocutor humano real, entao relatedness e estruturalmente
> fraca. Ancoramos o anti-evasao em autonomia (o aluno escolhe o projeto real) e competencia
> (entregavel observavel por marco). NAO inflamos um claim de relatedness que o formato nao
> sustenta.

### Mayer: so 3 de 12 principios em texto puro

> Ressalva Mayer: dos 12 principios multimidia de Mayer, so 3 transferem para texto puro
> (coerencia: corte o superfluo; sinalizacao: destaque o essencial; segmentacao: um passo
> atomico por vez). Os outros 9 tratam de audio/video/animacao que o metodo (markdown) nao
> tem, entao nao se aplicam. Citamos so os 3 aplicaveis; nao inflamos para "aplicamos Mayer".

## O que NAO usamos e por que

Estes 4 mitos SO aparecem aqui, com a razao da refutacao. Nunca cite nenhum positivamente
fora desta secao.

| Mito (NAO usar) | Razao da refutacao | Fonte de refutacao | Use no lugar |
|-----------------|--------------------|--------------------|--------------|
| Estilos de aprendizagem (VAK/VARK; "sou visual/auditivo") | A "meshing hypothesis" (ensinar no estilo preferido melhora aprendizado) foi testada e refutada repetidamente; e neuromito. 71 modelos revisados, nenhum se sustentou. | Pashler et al. (2008); BPS | Adaptar ao SUBSTRATO (conhecimento previo medido por sondagem), nao a "estilo" |
| "Nativos digitais" | Jovens nao tem proficiencia tecnologica inata; multitarefa e mito; design baseado nisso prejudica. | Kirschner & De Bruyckere (2017); Nature (2017) | Nao presumir competencia por idade; medir substrato sempre |
| Piramide de Aprendizagem / Cone de Dale com percentuais ("lembramos 10% do que lemos, 90% do que ensinamos") | Numeros fabricados, sem fonte/metodologia; corrupcao do Cone de Dale (1946, que nunca falou de retencao); rastreados a Treichler (1967, Mobil Oil). | Treichler (1967) corrompido; Thalheimer (worklearning.com); T&F (2018) | Para "ensinar e a melhor forma de aprender", citar testing effect / retrieval practice (efeito real, sem numeros inventados) |
| Taxonomia de Bloom como piramide rigida/sequencial ("dominar 'lembrar' antes de 'criar'") | Interpretacao equivocada; os niveis nao sao estritamente hierarquicos nem pre-requisitos lineares. Aprendizagem por projeto opera em "criar/aplicar" desde cedo. | Anderson & Krathwohl (2001, revisao) | Bloom so como banco de VERBOS para objetivos verificaveis, nao como sequencia obrigatoria |

## Nice-to-cite

Reforco, NAO estrutura -- 1 linha por item, fora do catalogo canonico 6+6. Nao construa secao
em torno destes.

- **Taxonomia de Bloom revisada** (Anderson & Krathwohl 2001) -- banco de VERBOS para objetivos; nao usar como piramide.
- **Principios Multimidia de Mayer** (2001/2021) -- ver ressalva acima (so 3 de 12 transferem).
- **ADDIE / SAM / Gagne** -- citar 1x so para situar a linhagem do design instrucional; nao estruturar nada neles.
