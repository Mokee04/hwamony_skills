---
name: hwamony-skill-showcase
description: Turn a local skill or skill repository into a public-facing showcase with clearer positioning, SEO-friendly README structure, example prompts, demo ideas, discoverability improvements, and launch-ready GitHub copy. Use when the user wants to publish a skill, improve GitHub or search discoverability, rewrite documentation for humans, prepare a repo for stars, or create concise showcase copy for directories, releases, or awesome lists.
---

# Hwamony Skill Showcase

## Overview

Use this skill when the user has already built a skill, but the presentation is not yet doing the work.

This skill reframes the asset for public discovery: identify what problem the skill solves, who should care, what proof is available, and how to present it in a README, category intro, repo blurb, demo prompt set, repository description, topics, and launch copy without overselling.

Prefer evidence over hype. Strong public docs should make the skill easier to trust and easier to try in under 5 minutes.

Treat the repository like a product page for technical users, not a filing cabinet. The first screen should make a stranger think:

- `I get what this is`
- `I see why this is different`
- `I know how to try it right now`
- `I believe the repo can back up its promise`

## Best Fits

Use this skill for requests such as:

- "make this skill publishable"
- "rewrite the README so people instantly get it"
- "turn this into a showcase repo"
- "help this skill get discovered on GitHub"
- "write example prompts and demo copy"
- "prepare this for an awesome list submission"
- "make the documentation friendlier for humans"

Good targets:

- a single `SKILL.md` that needs a friendlier public explanation
- a category folder that needs a stronger introduction
- a root repo README that currently lists files but does not sell the value
- a release, announcement, or submission blurb for a skill collection

## Outcome

Default outputs should include only the pieces that materially help the user right now.

Common deliverables:

- a short tagline or "about" phrase that makes the asset memorable
- a one-line value proposition
- a sharper README opening
- SEO-friendly phrasing that still reads naturally to humans
- "who this is for" and "when to use it"
- 3-5 example prompts
- 3-5 creative showcase examples that make the skill feel immediately worth trying
- a quickstart or first-run path
- a demo scenario or proof checklist
- GitHub repository description and topics
- release note copy
- awesome-list submission blurb
- collection integration cleanup when a skill needs to be folded into the `hwamony-` family

If the user asks for code changes, update the relevant files directly instead of only proposing text in chat.

When the user gives only partial context, do not stall by leading with requests for more files.

Default to a useful first draft that the user can paste or react to immediately, then add a short note about what extra context would make it more precise.

## Workflow

Follow this sequence unless the user asks for only one specific output.

1. Inspect the skill or repo structure.
2. Identify the real user job, audience, and proof points.
3. Extract the strongest positioning and headline.
4. Draft or rewrite the public-facing documentation.
5. Add examples, demos, and discovery metadata.
6. Normalize collection integration details when needed.
7. Flag proof gaps that weaken credibility.

## Repository Showcase Patterns

Use these patterns when the user wants a GitHub-first presentation, especially for open-source skills, agent systems, or workflow repos.

### 1. Lead With A Memorable Promise

Strong repos tend to have a short line that can function as the GitHub "About" text, tagline, and mental handle for the project.

Examples of the pattern:

- a short methodology claim
- a "what it becomes for you" phrase
- a single differentiator with attitude

Good outputs here are usually:

- `3-7 word tagline`
- `100-160 character GitHub description`
- `1 sentence value proposition`

### 2. Sell The Transformation, Not Just The Inventory

Do not open with a directory listing or a feature dump.

Instead, show the motion:

- messy starting point
- what the repo changes
- what the user gets after following it

When the source material supports it, a short "how it works" narrative often beats a flat feature list.

### 3. Put "Try It Now" Near The Top

High-performing open-source READMEs reduce the distance between curiosity and first use.

Bring one of these close to the opening:

- install or quickstart command
- first prompt to try
- "verify installation" step
- "start here" path for the primary persona

Do not bury the first usable action below long philosophy or inventory sections.

### 4. Turn Features Into Benefit-Led Blocks

When listing capabilities, phrase them as mini-promises with proof rather than nouns alone.

Prefer:

- short headline + concrete payoff
- differentiator + mechanism
- workflow step + resulting artifact

Avoid:

- undifferentiated bullet piles
- adjectives without mechanism
- repeated variants of `powerful`, `advanced`, or `comprehensive`

### 5. Name The Workflow

If the repo has a repeatable process, turn it into a named sequence that visitors can picture.

This is especially strong for:

- methodologies
- agent workflows
- skill collections
- research pipelines
- build or evaluation systems

### 6. Sync The Public Surfaces

A well-packaged repo does not stop at `README.md`.

Check alignment across:

- GitHub "About" sentence
- repository topics
- badges or credibility signals
- docs link
- install path
- release or changelog surfaces
- community or support links

If the README says one thing and the repo metadata says another, tighten the message.

## Step 1: Inspect The Asset

Start from the files that already exist.

Look for:

