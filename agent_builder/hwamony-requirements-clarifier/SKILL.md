---
name: hwamony-requirements-clarifier
description: Clarify ambiguous user requests into an actionable brief by asking the highest-value questions, proposing likely interpretations, surfacing assumptions, and converging on what the user actually wants before planning or implementation.
---

# Hwamony Requirements Clarifier

## Overview

Use this skill when the user's request is real but still fuzzy.

The goal is not to interrogate the user. The goal is to reduce ambiguity fast enough that the next step becomes obvious.

Use this skill to:

- identify what the user is actually trying to achieve
- separate the surface ask from the real deliverable
- expose hidden assumptions and missing constraints
- ask focused questions instead of broad questionnaires
- propose candidate interpretations when the user is unsure
- leave the conversation with a compact working brief

This skill is strongest before planning, architecture, implementation, or evaluation work.

## Best Fits

Use this skill when the user:

- asks for something broad, vague, or under-specified
- uses high-context language that leaves key details implicit
- seems unsure what output format or depth they want
- mixes multiple goals into one request
- asks for "something like this" without enough anchors
- needs help discovering the real problem before solution design

Do not use this skill when:

- the user already gave a concrete brief
- the task is simple enough to satisfy safely with a reasonable assumption
- the user explicitly wants broad ideation rather than convergence

## Core Stance

Default principles:

- clarify by reducing uncertainty, not by asking everything
- prefer the smallest set of questions that unlocks action
- ask only high-leverage questions first
- propose interpretations instead of forcing the user to invent structure alone
- use contrast, examples, and anti-goals to sharpen meaning
- keep a visible working brief as the conversation progresses
- stop clarifying once the brief is actionable

## Ambiguity Scan

Check for uncertainty in these areas:

- `goal:` what outcome the user actually wants
- `deliverable:` what artifact should be produced
- `audience:` who the result is for
- `scope:` how wide or narrow the work should be
- `constraints:` deadlines, budget, stack, policy, format, tone
- `evaluation:` how the user will decide whether the result is good
- `non-goals:` what should not happen or should not be included
- `examples:` what references, analogies, or precedents matter

If only one or two dimensions are unclear, ask about those only. Do not mechanically walk through the whole list.

## Workflow

### 1. Restate the Current Read

Start with a one-line interpretation of the request.

Good pattern:

- `My current read: you want X, mainly for Y, and the fuzzy part is Z.`

This gives the user something concrete to confirm, reject, or correct.

### 2. Identify the Highest-Value Gap

Find the single missing detail that most blocks good execution.

Common highest-value gaps:

- wrong or missing deliverable
- mixed-up target audience
- unclear success criteria
- hidden tradeoff between speed, depth, and polish
- vague "I want something better" language with no comparison point

### 3. Ask Focused Clarifying Questions

Ask 1-3 targeted questions at a time.

Prefer these patterns:

- `binary fork:` `Do you want A or B?`
- `constrained menu:` `If I had to frame it, is this closer to 1, 2, or 3?`
- `proposal + confirmation:` `I think you probably want X. If so, I should optimize for Y.`
- `anti-goal probe:` `What do you want to avoid?`
- `anchor example probe:` `What existing example feels closest?`
- `tradeoff probe:` `Should we bias toward speed, precision, or flexibility?`
- `success probe:` `What would make you say this is clearly good enough?`

Open-ended questions are allowed, but use them sparingly and only when narrower prompts would distort the answer.

### 4. Use Gentle Counterproposals

When the request is too fuzzy or self-contradictory, push back helpfully.

Useful patterns:

- `If we keep it this broad, the output will likely be generic.`
- `I can do that, but I think the real decision is between X and Y.`
- `Before I optimize for the wrong thing, I want to sanity-check one assumption.`
- `You may not need a full solution yet. A narrower artifact might be more useful first.`

The point is to narrow ambiguity, not to win an argument.

### 5. Maintain a Working Brief

As clarity improves, summarize the state in compact form:

- `goal`
- `deliverable`
- `audience`
- `constraints`
- `success criteria`
- `non-goals`
- `open questions`

If the brief is actionable, stop asking questions and proceed or hand off.

## Response Pattern

When invoked, use this shape unless the task clearly needs less:

1. `current read`
2. `what is still unclear`
3. `1-3 focused questions or options`
4. `provisional brief`

Keep the provisional brief short. It should help the user notice what is right or wrong.

## Decision Rules

- If the user seems overwhelmed, reduce the choice set.
- If the user is indecisive, propose a default and explain why.
- If the user says "just decide," make a reasonable assumption and state it.
- If the user gave enough detail, summarize and move forward instead of re-asking.
- If a question has non-obvious consequences, spell out the tradeoff.
- If the user is using high-context shorthand, translate it into explicit terms and confirm.

## Handoffs

Hand off to `$hwamony-agent-system-builder` when the clarified request becomes a real agent or system design brief.

Hand off to `$hwamony-prompt-architect` when the core need is prompt or workflow design rather than requirement discovery.

Hand off to `$hwamony-creative-thinking` when the user wants range, ideation, or concept generation more than convergence.

## Anti-Patterns

Do not:

- dump a long questionnaire on the user
- ask broad questions when a binary or option-based question would work
- keep clarifying after the brief is already good enough
- mistake uncertainty about wording for uncertainty about intent
- force the user to do all the structuring work
- ignore non-goals and failure conditions
- jump into planning or coding while the core deliverable is still unclear

## Example Triggers

- `The user wants help but the request is still too vague to plan confidently.`
- `The user seems to know the problem vaguely but not the deliverable.`
- `The user is speaking in shorthand and key assumptions are still implicit.`
- `Before building anything, clarify what success actually means here.`
