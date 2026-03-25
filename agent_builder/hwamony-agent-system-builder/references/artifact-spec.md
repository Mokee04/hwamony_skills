# Artifact Specification

## Project Layout

```text
agent-system-projects/
  <project-slug>/
    00-project-meta.yaml
    01-requirements.md
    02-task-brief.md
    03-architecture-options.md
    04-decision.md
    05-implementation/
      prompts/
      configs/
      code/
    06-test-plan.md
    07-runs/
    08-evaluation/
      rubric.md
      evaluation-summary.md
    09-feedback/
      user-feedback.md
      iteration-log.md
    HISTORY.md
```

## File Purpose

`00-project-meta.yaml`

- project slug
- created date
- owner or requester
- current status
- chosen vendor or stack when known

`01-requirements.md`

- raw requirements and constraints

`02-task-brief.md`

- normalized project brief

`03-architecture-options.md`

- 3 candidate architectures with tradeoffs

`04-decision.md`

- selected direction and reasons

`05-implementation/`

- prompts
- configs
- runtime code

`06-test-plan.md`

- test cases and pass criteria

`07-runs/`

- numbered run artifacts

`08-evaluation/`

- rubric
- scoring summary

`09-feedback/`

- user feedback
- iteration log

`HISTORY.md`

- short chronological list of material decisions

## Update Rules

- update files immediately after each phase
- keep reasoning brief and decision-oriented
- append, do not overwrite, in `HISTORY.md` and `iteration-log.md`
