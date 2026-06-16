---
phase: 6
slug: auditoria-de-consistencia
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-06-16
---

# Phase 6 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.
> DOC/SCRIPT-editing phase: no runtime, no test framework. **The permanent
> script `scripts/check-consistencia.sh` IS the validation mechanism** — the
> checks it encodes are the phase's automated verification and remain runnable
> forever (D-01 intent).

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | None — `sh` + `rg` + `awk` via `scripts/check-consistencia.sh` |
| **Config file** | None — script is self-contained (no `extract-fenced.sh` helper needed for Phase 6) |
| **Quick run command** | `rg -n "<padrao do criterio tocado>" mentor/<file>.md` |
| **Full suite command** | `sh scripts/check-consistencia.sh` (run from repo root) |
| **Estimated runtime** | ~2 seconds |

---

## Sampling Rate

- **After every task commit:** Run the touched criterion's `rg` one-liner (Quick run command)
- **After every plan wave / before status flip (D-04):** Run `sh scripts/check-consistencia.sh` — must be green EXCEPT V-16, which goes red→green once the IN-01 fix lands. Sequence: land script + IN-01 fix + status flip, then full suite green.
- **Before `/gsd-verify-work`:** Full suite green (V-01..V-16) + the agent's one-time CONS-02 semantic confirmation recorded in the closing report (D-03)
- **Max feedback latency:** ~2 seconds

---

## Per-Task Verification Map

| Check ID | Req / SC | Behavior | Test Type | Automated Command | File Exists | Status |
|----------|----------|----------|-----------|-------------------|-------------|--------|
| V-01..V-11 | CONS-02 / SC1 | each of the 11 anchor rows resolves in its cited doc (anti-cargo-cult) | grep | `rg -q '<anchor>' mentor/<doc>.md` (see CONS-02 map in RESEARCH) | ❌ W0 (script) — anchors PASS today | ⬜ pending |
| V-12 | CONS-03 / SC2 | all 5 canonical commands have `mentor/<cmd>.md` | existence | `for cmd in ...; do test -f mentor/$cmd.md; done` | ❌ W0 — PASS today (5/5) | ⬜ pending |
| V-13 | CONS-03 / SC2 | every repo-resident backtick path resolves (with not-in-repo SKIP list) | existence | Pattern-3 loop → `check_zero` on unresolved count | ❌ W0 — PASS today (0 unresolved) | ⬜ pending |
| V-14 | CONS-03 / SC4 | zero method jargon in adapters (`AGENTS.md`, `.claude/`) | grep negative | `rg -c "$LEAK" AGENTS.md .claude/` → 0 | ❌ W0 — PASS today (0) | ⬜ pending |
| V-15 | CONS-03 / SC3 | each of AGENTS.md/README.md/metodo.md references all 5 canonical commands, none outside set | grep | per-file allowlist intersection | ❌ W0 — PASS today | ⬜ pending |
| V-16 | IN-01 / D-07 | zero accented letters in `mentor/` (after debug.md:31-32 fix) | grep negative | `rg -c '[accented letters incl. çÇ]' mentor/` → 0 | ❌ W0 — FAIL today (2), PASS after fix | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky. "PASS today" reflects in-session verification of the criteria themselves; the SCRIPT that runs them is the Wave 0 deliverable.*

---

## Wave 0 Requirements

- [ ] `scripts/check-consistencia.sh` — the permanent harness encoding V-01..V-16 (D-01 artifact a). This is the ONLY Wave 0 build item.
- [ ] Closing audit report (`06-AUDITORIA.md` or VERIFICATION) — captures the agent's one-time semantic pass (D-03) + any D-05 escalations (none expected). Authored after the script is green.
- [ ] No test framework to install — phase has no runtime.

*(`extract-fenced.sh` is NOT a Wave 0 gap: the adapter-leak check runs whole-file, not fenced-only.)*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Each CONS-02 anchor application "makes SENSE" (not just present) | CONS-02 / D-03 | grep finds the word; it cannot judge whether the usage is the intended application | Agent reads the exact landing line(s) from the CONS-02 map (one per practice) and confirms in the closing report that the theory genuinely lands there. One-time pass. |

---

## Validation Sign-Off

- [ ] All checks have an `<automated>` command encoded in `scripts/check-consistencia.sh` (Wave 0)
- [ ] Sampling continuity: no 3 consecutive checks without automated verify (all 16 are automated; V-16 is the single one expected red→green)
- [ ] Wave 0 covers all MISSING references (the script itself)
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
