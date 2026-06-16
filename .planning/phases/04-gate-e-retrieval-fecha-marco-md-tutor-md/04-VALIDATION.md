---
phase: 4
slug: gate-e-retrieval-fecha-marco-md-tutor-md
status: draft
nyquist_compliant: true
wave_0_complete: false
created: 2026-06-15
---

# Phase 4 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.
> This is a DOCUMENTATION-EDITING phase: no runtime, no test framework. Validation is
> STATIC (grep presence/absence + anchor resolution + cross-file contract equality),
> modeled verbatim on Phase 2's `check-phase2.sh` + `extract-fenced.sh` harness.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | None — static verification via `rg`/`grep` + `extract-fenced.sh`, wrapped in `check-phase4.sh` |
| **Config file** | none — `extract-fenced.sh` cloned verbatim into the phase 4 scripts dir (Wave 0) |
| **Quick run command** | `rg -n "<padrao do criterio tocado>" mentor/<file>.md` |
| **Full suite command** | `sh .planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/check-phase4.sh` |
| **Estimated runtime** | ~2 seconds |

---

## Sampling Rate

- **After every task commit:** Run the `rg` for the criterion touched + the CONS-01 anti-leak grep when a fenced block was touched
- **After every plan wave:** Run `check-phase4.sh` + the CONTRACT cross-file grep (all three files must agree on section name + entry format)
- **Before `/gsd-verify-work`:** Full suite green + 1 manual hyperlink resolution in the target renderer (confirms A1 anchor slug `#sdt-relatedness-em-solo-ia`)
- **Max feedback latency:** ~2 seconds

---

## Per-Task Verification Map

> Static checks, not unit tests. "Automated Command" is a grep that must succeed (or, for
> anti-leak, return 0). File Exists is ✅ for all — the phase EDITS existing files, zero
> net-new code creation outside Wave 0 scripts.

| Check ID | Req / SC | Verifiable Behavior | Test Type | Automated Command (static) | File Exists | Status |
|----------|----------|---------------------|-----------|----------------------------|-------------|--------|
| V-01 | AVAL-01 / SC1 | New recall step heading exists in `tutor.md` BEFORE the recap heading | grep + order | `rg -n "[Rr]ecuperacao ativa" mentor/tutor.md` then confirm its line < the "Abertura da sessao" recap line | ✅ | ⬜ pending |
| V-02 | AVAL-01 / D-02 | Tutor reads STRICTLY the agenda, no ad-hoc question | grep | `rg -n "Agenda de retrieval" mentor/tutor.md` | ✅ | ⬜ pending |
| V-03 | AVAL-01 / D-04 | Empty-agenda skip rule present | grep | `rg -n "[Aa]genda.*vazia|[Nn]enhum conceito|[Pp]ule|[Ss]em entrada" mentor/tutor.md` (case-robusto via classes de char; sem `-i`) — PADRAO CANONICO, identico a plano 01 e plano 04 acceptance_criteria | ✅ | ⬜ pending |
| V-04 | AVAL-03 / SC2 | Passo 1 heading reframed as mastery gate | grep | `rg -n "mastery gate\|gate de maestria\|gate de marco" mentor/fecha-marco.md` | ✅ | ⬜ pending |
| V-05 | AVAL-03 / D-06 | Gate reads `**Capacidade:**` and demands it literally | grep | `rg -n "Capacidade" mentor/fecha-marco.md` (within the gate step) | ✅ | ⬜ pending |
| V-06 | AVAL-04 / D-07 | Extension/transfer question present (1, oral, no scaffold) | grep | `rg -n "como voce mudaria\|estender\|extensao\|transferencia" mentor/fecha-marco.md` | ✅ | ⬜ pending |
| V-07 | AVAL-04 / D-08 | Blocking-formative: marco does not close on failure | grep | `rg -n "NAO .*fecha\|volte ao ciclo" mentor/fecha-marco.md` | ✅ | ⬜ pending |
| V-08 | AVAL-02 / SC3 | `## Agenda de retrieval` section in PROGRESSO template | grep | `rg -n "## Agenda de retrieval" mentor/reference.md` | ✅ | ⬜ pending |
| V-09 | AVAL-02 / D-09 | Agenda distinct from `## Dividas de aprendizado` | grep | both `rg -n "## Agenda de retrieval"` AND `rg -n "## Dividas de aprendizado"` return distinct lines in `mentor/reference.md` | ✅ | ⬜ pending |
| V-10 | AVAL-02 / SC3 | fecha-marco writes 1 entry on close (Passo 4) | grep | `rg -n "Agenda de retrieval" mentor/fecha-marco.md` | ✅ | ⬜ pending |
| V-11 | ENG-01 / SC1 | "exactly 1 next action" verifiable in tutor close + fecha checkpoint | grep | `rg -n "exatamente 1\|uma .*proxima acao\|1 proxima acao" mentor/tutor.md mentor/fecha-marco.md` | ✅ | ⬜ pending |
| V-12 | ENG-01 / D-13 | SDT named in prose + link (both files) | grep link | `rg -n "fundamentos\.md#frameworks-supporting-ancoram-um-doc" mentor/tutor.md mentor/fecha-marco.md` AND `rg -n "fundamentos\.md#sdt-relatedness-em-solo-ia"` | ✅ | ⬜ pending |
| V-13 | CONTRACT | Section name + entry format identical across the 3 files | cross-file grep | `rg -n "Agenda de retrieval" mentor/reference.md mentor/fecha-marco.md mentor/tutor.md` (all present, same literal) | ✅ | ⬜ pending |
| V-14 | ANCHOR-RESOLVE | Every `fundamentos.md#anchor` used resolves to a real heading | anchor resolve | `rg -q '^## Frameworks supporting \(ancoram um doc\)' mentor/fundamentos.md` AND `rg -q '^### SDT relatedness em solo' mentor/fundamentos.md` AND `rg -q '^## Frameworks foundational \(load-bearing\)' mentor/fundamentos.md` | ✅ | ⬜ pending |
| V-15 | CONS-01 (anti-leak) | No framework jargon inside the PROGRESSO template fenced block | grep negative | `sh scripts/extract-fenced.sh mentor/reference.md \| rg -c "SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect"` → must be 0 | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/extract-fenced.sh` — clone verbatim from Phase 2 (proven anti-leak fenced-block isolator)
- [ ] `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/check-phase4.sh` — author from the `check-phase2.sh` template, encoding the V-01..V-15 checks (check_min for presence, check_zero for anti-leak, check_has + ANCHOR-RESOLVE for headings, plus the CONTRACT cross-file equality check)
- [ ] No framework install — `rg`, `awk`, `sh` already present (proven by Phase 2 gate)

*Baseline run before edits will FAIL positive checks (expected) and PASS only the anti-leak baseline — same convention as Phase 2.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| SDT-caveat hyperlink resolves in renderer | ENG-01 / A1 | GitHub-slug of `### SDT relatedness em solo+IA` (`+` drop, spaces→hyphens) cannot be 100% confirmed by grep alone | Open the rendered `tutor.md`/`fecha-marco.md`, click the `#sdt-relatedness-em-solo-ia` link, confirm it lands on the caveat heading |

---

## Validation Sign-Off

- [ ] All checks V-01..V-15 have a static `rg` command or Wave 0 dependency
- [ ] Sampling continuity: no 3 consecutive tasks without a static verify
- [ ] Wave 0 covers the 2 script clones/authoring (extract-fenced.sh + check-phase4.sh)
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter once plans bind each check to a task

**Approval:** pending
