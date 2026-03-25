# Artifact Specification

## Project Layout

```text
desk-research-projects/
  <project-slug>/
    00-project-meta.yaml
    01-research-brief.md
    02-source-strategy.md
    03-batches/
      batch-001.md
      batch-002.md
    04-sources/
      source-index.md
      raw/
        source-001.md
        source-002.md
    05-findings.md
    06-bibliography.md
    07-open-questions.md
    08-feedback-log.md
```

## File Purposes

`00-project-meta.yaml`

- project slug
- created date
- status
- current stage

`01-research-brief.md`

- research question
- audience
- scope
- exclusions

`02-source-strategy.md`

- source families
- search plan
- research batch proposal

`03-batches/*.md`

- batch focus
- search terms
- URLs reviewed
- interim findings
- next questions

`04-sources/source-index.md`

- master list of source files
- mapping between citation keys and source files

`04-sources/raw/source-###.md`

- individual preserved source text files

`05-findings.md`

- main synthesis

`06-bibliography.md`

- formatted source list

`07-open-questions.md`

- unresolved issues and future research

`08-feedback-log.md`

- user feedback and redirections between batches
