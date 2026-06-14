# Requirements: Mentor de Aprendizado por Projeto

**Defined:** 2026-06-13
**Core Value:** O agente ensina a construir (aluno sai capaz de explicar e estender o projeto sozinho), agora ancorado em ciência da aprendizagem reconhecida — nunca resolve pelo aluno.

> Cada requisito é uma capacidade verificável do MÉTODO (o que o toolkit passa a
> instruir o agente a fazer), não software. "Aplicado em <doc>" é a evidência: a prática
> tem de aterrissar num arquivo de `mentor/`, não só ser citada.

## v1 Requirements

### Fundamentos (FUND)

- [ ] **FUND-01**: Existe `mentor/fundamentos.md` catalogando os 6 frameworks foundational (First Principles/Merrill, Backward Design/UbD, Constructive Alignment/Biggs, Cognitive Load Theory/Sweller, Worked-Example+Expertise-Reversal, Retrieval Practice) e os supporting (SDT, ZPD, Mastery, Avaliação Formativa, Feedback Hattie, Spacing) — cada um com definição de 1 linha, fonte primária, termo equivalente no método e "aplicado em <doc>"
- [ ] **FUND-02**: `fundamentos.md` tem seção "O que NÃO usamos e por quê" sinalizando os mitos refutados (estilos de aprendizagem, nativos digitais, Cone de Dale/percentuais de retenção, Bloom como pirâmide rígida) com a razão
- [ ] **FUND-03**: O método declara que `fundamentos.md` é doc interno que guia o agente — nunca lido pelo aluno nem injetado na sessão

### Estrutura & objetivos (EST)

- [ ] **EST-01**: O template `CAMINHO.md` (em `reference.md`) ganha um campo "Objetivo" expresso como capacidade com verbo de Bloom, ao lado do "Entregável" de artefato
- [ ] **EST-02**: Backward design e Gradual Release of Responsibility (GRR) são nomeados nos docs onde já ocorrem (`reference.md`, `novo-projeto.md`), referenciando `fundamentos.md`
- [ ] **EST-03**: O bootstrap (`novo-projeto.md`) insere um Stage 2 (evidência de maestria por marco) entre o Passe 1 (caminho) e a montagem de marcos, com ~1 frase de capacidade por marco
- [ ] **EST-04**: A fase "we do" (nós-fazemos) do GRR é formalizada como etapa intermediária explícita entre o exemplo resolvido e o `TODO(human)` solo, na sintaxe de scaffold/tutoria

### Engajamento & retenção (ENG)

- [ ] **ENG-01**: `PROGRESSO.md` e `tutor.md` garantem uma "próxima ação única" inequívoca a cada sessão (mitigação da evasão assíncrona), ancorada em autonomia/competência (SDT, com a ressalva honesta sobre relatedness em solo+IA)
- [ ] **ENG-02**: O método nomeia e reforça o "primeiro done leve" (reduzir time-to-first-success) como princípio anti-evasão, conectado ao Walking Skeleton

### Avaliação & feedback (AVAL)

- [ ] **AVAL-01**: `tutor.md` abre a sessão com 1 pergunta de recuperação ativa (retrieval practice) sobre conceito anterior, sem o aluno consultar a aula
- [ ] **AVAL-02**: `fecha-marco.md` agenda revisão espaçada (spacing) de conceitos de marcos anteriores, e `PROGRESSO.md` ganha um campo de agenda de retrieval/dívidas para registrar isso
- [ ] **AVAL-03**: `fecha-marco.md` enquadra o gate de marco explicitamente como mastery gate, com critério de capacidade (não só "o código roda")
- [ ] **AVAL-04**: O gate inclui um componente de síntese/transferência (o aluno explica e estende sem andaime), combatendo proxy-completion / atomização
- [ ] **AVAL-05**: O gate de curadoria (`metodo.md`) inclui um check formativo + prompt de auto-explicação antes de avançar
- [ ] **AVAL-06**: O protocolo de forense (`debug.md`) é reescrito como feedback tri-partido (feed-up / feed-back / feed-forward, Hattie & Timperley), com a PISTA enquadrada como feed-forward que preserva a reflexão

