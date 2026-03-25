# Visualization Formats

`render_mindmap.py` supports two input shapes.

## 1. Outline Format

Best for normal mind maps.

```text
Seed: Urban gardening

- Motivation
  - Self-sufficiency
  - Stress relief
- Spaces
  - Balconies
  - Rooftops
- Community
  - Shared plots
  - Neighborhood swaps

@links
Motivation -> Community | reinforces
Spaces -> Community | enables
```

Rules:

- Use `Seed:` for the center node.
- Use bullets with two-space indentation.
- Use `@links` for optional cross-branch connections.
- Cross-links use `source -> target | optional label`.

## 2. JSON Format

Best when labels or cross-links are generated programmatically.

```json
{
  "root": "Urban gardening",
  "branches": [
    {
      "label": "Motivation",
      "children": ["Self-sufficiency", "Stress relief", "Beauty"]
    },
    {
      "label": "Spaces",
      "children": ["Balconies", "Rooftops", "Windowsills"]
    }
  ],
  "links": [
    {"source": "Motivation", "target": "Spaces", "label": "shapes choices"}
  ]
}
```

## Command Examples

```bash
python3 scripts/render_mindmap.py references/example.txt -o /tmp/mindmap.svg
python3 scripts/render_mindmap.py references/example.json --format json --render-format png
```
