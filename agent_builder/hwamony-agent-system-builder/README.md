# Hwamony Agent System Builder

An AI agent architecture skill for turning fuzzy requirements into a concrete implementation decision.

## 🧠 What It Does

This skill turns an early idea into a structured AI agent project. It clarifies requirements, writes a task brief, compares architecture options, defines the message-history strategy, and prepares a clean handoff to implementation or evaluation.

## ✨ Why It Is Different

- it treats message history as a first-class architecture decision, not an implementation detail
- it produces reusable project artifacts instead of leaving planning buried in chat
- it forces 3 real architecture candidates instead of one premature recommendation
- it is designed to hand off cleanly into implementation and evaluation

## 🎯 Best For

- teams with an agent idea but no trustworthy architecture yet
- builders who need to compare single-model and multi-agent paths before coding
- projects where history design, tool use, or vendor strategy will shape the whole system

## 🚫 Not Just Architecture Advice

This skill is not just a brainstorming layer before implementation.

It is strongest when you need an actual project decision package: requirements, task brief, architecture options, decision rationale, and a handoff that implementation can start from without redoing the thinking.

## 🧭 Use It When

- you have an AI product or internal assistant idea but no clear architecture yet
- you want to compare single-model vs agentic approaches
- you need a project folder with reusable artifacts instead of chat-only planning
- you want the implementation and evaluation phases to start from a better brief

## 📦 What You Get

- `01-requirements.md`
- `02-task-brief.md`
- `03-architecture-options.md`
- `04-decision.md`
- a clear handoff to `hwamony-agent-system-implementer` or `hwamony-agent-system-evaluator`

## ✍️ Example Prompts

- `Use $hwamony-agent-system-builder to turn this rough idea for a source-grounded market research agent into 3 real architecture options and a concrete recommendation.`
- `Use $hwamony-agent-system-builder to compare 3 architecture options for a customer support copilot and tell me which one is easiest to ship first.`
- `Use $hwamony-agent-system-builder to define the history strategy for a multi-step coding assistant before we write any runtime code.`
- `Use $hwamony-agent-system-builder to decide whether this workflow should stay single-model or become a real multi-agent system with handoff artifacts.`
