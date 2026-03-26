---
name: hwamony-creative-thinking
description: Generate, expand, combine, and narrow possibilities to surface strong candidates and insights. Use when the user needs creative thinking for problem solving, service naming, product concepts, positioning, messaging, feature ideas, or any task where many possibilities should be explored first and then reduced into promising directions.
---

# Hwamony Creative Thinking

## Overview

Use this skill when the job is not only to think broadly, but to end with something strong: a shortlist, a naming direction, a concept family, a recommended solution path, or a few high-potential combinations.

The skill intentionally moves through both divergence and convergence, but it also includes a diagnosis layer: before treating the user's topic as the real problem, inspect what deeper tension, hidden job, structural constraint, or decision driver may sit underneath it.

The aim is not just "many ideas." The aim is to uncover what really needs solving, then surface the strongest candidates that fit that deeper structure.

## Core Stance

Think in three motions:

- diagnose first
- widen second
- reduce third

Do not treat those as rigid phases. The point is to inspect the problem beneath the prompt, explore enough to see the landscape, then converge enough to surface signal.

Default principles:

- do not accept the surface ask as the whole problem
- diagnose before optimizing
- diagnose proportionally, not theatrically
- generate before judging
- compare before selecting
- combine before discarding
- name patterns, not just items
- end with candidates, not only analysis
- honor the user's explicit scope when they want only expansion, only narrowing, or critique of existing options

## Best Fits

This skill is especially strong for:

- problem solving
- service naming
- brand or product naming
- product concept generation
- positioning and messaging directions
- feature or solution ideation
- campaign or content directions
- strategic option narrowing

## Choose the Task Mode

Identify the task type quickly:

- `problem-solving`
- `service-naming`
- `product-concept`
- `positioning`
- `feature-ideation`
- `open exploration`

Then choose the right emphasis:

- more diagnosis when the user describes a problem, symptom, friction, or topic that may hide a deeper issue
- more divergence when the space is underexplored
- more convergence when options already exist
- more comparison and critique when the user already has candidates, drafts, or directions on the table
- a balanced loop when the user wants both "many ideas" and "the strongest ones"
- a lighter diagnosis when the brief is already concrete and the main need is range or structured comparison

## Hidden Problem Layer

When the user gives a theme, request, or symptom, do not jump straight to ideas.

First inspect the structure under it:

- what the user says they want
- what progress they likely actually want
- what symptom they are pointing at
- what deeper problem may produce that symptom
- what tension or tradeoff is keeping the problem alive
- what constraint, incentive, fear, or decision criterion is probably shaping the situation

Useful hidden-problem lenses:

- capability gap
- workflow friction
- incentive mismatch
- trust barrier
- decision overload
- timing mismatch
- behavior loop failure
- status or identity pressure
- coordination cost
- structural bottleneck

If the prompt is ambiguous, surface 2-3 plausible underlying problem hypotheses instead of pretending there is only one.

Treat hidden-problem analysis as a working hypothesis, not a reveal.

- label deeper interpretations as likely or plausible when inferred
- keep diagnosis brief when the prompt is already concrete
- do not invent psychological motives or false certainty from sparse evidence
- if the user already gave a strong candidate set, diagnose only enough to compare the set intelligently
- if the user explicitly asks for only idea expansion or only narrowing, keep the diagnosis layer compact and supportive rather than dominant

## Workflow

### 1. Define the Creative Frame

Extract:

- the topic or problem
- target audience
- desired outcome
- constraints
- tone or style
- evaluation criteria, if any
- requested quantity, shortlist size, or output count, if any

If criteria are missing, infer provisional ones from the task. For example:

- problem solving:
  usefulness, feasibility, distinctiveness, leverage, testability
- service naming:
  memorability, fit, distinctiveness, tone, extensibility
- positioning:
  clarity, resonance, differentiation, strategic tension

If the user requests a specific number of candidates, angles, or finalists, honor that count when it is reasonable. If you intentionally deviate, explain why instead of silently drifting.

Also identify the requested output scope early:

- `diagnose + expand + narrow`
- `expand only`
- `narrow only`
- `critique existing options`

