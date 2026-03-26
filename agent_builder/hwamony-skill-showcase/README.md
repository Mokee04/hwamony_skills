# Hwamony Skill Showcase

Turn internal skills into public-facing GitHub assets with clearer docs, examples, and launch copy.

## What It Does

This skill packages a local skill or skill repository for public discovery. It sharpens the positioning, restructures the README, writes example prompts, suggests demo assets, and prepares GitHub metadata. The agent using the skill writes the copy directly from the repo evidence instead of outsourcing wording to extra copy models.

When a skill is being brought into the `hwamony` collection, this skill should also handle the obvious integration work by default: rename it into the `hwamony-` namespace, add the skill README, sync `agents/openai.yaml`, and update the category and root READMEs.

## Why It Is Different

- it focuses on public packaging, not just nicer wording
- it identifies proof gaps and demo needs instead of polishing around missing substance
- it pushes the agent to write sharper copy directly from repo evidence
- it covers README, examples, metadata, and launch copy in one workflow

## Use It When

- a skill works, but the presentation is not doing it justice
- the README explains structure but not value
- you need better example prompts, demo hooks, or launch copy
- you want the agent to propose sharper phrasing variants directly

## Included Extras

- README structure guidance
- distribution checklist
- direct copywriting workflow inside the skill

## Example Prompts

- `Use $hwamony-skill-showcase to turn this skill into a public-facing README.`
- `Use $hwamony-skill-showcase to generate better example prompts and launch copy for this repo.`
- `Use $hwamony-skill-showcase to write 3 sharper tagline variants and pick the strongest one.`
