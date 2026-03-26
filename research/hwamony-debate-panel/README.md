# Hwamony Debate Panel

Run a real multi-agent debate instead of having one assistant fake both sides.

## What It Does

This skill takes a topic, narrows the resolution, creates five debate personas, writes their system prompts, runs the debate through LangGraph, and saves the session artifacts for later follow-up questions.

## Why It Is Different

- it uses an actual multi-agent workflow instead of one assistant roleplaying both sides
- it saves prompts and transcripts so the debate is inspectable later
- it includes a moderator and cross-examination structure, not just alternating speeches
- it supports follow-up questions to a specific panel after the main run

## Best For

- questions where the tension between positions matters as much as the conclusion
- users who want inspectable debate artifacts instead of improvised roleplay
- topics that benefit from a moderator, cross-examination, and saved prompts

## Not Just “Debate This”

This skill is not mainly for theatrical roleplay.

It is strongest when you want a real structure around disagreement: cleaner resolution framing, explicit panel roles, cross-examination, a saved transcript, and the ability to question one side afterward instead of rerunning the whole thing.

## Use It When

- you want multiple sides argued in a structured format
- you need debate artifacts you can inspect later
- you want moderated turns and cross-examination, not improvised roleplay
- you want to ask follow-up questions to a specific panel after the debate

## Artifacts

- `session.json`
- `transcript.md`
- `system-prompts.md`

## Example Prompts

- `Use $hwamony-debate-panel to run a debate on whether basic income should be adopted, with a moderator and saved transcript.`
- `Use $hwamony-debate-panel to narrow this messy topic into a cleaner resolution before debating it.`
- `Use $hwamony-debate-panel to run the debate in Korean, save the transcript, and let me ask follow-up questions to the con side afterward.`
- `Use $hwamony-debate-panel to pressure-test this policy claim with explicit pro and con panels instead of one assistant improvising both sides.`
