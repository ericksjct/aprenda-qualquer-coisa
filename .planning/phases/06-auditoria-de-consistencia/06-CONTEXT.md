# Phase 6: Auditoria de consistencia - Context

**Gathered:** 2026-06-16
**Status:** Ready for planning

<domain>
## Phase Boundary

ULTIMA fase do milestone v1.0. NAO escreve metodo novo: faz a conferencia
cruzada final dos 8 docs de `mentor/` (+ adaptadores) editados nas Fases 1-5,
fechando dois requisitos:

- **CONS-02 (anti-cargo-cult):** cada pratica catalogada em `fundamentos.md`
  tem um "aplicado em <doc>" e o doc citado REALMENTE contem a aplicacao
  (nenhuma teoria sem aterrissagem). Hoje ~10 linhas estao marcadas
  `(Fase N, pendente)` na coluna "Aplicado em (doc + status)".
- **CONS-03 (anti-drift):** todo `/comando` tem `mentor/<comando>.md`; paths em
  backticks resolvem; `README`/`AGENTS.md`/`metodo.md` descrevem o MESMO conjunto
  de procedimentos; nenhuma pratica deste milestone foi duplicada nos adaptadores
  (`.claude/`, `AGENTS.md`) — eles seguem so apontando para `mentor/`.

