# Roadmap: Mentor de Aprendizado por Projeto -- ancoragem em ciencia da aprendizagem

## Overview

Este milestone NAO constroi software: tece ciencia da aprendizagem reconhecida no metodo
markdown de `mentor/`. A jornada segue a ordem de edicao inegociavel ditada pela
propriedade fonte-unica: primeiro cria-se o catalogo teorico upstream (`fundamentos.md`),
depois os templates que todos consomem (`reference.md`), depois os procedimentos que
herdam esses templates (`novo-projeto.md`, depois o par inseparavel `fecha-marco.md` +
`tutor.md`), entao a persona que nomeia o ciclo completo (`metodo.md`, junto do
reenquadramento de feedback em `debug.md`) e, por fim, uma auditoria transversal de
consistencia. Cada fase entrega propriedades verificaveis dos docs (um revisor abre o
arquivo e confere), nao comportamentos de runtime.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Fundacao teorica (fundamentos.md)** - Catalogo upstream de frameworks com fontes, vocabulario do metodo e mitos refutados
- [ ] **Phase 2: Templates e sintaxe (reference.md)** - Objetivo de capacidade, GRR 3 fases, worked example e principios de Mayer nos templates
- [ ] **Phase 3: Bootstrap com Stage 2 (novo-projeto.md)** - Etapa de evidencia de maestria e primeiro done leve no bootstrap
- [ ] **Phase 4: Gate e retrieval (fecha-marco.md + tutor.md)** - Mastery gate, sintese/transferencia, retrieval ativo e revisao espacada
- [ ] **Phase 5: Persona e feedback (metodo.md + debug.md)** - Ciclo nomeado, anti-theory-leak, check formativo e feedback tri-partido
- [ ] **Phase 6: Auditoria de consistencia** - Verificacao transversal anti-drift e anti-cargo-cult

## Phase Details

### Phase 1: Fundacao teorica (fundamentos.md)
**Goal**: Existe um doc interno upstream que define o vocabulario canonico de frameworks que todos os outros docs vao referenciar, com fontes rastreaveis e mitos sinalizados.
**Depends on**: Nothing (first phase -- upstream da ordem inegociavel)
**Requirements**: FUND-01, FUND-02, FUND-03
**Success Criteria** (what must be TRUE):
  1. `mentor/fundamentos.md` existe e cataloga os 6 frameworks foundational (First Principles/Merrill, Backward Design/UbD, Constructive Alignment/Biggs, Cognitive Load Theory/Sweller, Worked-Example+Expertise-Reversal, Retrieval Practice) e os supporting (SDT, ZPD, Mastery, Avaliacao Formativa, Feedback Hattie, Spacing), cada um com definicao de 1 linha, fonte primaria, termo equivalente no metodo e um campo "aplicado em <doc>".
  2. Existe uma secao "O que NAO usamos e por que" que sinaliza estilos de aprendizagem, nativos digitais, Cone de Dale/percentuais de retencao e Bloom-como-piramide-rigida, cada um com a razao da refutacao.
  3. O doc declara explicitamente que `fundamentos.md` e interno (guia o agente) e nunca e lido pelo aluno nem injetado na sessao.
  4. O ressalva honesta sobre SDT relatedness em solo+IA e o limite de Mayer (so 3 de 12 principios em texto puro) aparecem registrados, sem inflar os claims.
**Plans**: 1 plan
- [x] 01-01-PLAN.md -- Criar mentor/fundamentos.md (preambulo de uso interno + catalogo 6+6 + ressalvas SDT/Mayer + mitos refutados + nice-to-cite)

### Phase 2: Templates e sintaxe (reference.md)
**Goal**: Os templates que todos os procedimentos consomem ganham o fio do verbo de capacidade, a sintaxe GRR de 3 fases e os principios de carga cognitiva, referenciando `fundamentos.md` para o "porque".
**Depends on**: Phase 1 (vocabulario canonico de fundamentos.md)
**Requirements**: EST-01, EST-02, EST-04, CARGA-01, CARGA-02, CARGA-03
**Success Criteria** (what must be TRUE):
  1. O template `CAMINHO.md` em `reference.md` tem um campo "Objetivo" expresso como capacidade com verbo de Bloom, ao lado do "Entregavel" de artefato; o template de aula espelha capacidade + artefato; o DONE do scaffold e enquadrado como evidencia de capacidade.
  2. A sintaxe de scaffold formaliza as 3 fases do GRR ("eu faco -> nos fazemos -> voce faz"), com a fase "nos fazemos" como etapa condicional explicita entre o exemplo resolvido e o `TODO(human)` solo.
  3. Backward design e GRR estao nomeados onde ja ocorrem, com referencia a `fundamentos.md` (sem reescrever a teoria localmente).
  4. O fading de scaffold por substrato (recuo do andaime conforme o dominio sobe) e o worked example analogo antes do `TODO(human)` para substrato baixo estao formalizados na sintaxe.
  5. A apresentacao de aula/scaffold aplica os 3 principios de Mayer que transferem para texto puro (coerencia, sinalizacao, segmentacao) e adota linguagem simples/legivel, citando honestamente o limite dos demais principios.
