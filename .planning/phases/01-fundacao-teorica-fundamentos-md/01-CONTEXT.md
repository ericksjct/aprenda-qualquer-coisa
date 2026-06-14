# Phase 1: Fundacao teorica (fundamentos.md) - Context

**Gathered:** 2026-06-14
**Status:** Ready for planning

<domain>
## Phase Boundary

Criar `mentor/fundamentos.md`: o doc interno upstream que define o vocabulario
canonico de frameworks de ciencia da aprendizagem. E a fonte rastreavel que todos
os outros docs de `mentor/` vao CITAR (nunca redefinir). E lido pelo AGENTE, nunca
pelo aluno nem injetado na sessao.

Entrega as propriedades de FUND-01, FUND-02, FUND-03 e os 4 Criterios de Sucesso da
Fase 1 no ROADMAP. O CONTEUDO (quais 6 frameworks foundational + 6 supporting, quais
mitos, as ressalvas SDT/Mayer) ja esta fixado pela pesquisa (HIGH confidence) e NAO
foi rediscutido. As decisoes abaixo sao sobre a FORMA do doc (a "costura especifica"
que a pesquisa marcou como MEDIUM confidence).

</domain>

<decisions>
## Implementation Decisions

### Formato do catalogo
- **D-01:** Formato HIBRIDO. Uma tabela-resumo no topo da pra um relance de todas as
  entradas; abaixo, notas curtas apenas para os frameworks que pedem nuance (ver D-03).
  Junta "escaneavel" com "espaco pra nuance onde precisa". Vale para o bloco
  foundational e o supporting.

### Profundidade por entrada
- **D-02:** Cada entrada tem a DEFINICAO de 1 linha (campo distinto, cumpre FUND-01) MAIS
  uma mini-nota "como usamos no metodo" (1-2 frases, curta). A definicao continua sendo
  exatamente 1 linha; a mini-nota e um campo adicional separado, nao um inchaco da
  definicao. Reconciliacao do pedido de mais profundidade com o limite FUND-01 e com o
  anti-padrao "paredao de teoria" — o doc e interno, entao um pouco mais de contexto
  ajuda o agente a APLICAR, mas a mini-nota tem de ficar curta.

### Posicionamento de ressalvas e mitos
- **D-03:** SECOES DEDICADAS, separadas do catalogo principal.
  - Uma secao "Limites e ressalvas" agrupa as ressalvas honestas: SDT relatedness
    estruturalmente fraca em solo+IA (ancorar anti-evasao em autonomia + competencia,
    nao inflar o claim); Mayer so 3 de 12 principios transferem para texto puro
    (coerencia, sinalizacao, segmentacao). Cobre o Criterio de Sucesso #4 da fase.
  - Uma secao "O que NAO usamos e por que" agrupa os mitos refutados: estilos de
    aprendizagem (Pashler 2008), nativos digitais, Cone de Dale/percentuais de
    retencao, Bloom-como-piramide-rigida — cada um com a razao. Cobre FUND-02.
  - Mantem o catalogo limpo e da um lugar que o agente consulta de proposito.

