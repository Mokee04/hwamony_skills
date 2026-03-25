---
name: hwamony-agent-system-builder
description: Design AI agent systems or single-model systems from requirements through implementation planning and evaluation planning. Use when the user wants to gather requirements, write a task brief, compare 3 architecture options, define vendor and message-history strategy, initialize a project folder, and coordinate handoff to implementation and evaluation.
---

# Hwamony Agent System Builder

## Overview

Orchestrate the full design loop for an AI agent or single-model system.

Use this skill to:

- clarify requirements
- write a task brief
- propose 3 architecture candidates
- define vendor, framework, and message-history strategy
- initialize a project workspace
- hand off cleanly to implementation and evaluation

Apply the model-routing and prompt-quality rules from `$hwamony-prompt-architect` whenever prompt design or vendor choice becomes central.

## Workflow

Follow this sequence unless the user explicitly asks to jump ahead.

1. Clarify the requirements.
2. Initialize the project folder.
3. Write the requirements artifact.
4. Write the task brief.
5. Propose 3 architecture candidates.
6. Define the message-history strategy.
7. Record the decision.
8. Hand off to `$hwamony-agent-system-implementer` or `$hwamony-agent-system-evaluator`.

## Step 1: Clarify Requirements

Ask only the highest-value questions first.

Cover these variables when relevant:

- user goal
- target users
- single model vs agent system preference
- required tools
- freshness requirements
- latency and cost sensitivity
- safety or compliance constraints
- preferred vendor or framework
- deployment context
- evaluation criteria

If the user already gave enough context, summarize it instead of re-asking.

## Step 2: Initialize The Project Folder

Create the project folder as early as possible so every later phase has a stable artifact home.

Default root:

```text
agent-system-projects/<project-slug>/
```

Use:

```bash
python3 scripts/init_agent_project.py <project-slug> --base-path <parent-dir>
```

If the user does not specify a location, default to the current working directory.

## Step 3: Write `01-requirements.md`

Capture:

- the problem to solve
- the desired user experience
- required inputs and outputs
- constraints
- open questions
- explicit non-goals

Keep this file factual and user-centered.

## Step 4: Write `02-task-brief.md`

Translate the requirements into an execution brief.

Include:

- objective
- success criteria
- target architecture style
- tool expectations
- output contract
- evaluation dimensions
- first implementation recommendation

## Step 5: Write `03-architecture-options.md`

Propose 3 materially different candidates.

Each candidate must include:

1. a title
2. a short description
3. whether it is single-model or agentic
4. vendor and model recommendation
5. framework choice
6. message-history approach
7. strengths
8. weaknesses
9. main implementation risk

Good default candidate mix:

- Candidate A: direct single-model system
- Candidate B: lightweight tool-using agent
- Candidate C: multi-stage or multi-agent system

## Step 6: Define Message-History Strategy

Treat history as a first-class architecture decision, not an implementation afterthought.

Always decide:

- canonical history schema
- source of truth
- vendor adapter shape
- replay policy
- summary policy
- tool-result retention policy
- cache policy

Write the result into:

- `03-architecture-options.md`
- `04-decision.md`

Use the guidance in [references/history-strategy.md](references/history-strategy.md).

## Step 7: Write `04-decision.md`

Once the user chooses a direction, record:

- chosen architecture
- chosen vendor and model
- chosen framework
- chosen history strategy
- chosen evaluation plan
- unresolved risks
- next action

Do not start implementation until the stack choice is explicit enough.

## Handoffs

Hand off to `$hwamony-agent-system-implementer` when:

- the brief is written
- the architecture is chosen
- the stack is clear enough to code

Hand off to `$hwamony-agent-system-evaluator` when:

- the implementation artifacts exist
- the user wants testing, logging, rubric scoring, or iteration

## Artifact Rules

Keep the project state in files, not only in chat.

After each major phase:

- update the relevant artifact
- add the next recommended action
- list unresolved questions

Treat the project folder as the canonical working memory for the system.

## Resources

Read these when needed:

- [references/workflow.md](references/workflow.md): end-to-end stage guidance
- [references/artifact-spec.md](references/artifact-spec.md): project file map and artifact rules
- [references/history-strategy.md](references/history-strategy.md): canonical history design and vendor-specific considerations
- `scripts/init_agent_project.py`: deterministic project scaffold creation
