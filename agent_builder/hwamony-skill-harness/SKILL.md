---
name: hwamony-skill-harness
description: Evaluate and improve other skills by analyzing their behavior, drafting skill-specific eval profiles, proposing test cases, running repeatable review loops, collecting user feedback, patching weak spots, and rerunning regressions. Use when a user wants to test a skill, harden a skill, compare skill revisions, or build a repeatable improvement loop for a skill library.
---

# Hwamony Skill Harness

## Overview

Operate a repeatable evaluation and improvement loop for another skill.

This is a meta skill. It does not replace the target skill. It inspects the target skill, drafts or refines an eval profile, creates representative cases, runs review loops, records evidence, proposes or applies patches, and reruns regression checks.

Prefer the bundled scripts over ad-hoc folder creation so the eval layout stays consistent.

Resolve `scripts/...` relative to this skill directory before running them. Do not assume the current working directory is the harness folder.

## Use This When

- a user wants to test whether a skill is actually good
- a user wants a repeatable improvement loop for one skill or a small skill set
- a skill feels promising but vague, brittle, or inconsistent
- a user wants to compare revisions of a skill against fixed cases
- a user wants help turning feedback into concrete `SKILL.md` improvements

## Do Not Use This When

- the user only wants to use a target skill for one task with no evaluation loop
- the target skill is missing or clearly outside this workspace
- the request is only about publishing or marketing a skill with no testing need

## Output Contract

For each harness engagement, produce or update artifacts under the target skill:

```text
<target-skill>/
  eval/
    profile.yaml
    cases/
    runs/
      run-###/
        manifest.json
        plan.md
        results.md
        feedback.md
        patch-plan.md
    summary.md
    history.md
```

Default storage policy:

- improve the target skill in place by editing its existing `SKILL.md`, references, or bundled scripts
- do not create a second "improved copy" of the skill unless the user explicitly asks for one
- keep optimization artifacts under `eval/` as local working files
- record what changed in `eval/history.md` so the patch trail survives even though the skill is edited in place

## Workflow

1. Resolve the target skill path.
2. Read the target `SKILL.md` first, then only the references and scripts needed for evaluation.
3. Classify the target skill using a small profile:
   - `artifact-producing`
   - `research-heavy`
   - `human-facing`
   - `safety-sensitive`
   - `agent-builder`
   - `tool-integration`
4. Initialize `eval/` artifacts if missing:
   - `python3 scripts/init_skill_eval.py <target-skill-path>`
5. Draft or refine `eval/profile.yaml`.
6. Create or refine a compact fixed case set in `eval/cases/`.
7. Run the target skill against the cases with minimal answer leakage.
8. Store results in a new run folder:
   - `python3 scripts/run_skill_eval.py <target-skill-path> --attempts 3`
9. Grade the results using the right mix of deterministic, model-based, and human review.
10. Summarize the main weaknesses and propose or apply a patch to the target skill.
11. Record the patch in history:
   - `python3 scripts/record_skill_patch.py <target-skill-path> --summary "<change-summary>"`
12. Rerun the same fixed cases and refresh the summary:
   - `python3 scripts/summarize_skill_eval.py <target-skill-path>`

## Profile Rules

Keep `profile.yaml` small and specific. It should define:

- skill type
- risk level
- goals
- failure modes
- scoring dimensions
- human review requirements
- pass thresholds
- default pass@k target

If the target is `human-facing` or `safety-sensitive`, require human review by default before broad edits.

Use the profile schema in [references/profile-schema.md](references/profile-schema.md).

## Case Design Rules

Build a small fixed set before widening coverage.

Always include:

- one happy-path case
- one edge or ambiguity case
- one regression case for a previously weak area

Add more only when justified by the target skill.

Each case should define:

- user input
- must-have outputs
- must-not behaviors
- grader hints

Keep cases stable across iterations unless the scope truly changes.

## Grading Rules

Use three grading lanes when appropriate:

1. Deterministic graders
   - required sections
   - file creation
   - format compliance
   - forbidden strings or patterns
2. Model-based graders
   - clarity
   - specificity
   - groundedness
   - fitness for the target workflow
3. Human review
   - safety
   - tone
   - practical usefulness
   - domain appropriateness

Prefer deterministic checks when possible. Use model grading for open-ended quality. Keep human review for safety-sensitive or high-judgment cases.

Use the patterns in [references/grading-patterns.md](references/grading-patterns.md).

## Patch Policy

Low-risk targets:

- you may patch `SKILL.md`, references, and bundled scripts directly when the improvement is clear

Higher-risk targets:

- draft the patch plan first
- summarize tradeoffs
- pause before editing when the change could alter scope, safety stance, or public-facing claims

Always record:

- what changed
- why it changed
- which run or case motivated it

Use [references/risk-modes.md](references/risk-modes.md) to decide how aggressive the edit loop should be.

## Response Pattern

When reporting back to the user, keep the sequence consistent:

1. what you analyzed
2. what profile or cases you created or changed
3. what the main failures were
4. what you patched or recommend patching
5. what improved on rerun
6. what still needs human review

## Scripts

- `scripts/init_skill_eval.py`: create a stable eval workspace beside the target skill
- `scripts/run_skill_eval.py`: create a numbered run folder and attach case manifests
- `scripts/summarize_skill_eval.py`: roll run metadata into `eval/summary.md`
- `scripts/record_skill_patch.py`: append a patch note to `eval/history.md`

## Resources

- [references/profile-schema.md](references/profile-schema.md): profile fields and example
- [references/grading-patterns.md](references/grading-patterns.md): recommended grading mixes by skill type
- [references/risk-modes.md](references/risk-modes.md): edit posture by risk level
