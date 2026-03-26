# Grading Patterns

Pick the lightest grading mix that still captures the target skill's real failure modes.

## Artifact-Producing

Use:

- deterministic checks for required sections, headings, or files
- model grading for clarity and reusability

Common dimensions:

- task success
- output structure
- specificity
- handoff quality

## Research-Heavy

Use:

- deterministic checks for source listing and citation shape when relevant
- model grading for scope discipline, synthesis quality, and groundedness
- human review for source judgment if the task is high stakes

Common dimensions:

- groundedness
- scoping quality
- evidence preservation
- synthesis usefulness

## Human-Facing

Use:

- deterministic checks for required boundaries or escalation language
- model grading for warmth, clarity, and scope discipline
- human review by default

Common dimensions:

- safety posture
- tone
- practical usefulness
- overclaim avoidance

## Agent-Builder

Use:

- deterministic checks for required artifacts and sections
- model grading for architecture quality, evaluation readiness, and implementation handoff

Common dimensions:

- task success
- structure
- technical specificity
- evaluation readiness

## Minimal Default Grader Stack

For a new target skill with no prior history:

1. deterministic required-output checks
2. model grader on 3-5 dimensions
3. human review only when the profile flags it
