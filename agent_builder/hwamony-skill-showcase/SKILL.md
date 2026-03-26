---
name: hwamony-skill-showcase
description: Turn a local skill or skill repository into a public-facing showcase with clearer positioning, README structure, example prompts, demo ideas, and launch-ready GitHub copy. Use when the user wants to publish a skill, improve discoverability, rewrite documentation for humans, prepare a repo for stars, or create concise showcase copy for directories, releases, or awesome lists.
---

# Hwamony Skill Showcase

## Overview

Use this skill when the user has already built a skill, but the presentation is not yet doing the work.

This skill reframes the asset for public discovery: identify what problem the skill solves, who should care, what proof is available, and how to present it in a README, category intro, repo blurb, demo prompt set, and launch copy without overselling.

Prefer evidence over hype. Strong public docs should make the skill easier to trust and easier to try in under 5 minutes.

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

- a one-line value proposition
- a sharper README opening
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
3. Extract the strongest positioning.
4. Draft or rewrite the public-facing documentation.
5. Add examples, demos, and discovery metadata.
6. Normalize collection integration details when needed.
7. Flag proof gaps that weaken credibility.

## Step 1: Inspect The Asset

Start from the files that already exist.

Look for:

- `SKILL.md`
- root or category `README.md`
- `agents/openai.yaml`
- scripts that can support a demo
- references that show depth or rigor

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

- one-line value proposition
- target user
- trigger situations
- outcome or artifact produced
- differentiator

If the skill is broad, narrow it to the most compelling promise rather than listing everything.

## Step 3: Choose The Right Public Surface

Match the output to the surface the user is trying to improve.

- Root repo README: explain why the collection matters, name flagship skills, and show how to try them quickly.
- Category README: explain the category's point of view, the included skills, and how they relate.
- Single skill showcase: explain when to use the skill, what happens when invoked, and show example prompts.
- Release or social post: emphasize problem, transformation, and proof in a tighter format.
- Awesome-list submission: keep it short, concrete, and legible to maintainers scanning many submissions.

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
2. who it is for
3. why it is different
4. how to try it now

Prefer:

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

- example prompts
- more vivid, tempting use examples that make the skill feel desirable rather than merely understandable
- expected artifacts or outcomes
- demo steps
- GitHub description
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

Good showcase examples should:

- sound like a real user with a high-value problem
- make the before/after transformation visible
- hint at why this skill beats a generic assistant answer
- feel specific enough that someone wants to try the prompt immediately

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

If the documentation is weak because the skill itself is underspecified, say that the positioning problem is partly a product-definition problem.

Do not polish around missing substance.

## Response Pattern

When the user asks for recommendations only, return:

- the core positioning
- the highest-impact doc changes
- the strongest next action

When the user asks for copy or showcase help and the context is incomplete, still return a starter pack:

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
