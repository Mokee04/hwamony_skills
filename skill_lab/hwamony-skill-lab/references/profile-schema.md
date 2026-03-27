# Profile Schema

Use this shape for `eval/profile.yaml`.

## Required Fields

- `skill_name`
- `skill_type`
- `risk_level`
- `goals`
- `failure_modes`
- `dimensions`
- `pass_thresholds`
- `pass_at_k`
- `autonomy_mode`

## Suggested Values

`skill_type`

- `artifact-producing`
- `research-heavy`
- `human-facing`
- `safety-sensitive`
- `agent-builder`
- `tool-integration`

`risk_level`

- `low`
- `medium`
- `high`

`autonomy_mode`

- `automatic`
- `guardrailed`
- `score-only`

Use:

- `automatic` for low-risk targets where direct promotion is acceptable
- `guardrailed` for medium-risk targets where the lab may promote improvements but must respect stricter regression rules
- `score-only` for high-risk targets where the lab should stop at scored recommendations without replacing the live skill

The typical run shape is:

- supervisor planning phase first
- one bounded mutation per run
- several worker shards
- evaluator judgments on each shard
- majority-over-baseline promotion

## Example

```yaml
skill_name: hwamony-prompt-architect
skill_type: agent-builder
risk_level: medium
goals:
  - design reusable prompt systems
  - choose fit-for-purpose models and tools
failure_modes:
  - vague prompt structure
  - weak tool policy
  - missing eval or rollback guidance
dimensions:
  task_success: 5
  output_structure: 5
  specificity: 4
  workflow_fitness: 4
pass_thresholds:
  task_success: 4
  output_structure: 5
  specificity: 4
  workflow_fitness: 4
pass_at_k: 3
autonomy_mode: guardrailed
```
