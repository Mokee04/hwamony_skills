# Hwamony Creative Thinking

`hwamony-creative-thinking` helps founders, product teams, and creators turn fuzzy briefs into structured concept maps, stronger idea combinations, and a shortlist that still preserves at least one surprising but viable direction.

This skill is for moments when a generic brainstorm is not enough. It defines the core concepts behind the brief, maps them visually, combines distant branches into candidate ideas, and narrows the set without flattening everything into the same safe answer. It is especially useful when you want both better structure and more interesting options.

## ✨ Why It Is Different

- it turns the brief into core concepts before proposing solutions
- it can render a mind map with Python instead of only describing the structure in prose
- it looks for distant-branch combinations, not only obvious neighboring ideas
- it protects at least one contrarian or weird-but-viable lane so the shortlist stays creatively useful
- it can still converge into a recommendation instead of ending with a brainstorm dump

## 🧭 When To Use It

- you need to figure out what problem you are actually solving before ideating
- you want concept families and a visual map before narrowing options
- you want stronger product, feature, campaign, naming, or positioning directions
- you want an idea set that includes one surprising but still workable lane
- you plan to iterate based on feedback instead of treating the first answer as final

## 📦 What It Produces

- a compact restatement of the brief and task mode
- core concepts and concept families
- a mind map summary, and optionally a rendered SVG or PNG
- distant-concept combinations translated into candidate ideas
- a shortlist with tradeoffs
- a recommended lane plus what to refine in the next loop

## 🧠 How It Works

1. define the core concepts behind the task
2. organize them into a mind map
3. combine distant branches into stronger ideas
4. preserve a non-obvious lane while narrowing
5. revise the concept system when the user gives feedback

## 🚀 Start Here

Safe examples:

- `Use $hwamony-creative-thinking to break this onboarding problem into core concepts, show the mind map structure, and suggest 4 solution directions.`
- `Use $hwamony-creative-thinking to map out service naming directions for this AI product, then keep one safer lane and one more surprising lane in the shortlist.`

Hook examples:

- `Use $hwamony-creative-thinking to figure out whether our team is solving the wrong problem, turn the brief into a visual concept map, and then combine distant branches into 5 product bets.`
- `Use $hwamony-creative-thinking to design an indie-game sprite production system, keep one contrarian architecture alive through the shortlist, and tell us why it is weird-but-viable instead of just weird.`

## 🔎 What Makes It Worth Trying

- it is not just “more ideas”; it gives you a visible concept structure you can react to
- it handles both safe and surprising directions in the same workflow
- it works well for tasks that need feedback loops, not one-shot inspiration

## 📁 Proof In This Skill

- `scripts/render_mindmap.py` renders concept maps to SVG or PNG
- `scripts/combine_options.py` helps turn branches into structured combination sets
- `eval/` contains fixed cases and regression runs for scope control, feedback loops, and novelty preservation

## ⚠️ Boundaries

- this skill is strongest for structured ideation, not for market research by itself
- if the recommendation depends on current vendor capabilities, pricing, or live facts, those should be verified before locking a direction
- surprising lanes are meant to stay viable, not to become random speculation