- `SKILL.md`
- root or category `README.md`
- `agents/openai.yaml`
- scripts that can support a demo
- references that show depth or rigor
- GitHub-facing metadata such as repository description, topics, badges, docs links, install instructions, and community links

Do not invent capabilities that are not supported by the files.

When the repository has multiple skills, first identify:

- the flagship skills
- which skills are mature enough to promote
- which files are acting as the public entry point

When a local skill is being folded into this collection, treat the following as the default procedure instead of something to ask permission for:

- rename the folder into the `hwamony-` namespace when it is not already there
- rename the skill frontmatter `name` into the same `hwamony-` namespace
- create or rewrite a public-facing `README.md`
- update `agents/openai.yaml` so the UI text matches the new identity
- add the skill to the relevant category `README.md`
- add the skill to the root `README.md` when it belongs in the shareable collection
- validate the skill after the rename and doc pass

Only pause to ask if the rename would create a collision, break an explicit dependency, or conflict with an existing naming convention the repo already uses on purpose.

## Step 2: Extract Positioning

Before rewriting anything, answer these questions:

- what concrete problem does this skill solve?
- who feels that problem strongly enough to care?
- what makes this skill more useful than a generic assistant answer?
- what proof exists in the repo?
- what should the user be able to do after 5 minutes with it?

Distill the result into:

- short tagline or "About" phrase
- one-line value proposition
- target user
- trigger situations
- outcome or artifact produced
- differentiator

If the skill is broad, narrow it to the most compelling promise rather than listing everything.

Also answer:

- what is the line that earns the scroll?
- what is the fastest believable way to try this?
- what one proof asset most reduces skepticism?

## Step 3: Choose The Right Public Surface

Match the output to the surface the user is trying to improve.

- Root repo README: explain why the collection matters, name flagship skills, and show how to try them quickly.
- Category README: explain the category's point of view, the included skills, and how they relate.
- Single skill showcase: explain when to use the skill, what happens when invoked, and show example prompts.
- Release or social post: emphasize problem, transformation, and proof in a tighter format.
- Awesome-list submission: keep it short, concrete, and legible to maintainers scanning many submissions.
- GitHub repository metadata: align the tagline, "About" sentence, topics, and primary link with the README promise

If the task is a collection-integration pass for one skill, the minimum public surfaces to update are:

- the skill's `SKILL.md` identity
- the skill's `README.md`
- the skill's `agents/openai.yaml`
- the category `README.md`
- the root `README.md` if the skill belongs in the shared collection

Use [references/readme-structure.md](references/readme-structure.md) when restructuring README content.

## Step 4: Write Human-Friendly Docs

Optimize for fast comprehension.

Good README openings usually answer, in order:

1. what this is
2. why it matters
3. who it is for
4. why it is different
5. how to try it now

For GitHub-facing open-source repos, a strong first screen often looks more like this:

1. title
2. short tagline
3. one-line value proposition
4. 2-4 sentence explanation with target user and differentiator
5. quickstart or first prompt
6. 3-5 benefit-led highlights
7. named workflow or "how it works"

When discoverability matters, make the first screen legible to both people and search engines:

- place the core job words early in the title, one-liner, and opening paragraph
- name the asset type clearly, such as `skill`, `workflow`, `README`, `GitHub repository`, or `agent skill`
- use concrete discovery terms when they are real, such as `GitHub discoverability`, `repository description`, `topics`, `README`, `launch copy`, or `SEO-friendly`
- keep phrasing natural; do not repeat keywords mechanically

Prefer:

- a memorable line plus a concrete line
- concrete nouns over abstract claims
- examples over adjectives
- one strong promise over five weak ones
- legible sections over giant prose blocks

Avoid:

- vague "AI-powered" filler
- repetitive benefit lists
- claiming production quality without evidence
- hiding the quickstart below long licensing text

When editing copy:

- preserve the author's tone when possible
- compress repetitive explanation
- keep safety boundaries visible for high-risk domains
- make the first screen useful even to someone who never heard of the project
- if context is incomplete, still lead with a best-effort first screen instead of an intake checklist
- use emojis deliberately when they improve scanability, warmth, or section signaling in a README

Emoji guidance:

- use 0-6 emojis across a typical README, not an emoji on every line
- best uses: section headers, quickstart cues, highlights, warnings, artifacts, and next steps
- prefer clear signals such as launch, spark, search, note, warning, tool, or folder cues over random decoration
- keep the emoji choice consistent with the skill's tone and audience
- skip emojis entirely when the repo tone is formal, enterprise-heavy, or safety-sensitive
- do not let emojis replace the actual meaning of the heading or sentence

When context is partial, the opening should still do real work.

Start with a concrete user, problem, or outcome before any caveat.

Good opening shape under uncertainty:

1. one-line promise
2. README-ready intro or showcase blurb
3. "Why It Is Different" block
4. 2 safe examples
5. 2 hook examples
6. one short proof or limitation note
7. one short note on what extra context would sharpen the copy

Do not open with:

