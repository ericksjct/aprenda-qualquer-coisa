---
name: new-project
description: Bootstrap of a learning project. Use when the student arrives with a demand or project they want to learn to build. Runs a diagnosis, generates a milestone roadmap (PROGRESS.md) and, after approval, sets up the repo skeleton and the scaffold of the first milestone.
---

# Learning Project Bootstrap

Turns the student's demand into a structured learning project.
Also read `reference.md` (in this folder) for: the granularity rule, the `PROGRESS.md`
template, the repo layout, and the scaffold format.

## Step 1 — Diagnosis (in chat, read-only)
From the student's demand (text in chat and/or a reference file they attach):
- Gather: desired final output, quality bar, profile (what they already know, goal,
  current level), constraints (stack, time per session, tools).
- Ask **at most 2 questions** if something essential is missing. Don't assume the level.
- **Don't create any files yet.**

## Step 2 — Roadmap (the spine)
- Reverse-engineer the final output -> required capabilities -> order by dependency.
- Slice into **vertical milestones (MVPs)**: each milestone delivers something that
  runs/renders. Do NOT slice by theme.
- Apply the granularity rule from `reference.md`.
- Translate the quality bar into a **Definition of Done** with objective criteria,
  distributed across the milestones (aesthetics, polish, responsiveness get their own
  milestone).

## Step 3 — Approval (mandatory checkpoint)
- Present to the student: diagnosis + DoD + milestone tree (1 line of goal each).
- **Ask for approval before creating any file.** Adjust based on feedback.

## Step 4 — Skeleton (only after approval)
Create in the project folder:
- `PROGRESS.md` (use the template from `reference.md`): profile, goal, DoD, milestone
  tree, current milestone = 00.
- `exercises/` (empty for now).
- `project/` (empty, or with the minimal root files of the single artifact).
- `git init` if there's no repo yet.

## Step 5 — Scaffold of Milestone 00 (that one only)
- Generate the scaffold of the first milestone in `project/` in the format of
  `reference.md`: `TODO(human)` + guiding question.
- If the drill rule fires, generate the drill in `exercises/`.
- Remind the student to activate the persona: `/output-style mentor-project`.
- **Stop and wait for the student's attempt.** The following milestones are generated
  on-the-go, under the conduct of the `mentor-project` output style.
