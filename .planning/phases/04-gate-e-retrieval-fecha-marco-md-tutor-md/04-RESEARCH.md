# Phase 4: Gate e retrieval (fecha-marco.md + tutor.md) - Research

**Researched:** 2026-06-15
**Domain:** Documentation editing (markdown procedure files read by an AGENT) — closing two assessment gaps in a learning-science-anchored mentor toolkit
**Confidence:** HIGH (all findings VERIFIED by reading the actual target files; zero theory re-derivation needed)

## Summary

This is a DOCUMENTATION-EDITING phase, not a software phase. The "code" is four markdown
procedure files in `mentor/` that an agent reads at runtime (`tutor.md`, `fecha-marco.md`)
plus a template owner (`reference.md`) and a hyperlink target (`fundamentos.md`). There is
NO test harness, NO build step, NO executable code in scope. "Verification" is grep-based
static checking: do the edited docs contain the required steps, sections, guardrails,
hyperlinks, and contract-consistent wording? [VERIFIED: read all 4 files + config.json]

The pedagogical theory (retrieval practice, mastery learning, spacing effect, SDT) is
ALREADY LOCKED in `mentor/fundamentos.md` from Phase 1. This phase does NOT re-research or
re-derive theory — it lands the theory into procedure prose by hyperlinking to the exact
anchors in `fundamentos.md` (each of which currently carries a `(Fase 4, pendente)` status
marker that Phase 6 will audit). [VERIFIED: fundamentos.md lines 28, 45, 47, 50]

The phase is tightly bounded by 13 locked decisions (D-01..D-13). The dominant
implementation risk is the **cross-file contract**: `fecha-marco.md` WRITES one entry to a
new `## Agenda de retrieval` section in `PROGRESSO.md`, and `tutor.md` READS that same
section at session open. Both edits must agree on the exact section name and the exact entry
line format, or the loop (AVAL-02 → AVAL-01) silently breaks. This contract must be fixed in
the plan before either file is edited.

**Primary recommendation:** Treat this as three coordinated string-insertion edits governed
by one shared contract. Fix the contract first (`## Agenda de retrieval` + entry format
`- <conceito> -- revisitar na abertura do marco <NN>`), then edit `reference.md` (template
owner, D-09), then `fecha-marco.md` (writer, D-05..D-10), then `tutor.md` (reader, D-01..D-04
+ D-12/D-13). Reuse the Phase 2 static-check harness pattern (`scripts/check-phase2.sh` +
`scripts/extract-fenced.sh`) verbatim as the validation model. Every framework name must
live in PROSE only — never inside a fenced block that becomes student-visible artifact text.

## Architectural Responsibility Map

The "tiers" here are documentation roles in the source-single design, not runtime tiers.

| Capability | Primary Tier (doc role) | Secondary Tier | Rationale |
|------------|------------------------|----------------|-----------|
| Active-recall question at session open (AVAL-01) | `mentor/tutor.md` (procedure read by agent) | `PROGRESSO.md` agenda (data source) | Tutor is the session-open procedure; it READS the scheduled debt, never invents it (D-02) |
| Mastery gate + capability criterion (AVAL-03) | `mentor/fecha-marco.md` Passo 1 (procedure) | `PROGRESSO.md` `**Capacidade:**` field (data source, Phase 3) | Gate reads the per-marco capability sentence and demands it literally (D-06) |
| Synthesis/transfer component (AVAL-04) | `mentor/fecha-marco.md` Passo 1 (procedure) | — | Gate is where "done" is judged; transfer is one oral extension question (D-07) |
| Spaced-review scheduling (AVAL-02 write side) | `mentor/fecha-marco.md` Passo 4 (procedure) | `mentor/reference.md` template (section definition) | Closing a marco is when the debt is created and written |
| Retrieval agenda data structure (AVAL-02 storage) | `mentor/reference.md` template owner | — | `reference.md` owns the `PROGRESSO.md` template; new section defined here (D-09) |
| Single next-action contract (ENG-01) | `mentor/tutor.md` Passo 4 + `mentor/fecha-marco.md` Checkpoint (procedures) | `PROGRESSO.md` Log (student-visible output) | Both session-close and marco-close must enforce exactly-1; jargon-free in the Log (D-12/D-13) |
| Theory definitions (retrieval/mastery/spacing/SDT) | `mentor/fundamentos.md` (upstream, NEVER edited here) | — | Source-single: theory is cited by hyperlink, never duplicated (ARCHITECTURE.md) |