**O que esta FORA (nao confundir):**
- NAO e o FUT-04 (verificador automatizado completo de drift) — isso e v2.
- NAO mexe em nenhuma etapa didatica do aluno; e fase de construcao do toolkit.
- NAO vira um linter de acentos permanente (Risco #5 fica fora; ver IN-01 abaixo).

</domain>

<decisions>
## Implementation Decisions

### Forma da auditoria — D-01
- **D-01:** A fase entrega DOIS artefatos: (a) um script leve PERMANENTE
  `scripts/check-consistencia.sh` (nome a confirmar no plano) commitado no repo, e
  (b) um relatorio de auditoria de fechamento (ex: `06-AUDITORIA.md` ou a propria
  VERIFICATION). Esta e uma mudanca deliberada de padrao: as Fases 2/4/5 usaram
  harness descartaveis (`check-phaseN.sh`) que NAO foram commitados (hoje so existe
  `scripts/roadmap_fetch.py`). O script da Fase 6 e a versao MINIMA e mecanica
  (so o que `grep`/teste de existencia consegue provar), atacando parcialmente o
  Risco #1 (drift) do mapa de codebase. A versao completa e o FUT-04 (v2).

### O que o script verifica — D-02 (CONS-03 mecanico)
- **D-02:** O script codifica os checks mecanicos do anti-drift:
  1. Todo `/comando` citado tem `mentor/<comando>.md` correspondente.
  2. Os paths em backticks (nos docs auditados) resolvem para arquivos existentes.
  3. Nenhuma pratica/jargao de metodo deste milestone vazou para os adaptadores
     (`.claude/`, `AGENTS.md`) — eles so apontam, sem conteudo de metodo.
  Reaproveitar o padrao de harness das fases anteriores (saida PASS/FAIL, exit 0).

### CONS-02 mora no script (grep) + confirmacao do agente — D-03
- **D-03:** A verificacao PROFUNDA do CONS-02 entra NO SCRIPT como rede de seguranca
  mecanica: para cada pratica de `fundamentos.md`, um `grep` confirma que o
  termo/aplicacao prometido APARECE no doc citado (ex: "feed-forward" em `debug.md`,
  GRR / "nos fazemos" em `reference.md`, "objetivo"/capacidade em `reference.md`).
  O AGENTE confirma UMA vez, na auditoria de fechamento, que a aplicacao faz SENTIDO
  (grep acha a palavra, nao julga semantica) e registra no relatorio.
  - **Racional (token economy):** custo unico baixo ao escrever; re-auditoria futura
    vira rodar 1 comando (~0 tokens) em vez de o agente reler 8 docs. A alternativa
    "so o agente le os docs" e a mais cara em tokens recorrentes e nao deixa artefato.

### Atualizacao dos status "pendente" — D-04
- **D-04:** Apos a verificacao profunda passar, virar as ~10 marcas
  `(Fase N, pendente)` da coluna "Aplicado em" de `fundamentos.md` para o status
  aplicado/feito (texto exato a definir no plano). So vira "aplicado" o que a
  verificacao profunda (D-03) confirmou de fato no doc citado.

### Politica de correcao ao achar problema — D-05
- **D-05:** Corrigir o TRIVIAL inline na Fase 6; ESCALAR o estrutural.
  - **Trivial (corrige direto):** flip de status `(Fase N, pendente)` -> aplicado
    (D-04); arrumar um path quebrado em backticks; remover acento solto (IN-01).
  - **Estrutural (mostra ao usuario ANTES de mexer):** uma teoria que realmente NAO
    aterrissou em lugar nenhum; conteudo de metodo de fato duplicado num adaptador;
    divergencia real no conjunto de procedimentos. Vira achado apresentado, nao
    fix silencioso.

### Rigor do Criterio 3 (conjunto de procedimentos) — D-06
- **D-06:** Igualdade de CONJUNTO, com a tabela de roteamento de `AGENTS.md` como
  fonte canonica da lista de procedimentos
  (`novo-projeto`, `tutor`, `fecha-marco`, `debug`, `spidr-split`). `README` e
  `metodo.md` tem de citar exatamente esse mesmo conjunto — sem sobra nem falta.
  Check objetivo e provavel (nao "ausencia de contradicao" frouxa).

### IN-01 (acentos) — D-07
- **D-07:** Corrigir os acentos `Peca`/`peca` em `debug.md:31-32` inline na Fase 6
  como conserto one-off (dívida adiada da Fase 5). NAO transformar em linter de
  acentos permanente — isso seria o Risco #5, fora de escopo.

### Claude's Discretion
- Nome exato do script (`check-consistencia.sh` vs outro), estrutura de saida e
  como ele lista as praticas de `fundamentos.md` para o grep.
- Texto exato do novo status que substitui `(Fase N, pendente)` em `fundamentos.md`.
- Se o relatorio de fechamento e um `06-AUDITORIA.md` proprio ou se cabe na
  VERIFICATION da fase — decisao do planner/executor.
- Como mapear cada linha de `fundamentos.md` ao termo-de-grep mais robusto (a
  palavra ancora menos fragil por pratica).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Contrato da fase (o que tem de ficar VERDADEIRO)
- `.planning/REQUIREMENTS.md` §CONS — CONS-02 (anti-cargo-cult) e CONS-03 (anti-drift).
- `.planning/ROADMAP.md` §"Phase 6: Auditoria de consistencia" — os 4 Criterios de Sucesso.

### Alvo principal da auditoria (anti-cargo-cult)
- `mentor/fundamentos.md` — coluna "Aplicado em (doc + status)"; ~10 linhas
  `(Fase N, pendente)` (Backward Design, Constructive Alignment, CLT/Mayer,
  Worked-Example, Retrieval, SDT, Mastery, Avaliacao Formativa, Hattie Feed-*,
  Spacing). Cada uma aponta o doc onde a aplicacao deve estar.

### Docs auditados / donos das aplicacoes (onde o grep procura)
- `mentor/reference.md` — GRR 3 fases, worked-example, objetivo/capacidade, Mayer.
- `mentor/novo-projeto.md` — backward design (Passe 1 -> Passe 2), Stage 2.
- `mentor/tutor.md` — retrieval na abertura, "proxima acao unica" (SDT).
- `mentor/fecha-marco.md` — mastery gate, spacing/dividas.
- `mentor/metodo.md` — anti-leak (CONS-01), avaliacao formativa, ciclo nomeado.
- `mentor/debug.md` — feedback tri-partido (Hattie), PISTA=feed-forward; acentos IN-01 (:31-32).
- `mentor/spidr-split.md` — comando coberto pela tabela de procedimentos.

### Adaptadores (anti-drift — devem SO apontar, nunca conter metodo)
- `AGENTS.md` — FONTE CANONICA do conjunto de procedimentos (tabela de roteamento
  `:16-23`); alvo do check de igualdade de conjunto (D-06).
- `README.md` — descricao de procedimentos (`:114-129`); deve casar com AGENTS.md/metodo.md.
- `.claude/` (skills nativas + output style `mentor-projeto`) — adaptadores finos.

### Convencoes, arquitetura e o concern que esta fase fecha
- `.planning/codebase/CONCERNS.md` §"Risco #1" — drift fonte<->adaptadores; esta fase
  e o down-payment mecanico parcial (FUT-04 = versao completa, v2).
- `.planning/codebase/ARCHITECTURE.md` — fonte-unica: teoria so em `mentor/`, citada
  por link, nunca duplicada nos adaptadores.
- `.planning/codebase/CONVENTIONS.md` — portugues SEM acentos; paths em backticks.
- `.planning/codebase/TESTING.md` — hoje a verificacao de consistencia e 100% manual.

### Padrao de harness das fases anteriores (referencia de estilo do script)
- Harness `check-phaseN.sh` das Fases 2/4/5 NAO estao no repo (descartaveis). O
  padrao (filtro stdin->stdout + checks PASS/FAIL, exit 0) esta descrito nos
  CONTEXT/SUMMARY dessas fases — reaproveitar a forma, agora PERSISTINDO o artefato.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `mentor/fundamentos.md` ja tem a coluna "Aplicado em (doc + status)" com a
  convencao `(Fase N, pendente)` — gancho pronto para D-04 (flip de status) e para
  o grep de D-03 (cada linha ja nomeia doc + termo no metodo).
- `AGENTS.md:16-23` ja tem a tabela situacao->procedimento — fonte canonica pronta
  para D-06 (lista de comandos).
- Padrao de harness PASS/FAIL ja foi exercitado 3x (Fases 2/4/5); o script da Fase 6
  reusa a forma, so que commitado.

### Established Patterns
- Fonte-unica + adaptadores finos: o anti-drift (D-02) verifica que isso nao foi
  violado; nao introduz excecao.
- Estilo: portugues SEM acentos, paths em backticks (o proprio check D-02 #2 e D-07
  defendem esse padrao).

### Integration Points
- Consome a saida de TODAS as fases anteriores (1-5) — so audita depois que tudo
  foi editado (Depends-on: Fases 1-5).
- Nao ha downstream: e a ultima fase; ao passar, o milestone v1.0 esta pronto para
  `/gsd-complete-milestone`.

</code_context>

<specifics>
## Specific Ideas

- Os 3 checks mecanicos do script (D-02): comando<->`mentor/<comando>.md`; paths em
  backticks resolvem; zero jargao de metodo nos adaptadores.
- O grep de CONS-02 (D-03) ancora em termos como "feed-forward" (`debug.md`),
  GRR/"nos fazemos" (`reference.md`), "backward design"/Passe 1->2 (`novo-projeto.md`).
- AGENTS.md como lista canonica de procedimentos para a igualdade de conjunto (D-06).
- IN-01: `debug.md:31-32` "Peca"/"peca" -> sem acento (D-07), one-off.

</specifics>

<deferred>
## Deferred Ideas

- **FUT-04** — verificador de drift automatizado COMPLETO. A Fase 6 entrega so o
  down-payment mecanico minimo (D-01/D-02); a versao robusta e v2.
- **Linter de acentos permanente** (Risco #5) — fora de escopo; D-07 e so o conserto
  pontual do IN-01, nao um lint imposto.
- Parametrizar a raiz do repo para o toolkit rodar fora dele (Risco #2) — fora de escopo.

</deferred>

---

*Phase: 06-auditoria-de-consistencia*
*Context gathered: 2026-06-16*
