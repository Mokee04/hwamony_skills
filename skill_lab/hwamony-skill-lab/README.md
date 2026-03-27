# Hwamony Skill Lab

Improve a `SKILL.md` through auditable baseline-vs-mutation runs instead of vague prompt tweaking.

`hwamony-skill-lab` helps skill authors tighten a promising but inconsistent skill with a repeatable experiment loop: a supervisor drafts one bounded mutation, the human reviews the plan before execution, workers run baseline and mutation on fixed shards, evaluators compare the outputs, and the mutation is kept only if a majority says it genuinely beat the baseline.

This is especially useful when you want more than a chat opinion. Each run leaves behind dated folders, snapshots, worker outputs, evaluator judgments, and a final decision trail you can inspect later.

## When To Use It

Use this when:

- a skill works on happy paths but breaks on ambiguity or edge cases
- you want fixed cases before touching the live `SKILL.md`
- you want a human-review gate before workers execute a plan
- you want multi-turn chat skills tested as actual conversations, not isolated one-off replies
- you want to know exactly why a mutation was kept or rejected

## What It Produces

One run gives you an `eval/` workspace beside the target skill with:

- dated run folders and skill snapshots for `baseline`, `mutation`, and optional promotion
- supervisor, worker, evaluator, and coordinator packets
- recorded baseline and mutation outputs for each shard
- preserved multi-turn conversation history for chat-oriented cases
- deterministic grades plus evaluator judgments
- final `decision.json`, `decision.md`, `summary.md`, and `history.md`

## Why It Is Different

Most skill tuning workflows collapse planning, execution, scoring, and judgment into one blurry loop.

`hwamony-skill-lab` separates those jobs on purpose:

- `supervisor`: drafts the improvement target, test plan, rubric, and one bounded mutation
- `human`: reviews the plan and can redirect the run before execution starts
- `workers`: naively execute baseline and mutation on assigned shards
- `evaluators`: compare the paired outputs and record a judgment
- `scripts`: scaffold runs, preserve artifacts, aggregate votes, and promote safely

That separation makes the run easier to trust. You can inspect the plan, the rubric, the raw worker outputs, the multi-turn history, the evaluator reasoning, and the exact backup chain used during promotion.

## How One Run Works

1. Initialize an `eval/` workspace beside the target skill.
2. Freeze the current skill into baseline and mutation snapshots.
3. Let the supervisor draft the plan, rubric, and one bounded mutation.
4. Get human feedback or approval before workers execute anything.
5. For chat skills, design cases as multi-turn conversations and preserve the full conversation history.
6. Run baseline and mutation on the same fixed shards.
7. Generate deterministic evidence from the recorded outputs.
8. Let evaluators judge whether the mutation actually improved over baseline.
9. Promote the mutation only if evaluator-majority says it won.

## Quickstart

Assume the target skill lives at `/path/to/my-skill`.

```bash
python3 scripts/init_skill_eval.py /path/to/my-skill
python3 scripts/orchestrate_skill_lab.py start /path/to/my-skill --attempts 3
```

Then:

1. Fill `eval/runs/run-YYYYMMDD-###/packets/supervisor.md`
2. Review the plan, rubric, and proposed mutation with the human before dispatching workers
3. Run baseline and mutation shards and record outputs under:
   - `outputs/baseline/...`
   - `outputs/mutation/...`
   - `outputs/transcripts/...` for multi-turn conversation history
4. Generate deterministic evidence:

```bash
python3 scripts/orchestrate_skill_lab.py review /path/to/my-skill --run-id run-YYYYMMDD-###
```

5. Let evaluators complete `judgments/*.json`
6. Finalize the run:

```bash
python3 scripts/orchestrate_skill_lab.py finalize /path/to/my-skill --run-id run-YYYYMMDD-### --summary "What changed and why"
```

## Example Prompts

Safe examples:

- `Use $hwamony-skill-lab to harden this skill with train and regression cases before we edit SKILL.md.`
- `Use $hwamony-skill-lab to draft the rubric and mutation plan first, show it to me for feedback, and only then run the loop.`
- `Use $hwamony-skill-lab to test one bounded mutation and keep it only if evaluator-majority says it beats the baseline.`

Hook examples:

- `Use $hwamony-skill-lab to turn this messy counseling skill into a real multi-turn evaluation loop with preserved agent-to-agent conversation history.`
- `Use $hwamony-skill-lab to find out whether this agent skill actually got better, or whether we just rewrote the prompt and hoped for the best.`
- `Use $hwamony-skill-lab to create a dated audit trail for this chat skill so I can inspect the plan, the transcripts, the evaluator votes, and the promotion decision.`

## What Makes It Credible

This skill is backed by a concrete script surface, not just README claims:

- `scripts/init_skill_eval.py`: scaffolds the eval workspace
- `scripts/run_skill_eval.py`: creates a dated run with snapshots and shard assignments
- `scripts/orchestrate_skill_lab.py`: generates supervisor, worker, evaluator, and coordinator packets
- `scripts/auto_grade_skill_eval.py`: turns recorded outputs into deterministic evidence
- `scripts/grade_skill_eval.py`: aggregates evaluator judgments into a keep/no-change decision
- `scripts/promote_skill_candidate.py`: promotes the winning mutation with backups
- `scripts/record_skill_patch.py` and `scripts/summarize_skill_eval.py`: keep long-run history readable

## Best Fit Demo

Starting state:
- you have a skill that feels useful, but the behavior drifts across turns or edge cases

Request:
- ask `hwamony-skill-lab` to build cases, draft one mutation, and show you the plan before any execution starts

Action:
- workers record baseline and mutation outputs on the same shards
- chat-oriented cases also preserve full multi-turn conversation history
- evaluators compare the paired runs with both deterministic evidence and qualitative judgment

Result:
- you get a clear keep/no-change decision with the underlying artifacts still intact for review

## Boundaries

- this is for improving a skill, not using a skill once
- it favors narrow, attributable mutations over broad rewrites
- deterministic checks are evidence, not the final judge of quality
- if the rubric is weak, the loop can still optimize the wrong thing
- public-facing polish does not replace real test coverage

## Credits

This skill draws directly on the baseline-first, single-mutation improvement pattern behind `$autoresearch` and Andrej Karpathy's broader `autoresearch` framing, but adapts that idea to `SKILL.md` behavior with human review, worker shards, evaluator judgments, transcript preservation, and promotion-safe backups.