**Misassignment to avoid:** Do NOT put theory text or a definition of any framework into
`tutor.md`/`fecha-marco.md`. Those docs CITE `fundamentos.md` by hyperlink. The only new
prose is the procedure mechanics + the framework NAME + the link. [VERIFIED: existing links
in reference.md L34/L98/L350/L408, novo-projeto.md L59/L150]

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| ENG-01 | `tutor.md` + `PROGRESSO.md` guarantee one unambiguous "next action" per session, anchored in autonomy/competence (SDT, honest relatedness caveat) | tutor.md Passo 4 already logs `proxima acao: <acao>` (L84) and says "despeca com a proxima acao explicita" (L87); fecha-marco Checkpoint already has "Aluno sabe qual e o proximo passo" (L106). D-12 makes these exactly-1 + verifiable; D-13 names SDT in prose with link to `fundamentos.md#frameworks-supporting-ancoram-um-doc` and the relatedness caveat `#sdt-relatedness-em-solo-ia` |
| AVAL-01 | `tutor.md` opens session with 1 active-recall question about a prior concept, without the student consulting the lesson | tutor.md Passo 1 (L37-48) already anticipates "se ha divida de aprendizado marcada para revisitar neste marco, anuncie" — the hook. D-01 inserts a dedicated recall step BEFORE the recap so the answer is not leaked by the recap's "o que ja funciona" line (L41) |
| AVAL-02 | `fecha-marco.md` schedules spaced review; `PROGRESSO.md` gains a retrieval/debt agenda field | fecha-marco Passo 4 (L51-60) is where PROGRESSO is updated — natural write site (D-10). reference.md `PROGRESSO.md` template (L198-250) gains `## Agenda de retrieval` (D-09), distinct from existing `## Dividas de aprendizado` (L243) |
| AVAL-03 | `fecha-marco.md` frames the marco gate explicitly as a mastery gate with a capability criterion (not just "code runs") | fecha-marco Passo 1 (L12-20) "Verificacao do done" with 3 checkboxes is the target; reframe as mastery gate (D-05) + read `**Capacidade:**` from PROGRESSO and demand it literally (D-06). Link `fundamentos.md#frameworks-supporting-ancoram-um-doc` (Mastery Learning row) |
| AVAL-04 | The gate includes a synthesis/transfer component (student explains AND extends without scaffold) | fecha-marco Passo 1 already has "O aluno consegue explicar o que cada parte faz?" (L17) and tutor Passo 3 has "me explica em 2 frases" (L71) — synthesis base. D-07 adds ONE oral extension question ("como voce mudaria isso para fazer X?") combining synthesis + transfer; blocking-but-formative (D-08) |
</phase_requirements>

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Area 1 — Retrieval na abertura do tutor (AVAL-01, AVAL-02 tutor side)**
- **D-01:** Insert a dedicated "Recuperacao ativa" step BEFORE the recap (current Passo 1), so recall happens without the student consulting the lesson (Criterio 1). 1 question only. Renumber the existing opening ritual. ("Doubling into Passo 1" was REJECTED because the recap reveals "o que ja funciona" and could hand over the answer.)
- **D-02:** Question source = CLOSED LOOP ONLY. Tutor demands STRICTLY the concept scheduled by `fecha-marco.md` in the `## Agenda de retrieval` section of `PROGRESSO.md` (see D-09/D-10). No ad-hoc question. This ties the AVAL-02 → AVAL-01 loop and fulfills Criterio 3.
- **D-03:** Recall is FORMATIVE, not a test. If the student does not remember: no penalty — it becomes/stays a review debt and the tutor re-points to the concept's lesson. Never blocks the session.
- **D-04:** "Empty agenda" edge (1st project session, and sessions within Marco 00 before the first close): no prior scheduled concept → tutor SKIPS recall and goes straight to recap. No ad-hoc fallback (coherent with D-02 and with "retrieval about a PRIOR concept"). The recall step only fires when there is an agenda entry.

**Area 2 — Mastery gate in fecha-marco.md (AVAL-03, AVAL-04)**
- **D-05:** Rename/reframe "Verificacao do done" (Passo 1) explicitly as a **mastery gate** — advance only after mastery, not just "the code runs". Keep it light: existing done-check renamed + criteria below (Criterio 4).
- **D-06:** Add capability criterion: the gate READS the `**Capacidade:**` field of the marco in `PROGRESSO.md` (written in Phase 3) and demands that capability literally ("ao terminar, voce consegue <verbo> <conceito>"). Contract already exists — just consume it.
- **D-07:** Transfer component (AVAL-04) = **1 oral/mental extension question** ("como voce mudaria isso para fazer X?"); the student describes or makes a tiny adjustment of the variation WITHOUT scaffold. Combines synthesis + transfer in one step. REJECTED: code extension mini-task (weighs the gate, conflicts with lightness) and "synthesis only" (does not fulfill the "extends" of AVAL-04).
- **D-08:** Gate **blocking but formative**: if the student cannot explain/extend, the marco does NOT close — return to the teaching cycle at the weak point (same as the "volte ao ciclo" that Passo 1 already does today). No grade, no punishment: it is diagnostic. REJECTED: advisory gate (would let proxy-completion through, exactly what AVAL-03/04 block).

**Area 3 — Spaced-review agenda (AVAL-02; fecha-marco.md + PROGRESSO.md template)**
- **D-09:** New section **`## Agenda de retrieval`** in the `PROGRESSO.md` template (in `mentor/reference.md`), SEPARATE from `## Dividas de aprendizado` (which are curation debts, a different thing). Unambiguous source the tutor demands (D-02 requires a clean source). Each entry is lean: 1 line (concept + which marco to revisit).
- **D-10:** When closing a marco, `fecha-marco.md` schedules **1 load-bearing concept** of the marco (essentially the `**Capacidade:**` sentence) to revisit at the OPENING of the next marco. 1 entry per close (lightness). REJECTED: increasing spaced interval (1+2 marcos — risks lightness) and "student chooses" (empties the agenda, breaks the loop).
- **D-11:** That agenda entry is the ONLY source the tutor demands at open (D-02) — the loop: fecha-marco writes → tutor reads and demands → student recalls → if fails, becomes formative debt (D-03).

