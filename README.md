# hwamony_skills

Reusable AI skills and agent workflows for prompt engineering, research workflows, ideation, skill improvement, and publishable GitHub docs.

This GitHub repository collects reusable `hwamony-` skills across agent building, prompt engineering, research workflows, ideation, naming, skill improvement, and careful human-facing conversations. Each skill is documented so a new visitor can inspect it quickly, understand what user job it solves, and decide whether it is worth trying.

If you only try a few first, start with the flagship skills below.

## 🔎 What Lives Here

- AI skills for agent building, prompt engineering, and system design
- research workflow skills for desk research, competitor scans, and source-backed memos
- ideation skills for problem framing, idea generation, naming, positioning, and launch copy
- skill improvement and skill showcase workflows for hardening and publishing reusable skills
- structured human-facing conversation skills with visible safety boundaries

## ⭐ Why Star This Repo

- the skills are built as reusable workflows, not random prompt snippets
- many of them produce files, folders, or handoff artifacts instead of chat-only output
- the collection covers the full loop from ideation to research to agent building to publishable docs
- each skill is documented so you can judge fit quickly instead of reading a giant monorepo blind

## 🧩 What You Can Do With It

- turn a fragile prompt into a schema-first prompt system
- turn a broad question into staged desk research with saved sources
- turn a vague problem into a shortlist of stronger solution directions
- turn a service brief into market-aware names and launch copy
- turn a promising but messy skill into fixed cases, dated runs, backups, and evidence-backed improvements
- turn a good internal skill into a public-facing README, stronger GitHub metadata, and a launch-ready showcase

## 🚀 Start Here

- [`hwamony-prompt-architect`](agent_builder/hwamony-prompt-architect/README.md)
  Design prompts as reusable systems with routing, schemas, tools, and production constraints.
- [`hwamony-desk-research`](research/hwamony-desk-research/README.md)
  Turn one-shot searching into staged desk research with saved sources and reusable artifacts.
- [`hwamony-creative-thinking`](ideation/hwamony-creative-thinking/README.md)
  Turn a fuzzy brief into core concepts, a visual map, distant-combination ideas, and a shortlist that still keeps one surprising lane alive.
- [`hwamony-skill-lab`](skill_lab/hwamony-skill-lab/README.md)
  Turn a promising skill into dated experiments, fixed cases, supervisor-planned mutations, evaluator-agent judgments, and safe promotion.
- [`hwamony-skill-showcase`](agent_builder/hwamony-skill-showcase/README.md)
  Turn an internal skill into a public-facing README, stronger discoverability signals, and launch-ready GitHub copy.

## ✨ Why This Repo Feels Different

- these are not one-shot prompt snippets; most skills define a reusable workflow
- many skills save artifacts to disk instead of leaving the work trapped in chat
- the collection spans ideation, research, agent building, and careful human-facing conversations
- several skills include scripts, references, or implementation scaffolds alongside the skill text
- the repo is organized so you can inspect one skill at a time without learning the whole system first

## 🧭 Pick A Starting Point

- If your prompt keeps breaking when the task gets real: start with [`hwamony-prompt-architect`](agent_builder/hwamony-prompt-architect/README.md)
- If your research questions are broad and you need saved evidence: start with [`hwamony-desk-research`](research/hwamony-desk-research/README.md)
- If the team is brainstorming the wrong thing: start with [`hwamony-creative-thinking`](ideation/hwamony-creative-thinking/README.md)
- If your skill is promising but you still cannot prove it is improving: start with [`hwamony-skill-lab`](skill_lab/hwamony-skill-lab/README.md)
- If you need a name and launch copy that still fits the live market: start with [`hwamony-service-naming-copy`](ideation/hwamony-service-naming-copy/README.md)
- If your skill works but still looks private or hard to discover on GitHub: start with [`hwamony-skill-showcase`](agent_builder/hwamony-skill-showcase/README.md)
- If you are building an agent from scratch: start with [`hwamony-agent-system-builder`](agent_builder/hwamony-agent-system-builder/README.md)

## ✍️ Quick Examples

- `Use $hwamony-prompt-architect to turn this messy system prompt into a production-ready prompt spec with schema, tool rules, and model guidance.`
- `Use $hwamony-desk-research to turn this vague market question into a scoped research folder with preserved sources and a final memo.`
- `Use $hwamony-creative-thinking to find the real product problem, map the concept space, and keep one contrarian option alive before we commit to the safe answer.`
- `Use $hwamony-skill-lab to turn this messy skill into fixed cases, dated runs, supervisor-planned mutations, and evaluator-backed keep/discard decisions.`
- `Use $hwamony-service-naming-copy to turn this service brief into strong naming lanes, shortlist candidates, and launch-ready copy.`
- `Use $hwamony-skill-showcase to rewrite this internal-only skill so strangers on GitHub immediately understand it and the repo metadata is ready to ship.`

## 🗂️ Full Collection

### `mind`

- [`hwamony-abc-fa`](mind/hwamony-abc-fa/README.md)
- [`hwamony-cbt-chats`](mind/hwamony-cbt-chats/README.md)

### `ideation`

- [`hwamony-creative-thinking`](ideation/hwamony-creative-thinking/README.md)
- [`hwamony-service-naming-copy`](ideation/hwamony-service-naming-copy/README.md)

### `research`

- [`hwamony-desk-research`](research/hwamony-desk-research/README.md)
- [`hwamony-debate-panel`](research/hwamony-debate-panel/README.md)

### `agent_builder`

- [`hwamony-agent-system-builder`](agent_builder/hwamony-agent-system-builder/README.md)
- [`hwamony-agent-system-evaluator`](agent_builder/hwamony-agent-system-evaluator/README.md)
- [`hwamony-agent-system-implementer`](agent_builder/hwamony-agent-system-implementer/README.md)
- [`hwamony-prompt-architect`](agent_builder/hwamony-prompt-architect/README.md)
- [`hwamony-search-skills`](agent_builder/hwamony-search-skills/README.md)
- [`hwamony-skill-showcase`](agent_builder/hwamony-skill-showcase/README.md)

### `skill_lab`

- [`hwamony-skill-lab`](skill_lab/hwamony-skill-lab/README.md)

This category now owns skill-improvement loops that used to be described more loosely as harness workflows. If the job is "make this skill reliably better over time," start here rather than in `agent_builder`.

## 📝 Repo Notes

- `hwamony-convergent-thinking` and `hwamony-divergent-thinking` are intentionally excluded.
- skills are shared here without local `.env`, `.DS_Store`, or `autoresearch-*` artifacts
- original code and prose use different licenses; see below

## ⚖️ Copyright and Licensing

Copyright (c) 2026 Hwamony.

This repository uses a split license model:

- original code inside `scripts/` directories is licensed under the MIT License
- original `SKILL.md`, `README.md`, and other prose documentation are licensed under `CC BY 4.0`

See:

- `LICENSE`
- `LICENSES/MIT.txt`
- `LICENSES/CC-BY-4.0.md`

## 📎 Notes
- each skill is meant to be inspectable on its own via its local `README.md`
- category READMEs give a faster entry point if you want to browse by workflow instead of by file tree

## 🙏 Attribution

If you reuse the skill text or documentation, please provide clear attribution to `Hwamony` and note any changes you made.
