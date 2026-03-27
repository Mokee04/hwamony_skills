# Grading Patterns

Pick the lightest grading mix that still captures the target skill's real failure modes.

Use deterministic checks wherever possible, but treat them as evidence rather than the whole judgment. This lab expects evaluator agents to make the final shard-level comparison against the supervisor's rubric.

## Core Shape

- let the supervisor define the test shape and rubric first
- measure a baseline snapshot first
- apply one bounded mutation to a separate mutation snapshot
- let worker shards run both versions on different fixed input slices
- generate deterministic evidence for each shard
- let evaluator agents compare each shard pair against the same rubric
- decide by majority evaluator judgment over baseline

## Artifact-Producing

Use:

- deterministic checks for required sections, headings, files, or formatting
- deterministic checks for explicit clarity or handoff requirements when they can be phrased concretely

Common dimensions:

- task success
- output structure
- specificity
- handoff quality

## Research-Heavy

Use:

- deterministic checks for source listing and citation shape when relevant
- deterministic checks for scope boundaries, evidence preservation, and citation shape

Common dimensions:

- groundedness
- scoping quality
- evidence preservation
- synthesis usefulness

## Human-Facing

Use:

- deterministic checks for required boundaries or escalation language
- deterministic checks for scope boundaries, escalation language, and required disclaimers

Common dimensions:

- safety posture
- tone
- practical usefulness
- overclaim avoidance

## Agent-Builder

Use:

- deterministic checks for required artifacts, sections, or lifecycle guidance
- deterministic checks for architecture artifacts, lifecycle guidance, and implementation handoff requirements

Common dimensions:

- task success
- structure
- technical specificity
- evaluation readiness

## Minimal Default Grader Stack

For a new target skill with no prior history:

1. deterministic required-output checks
2. deterministic case-level must-have and must-not checks
3. deterministic regression blocking

## Supervisor-Worker-Evaluator Notes

- have the supervisor define the rubric before the mutation is run
- grade the baseline and mutation on the same shard for each worker
- do not let a worker rewrite the rubric after seeing failures
- let workers execute; do not let them judge
- let evaluators judge; do not let them rewrite the mutation
- keep each iteration to one mutation so attribution remains clear