**Area 4 — Single next action + SDT anchor (ENG-01; tutor.md + fecha-marco.md)**
- **D-12:** Light VERIFIABLE reinforcement: make "exactly 1 next action" an explicit checklist item in the tutor's session close (current Passo 4) and in `fecha-marco.md`'s final Checkpoint. Not optional, exactly 1 (not a list). Reuses what exists (tutor Passo 4 "despeca com proxima acao"; fecha-marco Passo 6 "aluno sabe o proximo passo") — just binds as a verifiable contract.
- **D-13:** Name the SDT anchor (autonomy + competence, WITH the honest relatedness caveat in solo+AI) in the PROSE of the procedures + link to `fundamentos.md`. The next action the student READS in the `PROGRESSO.md` Log stays jargon-free (anti-leak CONS-01).

### Claude's Discretion
- Exact wording of the naming phrases (mastery gate, retrieval, SDT) and of the prompts (extension question, recall question).
- Exact numbering of the renumbered steps in `tutor.md` after inserting the recall step.
- Precise position of the hyperlink anchors — check the real headings of `fundamentos.md` ("Frameworks foundational (load-bearing)", "Frameworks supporting (ancoram um doc)", "Limites e ressalvas" > "SDT relatedness em solo+IA") when linking.
- Exact form of the `## Agenda de retrieval` line in the template (suggestion: `- <conceito> -- revisitar na abertura do marco <NN>`).

### Deferred Ideas (OUT OF SCOPE)
- Increasing spaced interval (revisit at 1 then 2 marcos) — REJECTED this phase (D-10) for lightness; could return as a future evolution.
- Code extension mini-task as transfer — REJECTED (D-07) for weight; possible future reinforcement, not this phase.
- Formative curation check and forensics protocol as tri-partite feedback — belong to Phase 5 (`metodo.md` + `debug.md`).
- Final audit that each "(Fase 4, pendente)" in `fundamentos.md` became real application — Phase 6 (CONS-02 / anti-cargo-cult).
</user_constraints>

## Project Constraints (from CLAUDE.md / STATE / CONVENTIONS)

- **No project CLAUDE.md with GSD rules** — the repo `.gitignore`s `CLAUDE.md` and uses `AGENTS.md` for the mentor persona. GSD context lives only in `.planning/`. The user-global `~/.claude/CLAUDE.md` (RTK token proxy) is environment tooling, not a project constraint on the docs. [VERIFIED: STATE.md L42-45]
- **Portuguese WITHOUT accents** in all `mentor/` files (encoding robustness). Paths/identifiers in backticks. [VERIFIED: STATE.md L47-48, CONVENTIONS referenced in CONTEXT.md]
- **Source-single (anti-drift):** theory only in `mentor/`, cited by link, never duplicated in adapters (`.claude/`, `AGENTS.md`). [VERIFIED: STATE.md L50-52, ARCHITECTURE.md cited]
- **Anti-cargo-cult:** every new practice in `fundamentos.md` needs a verifiable "aplicado em <doc>" — Phase 4 turns the `(Fase 4, pendente)` markers into real applications that Phase 6 audits. [VERIFIED: fundamentos.md L28/L45/L47/L50]
- **Skill adapters are thin pointers, NOT procedure bodies.** `.claude/skills/tutor/SKILL.md` and `.claude/skills/fecha-marco/SKILL.md` are each 12 lines and only say "Leia `mentor/<comando>.md` ... e siga o procedimento exatamente." This phase edits ONLY the `mentor/*.md` canonical bodies; the adapters need NO change (and changing them would violate source-single). [VERIFIED: read both SKILL.md files]

## Standard Stack

There is no software stack. The "stack" is the existing doc-editing + static-verification toolchain already established in Phases 1-3.

### Core
| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| `rg` (ripgrep) / `grep` | system | Static presence/absence checks against edited docs | Phase 2 established this as the verification mechanism (no test runtime) [VERIFIED: 02-VALIDATION.md L24] |
| `awk` (POSIX) | system | Extract fenced-block content for the anti-leak negative check | `extract-fenced.sh` already implements this [VERIFIED: read script] |
| `sh` (POSIX) | system | Wrap the grep checks into a pass/fail gate script | `check-phase2.sh` is the template [VERIFIED: read script] |

### Supporting (reuse, do not rebuild)
| Asset | Location | Purpose | When to Use |
|-------|----------|---------|-------------|
| `extract-fenced.sh` | `.planning/phases/02-.../scripts/` | Isolates ` ``` ` block content so the anti-leak grep does not false-positive on legitimate prose | Reuse verbatim — copy into phase 4 scripts dir for the CONS-01 check on `reference.md` template block |
| `check-phase2.sh` | `.planning/phases/02-.../scripts/` | Pattern for a PASS/FAIL static gate (check_min / check_zero / check_has + anchor-resolve) | Clone as `check-phase4.sh` with the Phase 4 criteria table |

**No installation needed** — `rg`, `awk`, `sh` already used by the Phase 2 gate.

## Architecture Patterns

### Data-flow Diagram — the retrieval loop this phase closes

```
                    fecha-marco.md (Passo 4, on marco close)
                              |
                  D-10: write 1 load-bearing concept
                  (= the **Capacidade:** sentence)
                              |
                              v
          PROGRESSO.md  ## Agenda de retrieval   <-- NEW section (D-09)
          - <conceito> -- revisitar na abertura do marco <NN>
                              |
                  D-02: tutor reads STRICTLY this
                              |
                              v
   tutor.md (NEW recall step, BEFORE recap)  <-- D-01
                              |
              agenda has entry? ----no----> SKIP recall, go to recap  (D-04)
                              |
                             yes
                              |
              ask 1 recall question (no lesson lookup)  (AVAL-01)
                              |
              student recalls? --no--> formative debt, re-point lesson (D-03)
                              |              (never blocks session)
                             yes
                              |
                              v
                       proceed to recap (current Passo 1)
