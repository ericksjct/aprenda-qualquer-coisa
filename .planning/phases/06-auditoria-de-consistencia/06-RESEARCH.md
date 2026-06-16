# Phase 6: Auditoria de consistencia - Research

**Researched:** 2026-06-16
**Domain:** Cross-document consistency auditing of a markdown method toolkit + a permanent POSIX-sh verification harness (Git Bash on Windows)
**Confidence:** HIGH (all claims verified by direct codebase grep/read in this session)

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** A fase entrega DOIS artefatos: (a) um script leve PERMANENTE `scripts/check-consistencia.sh` (nome a confirmar no plano) commitado no repo, e (b) um relatorio de auditoria de fechamento (ex: `06-AUDITORIA.md` ou a propria VERIFICATION). Mudanca deliberada de padrao: as Fases 2/4/5 usaram harness descartaveis NAO commitados. O script da Fase 6 e a versao MINIMA e mecanica (so o que `grep`/teste de existencia consegue provar), down-payment parcial do Risco #1 (drift). A versao completa e o FUT-04 (v2).
- **D-02 (CONS-03 mecanico):** O script codifica 3 checks: (1) todo `/comando` citado tem `mentor/<comando>.md`; (2) paths em backticks (nos docs auditados) resolvem para arquivos existentes; (3) nenhum jargao de metodo deste milestone vazou para os adaptadores (`.claude/`, `AGENTS.md`). Reaproveitar o padrao de harness das fases anteriores (PASS/FAIL, exit 0).
- **D-03 (CONS-02 mecanico + confirmacao do agente):** A verificacao PROFUNDA do CONS-02 entra NO SCRIPT: para cada pratica de `fundamentos.md`, um `grep` confirma que o termo/aplicacao prometido APARECE no doc citado. O AGENTE confirma UMA vez, na auditoria de fechamento, que a aplicacao faz SENTIDO (grep acha a palavra, nao julga semantica) e registra no relatorio.
- **D-04:** Apos a verificacao profunda passar, virar as ~10 marcas `(Fase N, pendente)` da coluna "Aplicado em" de `fundamentos.md` para status aplicado/feito (texto exato a definir no plano). So vira "aplicado" o que D-03 confirmou de fato.
- **D-05 (politica de correcao):** Corrigir o TRIVIAL inline (flip de status, path quebrado, acento solto IN-01); ESCALAR o estrutural (teoria que NAO aterrissou; metodo de fato duplicado num adaptador; divergencia real no conjunto de procedimentos) como achado apresentado, nao fix silencioso.
- **D-06 (rigor do Criterio 3):** Igualdade de CONJUNTO, com a tabela de roteamento de `AGENTS.md` como fonte canonica da lista (`novo-projeto`, `tutor`, `fecha-marco`, `debug`, `spidr-split`). `README` e `metodo.md` citam exatamente esse conjunto — sem sobra nem falta.
- **D-07 (IN-01 acentos):** Corrigir `Peca`/`peca` (na verdade `Peça`/`peça`) em `debug.md:31-32` inline como conserto one-off. NAO virar linter de acentos permanente (Risco #5 fora de escopo).

### Claude's Discretion
- Nome exato do script (`check-consistencia.sh` vs outro), estrutura de saida e como ele lista as praticas de `fundamentos.md` para o grep.
- Texto exato do novo status que substitui `(Fase N, pendente)` em `fundamentos.md`.
- Se o relatorio de fechamento e um `06-AUDITORIA.md` proprio ou cabe na VERIFICATION.
- Como mapear cada linha de `fundamentos.md` ao termo-de-grep mais robusto (a palavra ancora menos fragil por pratica).

### Deferred Ideas (OUT OF SCOPE)
- **FUT-04** — verificador de drift automatizado COMPLETO (v2). A Fase 6 entrega so o down-payment mecanico minimo.
- **Linter de acentos permanente** (Risco #5) — D-07 e so o conserto pontual do IN-01.
- Parametrizar a raiz do repo para rodar fora dele (Risco #2) — fora de escopo.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| CONS-02 | Cada pratica em `fundamentos.md` tem "aplicado em <doc>" verificavel; o doc citado realmente contem a aplicacao (anti cargo-cult). | §CONS-02 Anchor Map below: 10 practices, each with a VERIFIED grep anchor + exact line(s) in the cited doc (all resolve, ≥1 hit). Feeds the script's deep check (D-03) and the D-04 status flip. |
| CONS-03 | Auditoria final: todo `/comando` tem `mentor/<comando>.md`; paths em backticks resolvem; `README`/`AGENTS.md`/`metodo.md` descrevem o mesmo conjunto; nada duplicado nos adaptadores. | §CONS-03 Three Checks below: closed command allowlist, backtick-path resolution rules with not-in-repo allowlist, adapter jargon-leak definition with verified baseline. |
</phase_requirements>

## Summary

Phase 6 is a CONSTRUCTION phase (toolkit, not student-facing) that closes the v1.0 milestone with two artifacts: a PERMANENT POSIX-sh harness (`scripts/check-consistencia.sh`) and a one-time closing audit report. It writes NO new method content. The work is purely mechanical verification plus a handful of trivial inline fixes.

The single highest-value research output is the **CONS-02 Anchor Map**: for each of the ~10 theory practices catalogued in `fundamentos.md`, I read the cited doc and identified the least-fragile grep anchor proving the application really landed there, with the exact line(s). **All 10 practices resolve with ≥1 hit — none is a structural finding.** No theory landed nowhere. This means D-04 (flip `(Fase N, pendente)` → applied) is safe for all 10, and D-05 escalation is unlikely to fire on CONS-02.

For CONS-03 the three mechanical checks are each subtly trap-laden and the research pins down the safe definitions: (1) command check must use a **closed allowlist** anchored on AGENTS.md, NOT open `/[a-z-]+` detection (which yields false positives like `/renderiza`, `/config`, `/dados`); (2) backtick-path resolution must whitelist the large set of **intentionally-not-in-repo** paths (runtime artifacts in gitignored `.projetos/<slug>/`, `<placeholder>` paths, markdown-link relative forms); (3) the adapter jargon-leak check has a **verified-clean baseline** (the adapters today contain zero method jargon — they only point to `mentor/`).

The harness style is fully established: Phases 2/4/5 left `check-phaseN.sh` + `extract-fenced.sh` under `.planning/phases/NN-*/scripts/` (planning artifacts, never committed to the toolkit). Phase 6 reuses this exact form (`#!/usr/bin/env sh`, `rg`-based `check_min`/`check_zero`/`check_has`, `fails` counter, `exit $fails`) but PERSISTS it to `scripts/` as the first committed verification tool of the toolkit.

**Primary recommendation:** Write `scripts/check-consistencia.sh` as a single POSIX-sh file cloned from `check-phase5.sh`'s helper skeleton, encoding 4 check families: CONS-02 deep anchors (10 `check_has`/`check_min`), CONS-03 command↔file existence (closed allowlist loop), CONS-03 backtick-path resolution (with not-in-repo allowlist), CONS-03 adapter jargon-leak (`check_zero` over `AGENTS.md` + `.claude/`), plus the IN-01 accent guard (`check_zero` on a NARROW accented-letter class). Fix IN-01 inline, flip the 10 statuses inline, escalate nothing (nothing to escalate per current findings), and record the agent's one-time semantic confirmation in the closing report.

## Architectural Responsibility Map

Single-tier toolkit; no runtime, network, DB, or UI. Tiers here are conceptual document/script roles.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Theory vocabulary (single source) | `mentor/fundamentos.md` | — | Internal doc; all others cite it by link, never redefine (source-single design). |
| Method procedures (owners) | `mentor/<comando>.md` (5) + `reference.md` + `metodo.md` | — | Each procedure owns its content; theory is cited, not duplicated. |
| Canonical procedure list | `AGENTS.md` routing table (`:16-23`) | `metodo.md`, `README.md` (must mirror) | D-06 names AGENTS.md the canonical set; the other two are mirrors checked for set equality. |
| Tool adapters (point-only) | `.claude/` skills + output-style, `AGENTS.md` role text | — | Thin; must contain ZERO method content — only pointers to `mentor/`. The anti-drift check defends this. |
| Verification (the deliverable) | `scripts/check-consistencia.sh` | closing report (`06-AUDITORIA.md` or VERIFICATION) | Mechanical proof (grep/existence); the agent does ONE semantic pass in the report. |

## Standard Stack

### Core
| Library / Tool | Version | Purpose | Why Standard |
|----------------|---------|---------|--------------|
| POSIX `sh` (Git Bash on Windows) | bundled w/ Git for Windows | Harness shebang `#!/usr/bin/env sh` | [VERIFIED: check-phase5.sh:1] All prior harnesses use `sh`, not `bash` — maximal portability. |
| ripgrep (`rg`) | any recent | Pattern counting/matching in the harness | [VERIFIED: check-phase5.sh uses `rg -c`/`rg -q`] Prior harnesses standardized on `rg`; faster, sane defaults, recursive. |
| `awk` (POSIX) | bundled | Section isolation + fenced-block extraction | [VERIFIED: check-phase5.sh:91 awk section-isolation; extract-fenced.sh:22-25] |
| `printf` (POSIX) | bundled | Aligned PASS/FAIL output | [VERIFIED: check-phase5.sh:37] `printf 'PASS %-16s ...'` — never `echo -e` (non-portable). |

### Supporting
| Tool | Purpose | When to Use |
|------|---------|-------------|
| `extract-fenced.sh` | Print only content inside ` ``` ` fences | Only if a check must run on student-artifact content (anti-leak in fenced blocks). For Phase 6's adapter-leak check, NOT needed — adapters are checked whole-file (they should contain zero jargon anywhere). [VERIFIED: extract-fenced.sh purpose comment :6-9] |
| `dirname "$0"` | Resolve the script's own dir | [VERIFIED: check-phase5.sh:19] Used so the script can locate sibling helpers; for a committed standalone script, prefer resolving the repo root relative to the script and running checks against `mentor/`, `AGENTS.md`, etc. |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| `rg` | `grep -c` / `grep -E` | [CITED: prior harness convention] Prior phases chose `rg`. `grep` is more universally present but `rg` is already the established convention and assumed available. **Open question O-1:** confirm `rg` is acceptable as a hard dependency for a COMMITTED (vs disposable) script, or fall back to `grep -E` for wider portability. |
| `#!/usr/bin/env sh` | `#!/usr/bin/env bash` | `sh` is portable and sufficient (no bashisms used in the prior harnesses). Keep `sh`. |

**No installation required.** All tools ship with Git for Windows (the stated environment). Verify on the target machine:
```bash
command -v rg awk printf sh
```

## Architecture Patterns

### System Architecture Diagram (data flow of the audit)

```
                  scripts/check-consistencia.sh  (committed, permanent)
                                |
        +-----------------------+-----------------------+--------------------+
        |                       |                       |                    |
   [Check family A]        [Check family B]        [Check family C]    [Check family D]
   CONS-02 deep            CONS-03 #1              CONS-03 #2          CONS-03 #3 + IN-01
   (anti-cargo-cult)       command<->file          backtick paths     adapter jargon-leak
        |                       |                       |                    |
  for each of 10          closed allowlist        each repo-resident   rg over AGENTS.md
  practices: rg the       {novo-projeto,tutor,    backtick path        + .claude/  -> 0 ;
  anchor term in the      fecha-marco,debug,       resolves to a file  narrow accent class
  cited mentor/ doc       spidr-split} ->          (skip not-in-repo   over mentor/ -> 0
        |                 test -f mentor/<x>.md    allowlist)               |
        v                       v                       v                    v
     PASS/FAIL  ----------> fails counter <---------- PASS/FAIL  --------> PASS/FAIL
                                |
                                v
                         exit $fails  (0 = green)
                                |
              +-----------------+------------------+
              |                                    |
     If green: D-04 flip 10 statuses      Agent ONE-TIME semantic pass
     inline in fundamentos.md             -> closing report (06-AUDITORIA.md)
     + IN-01 accent fix inline            -> confirms each anchor "makes sense"
                                          -> escalate structural findings (D-05) [none expected]
```

File-to-implementation mapping is in the Architectural Responsibility Map above; the diagram shows the audit data flow.

### Recommended Project Structure
```
scripts/
├── roadmap_fetch.py          # existing (do not touch)
└── check-consistencia.sh     # NEW: the permanent harness (D-01 artifact a)

.planning/phases/06-auditoria-de-consistencia/
├── 06-RESEARCH.md            # this file
├── 06-PLAN.md / 06-NN-PLAN.md
├── 06-VALIDATION.md          # Nyquist contract (mirrors §Validation Architecture)
└── 06-AUDITORIA.md           # NEW: closing report (D-01 artifact b) — OR fold into 06-VERIFICATION.md
```

### Pattern 1: PASS/FAIL harness with `fails` counter (clone from check-phase5.sh)
**What:** A single `sh` script with `count()` + `check_min`/`check_zero`/`check_has` helpers, a `fails` accumulator, and `exit $fails`.
**When to use:** This is THE established convention; reuse verbatim.
**Example:**
```sh
# Source: .planning/phases/05-.../scripts/check-phase5.sh:29-64 [VERIFIED]
count() { rg -c "$1" "$2" 2>/dev/null || echo 0; }

check_min() {  # PASS when val >= min
  label="$1"; val="$2"; min="$3"
  if [ "$val" -ge "$min" ]; then printf 'PASS  %-20s got=%s need>=%s\n' "$label" "$val" "$min"
  else printf 'FAIL  %-20s got=%s need>=%s\n' "$label" "$val" "$min"; fails=$((fails + 1)); fi
}
check_zero() {  # PASS when val == 0  (anti-leak / anti-drift / accent)
  label="$1"; val="$2"
  if [ "$val" -eq 0 ]; then printf 'PASS  %-20s got=%s need=0\n' "$label" "$val"
  else printf 'FAIL  %-20s got=%s need=0\n' "$label" "$val"; fails=$((fails + 1)); fi
}
check_has() {  # PASS when rg -q finds pattern in file
  label="$1"; pat="$2"; file="$3"
  if rg -q "$pat" "$file" 2>/dev/null; then printf 'PASS  %-20s found in %s\n' "$label" "$file"
  else printf 'FAIL  %-20s NOT found in %s\n' "$label" "$file"; fails=$((fails + 1)); fi
}
```

### Pattern 2: Closed-allowlist existence loop (CONS-03 check #1)
**What:** Iterate the KNOWN canonical command set, assert each has a file. Do NOT discover commands by regex.
**Example:**
```sh
# The canonical set per D-06 (AGENTS.md routing table). reference/metodo are docs, not /commands.
for cmd in novo-projeto tutor fecha-marco debug spidr-split; do
  if [ -f "mentor/$cmd.md" ]; then printf 'PASS  cmd-file %-14s mentor/%s.md\n' "$cmd" "$cmd"
  else printf 'FAIL  cmd-file %-14s MISSING mentor/%s.md\n' "$cmd" "$cmd"; fails=$((fails+1)); fi
done
```

### Pattern 3: Backtick-path resolution with not-in-repo allowlist (CONS-03 check #2)
**What:** Extract backtick paths from audited docs; for each that is repo-resident, `test -f`. SKIP intentionally-not-in-repo patterns.
**Example:**
```sh
# Extract `path.ext` tokens, strip backticks, test only repo-resident ones.
# SKIP (regex of intentional non-files): student runtime artifacts, placeholders, link-relative forms.
SKIP='(<slug>|<comando>|<conceito>|<file>|P0x|GEMINI\.md|CAMINHO\.md|PROGRESSO\.md|APRENDIZADO\.md|aulas/|exercicios/|projeto/|referencias/)'
rg -oN '`[A-Za-z0-9_./<>-]+\.(md|py|sh|json)`' mentor/ AGENTS.md README.md \
  | sed 's/.*`\(.*\)`/\1/' | sort -u \
  | while IFS= read -r p; do
      echo "$p" | rg -q "$SKIP" && continue            # intentional non-file: skip
      if [ -f "$p" ]; then : ; else echo "UNRESOLVED: $p"; fi
    done
# Count UNRESOLVED lines; check_zero on that count.
```
**Note:** the relative-link forms `reference.md` / `metodo.md` (used inside `[x](x)` markdown links from within `mentor/`) are NOT repo-root files — they resolve relative to the linking doc's dir. Either normalize them to `mentor/<x>.md` before `test -f`, or add them to SKIP and rely on the `mentor/<x>.md` backtick variants (which DO resolve) to cover them. **Discretion item.**

### Anti-Patterns to Avoid
- **Open-ended command discovery (`rg -oP '/[a-z-]+'`):** [VERIFIED in session] yields false positives `/renderiza`, `/config`, `/clear`, `/dados`, `/video`, `/integracao`, `/vago`, `/padrao`. Use the closed allowlist.
- **Naive "no non-ASCII" accent check:** [VERIFIED] the repo intentionally uses em-dash `—` (U+2014) and middot `·` (U+00B7) HEAVILY as punctuation. A `[^\x00-\x7F]` check would emit hundreds of false FAILs. The accent check must target only accented LETTERS (see Pattern 4).
- **Reconstructing markdown header slugs for anchor checks:** [VERIFIED: check-phase5.sh:98 comment "nunca um slug reconstruido"] grep the LITERAL heading line, never a guessed `#slug`. (Relevant only if Phase 6 adds anchor-resolution checks; the CONS-02 anchors below are body-text terms, not header slugs, so this is lower-risk here.)
- **Running the adapter jargon-leak check on `mentor/` prose:** the jargon LEGITIMATELY lives in `mentor/`. The leak check runs ONLY over adapters (`AGENTS.md`, `.claude/`).

### Pattern 4: Narrow accent guard (IN-01, D-07)
**What:** Detect accented Portuguese LETTERS only, excluding intentional punctuation.
```sh
# [VERIFIED] Only matches in mentor/ today are the two cedillas in debug.md:31-32.
accents=$(rg -c '[áàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇ]' mentor/ 2>/dev/null | awk -F: '{s+=$NF} END{print s+0}')
check_zero "accents-mentor" "$accents"
```
After the IN-01 fix (`Peça`→`Peca`, `peça`→`peca` on debug.md:31-32) this count becomes 0. **Note:** this is NOT a permanent accent linter mandate (Risco #5) — it is a single check that happens to enforce the existing convention; keep it minimal and do not extend to adapters or to broader style rules.

## CONS-02 Anchor Map (THE highest-value output)

For each practice in `fundamentos.md`'s "Aplicado em (doc + status)" column with a `(Fase N, pendente)` mark, the least-fragile grep anchor proving the application landed, the exact line(s) in the cited doc, and a structural-finding flag. **All anchors VERIFIED present in-session via `rg -c` (≥1 hit each).**

The `fundamentos.md` rows carrying a pending mark (from [VERIFIED: fundamentos.md:24-50]):

| # | Practice (fundamentos.md row) | Pending mark @ line | Cited doc | **Robust grep anchor** | Exact landing line(s) in cited doc | Hits | Structural finding? |
|---|-------------------------------|---------------------|-----------|------------------------|-------------------------------------|------|---------------------|
| 1 | Backward Design / UbD | :24 (`Fase 2/3, pendente`) | reference.md, novo-projeto.md | `backward design` | reference.md:98 (`[backward design](fundamentos.md...)`); novo-projeto.md:59 + :86 (Passe 1→2 reverse-engineering) | ref 1, novo 2 | NO — landed in both |
| 2 | Constructive Alignment | :25 (`Fase 2, pendente`) | reference.md | `Objetivo (capacidade)` + `Entregavel` co-located in CAMINHO template | reference.md:76 + :77 (`Objetivo (capacidade)` next to `Entregavel`); template :85-87 | 2+ | NO — META→DONE/Objetivo↔Entregavel present |
| 3 | Cognitive Load Theory (Mayer/CARGA-03) | :26 (`Mayer/CARGA-03 Fase 2, pendente`) | reference.md | `so 3 de 12 principios` (or `coerencia`/`sinalizacao`/`segmentacao`) | reference.md:350-354 (Mayer 3 principles + ressalva link) | 1 (phrase) | NO — Mayer 3-of-12 landed |
| 4 | Worked-Example + Expertise-Reversal | :27 (`Fase 2, pendente`) | reference.md | `expertise-reversal` (and `eu faco -> nos fazemos -> voce faz`) | reference.md:34 (`[expertise-reversal effect]`); :406 GRR 3-phase heading; :416-418 worked-example "eu faco" | 1 + 1 | NO — both landed |
| 5 | Retrieval Practice / Testing Effect | :28 (`Fase 4, pendente`) | tutor.md | `retrieval practice` (and `Recuperacao ativa`) | tutor.md:44 (`[retrieval practice](fundamentos.md...)`); :37 `## Passo 1 — Recuperacao ativa` | 1 | NO — opening retrieval landed |
| 6 | Self-Determination Theory (SDT) | :45 (`Fase 4, pendente`) | tutor.md, PROGRESSO.md(via reference.md) | `proxima acao` (single next action) + SDT link | tutor.md:102-106 (`exatamente 1 proxima acao` + `[SDT]` + relatedness ressalva); fecha-marco.md:126-129 mirrors | tutor 3 | NO — single-next-action + SDT landed |
| 7 | Mastery Learning | :47 (`Fase 4, pendente`) | fecha-marco.md | `mastery learning` (and heading `Mastery gate`) | fecha-marco.md:15 (`[mastery learning](fundamentos.md...)`); :12 `## Passo 1 — Mastery gate` | 1 | NO — mastery gate landed |
| 8 | Avaliacao Formativa | :48 (`Fase 5, pendente`) | metodo.md, fecha-marco.md | `auto-explicacao` (formative check) | metodo.md:77 + :85 (formative check = 1 auto-explanation question); fecha-marco.md:24-26 (synthesis/transfer, no grade) | metodo 2 | NO — formative check landed |
| 9 | Feedback Hattie (Feed Up/Back/Forward) | :49 (`Fase 5, pendente`) | debug.md | `feed-forward` (and `Hattie`) | debug.md:17-18 (3 lenses mapped to 6 steps); :79 (`PISTA = feed-forward`); :20/:36/:68 lens-tagged step headings | feed-forward 4, Hattie 1 | NO — tri-partite feedback landed |
| 10 | Spacing Effect / Pratica Distribuida | :50 (`Fase 4, pendente`) | fecha-marco.md, PROGRESSO.md | `Agenda de retrieval` (spaced-review schedule) | fecha-marco.md:73-78 (`## Agenda de retrieval` write + spaced review of prior milestone); reference.md:247-249 template section | fcm 1 | NO — spaced review schedule landed |

**Additional load-bearing rows that are marked `(ja presente)` (NOT pending) — listed for completeness, no flip needed:**
- First Principles of Instruction → metodo.md, novo-projeto.md `(ja presente)` [fundamentos.md:23]
- CLT core → reference.md, metodo.md `(ja presente)` [:26]
- ZPD/Scaffolding → reference.md, metodo.md `(ja presente)` [:46]

**Result: 0 structural findings on CONS-02.** Every pending practice has a verified landing. D-04 can flip all 10 pending marks to "applied" once the script's deep check confirms (it will — all anchors resolve today). D-05 escalation for "theory landed nowhere" should NOT fire. The agent's one-time semantic confirmation (D-03) should focus on whether the grep-matched term is used in the INTENDED sense (e.g., "backward design" in reference.md:98 is genuinely about reverse-engineering the outcome, not an incidental mention) — and the lines above give the reviewer the exact spots to read.

**Anchor robustness notes:**
- Prefer the bracketed link form `[term](fundamentos.md...)` where it exists (rows 1,3,4,5,7,8,9) — it is the LEAST fragile because the application AND the citation co-occur on one line; a future edit removing either breaks the grep loudly.
- For rows where the link is in a different doc than the prose (row 6 SDT spans tutor.md + fecha-marco.md), anchor on `proxima acao` in tutor.md (3 hits, stable) rather than the link alone.
- Avoid anchoring on header slugs; anchor on body terms or literal heading text.

## CONS-03 Three Checks (mechanical definitions)

### Check #1 — every `/comando` has `mentor/<comando>.md`
- **Canonical set (closed allowlist, D-06):** `novo-projeto`, `tutor`, `fecha-marco`, `debug`, `spidr-split`. [VERIFIED: AGENTS.md:16-23 routing table; backtick-command inventory: `/tutor`×10, `/novo-projeto`×9, `/spidr-split`×8, `/fecha-marco`×8, `/debug`×6]
- **Files present today:** all 5 exist, plus `metodo.md`, `reference.md`, `fundamentos.md`. [VERIFIED: `ls mentor/*.md`]
- **Non-commands that appear as `/x` and MUST be excluded:** `/config`, `/clear` (Claude Code app commands, not mentor procedures); `/comando` (the literal convention placeholder); plus regex artifacts (`/renderiza`, `/dados`, etc.) if open detection is mistakenly used. [VERIFIED in session]
- **Implementation:** the closed-allowlist `for` loop (Pattern 2). Baseline: 5/5 PASS today.

### Check #2 — backtick paths resolve
- **Repo-resident paths that MUST resolve** (sample, [VERIFIED hit counts]): `mentor/reference.md`×24, `mentor/metodo.md`×7, `mentor/novo-projeto.md`×6, `mentor/tutor.md`×5, `mentor/fecha-marco.md`×5, `mentor/debug.md`×3, `mentor/spidr-split.md`×2, `AGENTS.md`×8, `scripts/roadmap_fetch.py`×1. All exist today.
- **Intentionally-NOT-in-repo (must be skipped, not failed):**
  - Student runtime artifacts in gitignored `.projetos/<slug>/`: `PROGRESSO.md`×35, `CAMINHO.md`×32, `APRENDIZADO.md`×10, `aulas/P0x-<slug>.md`×9.
  - Placeholders: `mentor/<comando>.md`×2, `aulas/P0x-<slug>.md`, `P0x-<slug>.md`.
  - Foreign-tool context file: `GEMINI.md`×2 (referenced as an example, not shipped).
  - Markdown-link relative forms used INSIDE `mentor/`: `reference.md`×2, `metodo.md`×1 (resolve relative to the linking doc, not repo root).
- **Implementation:** Pattern 3 with the SKIP regex. Baseline: 0 UNRESOLVED expected today. **Discretion:** decide whether to normalize link-relative `reference.md`/`metodo.md` to `mentor/` or SKIP them.

### Check #3 — no method jargon leaked into adapters
- **Adapters today (VERIFIED point-only):**
  - `AGENTS.md` — routing table + "leia/siga `mentor/...`"; no method theory. [VERIFIED: read in full]
  - `.claude/output-styles/mentor-projeto.md` — 20 lines, says "leia `mentor/metodo.md` ... e adote-o". [VERIFIED]
  - `.claude/skills/{debug,tutor,novo-projeto,fecha-marco,spidr-split}/SKILL.md` — each ~12 lines, "Leia `mentor/<x>.md` e siga". [VERIFIED debug + tutor; pattern identical]
- **Jargon-string set that would betray a leak** (reuse + extend the prior `LEAK_PAT` from check-phase5.sh:111): `SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect|feed-up|feed-back|feed-forward|Hattie|expertise-reversal|cognitive load|constructive alignment|first principles|formativ`.
- **Implementation:** `check_zero` over `rg -c "$LEAK_PAT" AGENTS.md .claude/` summed across files. [VERIFIED baseline: 0] Whole-file (NOT fenced-only) — adapters should contain zero jargon anywhere.
- **D-05 note:** if this check ever returns >0, that is a STRUCTURAL finding (real method content duplicated in an adapter) → escalate, do not silently delete.

### Set-equality for the procedure set (D-06, Criterio 3)
- **Canonical (AGENTS.md):** {novo-projeto, tutor, fecha-marco, debug, spidr-split}.
- **README.md mirror:** [VERIFIED: README.md:59-62 day-to-day table lists `/tutor /debug /fecha-marco /spidr-split`; README.md:116 + :125-129 "Como funciona por dentro" lists all 5 procedures] — set matches.
- **metodo.md mirror:** metodo.md routes to `/tutor`, `/fecha-marco`, `/spidr-split`, `/debug`, `/novo-projeto` across the doc [VERIFIED: present]. **Note:** metodo.md does not enumerate the set in one tidy table the way AGENTS.md/README do — it references commands inline. A strict "set equality" check should extract the distinct `/command` tokens (closed allowlist intersection) from each of the 3 files and assert each file mentions all 5. **Discretion:** define the comparison as "each of {AGENTS.md, README.md, metodo.md} references all 5 canonical commands and references no command outside the set" — objective and grep-able.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| PASS/FAIL harness scaffolding | A new bespoke output format | Clone `check-phase5.sh` helpers verbatim | [VERIFIED] 3 phases already exercised this exact form; consistency + zero design cost. |
| Fenced-block extraction | A regex to strip ` ``` ` | `extract-fenced.sh` (clone) IF needed | [VERIFIED] Already solved with a correct awk toggle; but Phase 6's adapter-leak check does NOT need it. |
| Command discovery | Regex over `/[a-z-]+` | Closed allowlist of 5 | Open detection produces false positives (proven in session). |
| Accent detection | `[^\x00-\x7F]` "non-ASCII" | Narrow accented-LETTER class | Em-dash/middot are intentional; broad class floods false FAILs. |
| Markdown anchor resolution | Reconstructing GitHub header slugs | Grep the literal heading line | [VERIFIED: check-phase5.sh:98 comment] slugs with `:`/`"`/`->` are unpredictable. |

**Key insight:** Phase 6's entire script is assembly of already-proven primitives. The novelty is (a) persisting it to `scripts/` and (b) the closed-allowlist + not-in-repo SKIP logic that the prior disposable harnesses didn't need.

## Runtime State Inventory

This is a doc/script-edit phase, but it touches a string-status flip (D-04) and an accent fix (D-07), so the inventory applies.

| Category | Items Found | Action Required |
|----------|-------------|------------------|
| Stored data | None — no DB, no datastore, no `.projetos/` artifacts edited (those are student-owned, gitignored). | None — verified: phase only edits `mentor/fundamentos.md`, `mentor/debug.md`, and adds `scripts/check-consistencia.sh`. |
| Live service config | None — no external service. | None — verified: toolkit is local markdown + one python ref script. |
| OS-registered state | None — no scheduler/daemon/registry entries. | None — verified. |
| Secrets/env vars | None — no secrets in repo. | None — verified. |
| Build artifacts | None — no compiled output; `roadmap_fetch.py` is stdlib-only, untouched. | None — verified: no egg-info/dist; phase adds a shell script (no build). |

**The status flip (D-04) is a content edit, not a data migration:** the `(Fase N, pendente)` strings live in tracked `mentor/fundamentos.md:24,25,26,27,28,45,47,48,49,50` — a plain in-file text change, fully covered by a normal commit. No runtime cache holds these.

## Common Pitfalls

### Pitfall 1: Em-dash false positives in any "no accents" check
**What goes wrong:** A broad non-ASCII check flags 100+ legitimate em-dashes/middots as accent violations.
**Why it happens:** The convention is "Portuguese without ACCENTS", but the prose uses `—`/`·` as deliberate punctuation.
**How to avoid:** Use the narrow accented-letter character class (Pattern 4). [VERIFIED: only 2 real matches today, both in debug.md:31-32.]
**Warning signs:** Hundreds of FAILs all on lines containing `—`.

### Pitfall 2: `/config` and `/clear` mistaken for missing commands
**What goes wrong:** A command-existence check flags `/config`/`/clear` as missing `mentor/config.md`.
**Why it happens:** They are Claude Code app commands cited in README/novo-projeto, not mentor procedures.
**How to avoid:** Closed allowlist of exactly 5 commands; never auto-discover.

### Pitfall 3: Backtick paths that legitimately don't exist in the repo
**What goes wrong:** `PROGRESSO.md`/`CAMINHO.md`/`aulas/P0x-<slug>.md` flagged as unresolved.
**Why it happens:** They are student runtime files in gitignored `.projetos/<slug>/`, or `<placeholder>` paths.
**How to avoid:** SKIP regex covering runtime artifacts + placeholders + foreign-tool files + link-relative forms (see Check #2). [VERIFIED inventory.]

### Pitfall 4: Running the jargon-leak grep over `mentor/`
**What goes wrong:** Method jargon flagged as a "leak" in the very docs that own it.
**Why it happens:** Confusing "no jargon in ADAPTERS" with "no jargon anywhere".
**How to avoid:** Scope the leak grep to `AGENTS.md` + `.claude/` only. [VERIFIED baseline 0.]

### Pitfall 5: Committing a script that depends on `rg` if `rg` may be absent
**What goes wrong:** The permanent script fails on a machine without ripgrep.
**Why it happens:** Prior harnesses were disposable and run in a known env; a COMMITTED script faces more environments.
**How to avoid:** Either (a) declare `rg` a documented prerequisite (consistent with prior phases), or (b) fall back to `grep -E -c`. **Open question O-1.** Add an upfront `command -v rg` guard that prints a clear message and exits non-zero if missing.

## Code Examples

### Full harness skeleton (assembled, ready for the planner)
```sh
#!/usr/bin/env sh
# check-consistencia.sh -- auditoria de consistencia permanente (CONS-02 + CONS-03).
# Roda da raiz do repo. PASS/FAIL por criterio; exit = numero de falhas (0 = verde).
# Source of helpers: cloned from .planning/phases/05-.../scripts/check-phase5.sh [VERIFIED]

command -v rg >/dev/null 2>&1 || { echo "check-consistencia.sh: requer ripgrep (rg)"; exit 2; }
fails=0
count() { rg -c "$1" "$2" 2>/dev/null || echo 0; }
check_min()  { l="$1"; v="$2"; m="$3"; [ "$v" -ge "$m" ] && printf 'PASS  %-22s %s>=%s\n' "$l" "$v" "$m" || { printf 'FAIL  %-22s %s>=%s\n' "$l" "$v" "$m"; fails=$((fails+1)); }; }
check_zero() { l="$1"; v="$2"; [ "$v" -eq 0 ] && printf 'PASS  %-22s =0\n' "$l" || { printf 'FAIL  %-22s got=%s need=0\n' "$l" "$v"; fails=$((fails+1)); }; }
check_has()  { l="$1"; p="$2"; f="$3"; rg -q "$p" "$f" 2>/dev/null && printf 'PASS  %-22s in %s\n' "$l" "$f" || { printf 'FAIL  %-22s NOT in %s\n' "$l" "$f"; fails=$((fails+1)); }; }

echo "== CONS-02: anti-cargo-cult (cada teoria aterrissa) =="
check_has "C2-backward-ref"   'backward design'                 mentor/reference.md
check_has "C2-backward-novo"  'backward design'                 mentor/novo-projeto.md
check_has "C2-align"          'Objetivo \(capacidade\)'         mentor/reference.md
check_has "C2-mayer"          'so 3 de 12 principios|coerencia' mentor/reference.md
check_has "C2-expertrev"      'expertise-reversal'              mentor/reference.md
check_has "C2-retrieval"      'retrieval practice'              mentor/tutor.md
check_has "C2-sdt"            'proxima acao'                    mentor/tutor.md
check_has "C2-mastery"        'mastery learning'                mentor/fecha-marco.md
check_has "C2-formativa"      'auto-explicacao'                 mentor/metodo.md
check_has "C2-hattie"         'feed-forward'                    mentor/debug.md
check_has "C2-spacing"        'Agenda de retrieval'             mentor/fecha-marco.md

echo "== CONS-03 #1: comando <-> mentor/<comando>.md =="
for cmd in novo-projeto tutor fecha-marco debug spidr-split; do
  [ -f "mentor/$cmd.md" ] && printf 'PASS  cmd-%-18s mentor/%s.md\n' "$cmd" "$cmd" \
    || { printf 'FAIL  cmd-%-18s MISSING\n' "$cmd"; fails=$((fails+1)); }
done

echo "== CONS-03 #2: backtick paths resolvem =="
SKIP='(<slug>|<comando>|<conceito>|P0x|GEMINI\.md|CAMINHO\.md|PROGRESSO\.md|APRENDIZADO\.md|aulas/|exercicios/|projeto/|referencias/|^reference\.md$|^metodo\.md$)'
unresolved=$(rg -oN '`[A-Za-z0-9_./<>-]+\.(md|py|sh|json)`' mentor/ AGENTS.md README.md \
  | sed 's/.*`\(.*\)`/\1/' | sort -u \
  | while IFS= read -r p; do echo "$p" | rg -q "$SKIP" && continue; [ -f "$p" ] || echo "$p"; done | wc -l | tr -d ' ')
check_zero "backtick-paths" "$unresolved"

echo "== CONS-03 #3: zero jargao nos adaptadores =="
LEAK='SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect|feed-up|feed-back|feed-forward|Hattie|expertise-reversal|cognitive load|constructive alignment|formativ'
leak=$(rg -c "$LEAK" AGENTS.md .claude/ 2>/dev/null | awk -F: '{s+=$NF} END{print s+0}')
check_zero "adapter-jargon" "$leak"

echo "== IN-01: zero acentos (letras) em mentor/ =="
acc=$(rg -c '[áàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇ]' mentor/ 2>/dev/null | awk -F: '{s+=$NF} END{print s+0}')
check_zero "accents-mentor" "$acc"

echo "== $fails fail(s) =="
exit $fails
```
**Note:** the C2-align and C2-mayer anchors above are the discretion-flagged ones (chosen for robustness); the planner may refine exact patterns. All other anchors are VERIFIED ≥1 hit in-session.

### IN-01 fix (D-07)
```
# mentor/debug.md
:31  - Peça a mensagem ...   ->  - Peca a mensagem ...
:32  ... peça para descrever ... -> ... peca para descrever ...
```
[VERIFIED: cat -A shows `PeM-CM-'a` = `Peça`; these are the ONLY accented letters in mentor/.]

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Disposable `check-phaseN.sh` under `.planning/phases/NN-*/scripts/`, not shipped | Permanent `scripts/check-consistencia.sh` committed with the toolkit | Phase 6 (this phase, D-01) | First committed verification tool; re-audit = run 1 command (~0 tokens) vs agent re-reading 8 docs. |
| Consistency verified 100% manually | Mechanical grep/existence harness (partial; FUT-04 = full) | Phase 6 | Down-payment on CONCERNS.md Risco #1 (drift). |

**Deprecated/outdated:** nothing — this phase only adds.

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | `rg` (ripgrep) is acceptable as a hard dependency for a COMMITTED script (prior harnesses assumed it). | Standard Stack / Pitfall 5 | LOW–MED: if a target machine lacks `rg`, the script exits 2 with a clear message. Mitigation: `command -v rg` guard, or `grep -E` fallback. User/planner should confirm. |
| A2 | The closing report can be either `06-AUDITORIA.md` or folded into `06-VERIFICATION.md` (CONTEXT leaves this to discretion). | Recommended Structure | NONE — explicitly a discretion item per CONTEXT. |
| A3 | metodo.md satisfies set-equality by referencing all 5 commands inline (not via a single table). | CONS-03 set-equality | LOW: VERIFIED all 5 are referenced; the check should assert "references all 5, none outside set" rather than "has a table". |
| A4 | The `Objetivo (capacidade)` / `so 3 de 12 principios` anchors (rows 2,3) are robust enough; chosen over alternatives. | CONS-02 map rows 2,3 | LOW: both VERIFIED present; planner may pick a different anchor at discretion. |

**No `[ASSUMED]`-from-training claims:** every factual statement here was verified by reading or grepping the repo in this session.

## Open Questions

1. **O-1: `rg` vs `grep -E` for the committed script.**
   - What we know: prior disposable harnesses use `rg`; the env is Git Bash on Windows where `rg` is commonly but not universally present.
   - What's unclear: whether the user wants the permanent toolkit script to hard-depend on ripgrep.
   - Recommendation: keep `rg` for convention consistency + add the `command -v rg` guard (already in the skeleton). Note it as a one-line prerequisite in the script header. Revisit only if the user objects.

2. **O-2: Link-relative backtick paths (`reference.md`, `metodo.md` used inside `mentor/` markdown links).**
   - What we know: these resolve relative to the linking doc's directory, not repo root; the `mentor/<x>.md` backtick variants already cover the same files and DO resolve from root.
   - What's unclear: whether to normalize-then-test or SKIP them.
   - Recommendation: SKIP them (they are covered by the `mentor/` variants); documented in the skeleton's SKIP regex. Discretion.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| POSIX `sh` (Git Bash) | the harness shebang | ✓ (stated env: Git Bash on Windows) | — | none needed |
| ripgrep (`rg`) | all grep checks | ✓ assumed (prior harness convention) | — | `grep -E -c` (O-1) |
| `awk` | path-sum / section isolation | ✓ (bundled with Git Bash) | — | none needed |
| `sed` | backtick token strip | ✓ (bundled) | — | `rg` replace |
| `git` | committing the script + status flip | ✓ (repo is git) | — | none |

**Missing dependencies with no fallback:** none.
**Missing dependencies with fallback:** `rg` → `grep -E` (only if O-1 resolves toward max portability).

## Validation Architecture

> Nyquist validation is ENABLED (`workflow.nyquist_validation: true` in `.planning/config.json`). DOC/SCRIPT-editing phase: no runtime, no test framework. **The permanent script IS the validation mechanism** — the checks it encodes are the phase's automated verification, and they remain runnable forever (D-01 intent).

### Test Framework
| Property | Value |
|----------|-------|
| Framework | None — `sh` + `rg` + `awk` via `scripts/check-consistencia.sh` |
| Config file | None — the script is self-contained (no sibling helper needed; `extract-fenced.sh` NOT required for Phase 6's checks) |
| Quick run command | `rg -n "<padrao do criterio tocado>" mentor/<file>.md` |
| Full suite command | `sh scripts/check-consistencia.sh` (run from repo root) |
| Estimated runtime | ~2 seconds |

### Phase Requirements → Test Map
| Check ID | Req / SC | Behavior | Test Type | Automated Command | File Exists? |
|----------|----------|----------|-----------|-------------------|--------------|
| V-01..V-11 | CONS-02 / SC1 | each of the 11 anchor rows resolves in its cited doc (anti-cargo-cult) | grep | `rg -q '<anchor>' mentor/<doc>.md` (see CONS-02 map) | ❌ Wave 0 (script) — anchors PASS today |
| V-12 | CONS-03 / SC2 | all 5 canonical commands have `mentor/<cmd>.md` | existence | `for cmd in ...; do test -f mentor/$cmd.md; done` | ❌ Wave 0 — PASS today (5/5) |
| V-13 | CONS-03 / SC2 | every repo-resident backtick path resolves (with not-in-repo SKIP) | existence | Pattern 3 loop → `check_zero` on unresolved count | ❌ Wave 0 — PASS today (0 unresolved) |
| V-14 | CONS-03 / SC4 | zero method jargon in adapters (`AGENTS.md`, `.claude/`) | grep negative | `rg -c "$LEAK" AGENTS.md .claude/` → 0 | ❌ Wave 0 — PASS today (0) |
| V-15 | CONS-03 / SC3 | each of AGENTS.md/README.md/metodo.md references all 5 canonical commands, none outside set | grep | per-file allowlist intersection | ❌ Wave 0 — PASS today |
| V-16 | IN-01 / D-07 | zero accented letters in `mentor/` (after the debug.md:31-32 fix) | grep negative | `rg -c '[áàâ...çÇ]' mentor/` → 0 | ❌ Wave 0 — FAIL today (2), PASS after fix |

*Status: ⬜ pending · ✅ green · ❌ red. The "PASS today" annotations reflect in-session verification of the criteria themselves; the SCRIPT that runs them is the Wave 0 deliverable.*

### Sampling Rate
- **Per task commit:** run the touched criterion's `rg` one-liner (the Quick run command).
- **Per wave merge / before status flip (D-04):** run `sh scripts/check-consistencia.sh` — must be green EXCEPT V-16, which goes red→green when the IN-01 fix lands. Sequence: land script + IN-01 fix + status flip, then full suite green.
- **Phase gate (before `/gsd-verify-work`):** full suite green (all V-01..V-16) + the agent's one-time CONS-02 semantic confirmation recorded in the closing report (D-03).

### Wave 0 Gaps
- [ ] `scripts/check-consistencia.sh` — the permanent harness encoding V-01..V-16 (D-01 artifact a). This is the ONLY Wave 0 build item.
- [ ] Closing audit report (`06-AUDITORIA.md` or VERIFICATION) — captures the agent's one-time semantic pass (D-03) + any D-05 escalations (none expected). Authored after the script is green.
- [ ] No test framework to install — phase has no runtime.

*(`extract-fenced.sh` is NOT a Wave 0 gap for Phase 6: the adapter-leak check runs whole-file, not fenced-only.)*

### Manual-Only Verifications
| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Each CONS-02 anchor application "makes SENSE" (not just present) | CONS-02 / D-03 | grep finds the word; it cannot judge whether the usage is the intended application | Agent reads the exact landing line(s) from the CONS-02 map (one per practice) and confirms in the closing report that the theory genuinely lands there. One-time pass. |

## Security Domain

`security_enforcement` is absent from `.planning/config.json`. This phase has no authentication, session, network, input-from-untrusted-source, cryptography, or data-storage surface — it edits markdown and adds a local read-only shell script that runs `rg`/`test -f` over repo files. **No ASVS category applies.** The only adjacent concern: the committed script executes shell; it contains no `eval`, no untrusted input, no network calls — it reads tracked files and prints PASS/FAIL. No threat patterns apply.

## Sources

### Primary (HIGH confidence — read/grepped in-session)
- `mentor/fundamentos.md` (full) — the 6+6 catalog + "Aplicado em" column + 10 pending marks (lines 24,25,26,27,28,45,47,48,49,50).
- `mentor/reference.md`, `novo-projeto.md`, `tutor.md`, `fecha-marco.md`, `metodo.md`, `debug.md`, `spidr-split.md` (full) — CONS-02 anchor landings.
- `AGENTS.md` (full) — canonical routing table :16-23.
- `README.md` (full) — procedure mirror :114-129 + day-to-day table :57-62.
- `.claude/output-styles/mentor-projeto.md`, `.claude/skills/debug/SKILL.md`, `.claude/skills/tutor/SKILL.md` — adapters verified point-only.
- `.planning/phases/05-.../scripts/check-phase5.sh` + `extract-fenced.sh` — harness convention (helpers, `fails`, `exit`, anti-leak, slug-fragility note).
- `.planning/phases/05-.../05-VALIDATION.md` — Nyquist validation format reused here.
- `.planning/REQUIREMENTS.md` §CONS, `.planning/ROADMAP.md` §Phase 6, `.planning/phases/06-.../06-CONTEXT.md` — phase contract.
- In-session greps: accent scan (2 hits), command inventory (false-positive proof), backtick-path inventory + counts, CONS-02 anchor verification (all ≥1 hit), `mentor/*.md` listing, command-set extraction.

### Secondary / Tertiary
- None — no external sources needed; all claims verified against the repo.

## Metadata

**Confidence breakdown:**
- CONS-02 anchor map: HIGH — every anchor verified present in-session with exact lines; 0 structural findings.
- CONS-03 three checks: HIGH — command set, backtick inventory, and adapter-clean baseline all directly verified.
- Harness style: HIGH — cloned from a read, working `check-phase5.sh`.
- Portability (`rg` dependency): MEDIUM — convention is clear but committed-script portability is an open question (O-1).

**Research date:** 2026-06-16
**Valid until:** ~30 days (stable; only invalidated if Phases 1-5 docs are re-edited before Phase 6 runs — re-run the in-session greps if so).