**Plans**: 3 plans
Plans:
- [x] 02-01-PLAN.md -- Wave 0: extrator de blocos cercados (anti-leak CONS-01) + smoke-test estatico da fase
- [x] 02-02-PLAN.md -- Fio do verbo de capacidade (EST-01): Objetivo no CAMINHO + aula espelha capacidade/artefato + DONE reenquadrado
- [x] 02-03-PLAN.md -- GRR 3 fases (EST-04) + fading/worked-example (CARGA-01/02) + Mayer (CARGA-03) + citacoes por hyperlink (EST-02)
**UI hint**: yes

### Phase 3: Bootstrap com Stage 2 (novo-projeto.md)
**Goal**: O bootstrap deixa de saltar do output desejado direto para o plano de passos: ganha uma etapa leve de evidencia de maestria por marco e nomeia o primeiro done leve como principio anti-evasao.
**Depends on**: Phase 1 (vocabulario), Phase 2 (templates de Objetivo/capacidade consumidos aqui)
**Requirements**: EST-03, ENG-02
**Success Criteria** (what must be TRUE):
  1. `novo-projeto.md` insere um Stage 2 (evidencia de maestria por marco) entre o Passe 1 (caminho) e a montagem de marcos, com ~1 frase de capacidade por marco (verbo de Bloom), enquadrado como backward design via referencia a `fundamentos.md`.
  2. A etapa Stage 2 e visivelmente leve (uma frase de capacidade por marco derivada da User Story, nao um sub-doc), preservando o bootstrap ja longo.
  3. O metodo nomeia e reforca o "primeiro done leve" (reduzir time-to-first-success) como principio anti-evasao, conectado explicitamente ao Walking Skeleton.
**Plans**: 2 plans
Plans:
- [x] 03-01-PLAN.md -- PAR ACOPLADO (D-02): campo Capacidade: no template PROGRESSO.md (reference.md) + Passo 5 instrui gravar a frase por marco + guardrail D-04 + primeiro marco menor
- [x] 03-02-PLAN.md -- Nomeacao + link: Passo 4 nomeia backward design; Passo 8 nomeia primeiro done leve (ENG-02), ambos com hyperlink para fundamentos.md

### Phase 4: Gate e retrieval (fecha-marco.md + tutor.md)
**Goal**: As duas maiores lacunas de avaliacao sao fechadas: o fechamento de marco vira mastery gate com sintese/transferencia e agenda de revisao espacada, e a sessao do tutor abre com recuperacao ativa e garante uma proxima acao unica.
**Depends on**: Phase 3 (Stage 2 define a evidencia que o gate cobra); Phase 2 (campo de agenda de retrieval no template PROGRESSO)
**Requirements**: ENG-01, AVAL-01, AVAL-02, AVAL-03, AVAL-04
**Success Criteria** (what must be TRUE):
  1. `tutor.md` abre a sessao com 1 pergunta de recuperacao ativa (retrieval practice) sobre conceito anterior, sem o aluno consultar a aula, e garante uma "proxima acao unica" inequivoca a cada sessao, ancorada em autonomia/competencia (SDT, com a ressalva sobre relatedness).
  2. `fecha-marco.md` enquadra o gate de marco explicitamente como mastery gate, com criterio de capacidade (nao so "o codigo roda") e um componente de sintese/transferencia (o aluno explica e estende sem andaime).
  3. `fecha-marco.md` agenda revisao espacada (spacing) de conceitos de marcos anteriores, e o campo de agenda de retrieval/dividas do `PROGRESSO.md` registra essa divida (a mesma divida que `tutor.md` vai cobrar na abertura).
  4. A mecanica de retrieval e gate permanece leve (1 pergunta na abertura; gate = verificacao de done ja existente renomeada + 1 criterio de capacidade), sem virar quiz formal ou checklist gigante.
