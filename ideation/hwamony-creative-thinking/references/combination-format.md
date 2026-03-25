# Combination Formats

Use `combine_options.py` when grouped possibilities should be combined across axes.

## Outline Input

```text
Audience:
- commuters
- students

Value:
- calm
- speed

Form:
- earbuds
- speaker
```

## JSON Input

```json
{
  "axes": {
    "Audience": ["commuters", "students"],
    "Value": ["calm", "speed"],
    "Form": ["earbuds", "speaker"]
  }
}
```

## Commands

```bash
python3 scripts/combine_options.py ideas.txt --size 2
python3 scripts/combine_options.py ideas.txt --size 3 --max-combos 20 -o /tmp/combinations.md
python3 scripts/combine_options.py ideas.json --format json --size 2
```

## Notes

- Use pairwise combinations first for signal.
- Use 3-way combinations only when the axes are already clean.
- Do not dump every possible combination if the list explodes. Sample the most informative combinations and interpret them.