### Declaracao de uso interno
- **D-04:** O doc declara EXPLICITAMENTE que `fundamentos.md` e interno (guia o agente)
  e nunca e lido pelo aluno nem injetado na sessao (FUND-03 + Criterio #3). Posicionar
  como cabecalho/preambulo no topo do arquivo, antes do catalogo, para que qualquer
  leitor (humano ou agente) veja a regra primeiro.

### Resolucoes pos-pesquisa (2026-06-14, confirmadas pelo usuario)
- **D-06 (conflito D-01 vs D-02 — mini-notas):** RESOLVIDO seguindo D-01. A mini-nota
  "como usamos no metodo" e OPCIONAL por entrada — aparece SO onde ha nuance, nao nas 12
  entradas. D-02 define o FORMATO da mini-nota (campo separado, 1-2 frases curtas) QUANDO
  ela existe; nao a torna obrigatoria. Resolve o conflito A3 sinalizado na pesquisa.
- **D-07 (GRR — Gradual Release of Responsibility):** Nao vira 13a entrada canonica. E
  coberto pela entrada Worked-Example (a sintaxe "eu faco -> voce faz" do metodo ja
  materializa o GRR) e sera nomeado explicitamente na Fase 2 (dona de `reference.md`).
  Mantem a lista canonica em 6+6, alinhada com FUND-01/ROADMAP.
- **D-08 (bloco "nice-to-cite"):** INCLUIR no doc, bem curto (1 linha por item:
  Bloom-verbos, Mayer-contexto, ADDIE/linhagem). E reforco, NAO estrutura — fica fora do
  catalogo canonico 6+6 e nao infla as entradas principais.

### Claude's Discretion
- **D-05 (campo "aplicado em <doc>" antecipado):** O usuario delegou esta decisao.
  Abordagem adotada: **forward-reference com marcador de status**. Como a ordem de build
  e inegociavel (`fundamentos.md` e escrito PRIMEIRO, mas os docs-alvo so sao editados
  nas Fases 2-6), o campo "aplicado em <doc>" aponta o DESTINO futuro com o status:
  ex. `aplicado em tutor.md (Fase 4, pendente)`. Para frameworks cuja aplicacao JA
  existe implicitamente hoje (ex: First Principles ja estrutura a espinha), o campo
  marca `(ja presente)` sem marcador de pendencia.
  - Implicacao para o planner desta fase: o "done" da Fase 1 e o campo PREENCHIDO com
    o destino + status, NAO a aterrissagem verificada (essa e verificada na Fase 6 /
    CONS-02).
  - Implicacao downstream: as Fases 2-6 NAO precisam voltar para reescrever o campo —
    elas fazem a aterrissagem acontecer; a auditoria final (Fase 6) confirma que cada
    "(Fase N, pendente)" virou realidade e troca o status. O planner de cada fase
    posterior deve incluir essa confirmacao no escopo, mas isso e problema das fases
    seguintes, nao da Fase 1.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Conteudo do catalogo (o QUE entra em fundamentos.md — ja decidido)
- `.planning/research/SUMMARY.md` — sintese decision-ready: lista canonica dos 6
  foundational + 6 supporting + nice-to-cite + nao-usar; gaps honestos (SDT, Mayer).
- `.planning/research/STACK.md` — frameworks com fonte primaria e atribuicao rastreada.
- `.planning/research/FEATURES.md` — tecnicas pedagogicas (tag reinforce/new) e o
  mapeamento pratica -> doc onde aterrissa.
- `.planning/research/PITFALLS.md` — cargo-cult (P8), teoria vazando (P9), mitos (P11),
  drift fonte-unica (P12) — os anti-padroes que o doc tem de evitar/sinalizar.

### Contrato da fase (o que tem de ficar VERDADEIRO)
- `.planning/REQUIREMENTS.md` §Fundamentos — FUND-01, FUND-02, FUND-03 (+ CONS-02 para
  a regra "aplicado em verificavel").
- `.planning/ROADMAP.md` §"Phase 1" — os 4 Criterios de Sucesso, incluindo a ressalva
  honesta SDT/Mayer (Criterio #4).

### Convencoes e arquitetura do toolkit (COMO escrever sem quebrar o design)
- `.planning/codebase/ARCHITECTURE.md` — design fonte-unica + adaptadores finos
  (teoria mora so em `mentor/`, nunca duplicada nos adaptadores).
- `.planning/codebase/STRUCTURE.md` — onde `fundamentos.md` se encaixa na pasta `mentor/`.
- `.planning/codebase/CONVENTIONS.md` — estilo: portugues sem acentos, paths em backticks.

### Docs-alvo do campo "aplicado em" (destinos das forward-references — D-05)
- `mentor/reference.md`, `mentor/novo-projeto.md`, `mentor/tutor.md`,
  `mentor/fecha-marco.md`, `mentor/metodo.md`, `mentor/debug.md` — sao os docs que o
  campo "aplicado em <doc>" vai referenciar; o executor deve conferir os caminhos/nomes
  reais ao preencher o campo.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `mentor/` ja contem 7 docs (`metodo.md`, `reference.md`, `novo-projeto.md`,
  `tutor.md`, `fecha-marco.md`, `debug.md`, `spidr-split.md`). `fundamentos.md` e NOVO
  e e o unico arquivo criado nesta fase. Os demais sao apenas destinos de referencia.
- Vocabulario do metodo ja existente (espinha passo/aula/scaffold, gate de curadoria,
  DONE, TODO(human), substrato, drill condicional, forense) e a fonte do campo "termo
  equivalente no metodo" de cada framework — o executor mapeia framework -> termo ja em
  uso, sem inventar jargao novo.

### Established Patterns
- Design fonte-unica: a teoria nova mora SO em `fundamentos.md`; nenhuma definicao de
  framework e duplicada nos adaptadores (`.claude/`, `AGENTS.md`). Inegociavel.
- Estilo: portugues SEM acentos (robustez de encoding); paths/identificadores em
  backticks.

### Integration Points
- `fundamentos.md` e upstream puro nesta fase: nenhum outro doc e editado para citar
  ele agora (isso comeca na Fase 2). A unica saida desta fase e o arquivo novo + os
  campos "aplicado em" apontando para frente (D-05).

</code_context>

<specifics>
## Specific Ideas

- Tabela-resumo sugerida (colunas, a refinar no plano): `Framework | Definicao (1 linha)
  | Fonte primaria | Termo no metodo | Aplicado em (doc + status)`. As mini-notas "como
  usamos" (D-02) ficam abaixo da tabela, nao numa coluna.
- Manter a separacao foundational (6, load-bearing) vs supporting (6, ancoram 1 doc),
  como na pesquisa — a ordem do catalogo segue o SUMMARY.md.
- Ressalvas a registrar literalmente "sem inflar": SDT relatedness fraca em solo+IA;
  Mayer 3-de-12 em texto puro.

</specifics>

<deferred>
## Deferred Ideas

- Aterrissagem real das praticas nos docs-alvo (reference.md, tutor.md, etc.) — e o
  trabalho das Fases 2-6, nao da Fase 1. O campo "aplicado em" so aponta para frente.
- Verificacao automatizada de drift `mentor/` <-> adaptadores — FUT-04 (v2).
- Productive Failure como modo opcional — FUT-02 (v2), evidencia MEDIUM.

None fora isso — a discussao ficou dentro do escopo da fase.

</deferred>

---

*Phase: 01-fundacao-teorica-fundamentos-md*
*Context gathered: 2026-06-14*
