---
phase: 02-templates-e-sintaxe-reference-md
verified: 2026-06-14T00:00:00Z
status: passed
score: 5/5 must-haves verified
overrides_applied: 0
---

# Phase 02: Templates e Sintaxe (reference.md) Verification Report

**Phase Goal:** Os templates que todos os procedimentos consomem ganham o fio do verbo de capacidade, a sintaxe GRR de 3 fases e os principios de carga cognitiva, referenciando `fundamentos.md` para o "porque".
**Verified:** 2026-06-14
**Status:** passed
**Re-verification:** No — initial verification

## Goal Achievement

### Observable Truths (ROADMAP Success Criteria)

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | `CAMINHO.md` tem "Objetivo (capacidade)" com verbo ao lado do "Entregavel"; aula espelha capacidade+artefato; DONE do scaffold enquadrado como evidencia de capacidade | VERIFIED | `reference.md:76` e `:85` — `- Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>` posicionada ACIMA de `- Entregavel:` em P01 e P02. Aula `## Objetivo do passo` (`:292-296`) reescrita para "capacidade ... e o artefato que prova isso". DONE (`:365`) = "evidencia observavel de que voce JA CONSEGUE <a capacidade...>, nao so 'o codigo compila'". Gate EST-01a=2, EST-01b=1 PASS |
| 2 | Sintaxe formaliza 3 fases do GRR com "nos fazemos" como etapa condicional explicita entre exemplo resolvido e `TODO(human)` solo | VERIFIED | `reference.md:400-423` — corpo da secao entrega **eu faco** (`:410`), **nos fazemos** (`:413`), **voce faz** (`:416`). Gatilho condicional explicito em `:419-423` ("ligue a etapa quando ... zero-absoluto/iniciante OU quando o salto ... e grande; PULE ... em intermediario/avancado"). Gate EST-04=4 PASS |
| 3 | Backward design e GRR nomeados onde ocorrem, referenciando `fundamentos.md` sem reescrever teoria localmente | VERIFIED | Backward design linkado em `reference.md:97-98`; GRR ("liberacao gradual de responsabilidade") linkado em `:406`. Ambos apontam `fundamentos.md#frameworks-foundational-load-bearing` (heading real em `fundamentos.md:19`). Teoria nao reescrita — so nomeada + linkada. Gate EST-02=4, ANCHOR-RESOLVE PASS |
| 4 | Fading de scaffold por substrato e worked example analogo antes do `TODO(human)` para substrato baixo formalizados | VERIFIED | Fading/expertise-reversal nomeado em `reference.md:33-39` (Sondagem) — "O andaime RECUA conforme a maestria sobe" + link. Worked example analogo (instancia DIFERENTE) na fase "eu faco" (`:410-412`), OBRIGATORIO para zero-absoluto. Gate CARGA-01=3, CARGA-02=8 PASS |
| 5 | Apresentacao aplica os 3 principios de Mayer que transferem para texto puro (coerencia, sinalizacao, segmentacao) + linguagem simples, citando honestamente o limite dos demais | VERIFIED | `reference.md:344-348` — "3 principios de Mayer que transferem para texto — coerencia ... sinalizacao ... segmentacao ... e linguagem simples/legivel. Os outros 9 ... nao se aplicam" + link `#mayer-so-3-de-12-principios-em-texto-puro` (heading real em `fundamentos.md:70`). Limite honesto "3 de 12" presente. Gate CARGA-03=1 PASS |

**Score:** 5/5 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `mentor/reference.md` | Templates com capacidade + GRR 3 fases + carga cognitiva + citacoes por hyperlink | VERIFIED | Todas as 6 edicoes presentes (Z1/Z2 fading, Z3 CAMINHO, Z4 aula+Mayer, Z5 DONE, Z6 GRR). Contem `Objetivo (capacidade):` e `nos fazemos` |
| `scripts/extract-fenced.sh` | Extrator de blocos cercados (isola conteudo para grep negativo) | VERIFIED | Existe (1009B). Isola conteudo de blocos cercados via awk toggle; saida = 0 jargao (baseline limpo) |
| `scripts/check-phase2.sh` | Smoke-test estatico (gate da fase): 9 checagens | VERIFIED | Existe (3.7K). Roda 9 checagens; chama extract-fenced.sh; reporta 0 fail(s) |

### Key Link Verification

