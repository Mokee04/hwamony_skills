---
name: hwamony-skill-lab
description: Improve another skill through supervisor-planned single-mutation iterations, naive execution workers, evaluator-agent judgments, dated run folders, backups, and majority-over-baseline keep/discard decisions.
---

# Hwamony Skill Lab

## Overview

Operate a lightweight skill experiment lab for another skill.

This skill creates a fixed evaluation loop around a target skill. A supervisor first proposes what to improve, how to test it, and how to score it. Then naive workers execute baseline and mutation on separate shards, evaluator agents compare the paired outputs against the rubric, and the mutation is kept only when a majority of evaluator judgments say it improved over baseline.

`Harness` is an accurate internal term, but `skill lab` is the better user-facing name here because the work is broader than wiring or scaffolding. It includes case design, experiment planning, scoring, promotion, and post-run review.

Use `scripts/orchestrate_skill_lab.py` as the interactive orchestration layer on top of the core run/review/finalize scripts.

Resolve `scripts/...` relative to this skill directory before running them. Do not assume the current working directory is the lab folder.

Use the local config files to avoid hardcoded assumptions:

- `config/roles.json`
- `config/lifecycle.json`
- `config/artifact-schema.json`

## Use This When

- a skill feels useful but inconsistent
- you want fixed cases before changing `SKILL.md`
- you want dated runs, backups, and a clear audit trail
- you want deterministic improvement loops instead of subjective chat-only opinions
- you want the improved `SKILL.md` to replace the original only after one bounded mutation earns promotion

## Do Not Use This When

- the user only wants to run a skill once
- the target skill is missing or outside the local workspace
- the work depends mainly on manual taste-based review
- the request is about marketing or publishing a skill rather than improving its behavior

## Output Contract

For each engagement, produce or update artifacts under the target skill:

```text
<target-skill>/
  eval/
    backups/
      run-YYYYMMDD-###/
        original/
          SKILL.md
        mutation/
          SKILL.md
        promotion/
    profile.yaml
    cases/
      train/
      regression/
      holdout/
    runs/
      run-YYYYMMDD-###/
        manifest.json
        plan.md
        plan.json
        rubric.json
        baseline.json
        mutation.json
        assignments.json
        packets/
          supervisor.md
          worker-a.md
          worker-b.md
          worker-c.md
          evaluator-worker-a.md
          evaluator-worker-b.md
          evaluator-worker-c.md
        outputs/
          baseline/
            worker-a/
            worker-b/
            worker-c/
          mutation/
            worker-a/
            worker-b/
            worker-c/
        grades/
          worker-a.json
          worker-b.json
          worker-c.json
        judgments/
          worker-a.json
          worker-b.json
          worker-c.json
        scores.json
        decision.md
        decision.json
        artifact-guide.md
        feedback.md
        patch-plan.md
    results.tsv
    summary.md
    history.md
```

## Core Rules

- measure the baseline before keeping any change
- use exactly one bounded mutation per run
- let the supervisor define the run before anyone executes it
- keep workers naive and execution-only
- let evaluator agents make the actual improvement judgments
- keep the rubric fixed during a run
- use deterministic checks as evidence, not as the only judge of quality
- replace the live `SKILL.md` only through explicit promotion

## Workflow

1. Resolve the target skill path.
2. Read the target `SKILL.md` and only the references needed for evaluation.
3. Initialize `eval/` if missing:
   - `python3 scripts/init_skill_eval.py <target-skill-path>`
4. Draft or refine `eval/profile.yaml`.
5. Build compact `train/`, `regression/`, and optional `holdout/` cases.
6. Create a dated run folder:
   - `python3 scripts/run_skill_eval.py <target-skill-path> --attempts 3`
   - or `python3 scripts/orchestrate_skill_lab.py start <target-skill-path> --attempts 3`
7. Let the supervisor fill in the planning phase:
   - what behavior should improve
   - how the test should be run
   - what rubric the evaluators should use
   - what one bounded mutation is being tested
