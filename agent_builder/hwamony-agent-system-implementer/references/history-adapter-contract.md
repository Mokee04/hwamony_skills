# History Adapter Contract

## Goal

Implement history in three layers:

1. canonical transcript
2. reducer
3. vendor adapter

## Canonical Types

Use simple internal types such as:

- `CanonicalTurn`
- `ToolCallTurn`
- `ToolResultTurn`
- `SummaryTurn`

Minimum fields:

- `turn_id`
- `timestamp`
- `role`
- `kind`
- `text`
- `tool_name`
- `tool_payload`
- `vendor_metadata`

## Store Layer

Persist:

- full canonical transcript
- rolling summary if used
- vendor session pointers such as response IDs or interaction IDs

## Reducer Layer

Implement the reducer separately from vendor APIs.

Recommended reducers:

- `build_full_replay()`
- `build_recent_window()`
- `build_summary_plus_recent()`
- `build_tool_pinned_context()`

## Vendor Adapter Layer

### OpenAI Adapter

Support:

- `server_chain` using `previous_response_id`
- `manual_replay` using explicit input history

Store:

- response ID
- previous response ID
- model used

### Anthropic Adapter

Support:

- full stateless replay
- cache-friendly separation of tools and system prompt

Store:

- replayable message list
- tool results with explicit typing

### Gemini Adapter

Support:

- SDK chat mode
- stateless replay
- chained interactions via previous interaction ID

Store:

- interaction ID when used
- model config that must be re-applied each turn

## Config File

Write a `history_policy.yaml` containing:

- canonical store path
- reducer type
- summary trigger
- pinned kinds
- vendor adapter mode
- max recent turns
