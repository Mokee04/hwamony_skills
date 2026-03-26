# Hwamony Search Skills

A GitHub skill discovery workflow for finding installable agent skills and bringing the best match into your toolkit.

## 🧠 What It Does

This skill searches public GitHub repositories for real `SKILL.md` paths, ranks the most relevant results, and can install the selected skill without making you manually assemble repo paths and install commands.

It now prefers pinned installs: review the candidate, then install with a commit SHA or reviewed tag instead of trusting a moving branch by default.

## ✨ Why It Is Different

- it looks for actual installable skill folders, not just related repos
- it ranks results with installability in mind, not only keyword match
- it can move from search to install in the same flow
- it is designed to reduce GitHub scavenger hunts to a short decision list
- it adds a safer default by preferring pinned refs over `main` installs

## 🎯 Best For

- users who know the job they want to solve but do not want to hunt manually through GitHub
- situations where installability matters more than vague repo relevance
- workflows where you want ranked options first and install next

## 🚫 Not Just GitHub Search

This skill is not just a nicer search query.

It is built to find actual skill folders, compare them as installable candidates, and shorten the path from “I need a skill for this” to “here is the one to try” without normalizing blind branch installs.

## 🧭 Use It When

- you want to find a skill for a framework, tool, or workflow
- you want to compare installable options before choosing one
- you already have a repo URL and want to install directly
- you want a stronger default than random GitHub browsing

## 📦 What You Get

- ranked candidates with repo, path, stars, and fit summary
- pinned install commands
- direct install support when the winner is clear

## ✍️ Example Prompts

- `Use $hwamony-search-skills to find an installable skill for React testing and give me the top 5 with repo, path, fit, and installability.`
- `Use $hwamony-search-skills to compare design-to-code skills on GitHub and tell me which one I can actually install fastest.`
- `Use $hwamony-search-skills to install a promising PostgreSQL skill from this repo URL without making me piece the path together manually.`
- `Use $hwamony-search-skills to find a skill for Figma-to-code work and rank the options by installability, stars, and likely fit.`
