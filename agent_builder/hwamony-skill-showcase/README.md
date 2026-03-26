# Hwamony Skill Showcase

A GitHub discoverability and README optimization skill for turning internal skills into public-facing assets with clearer positioning, example prompts, repository metadata, and launch copy.

## 🧠 What It Does

This skill packages a local skill or skill repository for public discovery on GitHub and beyond. It sharpens the positioning, rewrites the README opening, improves search-friendly wording, writes example prompts, suggests demo assets, and prepares GitHub metadata such as repository descriptions and topics. The agent using the skill writes the copy directly from the repo evidence instead of outsourcing wording to extra copy models.

When a skill is being brought into the `hwamony` collection, this skill should also handle the obvious integration work by default: rename it into the `hwamony-` namespace, add the skill README, sync `agents/openai.yaml`, and update the category and root READMEs.

## ✨ Why It Is Different

- it focuses on public packaging, not just nicer wording
- it improves discoverability without turning the docs into keyword spam
- it identifies proof gaps and demo needs instead of polishing around missing substance
- it pushes the agent to write sharper copy directly from repo evidence
- it covers README openings, examples, metadata, and launch copy in one workflow

## 🧭 Use It When

- a skill works, but the presentation is not doing it justice
- the README explains structure but not value
- you want stronger GitHub discoverability through better README copy, repository descriptions, or topics
- you need better example prompts, demo hooks, or launch copy
- you want the agent to propose sharper phrasing variants directly

## 📦 Included Extras

- README structure guidance
- distribution checklist
- direct copywriting workflow inside the skill

## 🔎 What It Improves

- first-screen README wording that helps readers and search engines understand the skill quickly
- GitHub repository descriptions and suggested topics
- example prompts that sound like real high-value use cases
- demo hooks and proof notes that make the skill easier to trust and try

## ✍️ Example Prompts

- `Use $hwamony-skill-showcase to rewrite this skill README so GitHub visitors instantly understand what it does and why it matters.`
- `Use $hwamony-skill-showcase to make this repo more discoverable with a better description, topics, and a clearer first-screen README opening.`
- `Use $hwamony-skill-showcase to generate sharper example prompts, proof hooks, and launch copy for this skill.`
- `Use $hwamony-skill-showcase to write 3 search-friendly tagline variants for this skill and pick the strongest one.`