8. Measure the current baseline. Workers A/B/C each run the unmodified baseline snapshot on their own shard of inputs and record outputs in `outputs/baseline/worker-*/`.
9. Apply exactly one bounded mutation to the mutation snapshot.
10. Rerun the same worker shards on the mutated snapshot and record outputs in `outputs/mutation/worker-*/`.
11. Generate deterministic evidence:
   - `python3 scripts/auto_grade_skill_eval.py <target-skill-path> --run-id <run-id>`
12. Let evaluator agents read the rubric, the paired baseline/mutation outputs, and the deterministic evidence, then write `judgments/*.json`.
13. Aggregate the evaluator judgments into the final decision:
   - `python3 scripts/grade_skill_eval.py <target-skill-path> --run-id <run-id>`
14. Promote the mutated snapshot if evaluator judgments give it the majority:
   - `python3 scripts/promote_skill_candidate.py <target-skill-path> --run-id <run-id>`
15. Record the patch and refresh the run summary:
   - `python3 scripts/record_skill_patch.py <target-skill-path> --summary "<change-summary>"`
   - `python3 scripts/summarize_skill_eval.py <target-skill-path>`
   - or `python3 scripts/orchestrate_skill_lab.py finalize <target-skill-path> --run-id <run-id> --summary "<change-summary>"`

## Case Rules

Always include:

- one happy-path case in `train/`
- one edge or ambiguity case in `train/`
- one regression case in `regression/`

Prefer deterministic case bullets:

- `literal:...` for substring requirements
- `regex:...` for pattern requirements

Each case should define:

- user input
- must-have outputs
- must-not behaviors
- grader hints

Do not weaken cases just because a mutation failed them.

## Mutation Rules

Each iteration should test one small and traceable mutation.

Good mutations:

- add one specific instruction
- reword one ambiguous instruction
- add one anti-pattern
- improve one example
- remove one confusing rule
- move one buried instruction higher

Bad mutations:

- rewriting the entire skill
- changing many instructions at once
- loosening the rubric or cases to rescue a mutation
- broad tone rewrites with no clear failure evidence

## Worker Rules

Workers are not judges and they are not mutation authors.

Each worker:

- receives one fixed shard of test inputs
- runs the baseline snapshot on that shard
- runs the mutated snapshot on the same shard
- records outputs only
- does not decide whether the mutation should be kept

## Evaluator Rules

Evaluators are not workers and they are not mutation authors.

Each evaluator:

- reads the supervisor's plan and rubric
- compares one worker shard's baseline and mutation outputs
- uses deterministic evidence as support, not as a substitute for judgment
- records one verdict in `judgments/<worker>.json`

Allowed verdicts:

- `mutation_better`
- `baseline_better`
- `tie`
- `incomplete`

## Audit Trail

Every run should make it easy to answer:

- what was the plan
- what cases and rubric were used
- what mutation was tested
- what each worker executed
- what each baseline and mutated output looked like
- what deterministic evidence was generated for each shard
- what each evaluator judged and why
- why the mutation was or was not promoted

Use both:

- human-readable `.md` notes
- machine-readable `.json` records

## Scripts

- `scripts/init_skill_eval.py`: initialize the eval workspace
- `scripts/run_skill_eval.py`: create a dated run folder, baseline and mutation snapshots, shard assignments, and output placeholders
- `scripts/orchestrate_skill_lab.py`: create supervisor, worker, and evaluator briefing packets for one mutation iteration and close the run after judgments are filled
- `scripts/auto_grade_skill_eval.py`: generate deterministic evidence from baseline and mutation outputs shard by shard and write `grades/*.json`
- `scripts/grade_skill_eval.py`: tally evaluator judgments and write the final keep/discard decision
- `scripts/promote_skill_candidate.py`: replace the live `SKILL.md` with the mutated snapshot while preserving backups
- `scripts/record_skill_patch.py`: append the patch note to `eval/history.md`
- `scripts/summarize_skill_eval.py`: refresh `eval/summary.md`, `results.tsv`, and `artifact-guide.md`
