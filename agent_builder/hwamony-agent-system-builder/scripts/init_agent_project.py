#!/usr/bin/env python3
"""Initialize a project folder for an agent-system build."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an agent-system project scaffold.")
    parser.add_argument("project_slug", help="Project slug used for the folder name")
    parser.add_argument(
        "--base-path",
        default=".",
        help="Parent directory where agent-system-projects/ lives",
    )
    args = parser.parse_args()

    root = Path(args.base_path).expanduser().resolve() / "agent-system-projects" / args.project_slug
    if root.exists():
        raise SystemExit(f"Project already exists: {root}")

    (root / "05-implementation" / "prompts").mkdir(parents=True)
    (root / "05-implementation" / "configs").mkdir(parents=True)
    (root / "05-implementation" / "code").mkdir(parents=True)
    (root / "07-runs").mkdir(parents=True)
    (root / "08-evaluation").mkdir(parents=True)
    (root / "09-feedback").mkdir(parents=True)

    write_text(
        root / "00-project-meta.yaml",
        dedent(
            f"""
            project_slug: "{args.project_slug}"
            status: "discovery"
            current_phase: "requirements"
            chosen_vendor: ""
            chosen_framework: ""
            chosen_model: ""
            history_policy: ""
            """
        ),
    )
    write_text(root / "01-requirements.md", "# Requirements\n\n## Goal\n\n## Constraints\n\n## Open Questions\n")
    write_text(root / "02-task-brief.md", "# Task Brief\n\n## Objective\n\n## Success Criteria\n\n## Output Contract\n")
    write_text(
        root / "03-architecture-options.md",
        "# Architecture Options\n\n## Candidate A\n\n## Candidate B\n\n## Candidate C\n",
    )
    write_text(root / "04-decision.md", "# Decision\n\n## Chosen Direction\n\n## Reasons\n\n## Next Action\n")
    write_text(root / "06-test-plan.md", "# Test Plan\n\n## Scenarios\n\n## Pass Criteria\n")
    write_text(root / "08-evaluation" / "rubric.md", "# Rubric\n\n## Dimensions\n")
    write_text(root / "08-evaluation" / "evaluation-summary.md", "# Evaluation Summary\n")
    write_text(root / "09-feedback" / "user-feedback.md", "# User Feedback\n")
    write_text(root / "09-feedback" / "iteration-log.md", "# Iteration Log\n")
    write_text(root / "HISTORY.md", "# History\n\n- Project initialized.\n")

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
