# Implementation Checklist

## Prompts

- create system prompt
- create developer prompt if needed
- align prompt with chosen architecture

## Configs

- create `model_config.yaml`
- create `history_policy.yaml`
- record vendor and framework choices

## Runtime Code

- create entry point
- create provider client wrapper
- create history store
- create history reducer
- create vendor adapters

## Quality Checks

- keep canonical history independent from vendor projection
- keep provider code isolated
- keep config values readable and editable
- keep evaluation handoff easy
