---
name: hwamony-search-skills
description: Search GitHub for agent skills that match a user's goal, surface the most relevant installable candidates, and install the selected skill directly from its GitHub repo path. Use when a user asks to find a skill for a task, browse GitHub for Codex or Claude Code skills, compare likely matches, or install a skill from a GitHub repository or skill URL.
---

# Hwamony Search Skills

## Overview

Search GitHub-first skill repositories, rank concrete `SKILL.md` candidates against the user's goal, and install the chosen skill without making the user assemble repo paths by hand.

Prefer the bundled scripts over ad-hoc GitHub browsing so the output stays reproducible and installable.

Resolve `scripts/...` relative to this skill directory before running them. Do not assume the current working directory is the skill folder.

## Routing

Choose the shortest path that satisfies the request:

1. If the user gives a GitHub tree URL, repo URL, or explicit `owner/repo` plus skill path, skip search and go straight to install.
2. If the user asks to browse, compare, or find a skill from intent, search first.
3. If the user says "find and install" and there is one clearly best candidate, recommend it briefly and install it in the same turn. Only stop to ask when the top results are genuinely ambiguous or a required install detail is missing.
4. After any successful installation, remind the user to restart Codex so the new skill is discovered.

## Workflow

1. Identify whether this is a search request, a direct install request, or a search-then-install request.
2. For search, turn the request into a focused 2-5 word query.
3. Run the search wrapper and inspect the top results for installable `SKILL.md` paths.
4. Present the strongest 3-5 candidates with repo, stars, updated date, skill path, and a one-line fit summary.
5. If the user asked to install, or if they confirm a candidate, run the install wrapper with the selected repo/path.
6. Tell the user to restart Codex after installation so the new skill is discovered.

## Query Drafting

Start with the most concrete nouns from the request: framework, tool, and task.

- Keep the query short: usually 2-5 words.
- Preserve canonical tool phrases such as `react testing`, `playwright e2e`, `figma design to code`, `postgres`, `openai docs`.
- Drop filler words like "please", "help me", "find a skill for".
- Prefer user-facing task words over internal implementation jargon.
- If the first search is weak, try up to 2 refined queries before giving up.

Useful refinements:

- narrow by framework or tool: `react testing` -> `vitest react` or `testing-library react`
- broaden slightly when zero results appear: `nextjs app router auth` -> `nextjs auth`
- rephrase into the dominant category term: `figma to code` -> `design to code`

## Search

Use the search script whenever the user starts from intent rather than a specific repo path.

Examples:

- `python3 scripts/search_github_skills.py "react testing"`
- `python3 scripts/search_github_skills.py "figma design to code" --limit 5`
- `python3 scripts/search_github_skills.py "playwright e2e" --format json`

The script searches public GitHub repositories, looks for real `SKILL.md` files, and ranks results by keyword match plus repository popularity. It works best with focused 2-5 word queries.

Because the script uses the GitHub API, request escalation when sandbox network limits block it. If a search command fails for likely sandbox/network reasons, rerun the same command with escalation instead of stopping at the first failure.

If the local Python SSL store is missing GitHub certificates, retry with `uv run --with certifi python scripts/search_github_skills.py "<query>"`.

If GitHub returns an API rate-limit error, ask for `GITHUB_TOKEN` or `GH_TOKEN` and rerun the same command with that environment variable available.

Rank and discuss results using:

- query match quality
- stars and recent maintenance
- skill path specificity
- whether the repository clearly contains installable skill directories

If the results are weak, say so plainly and either:

- run one refined query
- offer direct help without installing a skill
- offer to create a custom skill instead

## Install

Use the install wrapper when the user has selected a result or already gave a repo URL.

Examples:

- `python3 scripts/install_github_skill.py --repo vercel-labs/agent-skills --path skills/frontend-design`
- `python3 scripts/install_github_skill.py --url https://github.com/vercel-labs/agent-skills/tree/main/skills/frontend-design`

The wrapper delegates to the global GitHub installer if it exists under `${CODEX_HOME:-~/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py`.

Pass through any extra installer options the user needs, such as `--ref`, `--name`, `--dest`, or `--method`.

If HTTPS download fails because of local TLS issues, retry the installer with `--method git`.

If the destination already exists, do not overwrite it silently. Explain the conflict and offer `--name` or `--dest` if the user wants a second copy.

## Response Pattern

Keep the recommendation list brief and actionable. For each candidate, include:

- repository
- skill path
- stars
- updated date
- one-line fit summary
- install command when the user is ready

When the request is search-only, end with the strongest next action.

- If one candidate clearly stands out, say so.
- If two candidates are close, name the tradeoff in one sentence.
- If the user asked to install and the winner is clear, install it instead of making the user repeat the repo/path manually.

When the request is install-only, keep the answer shorter:

- what you installed
- which command you used
- whether it succeeded or failed
- the next recovery step if it failed
- restart Codex reminder if it succeeded

If no good candidates appear, say so plainly and offer either:

- a refined search query
- direct help without installing a skill
- creating a custom skill

## Scripts

- `scripts/search_github_skills.py`: Search GitHub repositories, discover `SKILL.md` directories, and rank installable results.
- `scripts/install_github_skill.py`: Forward install requests to the existing GitHub installer shipped with Codex.