If the user already supplied options, drafts, or names, treat those as first-class input rather than resetting the exercise from zero.

### 2. Discover the Hidden Problem

Separate the surface request from the deeper issue.

At minimum, identify:

- the surface ask
- the likely underlying problem or latent job
- 2-4 hidden factors behind it
- the leverage points that would most change the outcome

Good hidden factors include:

- root cause
- stakeholder tension
- structural constraint
- hidden motivation
- decision criterion
- incentive mismatch
- trust or credibility barrier
- fear of loss

For non-problem tasks, translate this step into diagnosis rather than therapy.

Examples:

- service naming:
  hidden buyer anxiety, trust barrier, selection heuristic, category expectation
- product concept:
  job-to-be-done, unmet tension, adoption barrier, emotional payoff
- positioning:
  stated claim, real decision driver, skeptical objection, strategic contrast

Useful output forms:

- surface ask vs underlying problem
- issue tree
- tension map
- hidden-driver list
- leverage-point list

### 3. Run the Divergence Pass

Expand the space before choosing.

Good divergence outputs:

- mind map
- branch table
- candidate list
- angle list
- semantic network
- intervention menu
- problem-frame variants

Use these moves:

- change the lens
- change the audience
- change the context
- change the emotional payoff
- move to an adjacent domain
- invert the assumption
- combine opposites
- solve the deeper problem instead of the stated symptom

Default targets:

- 5-8 idea families
- 10-25 raw candidates when naming or ideating
- at least 2 non-obvious directions
- at least 2 different problem frames when the brief is ambiguous

If a visual structure helps, use:

- `scripts/render_mindmap.py`
- `references/visualization-format.md`

### 4. Normalize into Candidate Units

Before converging, rewrite the divergence output into comparable units.

Examples:

- service naming:
  candidate names
- problem solving:
  solution concepts
- positioning:
  direction statements
- product concepts:
  concept bundles

Each unit should be short, legible, and tied to what problem it addresses.

For problem-oriented tasks, add one short line per unit:

- `addresses:` which hidden issue, tension, or leverage point this unit responds to

Remove duplicates with only wording differences.

If the user already supplied candidate units:

- clean and normalize those first
- cluster and critique them before generating replacements
- introduce new candidates only when the current set has clear gaps, repetition, or strategic blind spots

### 5. Cluster and Compare

Group candidates into families:

- by theme
- by mechanism
- by value proposition
- by emotional tone
- by strategic posture
- by hidden problem addressed

Then compare within and across families.

Useful outputs:

- theme clusters
- tradeoff table
- family comparison
- tension map
- leverage vs effort matrix

### 6. Run the Combination Pass

If insight comes from mixing elements, rewrite the set into axes and combine them.

Good axes:

- audience
- value
- tone
- channel
- feature
- context
- emotion
- form
- hidden problem
- intervention mechanism

Use:

- `scripts/combine_options.py`
- `references/combination-format.md`

Prefer 2-way combinations first. Move to 3-way combinations only when the axes are clean and meaningful.

Look for:

- reinforcement
- contradiction
- adjacency
- asymmetry
- hidden fit

### 7. Design Solution Paths

Before final narrowing, check that promising directions actually respond to the diagnosis.

For each strong candidate or lane, state:

- what it is
- which hidden problem it addresses
- why that makes it promising
- what tradeoff or risk remains

When the task is problem solving, include a mix of:

- low-effort fixes
- structural fixes
- behavioral fixes
- system or policy fixes
- fast learnable experiments

Prefer recommendations that solve a more valuable problem, not only the most visible symptom.

### 8. Converge into a Shortlist

After grouping and combining, explicitly surface the strongest candidates.

Recommended shortlist sizes:

- 3-5 for names
- 2-4 for solution directions
- 3-6 for concept bundles

For each shortlisted item, state:

- what it is
- what hidden problem it addresses
- why it stands out
- what makes it different
- what risk or tradeoff remains

### 9. Extract Insight and Recommendation

Do not stop at "here are the options." Say what the set reveals.

Strong synthesis forms:

