# Risk Modes

Choose edit posture based on the target skill's downside if it drifts.

## Low Risk

Examples:

- packaging or showcase skills
- structure-heavy builder skills
- formatting and artifact scaffolds

Default posture:

- allow `automatic` autonomy mode
- let the supervisor test one bounded mutation at a time
- patch directly when a majority of shards improve
- rerun after each accepted mutation

## Medium Risk

Examples:

- research workflows
- prompt systems with live vendor guidance
- tool-integration skills

Default posture:

- prefer `guardrailed` mode
- patch directly for structure and clarity
- prefer broader shard coverage and stricter evaluator rubrics before accepting a mutation
- pause when the change affects live claims, freshness rules, or tool safety

## High Risk

Examples:

- mental health support skills
- medical, legal, or financial guidance skills
- child safety or crisis-sensitive skills

Default posture:

- use `score-only` mode
- keep a strict rerun trail
- avoid broad tone or scope rewrites without a strong failure signal
- never let workers decide whether a mutation should be kept
- require evaluator rationale to be especially explicit
