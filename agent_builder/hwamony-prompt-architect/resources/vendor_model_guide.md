# Vendor Model Guide

As of `2026-03-25`, this guide summarizes the official model lineups and the most useful routing shortcuts for prompt-driven systems.

Use this file for:

- vendor selection
- model routing
- stable vs preview tradeoffs
- prompt-system defaults

## 1. OpenAI

OpenAI's official models pages currently position `gpt-5.4` as the default frontier choice for complex professional work, with `gpt-5-mini` and `gpt-5-nano` as cost and latency variants.

| Model | Status | Official positioning | Best use | Main advantage | Main caution |
| --- | --- | --- | --- | --- | --- |
| `gpt-5.4` | stable | Best intelligence at scale for agentic, coding, and professional workflows | default choice for hard prompt systems | strong reasoning, wide tool support, 1M context, structured outputs | costs more than mini and can be overkill for routine tasks |
| `gpt-5.4-pro` | stable | Smarter and more precise premium GPT-5.4 route | hardest planning, verification, and premium quality mode | strongest OpenAI route for difficult tasks | higher latency and cost; verify current feature support on the model page before rollout |
| `gpt-5-mini` | stable | Near-frontier intelligence for cost-sensitive, low-latency, high-volume workloads | high-volume production prompts and agent subtasks | major cost savings with still-strong capability | less headroom on ambiguous or unusually hard tasks |
| `gpt-5-nano` | stable | Fastest, most cost-efficient version of GPT-5 | classification, extraction, summarization, routing | cheapest OpenAI route | weakest option for complex planning |
| `gpt-4.1` | stable | Smartest non-reasoning model | deterministic non-reasoning workflows and legacy compatibility | useful when you want strong capability without reasoning behavior | not the latest frontier reasoning model |
| `o3-deep-research` | stable specialized | Most powerful deep research model | long-running cited research workflows | purpose-built for multi-step research across web and data sources | slower and more expensive than general-purpose defaults |

### OpenAI routing shortcuts

- default hard work: `gpt-5.4`
- premium hardest tasks: `gpt-5.4-pro`
- low-latency production: `gpt-5-mini`
- cheap routing, extraction, classification: `gpt-5-nano`
- deep research workflow: `o3-deep-research`

### OpenAI prompt-system notes

- prefer Responses API for modern tool-using systems
- prefer Structured Outputs over prompt-only JSON formatting
- web search is the official route for latest information with citations
- file search is the official hosted route for semantic plus keyword retrieval over uploaded corpora
- prompt caching works best when stable content is placed first and volatile content last

## 2. Anthropic

As of `2026-03-25`, Anthropic's latest model announcements and product pages show `Claude Opus 4.6`, `Claude Sonnet 4.6`, and `Claude Haiku 4.5` as the most relevant current routes.

| Model | Status | Official positioning | Best use | Main advantage | Main caution |
| --- | --- | --- | --- | --- | --- |
| `claude-opus-4-6` | stable | Most capable Anthropic model to date | deepest reasoning, difficult agent planning, high-stakes coding | strongest Claude route for long-horizon agentic work | premium price and slower than Sonnet or Haiku |
| `claude-sonnet-4-6` | stable | Superior intelligence for agents and coding | best general Claude default | strong coding and agent performance with much better price-performance than Opus | not the absolute strongest option for the hardest edge cases |
| `claude-haiku-4-5` | stable | Fastest, most cost-efficient Claude model | scaled deployments, sub-agents, latency-sensitive tasks | high capability at low cost and high speed | less headroom than Sonnet or Opus for hardest tasks |

### Anthropic routing shortcuts

- default Claude choice: `claude-sonnet-4-6`
- hardest Claude tasks: `claude-opus-4-6`
- fast sub-agents and high-volume use: `claude-haiku-4-5`

### Anthropic prompt-system notes

- Anthropic strongly emphasizes detailed tool descriptions
- tool descriptions matter more than examples for tool performance
- prompt caching is highly explicit and cache order is `tools` -> `system` -> `messages`
- changing `tool_choice` can invalidate later cache layers
- Sonnet and Opus are strong choices when the tool landscape is ambiguous

## 3. Gemini

As of `2026-03-25`, Google shows a split between stable `Gemini 2.5` production models and newer `Gemini 3` preview models.

