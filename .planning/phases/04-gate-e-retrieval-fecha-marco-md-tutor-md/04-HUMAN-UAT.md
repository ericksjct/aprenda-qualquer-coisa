---
status: partial
phase: 04-gate-e-retrieval-fecha-marco-md-tutor-md
source: [04-VERIFICATION.md]
started: 2026-06-15
updated: 2026-06-15
---

## Current Test

[awaiting human decision — anchor slug `#sdt-relatedness-em-solo-ia`]

## Tests

### 1. Anchor `#sdt-relatedness-em-solo-ia` resolves to the SDT ressalva heading
expected: The link `[ressalva honesta sobre relatedness em solo+IA](fundamentos.md#sdt-relatedness-em-solo-ia)` in `tutor.md:106` and `fecha-marco.md:129` navigates to `### SDT relatedness em solo+IA` (fundamentos.md:62).
result: [pending]
note: Under GitHub slug rules the heading `### SDT relatedness em solo+IA` slugifies to `sdt-relatedness-em-soloia` (the `+` is stripped, not converted to `-`), so the current link target `#sdt-relatedness-em-solo-ia` does NOT match and the link is broken on GitHub. The harness check V-14 only confirms the heading exists, not that the slug matches. Recommended fix: hyphenate the heading to `### SDT relatedness em solo-IA` (keeps the link target valid and V-14's `^### SDT relatedness em solo` regex still passes).

## Summary

total: 1
passed: 0
issues: 0
pending: 1
skipped: 0
blocked: 0

## Gaps
