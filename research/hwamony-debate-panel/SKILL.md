---
name: hwamony-debate-panel
description: Build and run a LangGraph-based multi-agent debate on a user-supplied topic. Use when the user wants debate topic intake, scope narrowing suggestions, five personas (moderator, pro1, pro2, con1, con2), moderator-led turn orchestration, cross-examination, saved system prompts for each panelist, and post-debate follow-up Q&A with a specific panel.
---

# Hwamony Debate Panel

Use this skill when the user wants an actual debate workflow, not a single assistant roleplaying all sides in one response.

This skill is designed to:

- take a debate topic from the user
- propose narrower debate resolutions before starting
- create five debate personas:
  `moderator`, `pro_1`, `pro_2`, `con_1`, `con_2`
- write a concrete system prompt for each persona
- run the debate as a LangGraph process with a moderator-led turn plan
- include cross-examination between opposing panelists
- save the session transcript and system prompts to disk
- let the user ask a follow-up question to one specific panel after the debate ends

## Workflow

1. Collect the topic.
2. Run the bundled CLI in `run` mode.
3. Review the scope-narrowing options and choose one unless the user already gave a precise resolution.
4. Let the script generate persona profiles and system prompts.
5. Let the LangGraph runtime execute the debate.
6. Save the session artifacts.
7. If the user wants follow-up questions, run the CLI in `ask` mode for the selected panel.

## Bundled CLI

Resolve `scripts/...` relative to this skill directory before running commands.

Primary entry point:

```bash
uv run --with langgraph --with langchain-openai --with google-genai python scripts/debate_panel.py run --topic "기본소득은 도입되어야 하는가"
```

Follow-up question to one panel:

```bash
uv run --with langgraph --with langchain-openai --with google-genai python scripts/debate_panel.py ask --session debate-sessions/<session-dir> --panel pro_1 --question "상대 측의 가장 강한 반론을 다시 하나만 꼽아줘"
```

## Authentication

- `OPENAI_API_KEY` must be set before live runs.
- Mixed-vendor or Gemini runs also require the Google GenAI SDK and `GEMINI_API_KEY`.
- Do not ask the user to paste the key into chat.

## Runtime Notes

- Prefer the bundled CLI over recreating the debate loop inline.
- The script uses LangGraph for the orchestration flow.
- The moderator is treated as a distinct agent with its own system prompt, not just a formatting wrapper.
- The debate session is persisted into a folder under `debate-sessions/` by default.

## Artifacts

Each run saves:

- `session.json`
- `transcript.md`
- `system-prompts.md`

These artifacts are meant to support later panel follow-up Q&A.

## Parameters Worth Adjusting

- `--topic`: raw user topic
- `--scope`: skip the interactive scope-choice step when the resolution is already precise
- `--auto-select-scope`: accept the recommended scope automatically
- `--model`: model name for all personas
- `--language`: response language, default `ko`
- `--output-root`: session output directory root

## When To Read The Script

Read `scripts/debate_panel.py` when you need to:

- modify the turn plan
- adjust persona system prompts
- change how cross-examination works
- alter output artifacts or saved session format