| From | To | Via | Status | Details |
|------|-----|-----|--------|---------|
| prosa de `reference.md` | `fundamentos.md#frameworks-foundational-load-bearing` | hyperlink relativo | WIRED | Heading real `## Frameworks foundational (load-bearing)` em `fundamentos.md:19`; usado em `:97-98` e `:406` |
| prosa de `reference.md` | `fundamentos.md#mayer-so-3-de-12-principios-em-texto-puro` | hyperlink relativo | WIRED | Heading real `### Mayer: so 3 de 12 principios em texto puro` em `fundamentos.md:70`; usado em `:347-348` |
| `check-phase2.sh` | `extract-fenced.sh` | chama extrator + grep negativo so na saida | WIRED | Gate invoca o extrator para a checagem ANTI-LEAK |

Apenas 2 ancoras distintas usadas em `reference.md`; ambas resolvem para headings reais. 0 links quebrados.

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|----------|---------|--------|--------|
| Gate da fase reporta 0 fails | `sh scripts/check-phase2.sh` | `== 0 fail(s) ==`, exit=0, 9/9 PASS | PASS |
| Anti-leak: 0 jargao dentro de blocos cercados | `extract-fenced.sh \| rg -c <jargao>` | 0 | PASS |
| Ancoras resolvem para headings reais | `rg -o "fundamentos.md#..." \| sort -u` + cross-check `^#` em fundamentos.md | 2 ancoras, ambas existem | PASS |
| Teoria single-sourced: "3 de 12" so na prosa | `extract-fenced.sh \| rg -c "3 de 12"` | 0 (fora dos blocos) | PASS |
| Convencao sem acentos | `rg -c "[acentos]" reference.md` | 0 | PASS |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|-------------|-------------|--------|----------|
| EST-01 | 02-02 | Campo "Objetivo" como capacidade ao lado do "Entregavel" | SATISFIED | `reference.md:76,85` (CAMINHO), `:292-296` (aula), `:365` (DONE). Gate EST-01a/b PASS |
| EST-02 | 02-03 | Backward design e GRR nomeados, referenciando `fundamentos.md` | SATISFIED | Links em `:97-98`, `:406`; 2 ancoras resolvem. Gate EST-02 PASS |
| EST-04 | 02-03 | Fase "we do" formalizada entre exemplo resolvido e `TODO(human)` solo | SATISFIED | `:413` "nos fazemos" condicional. Gate EST-04 PASS |
| CARGA-01 | 02-03 | Fading de scaffold por substrato (expertise-reversal) | SATISFIED | `:33-39`. Gate CARGA-01 PASS |
| CARGA-02 | 02-03 | Worked example analogo antes do `TODO(human)` para substrato baixo | SATISFIED | `:410-412` instancia diferente, obrigatorio zero-absoluto. Gate CARGA-02 PASS |
| CARGA-03 | 02-03 | 3 principios de Mayer + linguagem simples + limite honesto | SATISFIED | `:344-348`. Gate CARGA-03 PASS |

Todos os 6 requirement IDs (EST-01, EST-02, EST-04, CARGA-01, CARGA-02, CARGA-03) declarados nos PLANs e mapeados ao Phase 2 em REQUIREMENTS.md estao SATISFIED. Nenhum ID orfao. Plano 02-01 (`requirements: []`) e utilitario de verificacao (Wave 1), sem requisito proprio — esperado.

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| (nenhum) | — | — | — | Anti-leak = 0; nenhum jargao de framework dentro de blocos cercados; sem acentos; ordem dos campos do scaffold (META..PISTA) preservada |

### Human Verification Required

Nenhum item bloqueante para human verification. As edicoes sao documentacao em texto, totalmente verificaveis por grep/gate estatico, todos verdes. Opcional (nao-bloqueante): renderizar `reference.md` num visualizador markdown para confirmar visualmente que os 2 hyperlinks navegam ate as secoes corretas de `fundamentos.md` — ja confirmado mecanicamente que as ancoras existem como headings.

### Gaps Summary

Nenhuma gap. As 5 success criteria do ROADMAP estao verificadas contra o conteudo real de `mentor/reference.md`. O gate `check-phase2.sh` reporta `0 fail(s)` em 9 checagens. Os 6 requirement IDs da fase estao satisfeitos e mapeados. A teoria e single-sourced (nomeada na prosa + linkada a `fundamentos.md` por ancoras reais, sem reescrita local). Nenhum jargao de framework vazou para dentro de bloco cercado de artefato do aluno (CONS-01 preservado, embora CONS-01 seja formalmente da Fase 5 — aqui ja respeitado como constraint).

---

_Verified: 2026-06-14_
_Verifier: Claude (gsd-verifier)_
