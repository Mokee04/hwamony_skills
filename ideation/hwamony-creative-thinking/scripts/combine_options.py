#!/usr/bin/env python3
"""Generate pairwise or higher-order combinations from grouped idea axes."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Axis:
    name: str
    items: list[str]


def parse_outline(text: str) -> list[Axis]:
    axes: list[Axis] = []
    current_name: str | None = None
    current_items: list[str] = []

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.endswith(":") and not line.startswith("- "):
            if current_name:
                axes.append(Axis(current_name, current_items))
            current_name = line[:-1].strip()
            current_items = []
            continue
        if line.startswith("- "):
            if not current_name:
                raise ValueError("Bullet items must appear under an axis heading ending with ':'.")
            current_items.append(line[2:].strip())
            continue
        raise ValueError(f"Unsupported line: {line}")

    if current_name:
        axes.append(Axis(current_name, current_items))

    if len(axes) < 2:
        raise ValueError("Provide at least 2 axes with bullet items.")
    if any(not axis.items for axis in axes):
        raise ValueError("Every axis must contain at least 1 item.")
    return axes


def parse_json_input(text: str) -> list[Axis]:
    payload = json.loads(text)
    if not isinstance(payload, dict) or "axes" not in payload:
        raise ValueError("JSON must contain an 'axes' object.")
    axes = []
    for name, items in payload["axes"].items():
        if not isinstance(items, list) or not items:
            raise ValueError("Each axis must map to a non-empty list.")
        axes.append(Axis(str(name), [str(item) for item in items]))
    if len(axes) < 2:
        raise ValueError("Provide at least 2 axes.")
    return axes


def read_axes(path: str, fmt: str) -> list[Axis]:
    if path == "-":
        text = sys.stdin.read()
    else:
        text = Path(path).read_text(encoding="utf-8")

    if fmt == "auto":
        fmt = "json" if text.lstrip().startswith("{") else "outline"

    if fmt == "outline":
        return parse_outline(text)
    if fmt == "json":
        return parse_json_input(text)
    raise ValueError(f"Unsupported format: {fmt}")


def generate_combos(axes: list[Axis], size: int, max_combos: int) -> list[tuple[tuple[str, str], ...]]:
    combos: list[tuple[tuple[str, str], ...]] = []
    axis_groups = list(itertools.combinations(axes, size))
    for group in axis_groups:
        value_lists = [[(axis.name, item) for item in axis.items] for axis in group]
        for combo in itertools.product(*value_lists):
            combos.append(combo)
            if len(combos) >= max_combos:
                return combos
    return combos


def render_markdown(axes: list[Axis], combos: list[tuple[tuple[str, str], ...]], size: int) -> str:
    lines = ["# Combination Output", "", "## Axes", ""]
    for axis in axes:
        lines.append(f"- **{axis.name}**: {', '.join(axis.items)}")
    lines.extend(["", f"## {size}-Way Combinations", ""])
    for index, combo in enumerate(combos, start=1):
        combo_text = " + ".join(f"{axis}={item}" for axis, item in combo)
        lines.append(f"{index}. {combo_text}")
    lines.extend(
        [
            "",
            "## Insight Prompts",
            "",
            "- Which combinations recur around the same need, tension, or opportunity?",
            "- Which combinations feel strong because two axes reinforce each other?",
            "- Which combinations reveal a contradiction worth exploring?",
            "- Which combinations are niche but surprisingly compelling?",
            "- Which 3 combinations deserve deeper human interpretation rather than more expansion?",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate structured combinations from grouped ideas for convergent analysis."
    )
    parser.add_argument("input", nargs="?", default="-", help="Input file path, or '-' for stdin.")
    parser.add_argument("-o", "--output", help="Optional output markdown path.")
    parser.add_argument("--format", choices=["auto", "outline", "json"], default="auto")
    parser.add_argument("--size", type=int, default=2, help="Combination size, usually 2 or 3.")
    parser.add_argument("--max-combos", type=int, default=30, help="Maximum number of combinations to emit.")
    args = parser.parse_args()

    try:
        axes = read_axes(args.input, args.format)
        if args.size < 2:
            raise ValueError("--size must be 2 or greater.")
        if args.size > len(axes):
            raise ValueError("--size cannot exceed the number of axes.")
        combos = generate_combos(axes, args.size, args.max_combos)
        markdown = render_markdown(axes, combos, args.size)
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(markdown, encoding="utf-8")
            print(output_path)
        else:
            print(markdown)
        return 0
    except Exception as exc:  # pragma: no cover - CLI guard
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
