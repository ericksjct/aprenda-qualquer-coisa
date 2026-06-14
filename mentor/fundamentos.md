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
