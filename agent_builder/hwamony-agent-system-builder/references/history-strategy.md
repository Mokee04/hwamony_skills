# History Strategy

## Principle

Do not let any vendor API become the source of truth.

Use:

1. canonical internal transcript
2. vendor-specific projection layer
3. replay and reduction policy

## Canonical Turn Schema

Store turns in a normalized form such as:

- `id`
- `timestamp`
- `role`
- `kind`
- `text`
- `tool_name`
- `tool_args`
- `tool_result`
- `vendor_ids`
- `tags`

Useful `kind` values:

- `message`
- `tool_call`
- `tool_result`
- `summary`
- `system_event`

## Replay Policies

Choose one primary policy:

### `full_replay`

Re-send the entire relevant transcript each turn.

Best for:

- short conversations
- Anthropic stateless flows

### `recent_window`

Keep only the last N turns plus stable instructions.

Best for:

- short-lived chat tools
- cost-sensitive systems

### `summary_plus_recent`

Keep a rolling summary and the most recent turns.

Best for:

- longer sessions
- human-assistant workflows

### `tool_pinned_summary_recent`

Keep important tool outputs pinned, plus a summary and recent turns.

Best for:

- agent systems
- workflows where tool results must not drift out of context

## Vendor Notes

### OpenAI

- Prefer Responses API for modern systems.
- Choose between `previous_response_id` chaining and explicit full replay.
- Store response IDs even when canonical history is the real source of truth.

### Anthropic

- Treat the Messages API as stateless by default.
- Keep system instructions and tools separate from replayed conversation content.
- Use prompt caching only for stable prefixes.

### Gemini

- Choose between SDK chats, full stateless replay, or `previous_interaction_id`.
- Re-apply `tools`, `system_instruction`, and generation config each turn when using interaction chaining.

## Builder Deliverable

Always record:

- chosen policy
- summary trigger
- max recent turns
- pinned artifact rules
- vendor adapter notes
