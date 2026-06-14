# Project Research Summary

**Project:** Mentor de Aprendizado por Projeto -- ancoragem em ciencia da aprendizagem
**Domain:** Design instrucional para toolkit markdown assincrono mediado por IA
**Researched:** 2026-06-13
**Confidence:** HIGH

## Executive Summary

O metodo ja implementa, sem nomear, a maioria dos frameworks consagrados: bootstrap em 2
passes E backward design (Wiggins & McTighe); espinha passo/aula/scaffold E First Principles
of Instruction (Merrill); campo DONE E mastery learning (Bloom/Guskey) + constructive
alignment (Biggs); aula just-in-time E gestao de carga intrinseca (Sweller). O milestone
nao pede reestruturacao da espinha -- pede nomeacao das etapas existentes, completude de
3-4 lacunas reais e criacao de fundamentos.md como catalogo rastreavel de fontes.
Identidade central (ensinar-construindo, TODO(human), agnostico de LLM) preservada.

As lacunas genuinas sao pequenas em numero mas altas em impacto. A mais urgente e dupla:
tutor.md nao formaliza recuperacao ativa (retrieval practice) nem revisao espacada
(spacing) -- as 2 unicas estrategias de alta utilidade de Dunlosky et al. (2013), e
inseparaveis segundo Roediger/Butler. A segunda lacuna e o Stage 2 do UbD (evidencia de
dominio) ausente como etapa no bootstrap: o metodo salta de output desejado direto para
plano de passos sem definir como saber que o aluno aprendeu -- fragilizando o alinhamento
construtivo de todo o DONE downstream. A terceira lacuna e a fase we-do (pratica guiada)
do Gradual Release of Responsibility colapsada entre o exemplo e o TODO(human) solo.

Os principais riscos: cargo-culting (citar frameworks sem mudar comportamento do agente),
citar mitos refutados (estilos de aprendizagem, cone de Dale, nativos digitais) e drift
de fonte-unica ao editar 6+ docs em lote. Mitigacao: cada pratica em fundamentos.md
precisa de aplicado-em-<doc> verificavel; teoria nunca vaza para a sessao do aluno.

## Key Findings

### Frameworks de Ancoragem

**Foundational (load-bearing) -- os 6 que todo o resto cita:**

| Framework | Ancora no metodo | Lacuna revelada |
|-----------|-----------------|-----------------|
| First Principles of Instruction (Merrill 2002/2013) | Espinha inteira: problema real / ativacao / demonstracao / aplicacao / integracao | Nenhuma -- ancora tudo |
| Backward Design / UbD (Wiggins & McTighe 1998/2005) | Bootstrap Passe 1 -> Passe 2 como engenharia reversa | Stage 2 (evidencia de maestria) ausente como etapa explicita |
| Constructive Alignment (Biggs 1996) | Par META -> DONE; objetivo CAMINHO -> aula -> scaffold | Falta o verbo de capacidade conectando os tres |
| Cognitive Load Theory (Sweller 1988/2011) | 1 conceito dominante por passo; aula minima just-in-time | Scaffold de densidade fixa (sem fading por substrato) |
| Worked-Example + Expertise-Reversal (Sweller & Cooper 1985; Kalyuga 2003) | Scaffold TODO(human) como completion problem | Fading ausente: suporte deveria recuar conforme substrato sobe |
| Retrieval Practice / Testing Effect (Roediger & Karpicke 2006; Dunlosky 2013) | -- | LACUNA URGENTE: tutor.md nao pede recuperacao ativa |

**Supporting (ancoram um doc especifico):**
- SDT (Deci & Ryan): ancora anti-evasao via autonomia + competencia. LIMITE HONESTO:
  relatedness e estruturalmente fraca em solo+IA -- citar com ressalva, nao inflar.
- Scaffolding/ZPD (Vygotsky; Wood, Bruner & Ross 1976): raiz teorica do vocabulario
  scaffold; complementa CLT com a metafora mentor-aprendiz.
