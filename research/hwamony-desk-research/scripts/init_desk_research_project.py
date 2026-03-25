#!/usr/bin/env python3
"""Initialize a project folder for staged desk research."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a desk-research project scaffold.")
    parser.add_argument("project_slug", help="Project slug used for the folder name")
    parser.add_argument(
        "--base-path",
        default=".",
        help="Parent directory where desk-research-projects/ lives",
    )
    args = parser.parse_args()

    root = Path(args.base_path).expanduser().resolve() / "desk-research-projects" / args.project_slug
    if root.exists():
        raise SystemExit(f"Project already exists: {root}")

    (root / "03-batches").mkdir(parents=True)
    (root / "04-sources" / "raw").mkdir(parents=True)

    write_text(
        root / "00-project-meta.yaml",
        dedent(
            f"""
            project_slug: "{args.project_slug}"
            status: "scoping"
            current_stage: "brief"
            created_by: "hwamony-desk-research"
            """
        ),
    )
    write_text(
        root / "01-research-brief.md",
        "# Research Brief\n\n## Question\n\n## Audience\n\n## Scope\n\n## Exclusions\n",
    )
    write_text(
        root / "02-source-strategy.md",
        "# Source Strategy\n\n## Priority Source Families\n\n## Initial Batch Proposal\n",
    )
    write_text(root / "03-batches" / "batch-001.md", "# Batch 001\n\n## Focus\n\n## Queries\n\n## Sources Reviewed\n\n## Interim Findings\n")
    write_text(root / "04-sources" / "source-index.md", "# Source Index\n")
    write_text(root / "05-findings.md", "# Findings\n")
    write_text(root / "06-bibliography.md", "# Bibliography\n")
    write_text(root / "07-open-questions.md", "# Open Questions\n")
    write_text(root / "08-feedback-log.md", "# Feedback Log\n")

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