### Carga cognitiva & acessibilidade (CARGA)

- [ ] **CARGA-01**: O método formaliza o fading de scaffold por substrato (o andaime recua conforme o domínio do assunto sobe), tratando o expertise-reversal effect
- [ ] **CARGA-02**: O worked example análogo antes do `TODO(human)` é formalizado como etapa para substrato baixo (instância diferente da aplicação)
- [ ] **CARGA-03**: A apresentação de aula/scaffold aplica os 3 princípios de Mayer que transferem para texto puro (coerência, sinalização, segmentação) e adota linguagem simples/legível (acessibilidade), citando honestamente o limite dos demais princípios

### Consistência & integridade (CONS)

- [ ] **CONS-01**: `metodo.md` declara como regra/anti-padrão que a fundamentação guia o agente mas o jargão de framework nunca é citado ao aluno na sessão (anti theory-leak)
- [ ] **CONS-02**: Cada prática listada em `fundamentos.md` tem um "aplicado em <doc>" verificável (anti cargo-cult: nenhuma teoria sem aterrissagem)
- [ ] **CONS-03**: Auditoria de consistência final passa: todo `/comando` tem `mentor/<comando>.md`; paths em backticks resolvem; `README`/`AGENTS.md`/`metodo.md` descrevem o mesmo conjunto de procedimentos; nenhuma prática foi duplicada nos adaptadores (`.claude/`, `AGENTS.md`)

## v2 Requirements

### Futuro (FUT)

- **FUT-01**: Interleaving intencional de conceitos antigos dentro de marcos novos
- **FUT-02**: Modo "tente antes" opcional baseado em Productive Failure (Kapur) — evidência MEDIUM, validar primeiro
- **FUT-03**: Desafio opcional formalizado (autonomia SDT além do drill condicional)
- **FUT-04**: Script de verificação automatizada de drift `mentor/` ↔ adaptadores (resolve o concern #1 do mapa de codebase de forma mecânica, não por checklist manual)
- **FUT-05**: Rubrica reutilizável de critérios observáveis para curadoria de marco (além do critério por marco)

## Out of Scope

| Feature | Reason |
|---------|--------|
| Badges / pontos / XP / leaderboards / streaks | Gamificação extrínseca faz crowd-out da motivação intrínseca (SDT) — contraria o Core Value |
| Jargão de framework visível ao aluno (ADDIE/Bloom/CLT na sessão) | A fundamentação guia o agente, não vira conteúdo despejado no aluno |
| `fundamentos.md` injetado/lido na sessão do aluno | É doc interno do método; expor recria o "paredão de teoria" que o método combate |
| Adaptação por estilo de aprendizagem | Neuromito refutado (Pashler et al. 2008) |
| ADDIE waterfall como processo obrigatório do bootstrap | Conflita com o "roadmap vivo" (recalibração); citar só para situar linhagem |
| Duplicar práticas nos adaptadores (`.claude/`, `AGENTS.md`) | Viola o design fonte-única; só `mentor/` carrega conteúdo |
| Quiz somativo com nota / certificação | Avaliação aqui é formativa (a serviço do aprender), não somativa |
| Teoria despejada upfront antes de construir | Anti-padrão central do método; a aula é por passo, just-in-time |
| Código de aplicação / runtime / plataforma-LMS / vídeo | Milestone é de método em markdown; "curso assíncrono" é fonte de boas práticas, não artefato a construir |

## Traceability

> Preenchida pelo roadmapper na criação do ROADMAP.md.

| Requirement | Phase | Status |
|-------------|-------|--------|
| (a mapear) | — | Pending |

**Coverage:**
- v1 requirements: 21 total
- Mapped to phases: 0 (pré-roadmap)
- Unmapped: 21 ⚠️ (será resolvido pelo roadmapper)

---
*Requirements defined: 2026-06-13*
*Last updated: 2026-06-13 after initial definition*
