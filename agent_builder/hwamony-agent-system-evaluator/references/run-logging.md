# Run Logging

## Folder Shape

Each run should live in:

```text
07-runs/run-###
```

Minimum files:

- `input.md`
- `output.md`
- `metadata.yaml`
- `evaluation.md`
- `notes.md`

## What To Record

`input.md`

- user input
- relevant system state

`output.md`

- raw model or system output

`metadata.yaml`

- timestamp
- model
- vendor
- framework
- history policy
- run purpose

`evaluation.md`

- rubric scores
- pass or fail result

`notes.md`

- qualitative observations
- unexpected behavior
- next improvement

## Logging Rules

- keep raw output intact
- keep evaluation separate from output
- keep run numbering stable and monotonic