- Mastery Learning (Bloom 1968): ancora gate de aprovacao. Lacuna: ciclo de correcao
  quando DONE falha nao esta definido.
- Avaliacao Formativa (Black & Wiliam 1998): reenquadra DONE, pergunta-guia e diario
  como instrumentos formativos, nao somativos.
- Feedback Feed-Up/Back/Forward (Hattie & Timperley 2007): ancora PISTA como
  feed-forward (nao entrega a resposta; preserva reflexao do aluno).
- Spacing Effect (Cepeda et al. 2006): lacuna em tutor.md; inseparavel do retrieval.

**Nice-to-cite (reforco, nao estrutura):**
- Bloom revisado (Anderson & Krathwohl 2001): banco de verbos; NAO usar como piramide.
- Mayer (2001/2021): LIMITE -- so 3 de 12 principios transferem para texto puro
  (coerencia, sinalizacao, segmentacao); os 9 restantes sao sobre midia inexistente aqui.
- Productive Failure (Kapur 2008): modo tente-antes opcional; evidencia MEDIUM.
- ARCS (Keller 1987): checklist operacional de motivacao; SDT explica o por que.
- Microlearning, interleaving, ADDIE/SAM, Gagne: citar 1x para situar linhagem; nao
  estruturar o metodo neles.

**Nao usar (refutados -- sinalizar em fundamentos.md):**
- Estilos de aprendizagem / meshing hypothesis (VAK/VARK): neuromito refutado.
- Nativos digitais: sem base empirica.
- Piramide de aprendizagem / Cone de Dale com percentuais: numeros fabricados.
- Bloom como sequencia rigida obrigatoria: interpretacao equivocada.

### Tecnicas Pedagogicas

**Must-have (table stakes):**
- mentor/fundamentos.md novo: catalogo pratica -> fonte -> vocabulario do metodo ->
  aplicado em <doc>; o entregavel-ancora do milestone. (new)
- Objetivo mensuravel: verbo de capacidade (Bloom) ao lado do entregavel de artefato.
  Hoje o metodo tem so o segundo. (new, MEDIUM)
- Nomear backward design + GRR 3 fases nos docs onde ja acontecem. (reinforce, LOW)
- Check formativo + prompt de auto-explicacao no gate de curadoria. (new, LOW)
- Feedback tri-partido (Hattie) no protocolo de forense de debug.md. (new, MEDIUM)
- Regra explicita: jargao de framework invisivel ao aluno. (new, LOW)

**Should-have (diferenciam a qualidade pos-nucleo validado):**
- Retrieval practice + revisao espacada em tutor.md -- inseparaveis. (new, MEDIUM)
- Fading de scaffold por substrato: suporte recua conforme dominio sobe. (new, MEDIUM)
- Rubrica de criterios observaveis para curadoria de marco. (new, MEDIUM)
- Worked example analogo antes do TODO(human). (reinforce/new, MEDIUM)

**Defer (v2+):**
- Interleaving intencional de conceitos antigos em marcos novos.
- Desafio opcional formalizado (SDT alem do drill condicional).
- Verificacao automatizada de drift mentor/ vs adaptadores.

**Anti-features -- Out of Scope em REQUIREMENTS.md:**
- Badges / pontos / XP / leaderboards / streaks (crowd-out de motivacao intrinseca).
- Jargao de framework visivel ao aluno (ADDIE/Bloom/CLT na sessao).
- fundamentos.md injetado na sessao do aluno.
- Adaptacao por estilo de aprendizagem (mito refutado).
- ADDIE waterfall como processo obrigatorio do bootstrap.
- Duplicar praticas nos adaptadores (viola fonte-unica).
- Quiz somativo com nota / certificacao.
- Teoria upfront despejada antes de construir.

### Estrutura do Sistema

fundamentos.md (NOVO) e o upstream teorico -- todos os outros citam, nunca definem.
Regra de ouro: teoria mora em fundamentos.md; procedimentos referenciam por link.

