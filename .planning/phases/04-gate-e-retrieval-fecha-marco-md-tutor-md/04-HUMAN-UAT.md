---
status: resolved
phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md
source: [04-VERIFICATION.md]
started: 2026-06-15
updated: 2026-06-15
---

## Current Test

[resolved — link slug corrected to GitHub-valid `#sdt-relatedness-em-soloia`]

## Tests

### 1. Anchor `#sdt-relatedness-em-solo-ia` resolves to the SDT ressalva heading
expected: The link `[ressalva honesta sobre relatedness em solo+IA](fundamentos.md#sdt-relatedness-em-solo-ia)` in `tutor.md:106` and `fecha-marco.md:129` navigates to `### SDT relatedness em solo+IA` (fundamentos.md:62).
result: [passed]
note: Resolved 2026-06-15 (user chose "Fix the link slug"). The heading `### SDT relatedness em solo+IA` slugifies to `sdt-relatedness-em-soloia` under GitHub rules (the `+` is stripped, not converted to `-`). Updated both link targets (`tutor.md:106`, `fecha-marco.md:129`) from `#sdt-relatedness-em-solo-ia` to `#sdt-relatedness-em-soloia`, and updated the harness V-12-sdt-anchor grep to match. Heading and "solo+IA" terminology preserved everywhere. Harness re-run: == 0 fail(s) ==.

## Summary

total: 1
passed: 1
issues: 0
pending: 0
skipped: 0
blocked: 0

## Gaps
