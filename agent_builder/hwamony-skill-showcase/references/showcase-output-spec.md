# Showcase Output Spec

Use this reference when the user wants public-facing packaging, not only wording tweaks.

## Core Outputs

Choose only the outputs the situation needs.

### 0. Tagline

Target length:

- 3-7 words

Job:

- give the repo a memorable handle
- work in the README opening and GitHub "About" area

Good:

- `The agent that grows with you`
- `Your coding agent just has Superpowers`

Weak:

- `A useful workflow for developers`

### 1. One-Liner

Format:

`<skill or repo name>` helps `<target user>` do `<concrete job>` with `<specific advantage>`.

Good:

- `hwamony-skill-showcase` helps skill authors turn internal agent workflows into public-facing GitHub showcases with clearer positioning and demo-ready copy.

Weak:

- `A powerful AI skill for better documentation`

### 2. Short Description

Target length:

- 100-160 characters for GitHub description or directory blurb

Must include:

- what it helps with
- a human-readable object or job
- words a relevant GitHub visitor would plausibly search for

### 3. README Opening

Default structure:

1. short tagline
2. one-line value proposition
3. 2-4 sentence explanation
4. quickstart or "start here" path
5. 3-5 benefit-led highlights
6. workflow or "how it works" section when relevant

Optional polish:

- add a small number of well-chosen emojis when they improve first-screen scanability
- common good fits: `🚀` for launch/start, `✨` for differentiation, `🧭` for guidance, `⚠️` for caveats, `📦` for artifacts, `🔎` for research
- keep usage restrained; the emoji should support the structure, not become the structure

### 4. GitHub Surface Pack

When the request is about open-source discoverability, include:

- GitHub description or "About" line
- suggested repository topics
- docs or homepage link suggestion when appropriate
- release or launch blurb if the user is preparing a public push

### 5. Example Prompts

Good example prompts:

- sound like real user requests
- are concrete enough to trigger the skill
- show breadth without becoming generic
- make the skill feel worth trying right now
- imply a meaningful transformation, not just a task category

Target:

- 3-5 prompts per flagship skill

Add a second layer when useful:

- `safe examples`: clear, practical, low-risk starter prompts
- `hook examples`: more vivid prompts that make the skill feel unusually capable or strategically useful

Good hook examples create pull. They should make a reader think:

- `I want that outcome`
- `that is more specific than the generic alternative`
- `this skill may save me real time or improve the quality of my work`

Weak:

- `Use this skill to brainstorm ideas.`
- `Use this skill to do research on a topic.`

Stronger:

- `Use this skill to figure out why users ask for more features but still churn after week one, then narrow the best intervention bets.`
- `Use this skill to turn a loose market question into a research folder with scoped batches, saved source text, and a memo I can reuse next week.`
- `Use this skill to rewrite this internal-only skill so strangers on GitHub immediately understand why it deserves a star.`

At least one prompt should act like a "hero demo" and make the transformation easy to picture in one read.

### 6. Demo Scenario

A good demo scenario includes:

- starting state
- user request
- action taken
- resulting artifact

Keep it believable. One complete realistic path is stronger than many vague ideas.

### 7. Launch Copy

Useful launch surfaces:

- GitHub repository description
- release title
- release notes
- awesome-list submission blurb
- short post opener for X or LinkedIn

## Editing Rules

- Prefer claims the repo can already support.
- Keep adjectives scarce.
- Replace "comprehensive", "powerful", "advanced", and "robust" with actual proof.
- If a quickstart exists, pull it above secondary material.
- If there is no quickstart, create the lightest believable "try it now" path.
- If there are multiple skills, highlight the top 2-3 instead of giving every item equal weight.
- Write the copy directly from the repo evidence instead of delegating wording generation to extra comparison models.
- If alternate phrasing helps, draft 2-3 variants yourself and keep only the strongest one or two.
- Emojis can be used to decorate a README when they clearly improve scanability or warmth, but keep them sparse and intentional.
