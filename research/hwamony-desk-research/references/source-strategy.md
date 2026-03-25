# Source Strategy

## Choose Sources Before Searching

Start by deciding which source families matter most.

## Common Source Families

### Primary Sources

Use first when available.

Examples:

- government pages
- law or policy text
- company annual reports
- official product documentation
- academic papers
- direct datasets

### Secondary Sources

Use for synthesis, context, and comparison.

Examples:

- reputable newspapers
- trade publications
- research institutes
- industry analysis

### Background Sources

Use when you need orientation, not final authority.

Examples:

- summaries
- explainers
- reputable blog posts

## Tavily Mode Selection

### `$search`

Use when:

- queries are still exploratory
- you need to scan options fast
- you want to map the source landscape

### `$extract`

Use when:

- you already know the exact URLs
- you want to preserve source text
- you want a durable markdown artifact per source

### `$crawl`

Use when:

- one site is central
- the relevant content is spread across multiple pages
- you need to archive a documentation or knowledge base section

### `$research`

Use when:

- the batch deserves a broader multi-angle synthesis
- the question is comparative or market-oriented
- you want a higher-level survey before drilling into sources

## Source Proposal Template

```text
이번 배치는 아래 소스 축으로 가는 게 좋아 보여요.

1. 공식/1차 자료:
2. 보조 설명 자료:
3. 비교용 자료:

먼저 이 축으로 1차 배치를 진행해도 되는지 확인할게요.
```