**Componentes e responsabilidades:**
1. fundamentos.md (NOVO, upstream): catalogo de frameworks + fontes + vocabulario;
   define termos canonicos que todos os outros docs citam.
2. reference.md: templates de CAMINHO, aula, scaffold, PROGRESSO; dono da sintaxe GRR
   3 fases e do campo Objetivo (verbo Bloom).
3. novo-projeto.md: bootstrap em 3 stages: Stage 1 output/substrato, Stage 2 evidencia
   de maestria por marco (NOVO), Stage 3 CAMINHO + marcos.
4. fecha-marco.md: mastery gate enquadrado explicitamente; agenda retrieval espacado.
5. tutor.md: abertura com 1 pergunta de recuperacao ativa; nos-fazemos condicional.
6. metodo.md: persona/conduta/ciclo; etapas nomeadas; regra que fundamentos.md e
   invisivel ao aluno.

**Build order inegociavel:**
fundamentos.md -> reference.md -> novo-projeto + fecha-marco + tutor -> metodo.md.

### Pitfalls Criticos

1. **Cargo-cult de frameworks (P8):** citar sem mudar comportamento do agente.
   Prevencao: cada pratica em fundamentos.md exige aplicado em <doc> verificavel.
2. **Citar mitos refutados (P11):** estilos de aprendizagem, cone de Dale, nativos
   digitais. Prevencao: secao O que NAO usamos e por que em fundamentos.md.
3. **Teoria vazando para o aluno (P9):** agente citando CLT/Bloom/retrieval na sessao.
   Prevencao: regra explicita em metodo.md; fundamentos.md como doc interno.
4. **Avaliacao atomizada / proxy completion (P4):** done = roda, sem sintese.
   Prevencao: gate de fecha-marco exige sintese/transferencia alem do artefato.
5. **Drift fonte-unica ao editar em lote (P12):** milestone edita 6+ docs.
   Prevencao: praticas so em mentor/; checklist de ponteiros no fim.

Moderados: expertise-reversal (scaffold fixo prejudica avancado; modular por substrato);
over-formalizacao (backward design como lente, nao burocracia); feedback como elogio
vago; evasao async (PROGRESSO com next-action unico; primeiro done leve).

## Implications for Roadmap

### Fase 0: Fundacao upstream -- fundamentos.md
**Rationale:** Define vocabulario canonico que todos os outros docs citam. Qualquer
outro doc primeiro garante drift semantico desde o inicio.
**Delivers:** Catalogo de 6 frameworks foundational + 6 supporting, cada um com definicao,
fonte primaria, vocabulario do metodo, aplicado em <doc>. Secao O que NAO usamos e por que.
**Addresses:** Anti-features, cargo-cult, mitos.
**Avoids:** Pitfalls 8, 9, 11; drift semantico entre docs.
**Research flag:** Padrao bem-documentado; nenhuma pesquisa adicional necessaria.

### Fase 1: Templates e sintaxe -- reference.md
**Rationale:** Templates de CAMINHO e PROGRESSO sao consumidos pelos procedimentos das
fases seguintes. Sem campo Objetivo e agenda retrieval no PROGRESSO, os outros
procedimentos nao tem onde encaixar as etapas novas.
**Delivers:** Campo Objetivo (capacidade, verbo Bloom) ao lado de Entregavel no template
CAMINHO; DONE como evidencia de capacidade; GRR 3 fases formalizada; campo de agenda
retrieval/dividas no template PROGRESSO.
**Addresses:** Lacunas L4 (GRR colapsada) e L5 (verbo Bloom ausente).
**Avoids:** Pitfalls 4, 3.
**Research flag:** Padrao CLT + Bloom + GRR bem-estabelecido; sem pesquisa adicional.