**Plans**: 4 plans
Plans:
- [x] 04-01-PLAN.md -- Wave 0: clonar extract-fenced.sh + autorar check-phase4.sh (V-01..V-15)
- [x] 04-02-PLAN.md -- reference.md: secao `## Agenda de retrieval` no template PROGRESSO.md (D-09), dona do contrato cross-file
- [x] 04-03-PLAN.md -- fecha-marco.md: mastery gate + extensao (D-05..D-08), escreve a agenda (D-10), proxima acao unica + SDT (D-12/D-13)
- [x] 04-04-PLAN.md -- tutor.md: passo de Recuperacao ativa antes do recap (D-01..D-04), proxima acao unica + SDT (D-12/D-13) + gate cross-file (V-13)

### Phase 5: Persona e feedback (metodo.md + debug.md)
**Goal**: A persona amarra o ciclo por marco nomeando as etapas ja definidas, fixa a regra anti-theory-leak e o check formativo de curadoria, e o protocolo de forense vira feedback tri-partido.
**Depends on**: Phases 1-4 (metodo.md resume etapas que os outros docs ja nomearam)
**Requirements**: AVAL-05, AVAL-06, CONS-01
**Success Criteria** (what must be TRUE):
  1. `metodo.md` declara como regra/anti-padrao que a fundamentacao guia o agente mas o jargao de framework nunca e citado ao aluno na sessao (anti theory-leak), com 1 linha apontando `fundamentos.md` como o "porque" teorico.
  2. O gate de curadoria em `metodo.md` inclui um check formativo + prompt de auto-explicacao antes de avancar.
  3. O protocolo de forense em `debug.md` esta reescrito como feedback tri-partido (feed-up / feed-back / feed-forward, Hattie & Timperley), com a PISTA enquadrada como feed-forward que preserva a reflexao do aluno (nao entrega a resposta).
  4. O ciclo por marco em `metodo.md` cita as etapas nomeadas (gate, retrieval, GRR 3 fases) por referencia, sem duplicar a teoria que mora em `fundamentos.md` nem as definicoes que moram nos docs donos.
**Plans**: 3 plans
Plans:
- [x] 05-01-PLAN.md -- Wave 0: clonar extract-fenced.sh + autorar check-phase5.sh (V-01..V-18)
- [x] 05-02-PLAN.md -- metodo.md: anti-leak+FUND-03 (CONS-01) + check formativo (AVAL-05) + ciclo nomeado (C4) + ponteiro forense (D-07)
- [x] 05-03-PLAN.md -- debug.md: overlay Hattie feed-up/back/forward sobre os 6 passos + PISTA=feed-forward (AVAL-06)

### Phase 6: Auditoria de consistencia
**Goal**: Uma verificacao transversal final confirma que nenhuma teoria ficou sem aterrissagem (anti-cargo-cult) e que nenhum conteudo vazou para os adaptadores (anti-drift) apos editar 6+ docs em lote.
**Depends on**: Phases 1-5 (so se audita depois de todas as edicoes)
**Requirements**: CONS-02, CONS-03
**Success Criteria** (what must be TRUE):
  1. Cada pratica listada em `fundamentos.md` tem um "aplicado em <doc>" verificavel, e o doc citado realmente contem a aplicacao (anti cargo-cult: nenhuma teoria sem aterrissagem).
  2. Todo `/comando` tem `mentor/<comando>.md` correspondente e todos os paths em backticks resolvem.
  3. `README`, `AGENTS.md` e `metodo.md` descrevem o mesmo conjunto de procedimentos, sem divergencia.
  4. Nenhuma pratica deste milestone foi duplicada nos adaptadores (`.claude/`, `AGENTS.md`): eles continuam so apontando para `mentor/`, sem conteudo de metodo.
**Plans**: 3 plans
Plans:
- [ ] 06-01-PLAN.md -- Wave 1: escrever o harness permanente `scripts/check-consistencia.sh` (V-01..V-16; V-16 red esperado)
- [ ] 06-02-PLAN.md -- Wave 2: fix IN-01 (acentos debug.md:31-32) + flip dos 10 status pendentes em fundamentos.md (D-04) -> suite verde
- [ ] 06-03-PLAN.md -- Wave 3: relatorio de fechamento `06-AUDITORIA.md` (confirmacao semantica D-03 + politica de escalacao D-05)

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4 -> 5 -> 6

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Fundacao teorica (fundamentos.md) | 0/1 | Not started | - |
| 2. Templates e sintaxe (reference.md) | 0/TBD | Not started | - |
| 3. Bootstrap com Stage 2 (novo-projeto.md) | 0/TBD | Not started | - |
| 4. Gate e retrieval (fecha-marco.md + tutor.md) | 0/TBD | Not started | - |
| 5. Persona e feedback (metodo.md + debug.md) | 0/TBD | Not started | - |
| 6. Auditoria de consistencia | 0/TBD | Not started | - |
