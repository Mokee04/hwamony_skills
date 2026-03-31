# Agent Builder Skills

Turn a fuzzy AI idea into a designed system, working implementation, repeatable evaluation, and a publishable asset.

This category is strongest when the work stops being “just write me a prompt” and turns into AI agent architecture, prompt engineering, tooling, evaluation, or reusable system design. It gives you a path from messy requirements to build-ready artifacts and public-facing documentation without treating those as disconnected tasks.

`skill` improvement infrastructure now lives in the sibling [`skill_lab`](../skill_lab/README.md) category. `agent_builder` is for building, implementing, evaluating, extending, and showcasing agent systems themselves.

## 🚀 Start Here

Copy one of these prompts:

- `Use $hwamony-requirements-clarifier to figure out what I actually need from this vague project request before we plan anything.`
- `Use $hwamony-agent-system-builder to compare 3 architectures for this support copilot and tell me which one is easiest to ship first.`
- `Use $hwamony-prompt-architect to turn this fragile prompt into a schema-first prompt system with tool and failure rules.`
- `Use $hwamony-agent-system-evaluator to create a rubric and run log format for this agent before we iterate again.`
- `Use $hwamony-skill-showcase to rewrite this internal skill so GitHub visitors instantly understand it and search-friendly metadata is ready to ship.`

## 🧭 Best Starting Points

- building a new agent or assistant from requirements
- deciding whether a task should stay single-prompt or become a workflow
- implementing provider-aware runtime code after the architecture is chosen
- evaluating whether a built system is actually getting better
- packaging a good internal skill so other people can understand and reuse it
- finding external skills that can extend your toolkit

## ✨ Why This Category Is Different

- it covers the full loop from ambiguity to implementation to evaluation to public packaging
- it treats prompts, architecture, and history strategy as system decisions rather than isolated wording tasks
- it includes both build-side skills and publish-side skills, so strong internal work does not stay trapped inside the repo
- it gives visitors a readable path instead of a flat pile of AI engineering folders

## 🧰 Included Skills

### `hwamony-agent-system-builder`

[Open skill README](hwamony-agent-system-builder/README.md)

Designs an AI agent or single-model system from requirements through decision-making.

Use this when you want to:

- clarify requirements
- write a task brief
- compare architecture options
- define message-history strategy
- prepare a clean implementation handoff

### `hwamony-requirements-clarifier`

[Open skill file](hwamony-requirements-clarifier/SKILL.md)

Clarifies ambiguous user requests into actionable briefs through focused questions, proposed interpretations, and working-brief summaries.

Use this when you want to:

- turn a vague ask into a concrete deliverable
- uncover hidden assumptions and non-goals
- ask better clarification questions instead of broad questionnaires
- identify what the user really wants before planning or implementation

### `hwamony-agent-system-implementer`

[Open skill README](hwamony-agent-system-implementer/README.md)

Implements the selected system architecture.

Use this when you want help creating:

- prompts
- configs
- runtime code
- history adapters
- provider-aware implementation structure

### `hwamony-agent-system-evaluator`

[Open skill README](hwamony-agent-system-evaluator/README.md)

Evaluates and iterates on a built system.

Use this when you want:

- test planning
- run logging
- rubric-based scoring
- evaluation summaries
- a tighter feedback loop for the next iteration

### `hwamony-prompt-architect`

[Open skill README](hwamony-prompt-architect/README.md)

Designs prompts as reusable systems with routing, schemas, tools, and production constraints.

Use this when you need:

- a new prompt
- a prompt critique
- model or vendor routing guidance
- tool-aware prompt design
- a production-minded prompt system rather than a one-off string

### `hwamony-search-skills`

[Open skill README](hwamony-search-skills/README.md)

Searches GitHub for relevant agent skills and helps install the best match.

Use this when you want to:

- browse existing skills
- compare installable options
- find a skill for a specific framework or workflow
- install a promising skill from GitHub

### `hwamony-skill-showcase`

[Open skill README](hwamony-skill-showcase/README.md)

Transforms internal skills into public-facing showcases with SEO-friendly README copy, sharper examples, repository metadata, and launch-ready copy.

Use this when you want to:

- rewrite a README for humans instead of internal use only
- improve GitHub discoverability with clearer descriptions, topics, and first-screen wording
- clarify who the skill is for and when to use it
- generate example prompts and demo ideas
- prepare GitHub descriptions, topics, or launch copy
- turn a private-looking skill into a showcase-ready open source asset

## ✨ What This Category Is Good At

- turning fuzzy AI ideas into structured projects
- turning ambiguous asks into actionable briefs before the project starts
- reducing architecture guesswork
- building reusable systems instead of one-off experiments
- connecting design, implementation, and evaluation into one loop
- evaluating agent systems and hardening prompt systems
- helping strong internal skills look legible and valuable from the outside
- deciding when to stay inside `agent_builder` versus when to move into `skill_lab` for skill-level improvement loops

## 🎯 Good Fit

- AI engineers
- prompt engineers
- tool builders
- workflow designers
- teams building internal assistants or production agents

## 🧭 Suggested Reading Order

If you are new to this folder, a simple path is:

1. start with `hwamony-requirements-clarifier` when the ask is still fuzzy
2. move to `hwamony-agent-system-builder` once the brief is actionable
3. move to `hwamony-agent-system-implementer`
4. use `hwamony-agent-system-evaluator` after implementation exists
5. use the `skill_lab` category when you want to evaluate and improve the skills themselves

Use `hwamony-prompt-architect` whenever prompt design becomes central, `hwamony-search-skills` when you want to extend your toolkit with external skills, and `hwamony-skill-showcase` when the work shifts from building the skill to publishing it well.

## ⚖️ License Note

- `SKILL.md` and this README are shared under `CC BY 4.0`
- any original code inside nested `scripts/` directories is shared under the MIT License

See the repository root `LICENSE` files for details.