### Fase 2: Bootstrap com Stage 2 -- novo-projeto.md
**Rationale:** Lacuna estrutural do UbD: bootstrap hoje salta de output desejado para
plano de passos sem definir evidencia de maestria. Dependente de Fase 0 e Fase 1.
**Delivers:** Stage 2 entre Passe 1 e marcos: evidencia de maestria por marco; criterio
de capacidade (verbo Bloom) ao lado do DoD de artefato; bootstrap enquadrado como
backward design (referencia a fundamentos.md).
**Addresses:** Lacuna L1 (Stage 2 ausente).
**Avoids:** Pitfall 10 (over-formalizacao): Stage 2 = +1 frase de capacidade por marco.
**Research flag:** Padrao bem-documentado; sem pesquisa adicional.

### Fase 3: Gate e retrieval -- fecha-marco.md + tutor.md
**Rationale:** As duas maiores lacunas de avaliacao. Agrupadas porque retrieval e spacing
sao inseparaveis e porque fecha-marco agenda a divida que tutor vai cobrar.
Dependente de Fase 1 (campo de agenda no PROGRESSO).
**Delivers:**
- fecha-marco.md: mastery gate enquadrado; criterio de capacidade no gate; componente
  de sintese/transferencia (explique e estenda sem andaime); agendamento de retrieval.
- tutor.md: abertura com 1 pergunta de recuperacao ativa (sem consultar a aula);
  nos-fazemos condicional quando salto modelo->solo for grande.
**Addresses:** Lacunas L2 (mastery gate implicito), L3 (retrieval espacado ausente).
**Avoids:** Pitfalls 4 (proxy completion), 5 (sem retrieval/spacing).
**Research flag:** Mecanica simples; validar leveza na execucao, nao em pesquisa nova.

### Fase 4: Persona e conduta -- metodo.md
**Rationale:** Amarra o que todas as fases anteriores ja nomearam. Vai por ultimo porque
descreve o ciclo completo por marco -- so pode descrever etapas ja definidas nos outros.
**Delivers:** Ciclo por marco com etapas nomeadas (gate, retrieval, GRR 3 fases);
anti-padroes novos; regra: fundamentacao guia o agente, nunca citada ao aluno; 1 linha
apontando fundamentos.md como o por que teorico.
**Addresses:** Pitfalls 9 (teoria ao aluno), 6 (feedback elogio), 7 (gamificacao).
**Avoids:** Pitfalls 8 (cargo-cult), 10 (over-formalizacao).
**Research flag:** Padrao bem-claro; sem pesquisa adicional.

### Fase 5: Verificacao de consistencia (transversal)
**Rationale:** Milestone edita 6+ docs de mentor/. Concern #1 do mapa (drift) sem
verificacao automatizada.
**Delivers:** Checklist: todo /comando tem mentor/<comando>.md; paths resolvem;
README/AGENTS/metodo descrevem o mesmo conjunto; nenhum conteudo nos adaptadores;
nenhuma pratica em fundamentos.md sem aplicado em X.
**Avoids:** Pitfall 12 (drift); cargo-cult nao detectado.
**Research flag:** Auditoria interna; sem padrao externo a pesquisar.

### Phase Ordering Rationale

- fundamentos.md primeiro: vocabulario que todos os outros citam; inverter = drift.
- reference.md antes dos procedimentos: templates consumidos por novo-projeto,
  fecha-marco e tutor; sem campo de agenda nao ha onde registrar a divida de retrieval.
- novo-projeto antes de fecha-marco/tutor: Stage 2 define evidencias que o gate cobra;
  ordem reflete backward design no proprio processo de edicao.
- metodo.md por ultimo: pressupoe que os outros ja nomearam suas etapas.
- Verificacao no fim: conferir consistencia so depois de todas as edicoes.

### Research Flags

Todas as fases tem evidencia forte -- nenhuma requer /gsd-research-phase adicional.
O que precisa de validacao e de natureza de execucao:

