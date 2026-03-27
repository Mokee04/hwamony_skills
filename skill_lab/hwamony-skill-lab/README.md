# Hwamony Skill Lab

Improve another skill through small, auditable iterations instead of vague prompt tweaking.

`hwamony-skill-lab` wraps a target `SKILL.md` in an autoresearch-style experiment loop: a supervisor proposes one bounded mutation, naive workers execute the baseline and mutated skill on separate test shards, evaluator agents compare the paired outputs with a rubric, and the mutation is promoted only if a majority says it genuinely improved over baseline.

## Who This Is For

Use this when you already have a skill that is promising, but still inconsistent.

Good fits:

- the skill works on happy paths but breaks on ambiguity or edge cases
- you want dated runs and backups before touching the live `SKILL.md`
- you want a repeatable improvement loop, not one-off chat opinions
- you want to inspect exactly what changed, what got tested, and why a mutation was kept

## Why It Is Different

Most skill tuning workflows collapse everything into one agent doing everything at once.

`hwamony-skill-lab` splits the loop into clear roles:

- `supervisor`: proposes the improvement target, test plan, rubric, and one bounded mutation
- `workers`: naively execute baseline and mutation on assigned shards
- `evaluators`: compare baseline versus mutation outputs and record a judgment
- `scripts`: preserve snapshots, collect deterministic evidence, aggregate votes, and promote the winner safely

That means the run stays understandable after the fact. You can inspect the plan, the rubric, each worker shard, each evaluator judgment, and the exact backup chain used during promotion.

## How It Works

One run follows this loop:

1. Create a dated run folder beside the target skill.
2. Freeze the current skill as the baseline snapshot.
3. Let the supervisor define:
   - what behavior should improve
   - how the test should run
   - what rubric evaluators should use
   - what one bounded mutation to test
4. Have workers run the baseline snapshot on their own shards.
5. Apply one mutation to the mutation snapshot.
6. Have workers run the mutated snapshot on the same shards.
7. Generate deterministic evidence from the outputs.
8. Let evaluator agents compare baseline versus mutation on each shard.
9. Keep the mutation only if evaluator-majority says it improved over baseline.
10. Promote the mutated snapshot back into the live `SKILL.md` with backups and summaries.

## Quickstart

Assume the target skill lives at `/path/to/my-skill`.

```bash
python3 scripts/init_skill_eval.py /path/to/my-skill
python3 scripts/orchestrate_skill_lab.py start /path/to/my-skill --attempts 3
```

Then:

1. Fill the supervisor packet in `eval/runs/run-YYYYMMDD-###/packets/supervisor.md`
2. Run worker shards and record outputs under:
   - `outputs/baseline/...`
   - `outputs/mutation/...`
3. Generate deterministic evidence:

```bash
python3 scripts/orchestrate_skill_lab.py review /path/to/my-skill --run-id run-YYYYMMDD-###
```

4. Let evaluator agents complete `judgments/*.json`
5. Finalize the run:

```bash
python3 scripts/orchestrate_skill_lab.py finalize /path/to/my-skill --run-id run-YYYYMMDD-### --summary "What changed and why"
```

## What You Get

Every target skill gets an `eval/` workspace with:

- `profile.yaml`: evaluation profile
- `cases/train`, `cases/regression`, `cases/holdout`: fixed test cases
- `runs/run-YYYYMMDD-###/`: dated experiment folders
- `backups/`: original, mutation, and promotion snapshots
- `packets/`: supervisor, worker, evaluator, and coordinator briefs
- `outputs/`: recorded baseline and mutation executions
- `grades/`: deterministic evidence from the recorded outputs
- `judgments/`: evaluator-agent decisions per shard
- `scores.json`, `decision.json`, `decision.md`: aggregated result and rationale
- `artifact-guide.md`: human-readable explanation of what every generated file means
- `summary.md`, `results.tsv`, `history.md`: long-term experiment trail

## Example Prompts

- `Use $hwamony-skill-lab to harden this skill with train and regression cases before we edit SKILL.md.`
- `Use $hwamony-skill-lab to test one bounded mutation and keep it only if evaluator-majority says it beats the baseline.`
- `Use $hwamony-skill-lab to make this skill auditable with dated runs, backups, and judgment records.`
- `Use $hwamony-skill-lab to propose the rubric and shard plan first, then run a single autoresearch-style iteration.`

## Audit Trail

This skill is built for post-run review.

After a run, you should be able to answer:

- what the supervisor was trying to improve
- what exact mutation was tested
- which cases each worker ran
- what baseline and mutation outputs each shard produced
- what deterministic evidence existed
- how each evaluator judged the pair
- why the mutation was kept or discarded
- which snapshot replaced the live `SKILL.md`

## Boundaries

- this is for improving a skill, not using a skill once
- it favors narrow, attributable mutations over broad rewrites
- deterministic checks help, but they are not the final judge of quality
- if the rubric is weak, the loop can still optimize the wrong thing

## Credits

This skill was shaped with two explicit references:

- `$autoresearch`: for the single-mutation keep/discard loop, baseline-first mindset, and skill-optimization framing
- Andrej Karpathy's `autoresearch`: for the broader autonomous experimentation pattern of trying one bounded change, measuring it against a baseline, and only keeping verified improvements

`hwamony-skill-lab` adapts that research-loop idea to skill improvement: instead of optimizing training code, it optimizes `SKILL.md` behavior with supervisor planning, naive execution workers, evaluator-agent judgments, and promotion-safe backups.
