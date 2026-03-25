# Prompt Architect Knowledge Base

## 1. Default Operating Posture

Treat prompt design as systems design.

Default priorities:

1. correctness
2. groundedness
3. output reliability
4. tool correctness
5. latency and cost
6. wording polish

Default vendor posture:

- if the user does not constrain the vendor, start from the current OpenAI frontier recommendation for hard professional work
- if latency or cost dominates, route to smaller models
- if the task is production-bound, freeze a model version or alias policy and define evals

## 2. Vendor-Aware Model Routing

Use the detailed tables in `vendor_model_guide.md`.

Practical defaults:

- OpenAI `gpt-5.4`: best default for complex agentic and coding workflows
- OpenAI `gpt-5-mini`: low-latency, cost-sensitive, high-volume prompt systems
- OpenAI `gpt-5.4-pro`: premium mode for the hardest planning and verification tasks
- Anthropic `claude-sonnet-4-6`: best Claude default for coding, agents, and practical intelligence
- Anthropic `claude-opus-4-6`: premium Claude route for deepest reasoning and long-horizon agentic work
- Anthropic `claude-haiku-4-5`: fast, high-volume, budget-conscious route
- Gemini `gemini-2.5-pro`: best stable Gemini choice for complex reasoning and coding
- Gemini `gemini-2.5-flash`: best price-performance for low-latency reasoning
- Gemini `gemini-2.5-flash-lite`: fastest and cheapest Gemini route
- Gemini `gemini-3.1-pro-preview`: newest Gemini preview when the user wants the latest frontier capability and accepts preview risk

## 3. Prompt System Stack

A strong prompt system usually has six layers.

1. `Role`: who the model is
2. `Goal`: what must be achieved
3. `Constraints`: what must not drift
4. `Sources and Tools`: where truth comes from and what actions are allowed
5. `Output contract`: what success looks like in concrete form
6. `Operations`: how the prompt is versioned, evaluated, and cached

Long-form layout:

```xml
<persona>
  <role>...</role>
  <expertise>...</expertise>
</persona>
<task>
  <goal>...</goal>
  <success_criteria>...</success_criteria>
</task>
<constraints>
  ...
</constraints>
<sources>
  ...
</sources>
<tools>
  ...
</tools>
<output>
  ...
</output>
```

## 4. Reliability Ladder

Choose the output mechanism before polishing the prose.

1. plain text
2. sectioned markdown
3. prompt-only JSON
4. structured outputs with JSON Schema
5. function or tool calls

Decision rule:

- if humans just need to read it, markdown is often enough
- if software must consume it, move up to structured outputs or tool calls
- if downstream code depends on exact keys or enums, do not rely on prompt-only JSON

## 5. Single Prompt vs Agentic System

Use a single prompt when:

- the task is bounded and mostly one-shot
- tools are optional, not central
- memory is not essential beyond the current turn
- correctness can be enforced through structure and a schema

Promote to an agentic system when the task needs:

- decomposition into subproblems
- repeated tool interaction
- intermediate verification
- memory across steps or sessions
- specialized roles such as planner, researcher, executor, critic, synthesizer

A practical agentic stack:

1. `Planner`
2. `Researcher`
3. `Executor`
4. `Critic`
5. `Synthesizer`

## 6. Core Advanced Prompting Patterns

### 6.1 ReAct

Use ReAct when the model must reason and act in a loop.

Best for:

- web research
- tool-based QA
- debugging
- multi-step execution

Design note:

- make tool triggers explicit
- say when the model must search and when it may answer directly
- tell the model what to do after a failed tool call

### 6.2 Reflection

Use Reflection when a first draft is useful but not reliable enough.

Best for:

- reports
- requirements docs
- summaries
- persuasive writing

Design note:

- critique quality depends on the rubric

### 6.3 Reflexion

Use Reflexion when the model can improve from prior attempts.

Best for:

- coding agents
- search-heavy tasks
- repeated experiments

Design note:

- store short, generalizable lessons, not full transcript dumps

### 6.4 Self-Refine

Use Self-Refine for low-infrastructure polishing loops.

Best for:

- rewrites
- style cleanup
- prompt polishing
- structured cleanup

Design note:

