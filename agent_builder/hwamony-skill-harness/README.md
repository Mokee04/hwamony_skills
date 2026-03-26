# Hwamony Skill Harness

A skill evaluation workflow for turning a promising skill into a repeatable eval loop with fixed cases, run-by-run evidence, and patch history.

## 🧠 What It Does

This skill helps you evaluate and improve another skill without relying on vague impressions. It reads the target skill, initializes a stable `eval/` workspace, drafts or refines an eval profile, creates fixed cases, records run artifacts, and feeds the failures back into concrete patches.

It is strongest when a skill feels useful but inconsistent, underspecified, or hard to improve with confidence.

## ✨ Why It Is Different

- it treats skill quality as something you can measure, not just debate
- it keeps fixed cases and run folders beside the target skill so regressions stay visible
- it records patch history so the improvement trail does not disappear into chat
- it is built to harden the skill itself, not only judge one answer

## 🧭 Use It When

- a skill works on good days but feels brittle in edge cases
- you want repeatable evidence before editing `SKILL.md`
- you need a compact eval harness for one skill or a small skill set
- you want to compare revisions against the same fixed cases
- you want feedback to turn into concrete patches instead of more opinions

## 📦 What It Produces

- `eval/profile.yaml` for the target skill
- fixed cases under `eval/cases/`
- numbered run folders with manifests, plans, results, feedback, and patch notes
- `eval/summary.md` and `eval/history.md` so improvement survives across iterations

## 🔎 Demo Scenario

Starting point:
A skill feels useful, but the team keeps editing it from intuition and cannot tell whether the latest change actually helped.

What you ask for:
`Use $hwamony-skill-harness to create fixed eval cases for this skill, run the first review loop, and show me what keeps failing.`

What you get:
A stable `eval/` workspace beside the target skill, a compact fixed case set, numbered run artifacts, and a patch trail you can rerun after every edit.

## 🚀 First Good Use Case

Use this when you already have a skill that feels promising, but you cannot yet answer:

- where it fails consistently
- whether the latest edit helped
- which regression case should block the next change

## ✍️ Example Prompts

- `Use $hwamony-skill-harness to evaluate this skill, create a compact fixed case set, and show me the biggest repeat failures before we patch anything.`
- `Use $hwamony-skill-harness to build an eval loop for this skill with profile.yaml, 3 representative cases, and run-by-run evidence I can reuse next week.`
- `Use $hwamony-skill-harness to compare the current skill against the last revision and tell me which failures are true regressions.`
- `Use $hwamony-skill-harness to turn vague feedback on this skill into a repeatable patch loop with history and rerun summaries.`
- `Use $hwamony-skill-harness to harden this promising but messy skill so we stop arguing from impressions and start improving against evidence.`

## ⚠️ Boundaries

- this is not the right tool when you only want to use a skill once
- it does not replace the target skill; it evaluates and improves it
- higher-risk or safety-sensitive targets may still need human review before broader edits
