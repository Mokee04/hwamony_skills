#!/usr/bin/env python3
"""Render a mind map or semantic network to SVG/PNG using Graphviz."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Edge:
    source: str
    target: str
    label: str = ""
    style: str = "solid"
    color: str = "#7c8aa5"
    penwidth: float = 1.6


class MindMap:
    def __init__(self, root: str) -> None:
        self.root = root
        self.nodes: dict[str, str] = {}
        self.parents: dict[str, str | None] = {root: None}
        self.tree_edges: list[Edge] = []
        self.cross_edges: list[Edge] = []

    def add_node(self, node_id: str, label: str) -> None:
        self.nodes[node_id] = label

    def add_tree_edge(self, parent: str, child: str) -> None:
        self.parents[child] = parent
        self.tree_edges.append(Edge(parent, child))

    def add_cross_edge(self, source: str, target: str, label: str = "") -> None:
        self.cross_edges.append(
            Edge(
                source=source,
                target=target,
                label=label,
                style="dashed",
                color="#d67b44",
                penwidth=1.3,
            )
        )

    def level(self, node_id: str) -> int:
        depth = 0
        current = node_id
        while self.parents.get(current) is not None:
            current = self.parents[current]  # type: ignore[index]
            depth += 1
        return depth


def slugify(text: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "-", text.strip().lower()).strip("-")
    return normalized or "node"


def unique_id(base: str, taken: set[str]) -> str:
    candidate = slugify(base)
    if candidate not in taken:
        taken.add(candidate)
        return candidate
    index = 2
    while f"{candidate}-{index}" in taken:
        index += 1
    candidate = f"{candidate}-{index}"
    taken.add(candidate)
    return candidate


def parse_outline(text: str) -> MindMap:
    lines = [line.rstrip() for line in text.splitlines()]
    content_lines = [line for line in lines if line.strip()]
    if not content_lines:
        raise ValueError("Input is empty.")

    root_label = ""
    start_index = 0
    first = content_lines[0].strip()
    if first.lower().startswith("seed:"):
        root_label = first.split(":", 1)[1].strip()
        start_index = lines.index(content_lines[0]) + 1
    elif first.startswith("- ") or first.startswith("* "):
        root_label = "Mind Map"
    else:
        root_label = first
        start_index = lines.index(content_lines[0]) + 1

    mindmap = MindMap(root="root")
    mindmap.add_node("root", root_label)

    node_map: dict[str, str] = {root_label: "root"}
    taken_ids = {"root"}
    stack: list[tuple[int, str]] = [(-1, "root")]
    in_links = False

    for raw in lines[start_index:]:
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.lower() == "@links":
            in_links = True
            continue
        if in_links:
            edge = parse_link_line(stripped, node_map)
            mindmap.add_cross_edge(edge.source, edge.target, edge.label)
            continue
        if not stripped.startswith(("- ", "* ")):
            raise ValueError(f"Expected bullet item or @links section, got: {stripped}")

        indent = len(raw) - len(raw.lstrip(" "))
        if indent % 2 != 0:
            raise ValueError(f"Use multiples of two spaces for indentation: {stripped}")
        level = indent // 2
        label = stripped[2:].strip()
        if not label:
            raise ValueError("Found an empty node label.")

        while stack and stack[-1][0] >= level:
            stack.pop()
        if not stack:
            raise ValueError(f"Could not find parent for node: {label}")

        parent_id = stack[-1][1]
        node_id = unique_id(label, taken_ids)
        node_map[label] = node_id
        mindmap.add_node(node_id, label)
        mindmap.add_tree_edge(parent_id, node_id)
        stack.append((level, node_id))

    return mindmap


def parse_link_line(line: str, node_map: dict[str, str]) -> Edge:
    label = ""
    if "|" in line:
        line, label = [part.strip() for part in line.split("|", 1)]
    if "->" not in line:
        raise ValueError(f"Cross-link must use 'source -> target': {line}")
    source_label, target_label = [part.strip() for part in line.split("->", 1)]
    if source_label not in node_map:
        raise ValueError(f"Unknown cross-link source node: {source_label}")
    if target_label not in node_map:
        raise ValueError(f"Unknown cross-link target node: {target_label}")
    return Edge(node_map[source_label], node_map[target_label], label=label)


def parse_json_input(text: str) -> MindMap:
    payload = json.loads(text)
    root_label = payload.get("root") or payload.get("seed")
    if not root_label:
        raise ValueError("JSON input must include 'root' or 'seed'.")

    mindmap = MindMap(root="root")
    mindmap.add_node("root", str(root_label))

    taken_ids = {"root"}

    def add_children(parent_id: str, children: list[object]) -> None:
        for child in children:
            if isinstance(child, str):
                label = child
                nested = []
            elif isinstance(child, dict):
                label = str(child["label"])
                nested = child.get("children", [])
            else:
                raise ValueError("Children must be strings or objects with label/children.")
            node_id = unique_id(label, taken_ids)
            mindmap.add_node(node_id, label)
            mindmap.add_tree_edge(parent_id, node_id)
            add_children(node_id, nested)

    add_children("root", payload.get("branches", []))

    label_to_id = {label: node_id for node_id, label in mindmap.nodes.items()}
    for edge in payload.get("links", []):
        source = label_to_id.get(edge["source"])
        target = label_to_id.get(edge["target"])
        if not source or not target:
            raise ValueError("Cross-link references unknown source or target label.")
        mindmap.add_cross_edge(source, target, str(edge.get("label", "")))

    return mindmap


def dot_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def build_dot(mindmap: MindMap) -> str:
    lines = [
        "graph MindMap {",
        '  graph [layout=twopi, overlap=false, splines=true, ranksep=2.0, bgcolor="white", pad=0.4];',
        '  node [fontname="Helvetica", shape=box, style="rounded,filled", color="#6a7b99", penwidth=1.4];',
        '  edge [color="#7c8aa5", penwidth=1.6];',
    ]

    for node_id, label in mindmap.nodes.items():
        level = mindmap.level(node_id)
        attrs = node_attrs(label, level, node_id == "root")
        attr_str = ", ".join(f'{key}="{dot_escape(value)}"' for key, value in attrs.items())
        lines.append(f'  "{node_id}" [{attr_str}];')

    for edge in mindmap.tree_edges + mindmap.cross_edges:
        attrs = {
            "color": edge.color,
            "penwidth": f"{edge.penwidth}",
        }
        if edge.style != "solid":
            attrs["style"] = edge.style
        if edge.label:
            attrs["label"] = edge.label
            attrs["fontname"] = "Helvetica"
            attrs["fontsize"] = "10"
        attr_str = ", ".join(f'{key}="{dot_escape(str(value))}"' for key, value in attrs.items())
        lines.append(f'  "{edge.source}" -- "{edge.target}" [{attr_str}];')

    lines.append("}")
    return "\n".join(lines) + "\n"


def node_attrs(label: str, level: int, is_root: bool) -> dict[str, str]:
    if is_root:
        return {
            "label": label,
            "shape": "ellipse",
            "fillcolor": "#1f4b99",
            "fontcolor": "white",
            "fontsize": "22",
            "margin": "0.28,0.18",
        }
    if level == 1:
        return {
            "label": label,
            "fillcolor": "#dce8ff",
            "fontcolor": "#16345f",
            "fontsize": "15",
            "margin": "0.22,0.14",
        }
    if level == 2:
        return {
            "label": label,
            "fillcolor": "#eef4ff",
            "fontcolor": "#27436c",
            "fontsize": "12",
            "margin": "0.18,0.12",
        }
    return {
        "label": label,
        "fillcolor": "#f7f9fd",
        "fontcolor": "#3a4f70",
        "fontsize": "11",
        "margin": "0.16,0.11",
    }


def read_input(path: str, input_format: str) -> tuple[MindMap, str]:
    if path == "-":
        text = sys.stdin.read()
        source_name = "stdin"
    else:
        source_path = Path(path)
        text = source_path.read_text(encoding="utf-8")
        source_name = source_path.stem

    if input_format == "auto":
        input_format = "json" if text.lstrip().startswith("{") else "outline"

    if input_format == "json":
        return parse_json_input(text), source_name
    if input_format == "outline":
        return parse_outline(text), source_name
    raise ValueError(f"Unsupported input format: {input_format}")


def render(dot_text: str, output_path: Path, fmt: str, engine: str) -> None:
    executable = shutil.which("dot")
    if not executable:
        raise RuntimeError("Graphviz 'dot' is not installed or not on PATH.")

    dot_path = output_path.with_suffix(".dot")
    dot_path.write_text(dot_text, encoding="utf-8")

    command = [
        executable,
        f"-K{engine}",
        f"-T{fmt}",
        str(dot_path),
        "-o",
        str(output_path),
    ]
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a text outline or JSON mind map into SVG/PNG using Graphviz."
    )
    parser.add_argument("input", nargs="?", default="-", help="Input file path, or '-' for stdin.")
    parser.add_argument("-o", "--output", help="Output file path. Defaults beside the input.")
    parser.add_argument(
        "--format",
        choices=["auto", "outline", "json"],
        default="auto",
        help="Input format. Defaults to auto-detect.",
    )
    parser.add_argument(
        "--render-format",
        choices=["svg", "png"],
        default="svg",
        help="Output render format.",
    )
    parser.add_argument(
        "--engine",
        choices=["twopi", "dot", "fdp", "sfdp", "neato"],
        default="twopi",
        help="Graphviz layout engine.",
    )
    args = parser.parse_args()

    try:
        mindmap, source_name = read_input(args.input, args.format)
        dot_text = build_dot(mindmap)
        if args.output:
            output_path = Path(args.output)
        else:
            base_name = source_name if source_name != "stdin" else "mindmap"
            output_path = Path.cwd() / f"{base_name}.{args.render_format}"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        render(dot_text, output_path, args.render_format, args.engine)
        print(output_path)
        return 0
    except subprocess.CalledProcessError as exc:
        print(f"Graphviz failed with exit code {exc.returncode}.", file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover - CLI guard
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