```

Parallel, on the gate side (no PROGRESSO write, read-only of `**Capacidade:**`):

```
   fecha-marco.md Passo 1 = MASTERY GATE (D-05)
     |- [ ] code runs (existing)
     |- [ ] student explains each part (existing, AVAL-04 synthesis base)
     |- [ ] User Story satisfied (existing)
     |- [ ] reads **Capacidade:** from PROGRESSO, demands it literally (D-06, AVAL-03)
     |- [ ] 1 extension question "como mudaria para X?" answered w/o scaffold (D-07, AVAL-04)
            |
       all pass? --no--> marco NOT closed, return to cycle at weak point (D-08)
            |
           yes --> continue to Passo 2 (curadoria)
```

### Exact current structure of the 3 edited files (edit map)

**`mentor/tutor.md`** (110 lines) [VERIFIED: full read]
- L37-48 `## Passo 1 — Abertura da sessao (ritual de 30 segundos)` — recap in max 4 lines, includes the leak risk line L41 "O que ja funciona". L47-48 already hooks "Se ha divida ... anuncie". **D-01 inserts a NEW step BEFORE this** (becomes new Passo 1 "Recuperacao ativa"; current Passo 1 becomes Passo 2; renumber Passos 2/3/4 → 3/4/5). The new step reads `## Agenda de retrieval` from PROGRESSO; if empty, skip (D-04).
- L50 `## Passo 2 — Conduzir o passo atual` → renumber to Passo 3.
- L67 `## Passo 3 — Revisar a tentativa` → renumber to Passo 4. Already has "me explica em 2 frases" (L71) — synthesis base, do NOT duplicate; the GATE side (fecha-marco) owns transfer.
- L79 `## Passo 4 — Fechamento da sessao` → renumber to Passo 5. L84 logs `proxima acao: <acao>`; L87 "Despeca com a proxima acao explicita". **D-12 adds a verifiable "exactly 1 next action" checklist item here**; **D-13 names SDT anchor in prose + link**.
- L89 `## Roteamento`, L98 `## Anti-padroes do copiloto` — L102 "Abrir a sessao com aula em vez de recap" and L105 "Encerrar sessao sem registrar ... proxima acao" are existing anti-patterns; consider adding "Disparar recuperacao sem entrada na agenda" and "fechar com lista de proximas acoes em vez de exatamente 1" to keep guardrails co-located with style.

**`mentor/fecha-marco.md`** (113 lines) [VERIFIED: full read]
- L7-10 `## Pre-requisitos` — already states "consegue explicar".
- L12-20 `## Passo 1 — Verificacao do "done"` — 3 checkboxes (L16 code runs, L17 explains, L18 User Story). L20 "Se algum criterio falhar ... Volte ao ciclo" = already the blocking-formative behavior (D-08). **This is the mastery-gate target (D-05/D-06/D-07).** Rename heading to name mastery gate; add capability-criterion checkbox (D-06, reads `**Capacidade:**`) and extension-question checkbox (D-07). Link `fundamentos.md#frameworks-supporting-ancoram-um-doc`.
- L51-60 `## Passo 4 — Atualizar PROGRESSO.md` — 5 numbered items (L55 mark closed, L56 advance ATUAL, L57 Log, L58 transfer curation debts, L59-60 substrato table). **D-10 adds a 6th item: write 1 entry to `## Agenda de retrieval`.** Note item 4 (L58) already transfers `## Dividas de aprendizado` — keep the new agenda write DISTINCT from this.
- L96-106 `## Checkpoint final` — 7 checkboxes; L106 "Aluno sabe qual e o proximo passo". **D-12 makes this "exactly 1 proxima acao" verifiable.**
- L108-113 `## Anti-padroes` — co-locate a "agendar mais de 1 conceito por fechamento" guardrail if desired (lightness ceiling).

**`mentor/reference.md`** §"Template -- PROGRESSO.md" (L198-250) [VERIFIED: full read]
- L209 `## Objetivo`, L223 `## Marcos` with `**Capacidade:**` per marco at L228/L237 (Phase 3 contract the gate consumes), L243 `## Dividas de aprendizado`, L247 `## Log`. **D-09 adds `## Agenda de retrieval` as a NEW section in this template block**, placed sensibly between `## Dividas de aprendizado` (L243) and `## Log` (L247), with the entry format line `- <conceito> -- revisitar na abertura do marco <NN>`. This new section is INSIDE a ` ```markdown ` fenced block → it is student-visible artifact text → **must be jargon-free (CONS-01).**

### Exact hyperlink anchors in `fundamentos.md` (GitHub-slug verified against existing links)

[VERIFIED: existing link targets in reference.md L34/L98/L350 and novo-projeto.md L59/L150 resolve to these heading slugs]

| Framework (this phase) | Heading in fundamentos.md | Anchor slug to link |
|------------------------|---------------------------|---------------------|
| Retrieval Practice / Testing Effect (AVAL-01) | `## Frameworks foundational (load-bearing)` (L19), row at L28 | `fundamentos.md#frameworks-foundational-load-bearing` |
| Mastery Learning (AVAL-03) | `## Frameworks supporting (ancoram um doc)` (L41), row at L47 | `fundamentos.md#frameworks-supporting-ancoram-um-doc` |
| Spacing Effect (AVAL-02) | `## Frameworks supporting (ancoram um doc)` (L41), row at L50 | `fundamentos.md#frameworks-supporting-ancoram-um-doc` |
| SDT (ENG-01) | `## Frameworks supporting (ancoram um doc)` (L41), row at L45 | `fundamentos.md#frameworks-supporting-ancoram-um-doc` |
| SDT relatedness caveat (ENG-01 honest limit) | `### SDT relatedness em solo+IA` (L62, under `## Limites e ressalvas`) | `fundamentos.md#sdt-relatedness-em-solo-ia` |

