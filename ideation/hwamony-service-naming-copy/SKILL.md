---
name: hwamony-service-naming-copy
description: Generate service, product, app, or brand names plus launch-ready copy from a service introduction, PRD, landing page draft, pitch deck, memo, or rough notes. Use when Codex needs to read a service brief, research the market online, compare competitor or category naming patterns, and propose strong candidate names with taglines, headlines, subheads, positioning lines, or CTA copy.
---

# Hwamony Service Naming Copy

Turn a service brief into market-aware naming and copy recommendations. Combine structured interpretation of the brief with fresh web research so the output is imaginative, relevant, and grounded in the current category.

## Quick Start

Use this skill when the user wants:

- names for a service, product, SaaS, app, feature, or brand
- tagline, headline, subheadline, positioning line, or CTA copy
- Korean, English, or hybrid naming directions
- ideas grounded in current competitor/category language rather than pure intuition

Treat messy inputs as acceptable. The source can be a product intro, proposal, feature list, FAQ, deck excerpt, memo, or pasted notes.

If the user supplies existing candidate names, switch into critique-first mode before proposing replacements.

## Workflow

1. Read the brief and extract the minimum strategic core:
- audience
- painful problem
- promised outcome
- differentiation
- market/language scope
- tone
- hard constraints such as length, banned words, or desired style

2. Ask at most 1 or 2 tight questions only if the answer would materially change the recommendation.
Ask only about missing items such as geography/language, audience type, tone, or explicit naming constraints.
If the brief is usable, proceed with stated assumptions instead of blocking.

3. Decide 2 or 3 naming lanes before ideation. Common lanes:
- descriptive
- suggestive
- metaphorical
- invented or blended
- premium or enterprise
- friendly or consumer
- Korean
- English
- hybrid Korean-English

4. Research the live market before finalizing names.
Because naming conflict risk is time-sensitive, use web search whenever you reference existing brands, category conventions, SEO, domains, or availability.

Check for:
- direct competitors and adjacent players
- repeated category words and overused suffix/prefix patterns
- whether a candidate already belongs strongly to another company or product
- obvious negative meanings in target languages
- rough search ambiguity or discoverability issues
- handle/domain plausibility when relevant

Before presenting finalists, prepare a compact research snapshot with 2 to 4 cited examples of competitors, adjacent brands, or repeated category language. Tie this evidence directly to what naming patterns to avoid, borrow from, or differentiate against.

5. Generate a wide pool first, then narrow.
Create 20 to 40 raw ideas across multiple lanes, then shortlist 5 to 10 candidates worth presenting.
Do not present a final set that all follows the same naming pattern.

6. Score finalists with the rubric in `references/evaluation-rubric.md`.
Prefer names that are distinctive, pronounceable, memorable, aligned with the promised outcome, and broad enough to survive future product expansion.

7. Write copy for the strongest candidates.
Default deliverables:
- one-line brand essence
- 3 to 5 tagline options
- hero headline
- supporting subheadline
- 2 to 4 CTA/button options

8. End with clear caveats.
State that this is strategic naming guidance, not trademark clearance or legal advice.
If the user wants deeper legal or domain screening, say that it requires a dedicated follow-up pass.

## Research Rules

- Use current web information whenever the answer depends on competitor names, category trends, SEO, domains, or discoverability.
- Prefer primary sources: official sites, app store pages, product pages, and official social profiles.
- Cite or link sources when you mention real companies or market evidence.
- Do not present a winner without showing at least 2 pieces of live market evidence that influenced the recommendation.
- If the market is local, search in the local language as well as English.
- Avoid overfitting to a single competitor; synthesize patterns across several sources.

## Special Cases

- If the user asks for Korean, English, and hybrid outputs together, separate candidates by language bucket instead of mixing them into one list.
- If the user provides existing candidate names, evaluate those names first with the same rubric before introducing new ones.
- If the user mainly wants copy, still perform a light naming audit so the copy reflects the category and avoids incumbent language.
- If the user mainly wants names, keep the copy short but still provide at least one positioning line for the winning option.

## Output Format

Start with a compact brief summary:

- audience
- problem
- promise
- tone
- assumptions

Then include a `Research Snapshot` section with:

- 2 to 4 cited competitors, adjacent brands, or category references
- repeated wording or naming patterns observed
- what to avoid
- what whitespace or opportunity exists

Then present candidates in a clear list or table with:

- name
- lane
- why it fits
- strengths
- risks
- rough uniqueness note based on research

If the brief asked for multiple language tracks, group candidates under separate headings such as `Korean`, `English`, and `Hybrid`.
If the brief included existing candidate names, include a `Candidate Critique` section before any replacement ideas.

Then provide copy for the top 1 to 3 names:

- positioning line
- tagline options
- hero headline
- subheadline
- CTA options

Finish with:

- recommended winner
- second-best alternative
- what to validate next
- trademark or legal caution
- source links

## Quality Bar

Reject names that are:

- generic enough to disappear in search
- too close to dominant incumbents
- hard to pronounce or spell for the target market
- locked to a narrow feature if the business may expand
- clever but disconnected from the service promise

When the user wants more creativity, increase novelty but preserve strategic fit.
When the user wants safer options, bias toward clarity and lower collision risk.

Avoid these anti-patterns unless the brief explicitly wants them:

- generic AI or tech suffixes with little brand memory
- names that only describe a feature and cannot stretch with the product
- multiple finalists that sound like siblings rather than alternatives
- copy that praises the brand without stating the user outcome

## Response Skeleton

Use this compact structure by default:

1. Brief summary
2. Research Snapshot
3. Candidate Critique if existing names were provided
4. Final candidates grouped by lane or language
5. Copy for top candidates
6. Recommended winner
7. Second-best alternative
8. Next validation step
9. Trademark or legal caution
10. Sources

## Iteration Patterns

If the user asks for another round, vary one dimension at a time:

- more premium
- more playful
- shorter
- more Korean
- more global
- more B2B
- less literal
- stronger emotional language

If the user asks for only names or only copy, return only that slice, but still use the same research and evaluation logic.
If the user provides existing candidate names, critique them with the same rubric before suggesting replacements.
