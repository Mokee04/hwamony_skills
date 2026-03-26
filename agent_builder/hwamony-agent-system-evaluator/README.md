# Hwamony Agent System Evaluator

An AI agent evaluation skill for testing a built system with run logs, rubrics, and iteration-ready feedback.

## 🧠 What It Does

This skill treats AI agent evaluation as a repeatable workflow, not a one-off opinion. It reads implementation artifacts, writes or updates the test plan, initializes run folders, logs inputs and outputs, scores results with a rubric, and captures the next improvement loop.

## ✨ Why It Is Different

- it focuses on per-run evidence, not vague quality judgments
- it stores evaluation artifacts so iteration has a paper trail
- it combines scoring, notes, and user feedback into one loop
- it is built to feed implementation backlogs, not just generate a report

## 🎯 Best For

- systems that already run but are still improving
- teams that need evidence before changing prompts, code, or routing
- workflows where evaluation needs to create the next implementation backlog

## 🚫 Not Just “Test It”

This skill is not for giving a thumbs-up or thumbs-down impression.

It is strongest when you need repeatable run logs, rubric-based scoring, stored evidence, and a clear bridge from evaluation findings back into the next implementation pass.

## 🧭 Use It When

- your agent or prompt system already exists and you want to test it properly
- you need run-by-run evidence instead of vague impressions
- you want rubric-based scoring and structured feedback
- you are preparing for the next implementation iteration

## 📦 What You Get

- per-run artifacts under `07-runs/run-###/`
- evaluation summaries
- rubric-based scores
- feedback logs
- a clearer handoff back to implementation

## ✍️ Example Prompts

- `Use $hwamony-agent-system-evaluator to create a test plan for my research agent with run folders, rubric criteria, and failure notes.`
- `Use $hwamony-agent-system-evaluator to score 5 sample runs, preserve the evidence, and summarize the biggest weaknesses for the next implementation pass.`
- `Use $hwamony-agent-system-evaluator to set up a repeatable experiment log for this prompt system instead of relying on vague impressions.`
- `Use $hwamony-agent-system-evaluator to turn these runs into a backlog of prompt, routing, and implementation fixes.`
