---
phase: 06-auditoria-de-consistencia
plan: 01
subsystem: testing
tags: [posix-sh, ripgrep, harness, consistency-audit, anti-drift, anti-cargo-cult]

# Dependency graph
requires:
  - phase: 01-05
    provides: docs de mentor/ editados (fundamentos.md, reference.md, novo-projeto.md, tutor.md, fecha-marco.md, metodo.md, debug.md) + adaptadores (AGENTS.md, .claude/, README.md) que o script audita
provides:
  - "scripts/check-consistencia.sh: harness PASS/FAIL permanente codificando V-01..V-16 (primeiro tool de verificacao commitado do toolkit, D-01 artefato a)"
  - "Baseline mecanico: V-01..V-15 PASS, V-16 (acentos) FAIL got=2 -- red esperado ate o fix do Plano 02"
affects: [06-02-PLAN (consome o harness: fix do V-16 + flip de status D-04 + relatorio de fechamento)]

# Tech tracking
tech-stack:
  added: [POSIX sh (#!/usr/bin/env sh), ripgrep (rg) como dependencia documentada do script]
  patterns: ["harness PASS/FAIL com fails counter + exit $fails (clone do padrao Fases 2/4/5, agora PERSISTIDO em scripts/)", "set-fechado allowlist (nunca discovery por regex)", "extracao de /comando delimitada por backtick (`/x`) para evitar falsos de path", "classe estreita de letras acentuadas (nunca [^\\x00-\\x7F])"]

key-files:
  created: [scripts/check-consistencia.sh]
  modified: []

key-decisions:
  - "Manteve rg como dependencia (convencao das fases anteriores) com guard command -v no topo -> exit 2 com mensagem clara se ausente (O-1 resolvido pro lado da consistencia)"
  - "V-15 negativo usa extracao `/comando` delimitada por backtick (`/[a-z][a-z-]+`) em vez do /[a-z-]+ aberto: a forma aberta casava componentes de path (mentor/metodo.md -> /metodo, referencias/ -> /referencias, roadmap.sh -> /roadmap) gerando falsos; a forma com backtick captura so mencoes reais de comando"
  - "V-15 emitido como 3 checks agregados (1 linha PASS/FAIL por arquivo) cobrindo os dois lados (positivo: 5 canonicos presentes; negativo: zero fora-do-set)"
  - "Link-relative reference.md/metodo.md ficam no SKIP do V-13 (cobertos pelas variantes mentor/<x>.md que resolvem da raiz) -- O-2 resolvido por SKIP"

patterns-established:
  - "Verificacao de consistencia como artefato commitado e re-runnable (~0 tokens por re-auditoria) em vez de agente relendo 8 docs"
  - "Set-equality dois-lados (presenca + ausencia-de-sobra) como forma objetiva e grep-avel de igualdade de conjunto"

requirements-completed: [CONS-02, CONS-03]

# Metrics
duration: ~9min
completed: 2026-06-16
---

# Phase 6 Plan 01: Harness de Auditoria de Consistencia Summary

**`scripts/check-consistencia.sh` -- harness POSIX-sh permanente codificando V-01..V-16 (11 anchors anti-cargo-cult + comando<->arquivo + backtick-paths + jargao-zero-nos-adaptadores + set-equality dois-lados + guard de acentos); roda da raiz, V-01..V-15 verdes, V-16 vermelho got=2, exit 1.**

## Performance

- **Duration:** ~9 min
- **Started:** 2026-06-16T23:22Z
- **Completed:** 2026-06-16T23:31:56Z
- **Tasks:** 1
- **Files modified:** 1 (criado)

## Accomplishments
- Primeiro tool de verificacao COMMITADO do toolkit (`scripts/check-consistencia.sh`, D-01 artefato a) -- muda o padrao de harness descartavel das Fases 2/4/5 para artefato permanente re-runnable.
- Codifica as 16 verificacoes mecanicas do contrato Nyquist: 11 `check_has` para CONS-02 (cada teoria de `fundamentos.md` aterrissa no doc citado), V-12 (comando<->arquivo, set fechado), V-13 (backtick-paths com SKIP not-in-repo), V-14 (zero jargao nos adaptadores), V-15 (set-equality dois-lados), V-16 (acentos).
- V-15 adicionado alem do skeleton da RESEARCH (que o omitia): dois-lados (positivo: 5 canonicos presentes; negativo: zero `/comando` fora-do-set) sobre `AGENTS.md`, `README.md` e `mentor/metodo.md` -- 3 linhas PASS nomeando cada arquivo.
- Baseline verificado em-sessao ANTES de codificar cada check (todos os 11 anchors >=1 hit; V-12 5/5; V-13/V-14 zero; V-16 got=2 nas duas cedilhas de debug.md:31-32).

## Task Commits

Cada task committada atomicamente:

1. **Task 1: Escrever scripts/check-consistencia.sh (harness permanente V-01..V-16)** - `2861024` (feat)

**Plan metadata:** (commit final desta etapa de docs)

## Files Created/Modified
- `scripts/check-consistencia.sh` - Harness POSIX-sh permanente; guard de `rg`; helpers `check_min`/`check_zero`/`check_has`; blocos CONS-02 (11 anchors), CONS-03 #1/#2/#3, set-equality dois-lados (V-15) e IN-01 (acentos); `exit $fails`.

## Decisions Made
- **Extracao `/comando` por backtick (V-15 negativo):** o `/[a-z-]+` aberto casava componentes de path (`mentor/metodo.md` -> `/metodo`, `referencias/` -> `/referencias`, `roadmap.sh` -> `/roadmap`) e fragmentos de prosa, gerando falsos fora-do-set. Troquei pela extracao delimitada por backtick `` `/[a-z][a-z-]+` `` que so casa mencoes reais de comando. Verificado: os 3 arquivos rendem so os 5 canonicos + nao-comandos conhecidos (`comando`/`config`/`clear`), zero fora-do-set.
- **V-15 como 3 checks agregados:** uma linha PASS/FAIL por arquivo cobrindo os dois lados, satisfazendo a exigencia do plano de "nomear cada arquivo" e referenciar literalmente `README.md` e `metodo.md` no codigo-fonte.
- **rg mantido (O-1):** dependencia documentada no cabecalho + guard `command -v rg` -> exit 2 com mensagem clara. Consistente com as Fases 2/4/5.
- **Link-relative no SKIP (O-2):** `reference.md`/`metodo.md` em links markdown relativos entram no SKIP do V-13 (ja cobertos pelas variantes `mentor/<x>.md` que resolvem da raiz).

## Deviations from Plan

None - plan executed exactly as written. (As escolhas discricionarias acima -- forma do V-15, extracao por backtick, SKIP dos link-relative -- estavam explicitamente delegadas a "Claude's Discretion" no plano/RESEARCH; nao sao desvios das regras de deviation.)

## Issues Encountered
- Durante o desenvolvimento do V-15, a extracao `/[a-z][a-z-]+` aberta produziu falsos fora-do-set (componentes de path e prosa). Resolvido restringindo a extracao a tokens `` `/x` `` delimitados por backtick antes de codificar no script -- nenhum FAIL espurio resultou (3 PASS no baseline).

## User Setup Required
None - nenhuma configuracao de servico externo necessaria. (Pre-requisito do script: `ripgrep` -- ja presente no ambiente Git Bash; o guard avisa e sai 2 se ausente.)

## Next Phase Readiness
- Harness pronto e committado. O Plano 02 consome este baseline: aplica o fix do IN-01 (`Peca`/`peca` em `debug.md:31-32`) -> V-16 vira verde (got=0), faz o flip de status D-04 em `fundamentos.md`, e autora o relatorio de fechamento (D-03 confirmacao semantica + D-05 escalacoes, nenhuma esperada).
- Estado esperado pos-Plano-01 (confirmado por execucao): V-01..V-15 PASS, V-16 FAIL got=2, exit 1 -- exatamente o pre-fix do contrato Nyquist (06-VALIDATION.md).
- NAO foi aplicado nenhum fix de acento nem flip de status nesta etapa (escopo do Plano 02).

## Self-Check: PASSED

- FOUND: `scripts/check-consistencia.sh`
- FOUND: `.planning/phases/06-auditoria-de-consistencia/06-01-SUMMARY.md`
- FOUND: commit `2861024`

---
*Phase: 06-auditoria-de-consistencia*
*Completed: 2026-06-16*
