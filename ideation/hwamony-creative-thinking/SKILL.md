---
name: hwamony-creative-thinking
description: Generate, expand, combine, and narrow possibilities to surface strong candidates and insights. Use when the user needs creative thinking for problem solving, service naming, product concepts, positioning, messaging, feature ideas, or any task where many possibilities should be explored first and then reduced into promising directions.
---

# Hwamony Creative Thinking

## Overview

Use this skill when the user wants a creative task explored through a repeatable loop:

1. define the task's core concepts
2. build a mind map from those concepts
3. combine distant concepts to generate stronger ideas
4. repeat the loop based on user feedback

The point is not just to brainstorm. The point is to turn a vague or broad request into a visible concept structure, then use that structure to produce better combinations and better candidate ideas.

## Core Stance

Default principles:

- define concepts before proposing solutions
- keep hidden-problem diagnosis light but useful
- visualize the concept space before narrowing it
- prefer combinations across distant branches, not only nearby siblings
- interpret combinations into ideas instead of dumping raw mixes
- use user feedback to redraw the map, not only to reword the answer
- keep the loop tight, concrete, and easy to continue
- verify current product, pricing, or tool-capability facts before building recommendations when the task depends on real-world vendors
- preserve at least one contrarian or surprising lane that is unusual but still viable

## Best Fits

This skill is especially strong for:

- problem solving
- service naming
- product concept generation
- positioning and messaging directions
- feature ideation
- campaign or content directions
- open-ended exploration where structure is needed

## Choose the Task Mode

Identify the task type quickly:

- `problem-solving`
- `service-naming`
- `product-concept`
- `positioning`
- `feature-ideation`
- `open exploration`

Use the mode only to tune the concepts and evaluation criteria. Do not let the mode replace the main loop.

Also identify the requested output scope early:

- `diagnose + map + combine + narrow`
- `expand only`
- `narrow only`
- `critique existing options`

Honor the user's requested scope. Do not force full convergence when the user asked for range. Do not restart from zero when the user asked to critique an existing set.

## Main Loop

### 1. Define the Core Concepts

Start by translating the request into a compact creative frame.

Extract:

- the task or problem
- target audience
- desired outcome
- constraints
- tone or style
- evaluation criteria
- requested quantity, shortlist size, or output count, if any

If the user gave an explicit number such as 4 ideas, 12 angles, or 3 finalists, treat that as a real constraint unless there is a clear reason not to. If you intentionally deviate, explain why instead of drifting silently.

Then define the core concepts that make the task interesting or solvable.

Good concept sources:

- goals
- user motivations
- tensions or tradeoffs
- contexts of use
- emotional payoffs
- mechanisms
- constraints
- adjacent domains
- metaphors
- category expectations

Useful default target:

- 5-12 core concepts
- grouped into 3-6 families

For each concept, keep one short explanation:

- `concept:` the label
- `role:` why this concept matters for the task

If the prompt suggests a deeper tension, state it briefly as a hypothesis rather than a grand reveal.

If the brief is ambiguous, especially in problem-solving mode, surface 2-3 plausible hidden-driver or root-cause hypotheses instead of pretending there is only one.

Helpful structure:

- `surface ask`
- `likely tension or hidden driver`
- `core concept families`
- `core concepts`

If the user already supplied options, names, or draft directions:

- normalize those first
- critique or cluster them before proposing replacements
- add new options only when the current set has a clear gap, repetition problem, or strategic weakness

### 2. Build the Mind Map

Turn the concepts into a mind map before you start selecting ideas.

Mind map structure:

- center node: the task, challenge, or opportunity
- first-level branches: concept families
- second-level nodes: individual concepts
- optional cross-links: non-obvious relationships across branches

Use the bundled Python visualizer when a visual artifact would help the work.

If the user explicitly asks for a Python-based mind map, visual map, or rendered concept map, use the script by default instead of only describing the structure in prose.

Files:

- `scripts/render_mindmap.py`
- `references/visualization-format.md`

Preferred use:

- create a small outline or JSON input
- render to SVG or PNG
- mention the output path in the response when you generated it

Example command:

```bash
python3 scripts/render_mindmap.py /tmp/creative-map.txt -o /tmp/creative-map.svg
```

Mind map rules:

- keep labels short
- branch by meaning, not by sentence fragments
- separate clearly different concept families
- add cross-links only when they reveal a useful bridge
- do not overfill the map just to look comprehensive

### 3. Combine Distant Concepts

After the map exists, intentionally look for concepts that sit far apart.

Prefer combinations between:

- different top-level branches
- weakly linked concept families
- emotional and functional concepts
- constraints and aspirations
- category norms and unusual adjacent ideas

Avoid spending most of the time on combinations that are already obvious neighbors.

When helpful, convert distant branches into axes and use the bundled combination script.

Files:

- `scripts/combine_options.py`
- `references/combination-format.md`

Example command:

```bash
python3 scripts/combine_options.py /tmp/creative-axes.txt --size 2 -o /tmp/creative-combos.md
```

Interpret combinations into task-relevant ideas.

For each promising combination, rewrite it as:

- `idea:` what the combined direction is
- `from:` which distant concepts or branches were combined
- `fit:` why it matches the task
- `risk:` what remains weak, unclear, or hard

Do not let all combinations collapse into the same strategic answer.

