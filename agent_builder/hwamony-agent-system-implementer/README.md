# Hwamony Agent System Implementer

Turn a chosen agent design into prompts, configs, runtime code, and history adapters.

## 🧠 What It Does

This skill picks up after the architecture decision is made. It reads the builder artifacts, confirms the stack, generates prompts and config files, implements the runtime, and handles vendor-aware history design so the system is ready for evaluation.

## ✨ Why It Is Different

- it starts from decision artifacts instead of improvising a codebase from scratch
- it implements prompts, configs, runtime code, and history adapters together
- it keeps vendor-specific behavior behind an adapter layer
- it aims at evaluation-ready structure, not only a demo script

## 🎯 Best For

- teams that already made the architecture decision and want to move into code
- systems where prompt files, configs, history handling, and runtime logic need to line up
- builders who want an evaluation-ready baseline instead of a fragile prototype

## 🚫 Not Just Scaffolding

This skill is not just “make me a quick demo.”

It is built for the messy middle where a design already exists and someone needs to turn that design into prompts, adapters, configs, and runtime structure that can survive the next evaluation cycle.

## 🧭 Use It When

- the requirements and architecture are already defined
- you want code and runtime structure, not more brainstorming
- you need prompt files, model config, and history handling in one pass
- you want an evaluation-ready implementation baseline

## 📦 What You Get

- `prompts/`
- `configs/`
- `code/runtime.py`
- history types and adapters
- a concrete implementation aligned with the decision artifacts

## ✍️ Example Prompts

- `Use $hwamony-agent-system-implementer to scaffold the runtime for this multi-vendor assistant from the builder artifacts, not from scratch.`
- `Use $hwamony-agent-system-implementer to implement the history adapter layer from my architecture brief and keep vendor-specific behavior behind adapters.`
- `Use $hwamony-agent-system-implementer to generate prompts, configs, and runtime code for a LangChain-based research agent that is ready for evaluation.`
- `Use $hwamony-agent-system-implementer to turn this decision package into a runnable baseline with prompts, config, and message-history handling.`