- cap iterations to avoid drift

### 6.5 Routing

Routing classifies the task and sends it to the right prompt, tool chain, or model profile.

Examples:

- factual lookup -> search-first prompt
- code generation -> Context7 + schema-first coding prompt
- source-grounded analysis -> retrieval + citation rules
- high-risk prompt -> scope limits + escalation path + structured refusal behavior

## 7. Tool Design Principles

Reliable tool prompts define:

1. when the tool is mandatory
2. which tool to prefer
3. how to form arguments
4. how to validate tool results
5. what to do after failure

Vendor notes:

- Anthropic strongly emphasizes detailed tool descriptions over examples
- OpenAI and Gemini both benefit from schema-rich function definitions and explicit downstream contracts
- when tool results feed more reasoning, keep result formatting predictable

## 8. Retrieval And Search Policy

Use web search when:

- the task depends on current facts
- the user asks for latest, current, today, recent, or new
- recommendations could be affected by market changes

Use file search or retrieval when:

- the answer should come from a supplied corpus
- the context is too large to paste into every request
- citation to uploaded or indexed files matters

Use both when:

- the system must combine internal knowledge bases with current external facts

## 9. Cache-Aware Context Architecture

### 9.1 Global rule

Place stable content before volatile content.

Recommended order:

1. system or developer instructions
2. tool definitions
3. schemas and rubrics
4. reusable examples
5. retrieved references
6. live user input

### 9.2 OpenAI notes

Official OpenAI guidance says cache hits require exact prefix matches. Put static instructions and examples first, variable user-specific content last, and use `prompt_cache_key` consistently for shared long prefixes.

Also note:

- caching is available automatically on recent models for prompts of 1024 tokens or more
- `prompt_cache_retention` can extend retention up to 24 hours on supported models
- structured output schemas and tool definitions can participate in caching

### 9.3 Anthropic notes

Official Anthropic guidance says prompt caching builds prefixes in this order:

1. `tools`
2. `system`
3. `messages`

Also note:

- automatic caching now exists in addition to block-level `cache_control`
- changing `tool_choice` can invalidate later cache layers
- 5-minute TTL is the default and 1-hour TTL is optional at added cost

### 9.4 Gemini notes

Gemini context caching is explicit. You create reusable cached content resources and then reference them from generation requests.

Use it when:

- a long document or media input is reused across multiple questions
- a chat session accumulates a reusable history
- cost and latency matter across repeated large-context calls

## 10. Structured Outputs And Schemas

Prefer vendor-native schema enforcement whenever possible.

OpenAI:

- use Structured Outputs for type-safe JSON with explicit refusal detection

Anthropic:

- use tools for schema-constrained JSON when you need machine-readable outputs

Gemini:

- use `response_json_schema` with `response_mime_type: application/json`
- remember Gemini supports only a subset of the JSON Schema spec

## 11. Production Prompt Ops

Treat prompts like deployable artifacts.

Minimum production package:

1. prompt id or name
2. prompt version
3. model alias or snapshot policy
4. output schema
5. eval set
6. pass or fail thresholds
7. rollback trigger

Good rollback triggers:

- accuracy drops below threshold
- formatting compliance breaks
- tool-call correctness regresses
- latency or cost blows past budget
- a vendor alias silently changes behavior

## 12. Failure Modes And Fixes

Common failures:

- vague task objective
- missing source of truth
- tool choice left implicit
- output format described only in prose
- too many priorities with no ranking
- prompt cache destroyed by moving volatile content too early
- no eval suite for regressions

Standard fixes:

- rewrite the goal as a measurable success criterion
- enforce a schema
- separate hard constraints from soft style preferences
- add explicit tool rules
- move volatile content later
- reduce task scope or route to an agentic workflow
- add regression evals before rollout

## 13. Source Notes

This knowledge base is grounded in official vendor documentation checked on `2026-03-25`.

Key source families:

- OpenAI models, structured outputs, web search, file search, and prompt caching docs
- Anthropic models overview, tool-use docs, prompt caching docs, and 2026 Claude release announcements
- Gemini models, structured outputs, function calling, and caching docs

Use `vendor_model_guide.md` for the current model tables and direct URLs.
