# Reference — Project Mentor

## Granularity rule
- Unit = **1 cohesive capability**, not 1 atom of a concept. Test: when closing the unit,
  the student can articulate ONE whole "why".
- **Verifiable closing criterion**: each unit has an objective "done" (something runs,
  renders, passes a visual check). A green check only counts if there was synthesis.
- **Size**: completable in one focused session (~30-90 min). Bigger -> split; smaller ->
  merge.
- **Smooth jump**: each unit introduces at most 1 new dominant concept and reuses the
  previous ones. No big steps.
- **Granularity ~ 1/level**: beginner -> smaller units + more scaffolding; advanced ->
  bigger units + more gap to fill.

## Vertical milestones, never themes
Don't organize by pure theme (`01-html/`, `02-css/`, `03-js/`). That recreates the
traditional course: the student learns an entire subject before knowing what it's for ->
a jump in motivation and integration. Each milestone is a **vertical slice** that crosses
several subjects but always delivers something visible and functional.

## Conditional drill (`exercises/`)
- Generate ONLY when: concept new x non-trivial x above the current level.
- **Different angle** from the application: drill = intuition of the isolated mechanism;
  application = decision/integration in the artifact. The drill must never deliver the
  application's answer.
- **Just-in-time**: at the start of the milestone that needs it, not all upfront.
- A folder per drill makes sense here (drills are isolated): `exercises/NN-<concept>/`.

## Living roadmap
At each closed milestone, re-read `PROGRESS.md` and **recalibrate the remaining milestones**
(split, merge, adjust granularity) based on how the student performed. The roadmap is a
stable spine, but the leaves adapt.

## Milestones = git, not folders (for a single artifact)
For a single artifact that grows (an app, a site), milestones are **stages** marked with
`git tag milestone-NN-<slug>`, NOT folders. `project/` has ONE set of files that evolves
milestone by milestone. Folders-per-concept exist only in `exercises/` (isolated drills).

## Student repo layout
```text
<project>/
├── PROGRESS.md           # source of truth: profile, DoD, milestones, debts, log
├── exercises/            # ISOLATED drills, generated just-in-time
│   └── NN-<concept>/      #   folder-per-concept only here
└── project/              # the SINGLE ARTIFACT; grows milestone by milestone (milestones = git tags)
```

## Template — PROGRESS.md
```markdown
# PROGRESS — <project name>

## Student profile
- Already knows: ...
- Goal: ...
- Current level: ...
- Constraints (stack/time/tools): ...

## Final output
<description of what will be built>

## Definition of Done
- [ ] <objective criterion 1>
- [ ] <objective criterion 2>

## Milestones
- [ ] 00 — <goal>   <- CURRENT
- [ ] 01 — <goal>
- [ ] 02 — <goal>

## Learning debts
- (recorded during curation; revisit when it makes sense)

## Log
- YYYY-MM-DD — milestone-00 closed: <what got done>
```

## Scaffold format (TODO human)
Each file handed to the student in `project/` gets, at the top, a comment like this
(adapt the comment syntax to the language):
```text
/*
  MILESTONE NN — <name>
  GOAL: <what will get done>
  WHY: <what capability this unlocks in the project>
  DONE: <how the student knows they finished>
  GUIDING QUESTION: <socratic question the student answers BEFORE coding>
*/
// TODO(human): <what the student should implement here>
// HINT (reveal only if they get stuck): <gradual hint, commented out>
```
NEVER fill in the `TODO(human)`. The scaffold is the skeleton; the flesh is the student's.
