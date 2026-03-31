# Hwamony Requirements Clarifier

Turn vague, high-context requests into actionable briefs before planning, prompting, or implementation begins.

This skill helps an agent figure out what the user actually wants when the request is still fuzzy. It narrows ambiguity through focused questions, proposed interpretations, light pushback, and compact working-brief summaries so the next step becomes obvious instead of guessed.

## 🚀 Start Here

- `Use $hwamony-requirements-clarifier to turn this vague request for an internal AI tool into a concrete brief before we plan anything.`
- `Use $hwamony-requirements-clarifier to figure out what I actually mean by "something like a research copilot" and what the deliverable should be.`
- `Use $hwamony-requirements-clarifier to ask the smallest set of questions needed to make this project request actionable.`

## ✨ Why It Is Different

- it does not dump a long intake questionnaire on the user
- it proposes likely interpretations instead of making the user structure everything alone
- it uses binary forks, constrained options, anti-goals, and tradeoff probes to get to clarity faster
- it knows when to stop clarifying and hand off once the brief is actionable

## 🧭 Use It When

- a user request is too broad to plan confidently
- the user is mixing multiple goals into one ask
- you need to clarify audience, deliverable, or success criteria before moving forward
- you want to avoid building the right thing for the wrong problem

## 📦 What You Get

- a one-line current read of the request
- the highest-value ambiguity called out explicitly
- 1-3 focused clarification questions or option forks
- a provisional working brief with goal, deliverable, constraints, and open questions
- a cleaner handoff into `hwamony-agent-system-builder`, `hwamony-prompt-architect`, or another downstream skill

## 🧠 Best Fit

- high-context requests where key assumptions are still implicit
- users who know the problem vaguely but not yet the deliverable
- early conversations where the wrong interpretation would waste planning or build time

## ⚠️ Boundary

This skill is strongest when the job is convergence, not open-ended brainstorming. If the user already gave a clear goal, deliverable, and constraints, move into planning or implementation instead of forcing more clarification.
