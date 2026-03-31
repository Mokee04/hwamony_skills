# Hwamony Agent System Implementer

Turn a chosen system design into prompts, configs, runtime code, and history adapters.

This skill picks up after the architecture decision is made. It reads the builder artifacts, confirms the stack, generates prompts and config files, implements the runtime, and handles vendor-aware history design so the AI system is ready for evaluation.

## 🚀 Start Here

- `Use $hwamony-agent-system-implementer to scaffold the runtime for this multi-vendor assistant from the builder artifacts, not from scratch.`
- `Use $hwamony-agent-system-implementer to implement the history adapter layer from my architecture brief and keep vendor-specific behavior behind adapters.`
- `Use $hwamony-agent-system-implementer to turn this decision package into a runnable baseline with prompts, config, and message-history handling.`

## ✨ Why It Is Different

- it starts from decision artifacts instead of improvising a codebase from scratch
- it implements prompts, configs, runtime code, and history adapters together
- it keeps vendor-specific behavior behind an adapter layer
- it aims at evaluation-ready structure, not only a demo script

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

## 🧠 Best Fit

- teams that already made the architecture decision and want to move into code
- systems where prompt files, configs, history handling, and runtime logic need to line up
- builders who want an evaluation-ready baseline instead of a fragile prototype

## ⚠️ Boundary

This skill is not for deciding the architecture from scratch. If the design is still unstable, go back to `hwamony-agent-system-builder` before implementation starts drifting.
