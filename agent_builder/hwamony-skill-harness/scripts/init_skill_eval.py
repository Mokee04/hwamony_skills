#!/usr/bin/env python3
"""Initialize a stable eval workspace beside a target skill."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


def write_text(path: Path, content: str, force: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create eval scaffolding under a target skill.")
    parser.add_argument("target_skill_path", help="Path to the target skill directory")
    parser.add_argument("--force", action="store_true", help="Overwrite template files if they exist")
    args = parser.parse_args()

    target_root = Path(args.target_skill_path).expanduser().resolve()
    if not target_root.exists():
        raise SystemExit(f"Target skill does not exist: {target_root}")
    if not (target_root / "SKILL.md").exists():
        raise SystemExit(f"Target skill is missing SKILL.md: {target_root}")

    eval_root = target_root / "eval"
    (eval_root / "cases").mkdir(parents=True, exist_ok=True)
    (eval_root / "runs").mkdir(parents=True, exist_ok=True)

    write_text(
        eval_root / "profile.yaml",
        dedent(
            f"""
            skill_name: {target_root.name}
            skill_type: artifact-producing
            risk_level: medium
            goals:
              - describe what good behavior looks like
            failure_modes:
              - describe likely failure modes here
            dimensions:
              task_success: 5
            human_review_required: false
            pass_thresholds:
              task_success: 4
            pass_at_k: 3
            """
        ),
        force=args.force,
    )
    write_text(
        eval_root / "cases" / "case-template.md",
        dedent(
            """
            # Case Title

            ## User Input

            ## Must Have

            - required behavior

            ## Must Not

            - forbidden behavior

            ## Grader Hints

            - what matters most
            """
        ),
        force=args.force,
    )
    write_text(
        eval_root / "summary.md",
        "# Eval Summary\n\nNo runs recorded yet.\n",
        force=args.force,
    )
    write_text(
        eval_root / "history.md",
        "# Eval History\n\n- Eval workspace initialized.\n",
        force=args.force,
    )

    print(eval_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
