# Profile Schema

Use this shape for `eval/profile.yaml`.

## Required Fields

- `skill_name`
- `skill_type`
- `risk_level`
- `goals`
- `failure_modes`
- `dimensions`
- `human_review_required`
- `pass_thresholds`
- `pass_at_k`

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
human_review_required: false
pass_thresholds:
  task_success: 4
  output_structure: 5
  specificity: 4
  workflow_fitness: 4
pass_at_k: 3
```
