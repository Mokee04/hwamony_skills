---
name: hwamony-desk-research
description: Conduct staged desk research on a user-supplied topic, clarify the scope, propose source strategies, gather evidence in batches, ask for feedback between batches, and organize the full process into a project folder with step-by-step markdown files and preserved source texts. Use when the user wants topic research, market scans, trend analysis, literature overviews, competitor/category scans, policy summaries, or sourced briefing documents.
---

# Hwamony Desk Research

## Purpose

Use this skill to run structured desk research that is:

- scoped before searching
- source-strategy driven
- iterative rather than one-shot
- checkpointed with the user between batches
- fully documented in project artifacts
- backed by preserved source text files

This skill is for:

- topic exploration
- market or category scans
- industry or competitor desk research
- policy or regulation overviews
- literature or article reviews
- briefing memos and research packs

## Workflow

Follow this sequence unless the user explicitly asks to skip ahead.

1. Clarify the topic and narrow the scope.
2. Initialize the research project folder.
3. Write the research brief.
4. Propose the source strategy.
5. Run research batch 1.
6. Summarize current findings and ask whether to continue.
7. Run the next batch if approved.
8. Preserve source texts as separate markdown files.
9. Write the final synthesis and bibliography.

## Step 1: Clarify The Topic

Do not search immediately unless the request is already precise enough.

Clarify:

- exact question
- intended output
- audience
- geography
- timeframe
- source preferences
- exclusions
- depth required

Ask only the next high-value questions.

Good examples:

- `이 리서치를 어떤 의사결정에 쓰려는지 같이 정할까요?`
- `비교가 필요하면 비교 대상도 같이 고를게요.`
- `Do you want a broad landscape, a comparison, or a source-backed answer to one specific question?`

## Step 2: Initialize The Project Folder

Create the folder early so every stage has an artifact home.

Default root:

```text
desk-research-projects/<project-slug>/
```

Use:

```bash
python3 scripts/init_desk_research_project.py <project-slug> --base-path <parent-dir>
```

If the user does not specify a location, default to the current working directory.

## Step 3: Write The Research Brief

Write:

- `00-project-meta.yaml`
- `01-research-brief.md`

The brief should contain:

- research question
- scope
- non-goals
- audience
- expected output
- key unknowns

## Step 4: Propose The Source Strategy

Before running searches, propose where the research should come from.

Typical source buckets:

- official docs or government sources
- company pages
- academic or institutional sources
- reputable news or trade publications
- books or reports
- expert commentary

Use the guidance in [references/source-strategy.md](references/source-strategy.md).

When Tavily-backed skills are available, use them selectively:

- `$search` for query discovery and result scanning
- `$extract` for preserving known URLs
- `$crawl` for site-level documentation or archives
- `$research` for broad multi-angle synthesis when a batch deserves a heavier pass

Do not default to one giant `research()` call if the user needs staged approval.

## Step 5: Work In Batches

Research in batches rather than trying to finish everything in one pass.

Each batch should have:

- a research focus
- a source plan
- a short evidence summary
- a decision on what to research next

Write each batch into:

- `03-batches/batch-001.md`
- `03-batches/batch-002.md`
- and so on

## Step 6: Ask For Feedback Between Batches

After each meaningful batch:

- say what you researched
- summarize what you found
- name the current gaps
- ask whether to continue, redirect, deepen, or stop

Do not silently keep expanding the research forever.

## Step 7: Preserve Source Texts

Preserve source texts in separate markdown files, not only inline citations.

Store:

- article or web page text in its own file
- relevant book passage or paragraph in its own file
- notes on why the source matters

Use:

- `04-sources/source-index.md`
- `04-sources/raw/source-001.md`
- `04-sources/raw/source-002.md`

For books:

- save only the relevant paragraph or quoted passage the user has access to or that is lawfully available
- include bibliographic metadata

For web pages and articles:

- save the URL
- access date
- page title
- extracted text or relevant excerpt

Use [references/source-preservation.md](references/source-preservation.md).

## Step 8: Write The Final Synthesis

Write:

- `05-findings.md`
- `06-bibliography.md`
- optionally `07-open-questions.md`

The final synthesis should include:

- what is known
- what is uncertain
- where sources agree
- where sources conflict
- what the user may want to research next

## Artifact Rules

Keep the working memory in files, not only in chat.

Update files as you go:

- after scoping
- after source planning
- after each batch
- after each major user feedback point

## Citation Rules

- cite every external factual claim in the final synthesis
- link each citation back to a source file in `04-sources/`
- distinguish source text from your synthesis
- distinguish verified source claims from inference

## Resources

Read these when needed:

- [references/workflow.md](references/workflow.md): staged research flow
- [references/source-strategy.md](references/source-strategy.md): how to choose source types and Tavily modes
- [references/artifact-spec.md](references/artifact-spec.md): project file map
- [references/source-preservation.md](references/source-preservation.md): how to store source texts
- `scripts/init_desk_research_project.py`: deterministic research-project scaffold creation
