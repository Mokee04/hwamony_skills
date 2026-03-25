# Testing Playbook

## Core Test Categories

Always consider:

- happy path
- ambiguous input
- malformed input
- long context
- instruction conflict
- tool failure
- history continuity
- summary drift

## Agent-System Additions

For agentic systems also test:

- planner quality
- tool selection quality
- retry behavior
- stop condition behavior

## Test Sequence

1. define scenario
2. define expected behavior
3. define pass or fail criteria
4. run the system
5. store artifacts
6. score with the rubric

## Notes

- prefer a small, representative test set first
- expand only after the basics work
- keep the same inputs across iterations when measuring improvement
