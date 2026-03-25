---
name: hwamony-agent-system-evaluator
description: Evaluate and iterate AI agent or single-model systems after implementation exists. Use when the user wants test planning, run logging, rubric-based scoring, feedback collection, input-output trace storage, and looped improvement across experiments.
---

# Hwamony Agent System Evaluator

## Overview

Test the built system, store every run in artifacts, score the results with a rubric, and manage iteration.

Use this skill to:

- propose a test plan
- run evaluation cycles
- create per-run folders
- log inputs and outputs
- score quality with a rubric
- request user feedback
- loop back into another iteration when needed

## Workflow

1. Read the implementation and decision artifacts.
2. Write or update the test plan.
3. Confirm or refine the rubric.
4. Initialize a run folder.
5. Execute or simulate the test.
6. Log the input, output, and metadata.
7. Score the result.
8. Summarize weaknesses and request feedback.
9. If the user wants changes, update the iteration log and hand back to the implementer.

## Required Artifacts

Read:

- `04-decision.md`
- `05-implementation/`
- `06-test-plan.md`

Write:

- `07-runs/run-###/`
- `08-evaluation/evaluation-summary.md`
- `09-feedback/user-feedback.md`
- `09-feedback/iteration-log.md`

## Test Plan Rules

Cover:

- happy path
- edge cases
- long-history behavior
- tool failure behavior when relevant
- summary drift or history loss when relevant
- formatting or schema compliance

## Run Logging Rules

For each run, store:

- `input.md`
- `output.md`
- `metadata.yaml`
- `evaluation.md`
- `notes.md`

Use:

```bash
python3 scripts/init_experiment_run.py <project-path>
```

## Rubric Rules

Use a rubric that scores at minimum:

- task success
- correctness
- groundedness
- output compliance
- history continuity
- latency or cost notes

If the system is agentic, also score:

- tool-use correctness
- recovery behavior

## Feedback Loop

After evaluation:

- summarize what worked
- summarize what failed
- request focused user feedback
- record the next recommended change

If the user wants iteration:

- append a short entry to `iteration-log.md`
- update `HISTORY.md`
- hand back to `$hwamony-agent-system-implementer`

## Resources

Read these when needed:

- [references/testing-playbook.md](references/testing-playbook.md): test design guidance
- [references/rubric-template.md](references/rubric-template.md): rubric structure
- [references/run-logging.md](references/run-logging.md): run artifact rules
- `scripts/init_experiment_run.py`: deterministic run-folder creation