| Model | Status | Official positioning | Best use | Main advantage | Main caution |
| --- | --- | --- | --- | --- | --- |
| `gemini-2.5-pro` | stable | Most advanced stable Gemini model for complex tasks | stable production reasoning and coding | strongest stable Gemini route | slower and more expensive than Flash variants |
| `gemini-2.5-flash` | stable | Best price-performance model for low-latency, high-volume tasks that require reasoning | cost-efficient production prompts | strong speed-cost balance | less headroom than Pro |
| `gemini-2.5-flash-lite` | stable | Fastest and most budget-friendly multimodal model in the 2.5 family | cheapest Gemini route | speed and low cost | least capable among current Gemini text routes |
| `gemini-3.1-pro-preview` | preview | Advanced intelligence, complex problem-solving, powerful agentic and vibe coding capabilities | newest Gemini frontier preview | most current preview intelligence | preview risk and deprecation churn are possible |
| `gemini-3-flash-preview` | preview | Frontier-class performance at a fraction of the cost | newer fast preview route | strong preview speed-performance balance | preview stability risk |
| `gemini-3.1-flash-lite-preview` | preview | Frontier-class performance at a fraction of the cost in a lighter tier | preview low-cost route | current preview speed and budget option | preview stability risk |

### Gemini routing shortcuts

- safest stable default: `gemini-2.5-pro`
- best stable price-performance: `gemini-2.5-flash`
- cheapest stable route: `gemini-2.5-flash-lite`
- newest preview intelligence: `gemini-3.1-pro-preview`

### Gemini prompt-system notes

- Gemini has strong native structured outputs with `response_json_schema`
- Gemini supports combining tools with structured outputs on supported models
- Gemini caching is explicit through cached content resources
- stable production apps should prefer specific stable model strings over previews

## 4. Cross-Vendor Routing Heuristics

### Hardest prompt systems

- OpenAI: `gpt-5.4`
- Anthropic: `claude-sonnet-4-6`
- Gemini: `gemini-2.5-pro`

Preferred default:

- `gpt-5.4` when tool breadth, structured outputs, and modern agent tooling matter most

### Premium hardest tasks

- OpenAI: `gpt-5.4-pro`
- Anthropic: `claude-opus-4-6`
- Gemini: `gemini-3.1-pro-preview` if preview is acceptable, otherwise `gemini-2.5-pro`

### High-volume production prompts

- OpenAI: `gpt-5-mini`
- Anthropic: `claude-haiku-4-5`
- Gemini: `gemini-2.5-flash`

### Cheapest routing or extraction tier

- OpenAI: `gpt-5-nano`
- Anthropic: `claude-haiku-4-5`
- Gemini: `gemini-2.5-flash-lite`

### When structured outputs matter most

- OpenAI: very strong native Structured Outputs support
- Gemini: very strong native JSON Schema support
- Anthropic: often best solved through tool schemas and tool use patterns

### When tool descriptions matter most

- Anthropic is especially sensitive to tool-description quality

### When cache-aware prompt layout matters most

- OpenAI and Anthropic both strongly reward stable-prefix prompt design
- Gemini benefits more from explicit reusable cached content objects

## 5. Official Source Notes

Checked on `2026-03-25`.

OpenAI:

- Models overview and compare pages:
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/models/compare
  - https://developers.openai.com/api/docs/models/gpt-5.4
  - https://developers.openai.com/api/docs/models/gpt-5.4-pro
- Structured outputs:
  - https://developers.openai.com/api/docs/guides/structured-outputs
- Web search:
  - https://developers.openai.com/api/docs/guides/tools-web-search
- File search:
  - https://developers.openai.com/api/docs/guides/tools-file-search
- Prompt caching:
  - https://developers.openai.com/api/docs/guides/prompt-caching

Anthropic:

- Models overview:
  - https://platform.claude.com/docs/en/about-claude/models/overview
- Tool use:
  - https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
- Prompt caching:
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Latest model announcements:
  - https://www.anthropic.com/news/claude-opus-4-6
  - https://www.anthropic.com/news/claude-sonnet-4-6
  - https://www.anthropic.com/news/claude-haiku-4-5

Gemini:

- Models:
  - https://ai.google.dev/gemini-api/docs/models
- Structured outputs:
  - https://ai.google.dev/gemini-api/docs/structured-output
- Function calling:
  - https://ai.google.dev/gemini-api/docs/function-calling
- Caching:
  - https://ai.google.dev/api/caching