Before narrowing, make sure the set includes different creative postures such as:

- conservative
- operational
- contrarian
- weird but viable
- system-design heavy

Default targets:

- generate 6-12 raw combinations
- turn the best 3-5 into candidate ideas
- keep at least 2 non-obvious combinations in the final set
- keep at least 1 contrarian or surprising lane in the candidate set unless the user explicitly asks for only safe options

If the user requested a specific final count, shape the candidate set to that count.

### 4. Converge into Candidate Ideas

Do not stop at the map or the combinations. Turn them into candidate units that the user can react to.

Examples:

- service naming: name directions or candidate names
- problem solving: solution concepts
- product concept: concept bundles
- positioning: message territories or direction statements

Shortlist using the task's criteria, usually some mix of:

- usefulness
- distinctiveness
- coherence
- feasibility
- memorability
- leverage
- testability

Scope rules:

- `expand only`: keep diagnosis brief, show breadth, and avoid premature narrowing
- `narrow only`: work mainly from the supplied set or already generated set
- `critique existing options`: evaluate the current options first and only then add limited replacements if needed
- `diagnose + map + combine + narrow`: run the full loop

Before final recommendation, compare the shortlist across at least 2 different creative postures. Do not make every finalist a variation of the same safe answer.

For each shortlisted item, state:

- what it is
- which concepts it combines
- why it stands out
- what tradeoff remains

For at least one shortlisted item, explicitly label:

- `lane:` contrarian, weird-but-viable, or unexpected

### 5. Repeat with User Feedback

Treat feedback as a signal to redraw the concept system, not only to regenerate wording.

When the user gives feedback:

- revise the core concepts
- add, remove, split, or merge branches
- redraw the mind map if the structure changed
- rerun distant-concept combinations
- present the new candidate set and explain what changed

Typical feedback moves:

- "too generic" -> add sharper concepts or more specific branches
- "too unrealistic" -> strengthen feasibility and constraint branches
- "too safe" -> combine more distant branches
- "not creative enough" -> force a contrarian lane and a weird-but-viable lane before narrowing again
- "not aligned with the task" -> redefine the center node and criteria
- "I like this lane" -> deepen that branch and recombine within its neighboring distant branches

## Task-Specific Guidance

### Problem Solving

Core concepts often include:

- symptoms
- root causes
- constraints
- stakeholder tensions
- incentives
- behavior loops
- structural bottlenecks

Strong distant combinations often mix:

- structural fixes with emotional barriers
- workflow friction with trust or motivation
- low-effort fixes with system-level changes

### Service Naming

Core concepts often include:

- category expectations
- buyer anxiety
- trust signals
- emotional tone
- metaphor fields
- language texture

Strong distant combinations often mix:

- credibility with surprise
- category clarity with emotional payoff
- functional meaning with metaphorical language

### Product Concept

Core concepts often include:

- job-to-be-done
- behavior barrier
- use context
- emotional reward
- delivery mechanism
- adjacent substitutes

Strong distant combinations often mix:

- usage context with emotion
- adoption friction with reward loop
- category norm with adjacent-domain behavior

### Positioning

Core concepts often include:

- audience doubt
- real decision driver
- strategic contrast
- proof signal
- promise type
- tone of voice

Strong distant combinations often mix:

- decision criteria with emotional reassurance
- proof with contrast
- category language with outsider framing

## Response Pattern

When invoked, follow this pattern:

1. Restate the brief in one line.
2. Name the task mode.
3. Define the core concepts and, if useful, the likely hidden tension.
4. Start from the user's existing options when they supplied them.
5. Show the mind map structure in a compact form.
6. Render the mind map with Python when it materially helps, and by default when the user explicitly asked for Python-based visualization.
7. Combine distant concepts into candidate ideas.
8. Preserve at least one contrarian or weird-but-viable lane before narrowing.
9. Honor explicit quantity requests in the final candidate set or shortlist.
10. Ask for targeted feedback only after the first loop is complete, unless the task is blocked by missing essentials.

## Default Output Shape

Use the lightest structure that still shows the loop clearly.

- brief
- task mode
- core concepts
- mind map summary
- distant-concept combinations
- shortlist
- what to refine in the next loop

If a visual file was generated, include:

- the render path
- one line on what the map reveals

## Anti-Patterns

Do not:

- jump straight to ideas without defining concepts
- keep the concept list so abstract that it cannot shape a map
- build a mind map and then ignore it
- combine only nearby or obvious nodes
- dump raw combinations without interpreting them
- ignore user-supplied options and restart from zero
- drift away from an explicit requested count without saying so
- let all candidate lanes converge into the same practical answer too early
- remove every surprising lane before the user has a chance to react to it
- treat the first loop as final when the user gave clear directional feedback
- preserve a weak center node after feedback changed the task
- over-diagnose when the brief is already concrete

## Example Triggers

- "이 과제를 핵심 개념으로 분해하고 마인드맵으로 정리한 뒤 아이디어를 만들어줘."
- "먼 개념끼리 조합해서 새로운 컨셉을 뽑아줘."
- "먼저 개념 구조를 잡고, 그걸 바탕으로 서비스 아이디어를 발전시켜줘."
- "한 번에 끝내지 말고 피드백 반영해서 반복해줘."
- "브레인스토밍 말고 개념 정의 -> 시각화 -> 조합 순서로 해줘."