- `paste the files`
- `I need more context first`
- a long audit checklist

unless the user explicitly asked for a repo-specific audit and nothing reusable can be drafted honestly.

Use [references/showcase-output-spec.md](references/showcase-output-spec.md) for the standard output set.

## Step 5: Add Discovery And Proof

A strong showcase is not only good prose. It also lowers the cost of belief.

Add or improve:

- short tagline variants when the current opening has no hook
- example prompts
- more vivid, tempting use examples that make the skill feel desirable rather than merely understandable
- expected artifacts or outcomes
- demo steps
- README openings that naturally include high-intent search terms when appropriate
- GitHub description
- GitHub "About" text when the repo has a weaker short description than the README
- suggested repository topics
- release title and release notes
- awesome-list or directory submission copy

If the repo lacks proof, say so plainly and recommend the lightest proof asset that would help most:

- one realistic before/after example
- one screenshot or terminal transcript
- one sample artifact produced by the skill
- one quickstart path with expected output

Use [references/distribution-checklist.md](references/distribution-checklist.md) when preparing launch surfaces.

When writing examples, do not stop at safe generic prompts.

When the user explicitly asks for SEO or search visibility help:

- improve the README opening first
- make the repository description concrete and keyword-aware
- suggest focused topics rather than broad buzzwords
- prefer discoverability language that matches the actual artifact
- avoid promising Google ranking outcomes you cannot verify

Good showcase examples should:

- sound like a real user with a high-value problem
- make the before/after transformation visible
- hint at why this skill beats a generic assistant answer
- feel specific enough that someone wants to try the prompt immediately

At least one example in a public showcase pack should function like a "hero demo":

- the starting mess is obvious
- the artifact is desirable
- the transformation can be imagined in one read

Avoid example prompts that sound like placeholders, such as:

- `help me with this skill`
- `improve my prompt`
- `do some research`

Prefer examples that create curiosity or ambition, such as:

- turning a messy internal workflow into a publishable open-source asset
- narrowing a vague market question into a reusable research pack
- finding the hidden product problem before brainstorming features
- converting an AI idea into a build-ready architecture brief

At least one hook example should show a visible transformation:

- messy starting point
- meaningful stakes
- artifact or outcome the reader wants now

When the user asks for examples, prompt rewrites, or showcase prompts, do not answer with planning notes, brainstorms, or descriptions of what you could generate.

Return the examples themselves.

Default structure for example-focused requests:

1. one-line diagnosis of why the current examples feel weak
2. 2 safe examples
3. 2 hook examples
4. 2 `bland -> better` rewrites
5. one sentence on why the stronger examples beat a generic assistant prompt
6. one proof gap, limitation, or next proof asset

Avoid openings like:

- `I could frame this as`
- `I might structure it like`
- `maybe I should`
- `send the skill and I can tailor this`

unless that tailoring note is the final line after the actual example pack.

Do not offload copy generation to extra copywriting models or comparison scripts.

The agent using this skill should read the repo evidence, extract the differentiators, and write the copy directly.

If the wording still feels uncertain, draft 2-3 variants yourself and choose the strongest one based on:

- clarity in the first screen
- specificity of the user and outcome
- visible contrast against generic alternatives
- honesty about proof and limits

## Step 6: Protect Credibility

Public docs should make adoption easier without overstating the asset.

Always distinguish:

- verified capability vs hoped-for capability
- current examples vs future roadmap
- broad applicability vs the best-fit use case

If you borrow a bold open-source pattern such as a sharp tagline or ambitious differentiator, back it with one of:

- mechanism
- workflow
- proof asset
- credible limitation note

If the documentation is weak because the skill itself is underspecified, say that the positioning problem is partly a product-definition problem.

Do not polish around missing substance.

## Response Pattern

When the user asks for recommendations only, return:

- the core positioning
- the highest-impact doc changes
- the strongest next action

When the user asks for copy or showcase help and the context is incomplete, still return a starter pack:

- short tagline
- one-line value proposition
- short README opening
- "Why It Is Different" section
- 2 safe examples
- 2 hook examples
- one proof gap, limit, or next demo asset
- the single highest-impact proof asset to add next

If the user wants alternate phrasings, generate them directly in the response as compact variants instead of invoking another model.

When the user asks for edits, update files directly and then summarize:

- what changed
- what message the new docs now lead with
- which GitHub-facing surfaces are now aligned
- what proof or demo gap still remains

When a non-`hwamony` skill is being adopted into this collection, do not stop after the first file edit.

Carry the work through the full integration pass by default:

- rename the skill into the `hwamony-` namespace
- add the skill README
- sync `agents/openai.yaml`
- update category and root collection docs
- validate the result

## Resources

Read these when needed:

- [references/showcase-output-spec.md](references/showcase-output-spec.md): standard deliverables and copy blocks
- [references/readme-structure.md](references/readme-structure.md): practical README section order
- [references/distribution-checklist.md](references/distribution-checklist.md): GitHub and launch-surface checklist
