# Hwamony Prompt Architect

Design prompts as schema-first, tool-aware systems, not one-off strings that break the moment the task gets real.

## What It Does

Use this skill when you need a new system prompt, a prompt refactor, or a decision on whether a task should stay single-prompt or become an agent workflow. It covers model routing, tool-aware and schema-first design, and production prompt systems with caching, evals, versioning, and rollback.

## Why It Is Different

- it treats prompts as systems with routing, schemas, tools, and lifecycle decisions
- it decides when a task should stop being a prompt and become a workflow
- it bakes in freshness checks and Context7 use for unstable technical guidance
- it is built for reusable production prompts, not just clever wording

## Best For

- teams shipping assistants, copilots, or prompt-heavy tools
- users who need output schemas, tool rules, and failure handling
- moments when prompt quality now affects reliability, not just style

## Not Just

- not just “make this prompt better”
- not just “pick a model for me”
- not just “rewrite the wording”

This skill is strongest when the real problem is system design around the prompt: routing, output shape, tool use, guardrails, and what should happen when the prompt alone stops being enough.

## Use It When

- you need a new system prompt or developer prompt
- you want to refactor an existing prompt into something more reliable
- you need help choosing between a single prompt and an agent workflow
- you want schemas, tool rules, caching, evals, or rollback thinking built in

## What It Covers

- new prompt design
- prompt critique and rewrite
- production prompt systems
- cross-vendor model selection
- source-grounded and tool-aware prompt design

## Example Prompts

- `Use $hwamony-prompt-architect to turn this fragile support prompt into a schema-first prompt system with tool rules, failure handling, and eval hooks.`
- `Use $hwamony-prompt-architect to refactor this messy research prompt into a reusable system prompt with clear output schema and citation rules.`
- `Use $hwamony-prompt-architect to decide whether this workflow should stay single-prompt or become an agent workflow with memory and tools.`
- `Use $hwamony-prompt-architect to compare what should live in the system prompt, tool contract, and downstream evaluator for this task.`
