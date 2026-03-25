---
name: hwamony-agent-system-implementer
description: Implement the selected AI agent or single-model architecture after design is chosen. Use when the user has a brief or architecture and wants Python code, prompts, configs, vendor setup, message-history adapters, and runtime scaffolding using direct vendor APIs or LangChain.
---

# Hwamony Agent System Implementer

## Overview

Implement the chosen architecture inside the project folder created by the builder skill.

Use this skill to:

- confirm the implementation stack
- generate prompts and config files
- implement runtime code
- implement vendor-aware history handling
- prepare the system for evaluation

Apply `$hwamony-prompt-architect` when prompt quality, model routing, or output contracts need refinement.

## Required Inputs

Read these artifacts before coding:

- `01-requirements.md`
- `02-task-brief.md`
- `03-architecture-options.md`
- `04-decision.md`

If one of them is missing, state what is missing and create the smallest reasonable placeholder only when the user wants you to proceed.

## Stack Selection

If the stack is not locked, ask the user to choose among:

1. direct vendor API
2. LangChain
3. lightweight multi-vendor wrapper

Default recommendation:

- choose direct vendor API for the cleanest single-vendor production system
- choose LangChain when chain composition, memory abstractions, or tool integration layers clearly help
- choose a lightweight wrapper when vendor comparison is a first-class requirement

## Implementation Targets

Implement under:

```text
05-implementation/
  prompts/
  configs/
  code/
```

Create at minimum:

- `prompts/system_prompt.md`
- `prompts/developer_prompt.md` when needed
- `configs/model_config.yaml`
- `configs/history_policy.yaml`
- `code/runtime.py`
- `code/history_types.py`
- `code/history_store.py`
- `code/history_adapters.py`

Add vendor-specific provider files only when needed.

## History Requirements

Always implement history as:

1. canonical internal transcript
2. vendor adapter layer
3. replay or reduction policy

Do not let vendor-native sessions become the only source of truth.

Use the contract in [references/history-adapter-contract.md](references/history-adapter-contract.md).

## Vendor-Specific Expectations

### OpenAI

- Prefer the Responses API for modern systems.
- Choose between `previous_response_id` chaining and full replay.
- Store response IDs separately from the canonical transcript.

### Anthropic

- Assume stateless replay unless the product architecture says otherwise.
- Keep system prompt and tool definitions distinct from replayed user or assistant turns.
- Keep tool calls and tool results explicit in the canonical transcript.

### Gemini

- Choose between SDK chats, stateless replay, or interaction chaining.
- Re-apply system instructions, tools, and generation config each turn when using chained interactions.

## History Policies

Choose and implement one:

- `full_replay`
- `recent_window`
- `summary_plus_recent`
- `tool_pinned_summary_recent`

Record the choice in `configs/history_policy.yaml`.

## Output Rules

When generating code:

- favor clarity over excessive abstraction
- keep provider-specific logic isolated
- keep history-reduction logic separate from provider adapters
- use plain, readable Python unless the repo already requires another style

## Handoff To Evaluation

Before handing off to `$hwamony-agent-system-evaluator`, ensure:

- prompts exist
- configs exist
- runtime code exists
- history handling is implemented
- at least one runnable path is present

## Resources

Read these when needed:

- [references/stacks.md](references/stacks.md): stack tradeoffs
- [references/history-adapter-contract.md](references/history-adapter-contract.md): canonical history model and vendor mappings
- [references/implementation-checklist.md](references/implementation-checklist.md): file-level implementation checklist
