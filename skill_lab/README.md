# Skill Lab Skills

Turn a promising skill into something you can test, inspect, and improve with evidence.

This category is for skill hardening rather than agent architecture. It is the right place when the core job is not "design a new system" but "make an existing skill reliably better over time." The focus is on bounded mutations, fixed cases, preserved artifacts, and promotion rules that make improvement easier to trust.

## 🚀 Start Here

Copy one of these prompts:

- `Use $hwamony-skill-lab to harden this skill with train and regression cases before we edit SKILL.md.`
- `Use $hwamony-skill-lab to draft the rubric and mutation plan first, show it to me for feedback, and only then run the loop.`
- `Use $hwamony-skill-lab to find out whether this skill actually got better, or whether we just rewrote the prompt and hoped for the best.`

## ✨ Why This Category Is Different

- it treats skill improvement as an auditable experiment loop, not a vibes-based rewrite
- it preserves the baseline, the mutation, the rubric, and the judgment trail
- it works for multi-turn chat skills as well as one-shot instruction skills
- it gives you a promotion-safe path instead of editing the live skill blind

## Included Skills

### `hwamony-skill-lab`

[Open skill README](hwamony-skill-lab/README.md)

Runs a deterministic improvement lab around a target skill with dated runs, fixed cases, backups, grading, and promotion.

Use this when you want to:

- create fixed train and regression cases
- compare bounded candidate edits against a baseline
- preserve original and intermediate `SKILL.md` snapshots
- promote only the winner back into the live skill
- inspect the full artifact trail after the run

## 🎯 Best Fit

- skill authors who want evidence before changing a live skill
- repos with a promising workflow but unreliable edge-case behavior
- chat-oriented skills that need multi-turn evaluation, not just one-off spot checks
- anyone who wants a cleaner keep/no-change decision trail

## ⚖️ License Note

- `SKILL.md` and this README are shared under `CC BY 4.0`
- any original code inside nested `scripts/` directories is shared under the MIT License

See the repository root `LICENSE` files for details.