- **Fase 3 (tutor.md):** confirmar que 1 pergunta de recuperacao nao adiciona friccao
  excessiva ao ritual de sessao (validar leveza, nao pesquisa nova).
- **Fase 2 (Stage 2 do UbD):** confirmar que a frase de capacidade nao incha o
  bootstrap (~1 frase por marco, nao sub-doc).
- **Fase 5:** execucao de checklist de consistencia, nao pesquisa.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Frameworks (STACK) | HIGH | Fontes primarias verificadas; atribuicoes rastreadas; debunked sinalizado |
| Tecnicas pedagogicas (FEATURES) | HIGH | Ancoradas nas mesmas fontes; tag reinforce/new clara |
| Estrutura e build order (ARCHITECTURE) | HIGH/MEDIUM | Frameworks HIGH; costura especifica MEDIUM |
| Pitfalls | HIGH/MEDIUM | Claims centrais HIGH; aplicacao ao toolkit e inferencia (MEDIUM) |

**Overall confidence:** HIGH nos frameworks e lacunas identificadas; MEDIUM nas escolhas
de costura especificas (forma exata de cada campo, frase de capacidade).

### Gaps to Address

- **SDT relatedness em solo+IA:** estruturalmente fraca sem interlocutor humano. Citar
  honestamente; nao inflar o claim de SDT em fundamentos.md.
- **Mayer multimidia em texto puro:** 9 de 12 principios nao se transferem para markdown
  sem audio/video. Citar so os 3 aplicaveis (coerencia, sinalizacao, segmentacao).
- **Productive Failure como modo opcional:** evidencia MEDIUM; nao entra neste milestone;
  registrar para v1.x.
- **Verificacao automatizada de drift:** concern #1 sem solucao neste milestone. Follow-up
  pos-entrega (script de verificacao de ponteiros).
- **Custo do Stage 2 no bootstrap:** confirmar na execucao que o campo nao pesa para
  projetos com muitos marcos (mitigacao: campo opcional inicialmente).

## Sources

### Primary (HIGH confidence)

- Merrill (2002/2013), First Principles of Instruction, ETR&D
- Wiggins & McTighe (1998/2005), Understanding by Design (ASCD)
- Biggs (1996), Enhancing teaching through constructive alignment
- Sweller (1988); Sweller, Ayres & Kalyuga (2011), Cognitive Load Theory
- Sweller & Cooper (1985) worked-example; Kalyuga et al. (2003) expertise-reversal
- Roediger & Karpicke (2006), Test-Enhanced Learning, Psych Science
- Dunlosky et al. (2013), Improving Students Learning
- Deci & Ryan (1985; 2017), Self-Determination Theory
- Vygotsky (ZPD); Wood, Bruner & Ross (1976), scaffolding
- Bloom (1968), Mastery Learning; Guskey
- Black & Wiliam (1998), formative assessment
- Hattie & Timperley (2007), The Power of Feedback, RER
- Pearson & Gallagher (1983); Fisher & Frey -- Gradual Release of Responsibility
- Anderson & Krathwohl (2001), Bloom revisado
- Cepeda et al. (2006), spacing; Rohrer & Taylor (2007), interleaving

### Secondary (MEDIUM confidence)

- Kapur (2008); Sinha & Kapur (2021), Productive Failure
- Keller (1987), ARCS Model
- Mayer (2001/2021), principios multimidia -- aplicabilidade parcial em texto puro
- Kirschner, Sweller & Clark (2006) -- contra descoberta nao-guiada

### Debunked (sinalizar ativamente, nao citar como fundamento)

- Pashler et al. (2008); BPS -- estilos de aprendizagem (meshing hypothesis refutada)
- Kirschner & De Bruyckere (2017); Nature (2017) -- nativos digitais
- Treichler (1967) / corrupcao do Cone de Dale -- percentuais de retencao fabricados
- Interpretacao rigida de Bloom como piramide sequencial

---
*Research completed: 2026-06-13*
*Ready for roadmap: yes*
