---
phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md
plan: 01
subsystem: validation-harness
tags: [shell, grep, static-verification, gate, wave-0]
requires: []
provides:
  - "scripts/extract-fenced.sh -- isolador de bloco cercado (anti-leak CONS-01)"
  - "scripts/check-phase4.sh -- gate estatico PASS/FAIL para V-01..V-15"
affects:
  - "planos 04-02 / 04-03 / 04-04 (cada edicao de mentor/ usa este gate para provar conclusao)"
tech-stack:
  added: []
  patterns:
    - "Harness de verificacao estatica clonado verbatim da Fase 2 (count/check_min/check_zero/check_has + ANCHOR-RESOLVE)"
    - "Convencao de baseline: positivos FALHAM ate as edicoes; anti-leak e anchor-resolve PASSAM"
key-files:
  created:
    - ".planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/extract-fenced.sh"
    - ".planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/check-phase4.sh"
  modified: []
decisions:
  - "V-15 anti-leak usa forma de FRASE para retrieval (retrieval practice|testing effect) para nao colidir com o rotulo de contrato legitimo '## Agenda de retrieval'"
  - "V-03 skip-on-empty case-robusto via classes de char ([Aa]genda...) sem flag -i, mantendo o count/rg -c igual a Fase 2"
metrics:
  duration: "~6 min"
  completed: 2026-06-16
---

# Phase 4 Plan 01: Harness de Verificacao Estatica Summary

Gate estatico da Fase 4 (Wave 0): `extract-fenced.sh` clonado verbatim da Fase 2 + `check-phase4.sh` codificando os 15 checks V-01..V-15 de `04-VALIDATION.md`, com a convencao de baseline da Fase 2 preservada (positivos falham ate as edicoes; ANCHOR-RESOLVE e ANTI-LEAK passam).

## What Was Built

Dois scripts shell em `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/`:

1. **`extract-fenced.sh`** — clone byte-identico (mesmo conteudo e mesmas line endings CRLF) do `extract-fenced.sh` da Fase 2. Isola SO o conteudo dentro de blocos cercados (` ``` `) via toggle awk `inside = !inside`, para que o grep anti-leak (V-15/CONS-01) rode somente contra o texto que vira artefato do aluno, sem falso-positivo na prosa legitima.

2. **`check-phase4.sh`** — autorado a partir do template `check-phase2.sh`, reusando `count`/`check_min`/`check_zero`/`check_has` verbatim. Define `TUT`/`FCH`/`REF`/`FUN`/`DIR` e codifica os 15 checks:
   - V-01..V-12: `check_min` positivos (presenca de headings, links e regras nos docs editados). V-11 e V-12 expandidos em sub-checks (a/b por arquivo, anchor SDT somando os dois arquivos) conforme o plano.
   - V-13: CONTRACT cross-file via `check_has` por arquivo (literal `Agenda de retrieval` nos 3 docs).
   - V-14: ANCHOR-RESOLVE (bloco `if` clonado da Fase 2) — as 3 headings de `fundamentos.md` ja resolvem.
   - V-15: `check_zero` anti-leak com o padrao canonico final `SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect` (frase para retrieval, sem o token isolado).

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Clonar extract-fenced.sh verbatim | 6895f1b | scripts/extract-fenced.sh |
| 2 | Autorar check-phase4.sh (V-01..V-15) | 3a8a3c5 | scripts/check-phase4.sh |

## Verification

`sh scripts/check-phase4.sh` roda em ~2s, imprime uma linha PASS/FAIL por check e termina com `== 16 fail(s) ==` (exit 16). Baseline observado (antes das edicoes 02/03/04):

- **V-14 (ANCHOR-RESOLVE) = PASS** — as 3 headings existem em `mentor/fundamentos.md`.
- **V-15 (ANTI-LEAK) = PASS** — got=0, nenhum jargao dentro de bloco cercado.
- Positivos das edicoes ainda nao aplicadas = FAIL (esperado, igual Fase 2).
- V-07 e V-09 passam no baseline por casarem literais ja presentes em `fecha-marco.md`/`reference.md` — inocuo; viram parte do gate verde apos as edicoes.

Patterns canonicos confirmados literais no script:
- V-15: `SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect`
- V-03: `[Aa]genda.*vazia|[Nn]enhum conceito|[Pp]ule|[Ss]em entrada`

`sh scripts/extract-fenced.sh mentor/reference.md` imprime conteudo de bloco cercado (nao vazio, sem as cercas).

## Deviations from Plan

None - plan executed exactly as written. (As line endings dos scripts sao CRLF para casar os originais da Fase 2 versionados no repo; o aviso `LF will be replaced by CRLF` do git e cosmetico e nao altera a logica.)

## Decisions Made

- **V-15 frase para retrieval:** padrao usa `retrieval practice|testing effect` em vez do token isolado `retrieval`, evitando falso-positivo no rotulo de contrato `## Agenda de retrieval`. Padrao FINAL desde o Wave 0 — nenhum plano posterior edita este script.
- **V-03 case-robusto sem `-i`:** classes de char `[Aa]`/`[Nn]`/`[Pp]`/`[Ss]` mantem o `count`/`rg -c` sem flag, identico a Fase 2.

## Known Stubs

None.

## Self-Check: PASSED

- FOUND: .planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/extract-fenced.sh
- FOUND: .planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/check-phase4.sh
- FOUND commit: 6895f1b (Task 1)
- FOUND commit: 3a8a3c5 (Task 2)