- "The surface request looks like a speed problem, but the deeper issue is coordination cost."
- "Most strong candidates cluster around reassurance rather than authority."
- "The real divide is playful naming vs credible naming."
- "Several combinations converge on low-friction behavior plus status signaling."
- "The highest-potential direction is not the most novel, but the one that resolves the hidden trust barrier."

End with:

- a recommended winner or top lane
- the main reason it wins
- the main tradeoff
- the next validation move

## Task-Specific Guidance

### Problem Solving

Generate:

- symptom hypotheses
- root-cause angles
- intervention types
- low-effort fixes
- systemic fixes
- unconventional fixes

Distinguish clearly between:

- symptom
- underlying constraint
- structural cause
- behavior cause
- incentive mismatch
- coordination failure

Converge toward:

- highest leverage
- fastest learnable experiments
- strongest fit to the real constraint

### Service Naming

Before generating names, surface:

- hidden buyer anxiety
- trust threshold
- decision heuristic
- category expectation
- language tension, if any

Generate across naming lanes:

- descriptive
- suggestive
- metaphorical
- coined
- hybrid

Converge toward:

- memorability
- category fit
- distinctiveness
- tone alignment
- extensibility

### Product Concept

Before ideating concepts, surface:

- job-to-be-done
- behavior barrier
- adoption friction
- emotional payoff
- adjacent substitutes

Generate across:

- audience
- core value
- behavior loop
- emotional payoff
- delivery form

Converge toward:

- coherent bundles
- strong need-solution fit
- clear difference from adjacent concepts

### Positioning

Before writing directions, surface:

- what the user says they want
- what they actually need confidence about
- what objection or doubt blocks adoption
- what strategic contrast matters most

Converge toward:

- clarity
- differentiation
- resonance
- decision relevance
- believable promise

## Anti-Patterns

Do not:

- accept the user's stated ask as the whole problem without testing it
- jump straight to solutions before naming the hidden issue
- stay only in divergence and forget to shortlist
- converge so fast that the space never opens
- dump every combination without interpreting it
- confuse criteria with candidates
- preserve near-duplicates as fake variety
- give solutions that are not traceable to the diagnosed issue
- force one deep root cause when multiple tensions matter
- over-interpret a sparse brief just to sound insightful
- ignore user-supplied candidates and restart from zero without reason
- hide behind framework language when the user needs concrete options
- end with generic observations instead of actionable signal

## Response Pattern

When invoked, follow this pattern:

1. Restate the creative brief in one line.
2. Name the task mode.
3. State the surface ask and the likely hidden problem or tension, labeling inferences as hypotheses when needed.
4. Show the diagnosis or divergence output in a compact structure.
5. Normalize into candidate units, families, or solution directions, starting with user-supplied options when they exist.
6. Show the convergent comparison, combinations, critique, or shortlist.
7. State the main insights explicitly.
8. End with the strongest candidate or lane, the tradeoff, and the next validation move.

## Default Output Shapes

Use the lightest shape that still fits the brief.

### Diagnose + Expand + Narrow

- brief
- task mode
- hidden problem hypotheses
- idea families or candidate directions
- shortlist
- recommendation and next move

### Critique Existing Options

- brief
- task mode
- what criteria matter most
- clustered critique of the existing options
- shortlist or ranked set
- only then, optional replacement ideas if the current set is weak

### Expand Only

- brief
- task mode
- concise diagnosis
- idea families
- raw candidates
- short note on which lanes look strongest if the user wants narrowing next

## Example Triggers

- "이 문제를 여러 방향으로 풀어보고 유력한 해결책을 골라줘."
- "표면적으로 보이는 문제 말고, 진짜 해결해야 할 이면의 문제를 찾아서 방향을 제안해줘."
- "서비스명을 많이 뽑되, 고객의 숨은 불안과 선택 기준을 먼저 드러내고 추려줘."
- "여러 컨셉을 만들고 조합해서 유망한 방향을 찾아줘."
- "브레인스토밍부터 shortlist까지 한 번에 해줘."
- "가능성을 넓힌 뒤 패턴을 보고 가장 좋은 후보를 발굴해줘."