**Anchor caveat [ASSUMED → verify by render]:** `#frameworks-supporting-ancoram-um-doc` is the
SECTION heading shared by Mastery, Spacing, and SDT (the table is not individually
anchorable). The precedent `novo-projeto.md` L150 already links SDT to exactly this slug, so
it is the established pattern. The `### SDT relatedness em solo+IA` slug — `+` drops, spaces →
hyphens — should render as `#sdt-relatedness-em-solo-ia`; confirm in the target renderer
during execution (Claude's Discretion item already flags this). The `check-phase4.sh` script
should include an ANCHOR-RESOLVE check (like check-phase2.sh L84-90) that greps the literal
headings exist in `fundamentos.md`.

### Pattern: source-single citation (inherited, inviolable)
**What:** New theory text is NEVER written in `tutor.md`/`fecha-marco.md`. Procedures name
the framework + link `fundamentos.md`. [VERIFIED: existing links, ARCHITECTURE.md]
**Example (the established form):**
```
([anti-evasao da SDT](fundamentos.md#frameworks-supporting-ancoram-um-doc) —
competencia via micro-vitorias)
```
(from novo-projeto.md L150 — copy this exact link/prose shape for the ENG-01 SDT anchor)

### Anti-Patterns to Avoid
- **Theory leak into student-visible text (CONS-01):** the `## Agenda de retrieval` entry, the next-action Log line, and the `**Capacidade:**` phrasing are READ BY THE STUDENT → zero jargon. Procedure prose (read by agent) MAY name SDT/mastery/retrieval/spacing. The boundary is fenced-block (student) vs prose (agent). [VERIFIED: CONTEXT.md L29-31, fundamentos.md L3-8]
- **Duplicating debt semantics:** `## Agenda de retrieval` (spaced-review of mastered concepts) must stay SEPARATE from `## Dividas de aprendizado` (curation debts). Merging them breaks D-02's "clean source" requirement. [VERIFIED: D-09]
- **Ad-hoc recall question:** tutor must NOT generate its own question; only the scheduled agenda entry (D-02). Empty agenda → skip, no fallback (D-04).
- **Heavy gate:** no quiz, no grade, no giant checklist. Gate = renamed done-check + 1 capability criterion + 1 extension question. [VERIFIED: ROADMAP SC4]
- **Editing skill adapters:** do not touch `.claude/skills/*/SKILL.md` — they are pointers (source-single). [VERIFIED: read both]

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Verifying edited docs | A new test framework | `rg`/`grep` static checks + clone of `check-phase2.sh` | No runtime exists; Phase 2 already established the gate pattern [VERIFIED] |
| Anti-leak check on fenced template | A custom markdown parser | `extract-fenced.sh` (awk toggle) | Already written and proven; isolates ` ``` ` content so prose framework-names don't false-positive [VERIFIED: read script] |
| Theory definitions | Writing retrieval/spacing/mastery/SDT text into the procedures | Hyperlink to `fundamentos.md` anchors | Source-single design; Phase 6 audits for duplication [VERIFIED] |
| Capability sentence | A new schema in PROGRESSO | Read the existing `**Capacidade:**` field (Phase 3, reference.md L228/L237) | Contract already shipped; D-06 just consumes it [VERIFIED] |

**Key insight:** Nearly every hook this phase needs already exists in the target files. The
work is INSERTION + RENAME + LINK + one new template section + binding existing behaviors as
verifiable contracts — not net-new construction. The biggest source of bugs would be
re-inventing something already present (a second debt section, an ad-hoc question source, a
local theory paragraph).

## Runtime State Inventory

This is a doc-edit phase, but the new `## Agenda de retrieval` is RUNTIME STATE in every
student's `PROGRESSO.md`, so the inventory matters for the contract.

| Category | Items Found | Action Required |
|----------|-------------|------------------|
| Stored data | Student `PROGRESSO.md` files live in `.projetos/<slug>/` which is `.gitignore`d (personal, not in toolkit repo) [VERIFIED: reference.md L181-183]. They were generated from the OLD template (no `## Agenda de retrieval`). | Code edit only — the template in `reference.md` gains the section; existing student files won't auto-migrate. **Plan must note:** the tutor's recall step (D-04) already handles "no agenda entry" by skipping, so old PROGRESSO files degrade gracefully (no crash, just no recall until next marco close writes an entry). No data migration script needed — the empty-agenda edge IS the migration path. |
| Live service config | None — no external services. Verified: only `scripts/roadmap_fetch.py` exists in repo, unrelated. [VERIFIED: ls scripts/] |
| OS-registered state | None — no schedulers, daemons, or registered tasks. [VERIFIED: repo is a markdown toolkit] |
| Secrets/env vars | None. [VERIFIED] |
| Build artifacts | None — no compiled output. The `.claude/skills/*/SKILL.md` adapters reference `mentor/*.md` by path and need no rebuild since they don't embed content. [VERIFIED: read adapters] |

**The canonical question — after every file is updated, what runtime state still has the old
shape?** Only student `PROGRESSO.md` files (gitignored, personal). They lack the new section,
but D-04's skip-on-empty rule makes that safe by design. No migration task required; the
plan should explicitly state this so the planner does not invent one.

## Common Pitfalls

### Pitfall 1: Contract drift between writer and reader
**What goes wrong:** `fecha-marco.md` writes `## Agenda de retrieval` but `tutor.md` looks for `## Agenda de revisao` (or the entry format differs). The loop silently produces no recall question forever.
**Why it happens:** Three files edited (possibly in separate plans/waves); the section name and entry format are free text.
**How to avoid:** FIX the contract in the plan before editing — one canonical section name + one canonical entry line, copied verbatim into all three edits. Add a grep check that the SAME literal string appears in `reference.md` (template), `fecha-marco.md` (writes it), and `tutor.md` (reads it).
**Warning signs:** Any of the three files spells the section differently; the entry format in the template doesn't match what fecha-marco's instruction tells the agent to write.

### Pitfall 2: Recall answer leaked by the recap
**What goes wrong:** Recall happens during/after the recap, and the recap's "o que ja funciona" line (tutor.md L41) reveals the answer.
**Why it happens:** Tempting to "double into Passo 1" instead of inserting a new step — explicitly REJECTED by D-01.
**How to avoid:** The new recall step MUST be its own step BEFORE the recap. Verify ordering: recall heading appears at a lower line number than the recap heading.
**Warning signs:** Recall instructions placed inside the recap step.

### Pitfall 3: Theory jargon leaks into student-visible text (CONS-01 violation)
**What goes wrong:** "SDT" or "retrieval practice" appears in the `## Agenda de retrieval` template entry, the next-action Log line, or the `**Capacidade:**` phrasing — all of which the student reads.
**Why it happens:** The procedure prose legitimately names frameworks; copy-paste bleeds a name into the fenced template block.
**How to avoid:** Run `extract-fenced.sh reference.md | rg "SDT|retrieval|mastery|spacing|backward design|Bloom"` → must be 0. Keep all framework names in prose + links only.
**Warning signs:** A framework name inside any ` ``` ` block, or in an instruction describing what the student will SEE.

### Pitfall 4: Gate becomes heavy (violates Criterio 4)
**What goes wrong:** The mastery gate grows into a multi-question quiz or a long checklist; transfer becomes a code task.
**Why it happens:** Over-engineering "rigor".
**How to avoid:** Hold the ceiling written in CONTEXT: 1 capability criterion + 1 extension question (oral/mental, D-07). Write the "1 pergunta" / "exatamente 1" guardrails into the doc itself (Phase 3 D-04 style).
**Warning signs:** More than one new question in the gate; an extension task that requires writing code with scaffold.

### Pitfall 5: Accent characters sneak in
**What goes wrong:** Editing introduces accented Portuguese (ç, ã, é), breaking the no-accent convention.
**Why it happens:** Natural Portuguese spelling.
**How to avoid:** Match the existing accent-free style of the surrounding text; grep for common accented chars before commit.
**Warning signs:** Any accented character in the diff to `mentor/*.md`.

## Code Examples

### The new agenda entry — template form (student-visible → jargon-free)
```markdown
## Agenda de retrieval

- <conceito> -- revisitar na abertura do marco <NN>
```
Source: D-09 suggested form + reference.md existing template style (L243-250). Note: no
framework name; `<conceito>` is plain language derived from the `**Capacidade:**` sentence.

### The SDT prose+link form (agent-visible prose → may name framework)
```
A proxima acao e exatamente UMA (se virou lista, corte): ancora a motivacao em autonomia
(voce escolheu este projeto) e competencia (voce ja VE isso funcionando) —
[SDT](fundamentos.md#frameworks-supporting-ancoram-um-doc), com a
[ressalva honesta sobre relatedness em solo+IA](fundamentos.md#sdt-relatedness-em-solo-ia).
```
Source: modeled on novo-projeto.md L150 link shape [VERIFIED]. The next-action LINE written
to the student's Log stays jargon-free; only this procedure prose names SDT.

### Anti-leak verification (reuse from Phase 2)
```sh
sh extract-fenced.sh mentor/reference.md | rg -c "SDT|retrieval|mastery|spacing|backward design|Bloom|GRR|Mayer"
# expected: 0
```
Source: extract-fenced.sh + check-phase2.sh L92-96 [VERIFIED: read both].

## State of the Art

Not applicable — no external libraries or fast-moving ecosystem. The relevant "state" is the
internal build order and prior-phase contracts, all stable:

| Prior contract | Status | Impact on Phase 4 |
|----------------|--------|-------------------|
| `**Capacidade:**` per marco in PROGRESSO (Phase 3, D-02) | Shipped [VERIFIED: reference.md L228/L237] | D-06 reads it; do not redefine |
| `## Dividas de aprendizado` section (pre-existing) | Shipped [VERIFIED: reference.md L243] | Keep `## Agenda de retrieval` distinct from it |
| `fundamentos.md` rows with `(Fase 4, pendente)` | Shipped, awaiting landing [VERIFIED: L28/L45/L47/L50] | This phase lands them; Phase 6 audits the status flip |
| Phase 2 static-check harness | Shipped [VERIFIED: check-phase2.sh] | Clone as check-phase4.sh |

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | `### SDT relatedness em solo+IA` renders to anchor `#sdt-relatedness-em-solo-ia` (`+` drops, spaces→hyphens) | Hyperlink anchors | Dead link in `tutor.md`/`fecha-marco.md`; caught by ANCHOR-RESOLVE grep + 1 manual render check (Claude's Discretion already flags verifying this) |
| A2 | Old student `PROGRESSO.md` files need NO migration because D-04 skip-on-empty handles the missing section gracefully | Runtime State Inventory | If a future tutor edit assumes the section always exists, old files could error — mitigated by writing D-04 skip rule explicitly into tutor.md |

**Note:** The pedagogical theory itself carries NO assumptions — it is locked upstream in
`fundamentos.md` (Phase 1) and explicitly out of scope to re-derive. All theory claims here
are [VERIFIED: fundamentos.md].

## Open Questions

1. **Where exactly to place `## Agenda de retrieval` within the PROGRESSO template?**
   - What we know: it must be distinct from `## Dividas de aprendizado` (L243) and before/around `## Log` (L247).
   - What's unclear: between Dividas and Log, or after Log? (cosmetic)
   - Recommendation: place it immediately after `## Dividas de aprendizado` (both are "debt-like" forward-looking sections) and before `## Log`. Low stakes; planner's discretion.

2. **Should the new tutor recall step and renumbering be one plan or split?**
   - What we know: three files, one shared contract.
   - Recommendation: single coordinated phase; if split into plans, the contract (section name + entry format) must be fixed in a shared artifact BEFORE any file edit, and the cross-file grep check must run after all three are edited (per-wave merge gate).

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| `rg` (ripgrep) | Static verification gate | ✓ (used by Phase 2 gate) | system | `grep -c` (check-phase2.sh count() already falls back) |
| `awk` (POSIX) | extract-fenced.sh | ✓ | system | none needed |
| `sh` (POSIX) | check-phase4.sh wrapper | ✓ | system | run greps manually |

**Missing dependencies with no fallback:** None.
**Missing dependencies with fallback:** None blocking — Phase 2 already proved the toolchain works in this repo.

## Validation Architecture

> `nyquist_validation: true` in config.json → this section is included. No runtime test
> framework exists; validation is STATIC (grep presence/absence + anchor resolution),
> modeled exactly on Phase 2's `02-VALIDATION.md` + `check-phase2.sh`.

### Test Framework
| Property | Value |
|----------|-------|
| Framework | None — static verification via `rg`/`grep` + `extract-fenced.sh`, wrapped in `check-phase4.sh` |
| Config file | none — clone `extract-fenced.sh` into the phase 4 scripts dir (Wave 0) |
| Quick run command | `rg -n "<padrao do criterio tocado>" mentor/<file>.md` |
| Full suite command | `sh .planning/phases/04-.../scripts/check-phase4.sh` |
| Estimated runtime | ~2 seconds |

### Phase Requirements → Test Map (grep-able acceptance criteria)

| Req / SC | Behavior verificavel | Test Type | Automated Command (static) | File Exists? |
|----------|----------------------|-----------|----------------------------|--------------|
| AVAL-01 / SC1 | New recall step heading exists in `tutor.md` BEFORE the recap heading | grep + order | `rg -n "Recuperacao ativa\|recuperacao" mentor/tutor.md` then confirm its line < the "Abertura da sessao" recap line | ✅ |
| AVAL-01 / SC1 | Tutor reads STRICTLY the agenda (D-02), no ad-hoc | grep + inspection | `rg -n "Agenda de retrieval" mentor/tutor.md` (must reference the section) | ✅ |
| AVAL-01 / D-04 | Empty-agenda skip rule present | grep | `rg -n "se .*agenda.*vazia\|nenhum conceito\|pule\|skip" mentor/tutor.md` | ✅ |
| AVAL-03 / SC2 | Passo 1 heading reframed as mastery gate | grep | `rg -n "mastery gate\|gate de marco\|gate de maestria" mentor/fecha-marco.md` | ✅ |
| AVAL-03 / SC2 | Gate reads `**Capacidade:**` and demands it | grep | `rg -n "Capacidade" mentor/fecha-marco.md` (in the gate step) | ✅ |
| AVAL-04 / SC2 | Extension/transfer question present (1, oral) | grep | `rg -n "como voce mudaria\|estender\|extensao\|transferencia" mentor/fecha-marco.md` | ✅ |
| AVAL-04 / D-08 | Blocking-formative: marco does not close on failure | grep | `rg -n "NAO .*fecha\|volte ao ciclo" mentor/fecha-marco.md` | ✅ |
| AVAL-02 / SC3 | `## Agenda de retrieval` section in PROGRESSO template | grep | `rg -n "## Agenda de retrieval" mentor/reference.md` | ✅ |
| AVAL-02 / D-09 | Agenda distinct from `## Dividas de aprendizado` | grep | both `rg -n "## Agenda de retrieval"` AND `rg -n "## Dividas de aprendizado"` return distinct lines in `mentor/reference.md` | ✅ |
| AVAL-02 / SC3 | fecha-marco writes 1 entry on close (Passo 4) | grep | `rg -n "Agenda de retrieval" mentor/fecha-marco.md` | ✅ |
| ENG-01 / SC1 | "exactly 1 next action" verifiable in tutor close + fecha checkpoint | grep | `rg -n "exatamente 1\|uma .*proxima acao\|1 proxima acao" mentor/tutor.md mentor/fecha-marco.md` | ✅ |
| ENG-01 / D-13 | SDT named in prose + link (both files) | grep link | `rg -n "\]\(fundamentos\.md#frameworks-supporting-ancoram-um-doc\)" mentor/tutor.md mentor/fecha-marco.md` and `rg -n "\]\(fundamentos\.md#sdt-relatedness-em-solo-ia\)"` | ✅ |
| CONTRACT | Section name + entry format identical across the 3 files | cross-file grep | `rg -n "Agenda de retrieval" mentor/reference.md mentor/fecha-marco.md mentor/tutor.md` (all three present, same literal) | ✅ |
| ANCHOR-RESOLVE | Every `fundamentos.md#anchor` used resolves to a real heading | anchor resolve | `rg -q '^## Frameworks supporting \(ancoram um doc\)' mentor/fundamentos.md` AND `rg -q '^### SDT relatedness em solo' mentor/fundamentos.md` AND `rg -q '^## Frameworks foundational \(load-bearing\)' mentor/fundamentos.md` | ✅ |
| CONS-01 (anti-leak) | No framework jargon inside the PROGRESSO template fenced block | grep negative | `sh extract-fenced.sh mentor/reference.md \| rg -c "SDT\|retrieval\|mastery\|spacing\|backward design\|Bloom\|GRR\|Mayer"` → must be 0 | ✅ |

*File Exists ✅ for all because the phase EDITS existing files — zero Wave 0 code creation.*

### Sampling Rate
- **Per task commit:** the `rg` for the criterion touched + the CONS-01 anti-leak grep (when a fenced block is touched).
- **Per wave merge:** full `check-phase4.sh` + the CONTRACT cross-file grep (all three files must agree).
- **Phase gate:** full suite green + 1 manual hyperlink resolution in the target renderer (confirms A1 anchor slug) before `/gsd-verify-work`.

### Wave 0 Gaps
- [ ] Clone `extract-fenced.sh` into `.planning/phases/04-.../scripts/` (reuse verbatim — proven).
- [ ] Author `check-phase4.sh` from the `check-phase2.sh` template with the table above (check_min for presence, check_zero for anti-leak, check_has + ANCHOR-RESOLVE for headings, plus the CONTRACT cross-file equality check).
- [ ] No framework install needed (rg/awk/sh present).

*Note: baseline run before edits will FAIL positive checks (expected) and PASS only the anti-leak baseline — same convention as Phase 2 (check-phase2.sh L12-15).*

## Security Domain

> `security_enforcement` is not set in config.json, and this is a markdown documentation
> phase with no auth, network, input parsing, crypto, or data handling. No ASVS category
> applies. The only "integrity" concern is editorial (anti-drift / anti-leak), covered by
> the Validation Architecture above. Section omitted as not applicable.

## Sources

### Primary (HIGH confidence — read this session)
- `mentor/tutor.md` (110 lines, full read) — current step structure, hooks at L41/L47/L71/L84/L87
- `mentor/fecha-marco.md` (113 lines, full read) — Passo 1 gate L12-20, Passo 4 PROGRESSO write L51-60, Checkpoint L96-106
- `mentor/reference.md` (454 lines, read) — PROGRESSO template L198-250, `**Capacidade:**` L228/L237, `## Dividas de aprendizado` L243, existing fundamentos links L34/L98/L350/L408
- `mentor/fundamentos.md` (97 lines, full read) — anchor headings + `(Fase 4, pendente)` rows L28/L45/L47/L50, SDT caveat L62
- `.claude/skills/tutor/SKILL.md`, `.claude/skills/fecha-marco/SKILL.md` (12 lines each) — confirmed thin adapters, not procedure bodies
- `.planning/phases/02-.../scripts/check-phase2.sh` + `extract-fenced.sh` — validation harness pattern to clone
- `.planning/phases/02-.../02-VALIDATION.md` — VALIDATION.md format model
- `.planning/phases/04-.../04-CONTEXT.md` — 13 locked decisions
- `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`, `.planning/STATE.md`, `.planning/config.json`

### Secondary (MEDIUM)
- `mentor/novo-projeto.md` L145-155 — precedent SDT link shape (`#frameworks-supporting-ancoram-um-doc`)

### Tertiary (LOW)
- None. No web research was needed or appropriate; all findings are from the codebase.

## Metadata

**Confidence breakdown:**
- Edit map (exact structure of 3 files): HIGH — read every target file in full.
- Hyperlink anchors: HIGH for section-level slugs (precedent in repo); MEDIUM for the SDT-caveat sub-anchor (A1 — verify by render).
- Cross-file contract: HIGH — the risk is identified and a grep check is specified.
- Validation architecture: HIGH — directly modeled on the proven Phase 2 harness.
- Runtime state: HIGH — repo audited, only gitignored student PROGRESSO files, handled by D-04.

**Research date:** 2026-06-15
**Valid until:** Stable — these are internal docs; valid until the target files change (re-verify line numbers if `tutor.md`/`fecha-marco.md`/`reference.md` are edited before planning).
