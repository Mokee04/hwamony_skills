# Builder Workflow

## Stage Map

### Stage 1: Discovery

Capture:

- the user's real goal
- operating environment
- constraints
- success criteria

Output:

- `01-requirements.md`

### Stage 2: Brief

Turn requirements into an execution brief.

Output:

- `02-task-brief.md`

### Stage 3: Architecture Options

Write 3 candidates with real tradeoffs.

Recommended candidate pattern:

1. direct single-model
2. lightweight agent with tools
3. multi-stage or multi-agent workflow

Output:

- `03-architecture-options.md`

### Stage 4: History Strategy

Choose:

- canonical transcript schema
- replay mode
- summary policy
- vendor adapter strategy
- cache policy

Output:

- update `03-architecture-options.md`
- record final choice in `04-decision.md`

### Stage 5: Implementation Handoff

Confirm:

- vendor
- framework
- model
- history strategy

Then hand off to `$hwamony-agent-system-implementer`.

### Stage 6: Evaluation Handoff

Once implementation exists, hand off to `$hwamony-agent-system-evaluator`.

## Decision Rules

- Prefer a single-model system first when the task is bounded.
- Prefer an agent system when planning, tools, and verification are all central.
- Treat message-history design as part of architecture, not a later code detail.
- Keep project memory in files so future turns can reconstruct state quickly.
