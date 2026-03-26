#!/usr/bin/env python3
"""Create a numbered skill-eval run folder and attach selected cases."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def next_run_id(runs_dir: Path) -> str:
    existing = sorted(
        path.name for path in runs_dir.iterdir() if path.is_dir() and path.name.startswith("run-")
    )
    if not existing:
        return "run-001"
    last = existing[-1].split("-")[-1]
    return f"run-{int(last) + 1:03d}"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def collect_cases(cases_dir: Path, selected: list[str]) -> list[str]:
    case_files = sorted(path.name for path in cases_dir.glob("*.md"))
    if selected:
        wanted = set(selected)
        return [name for name in case_files if name in wanted]
    return [name for name in case_files if name != "case-template.md"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a run folder for target-skill evaluation.")
    parser.add_argument("target_skill_path", help="Path to the target skill directory")
    parser.add_argument("--attempts", type=int, default=1, help="Planned pass@k attempt count")
    parser.add_argument(
        "--case",
        action="append",
        dest="cases",
        default=[],
        help="Specific case filename to include; repeat for multiple cases",
    )
    parser.add_argument("--run-id", help="Optional explicit run id such as run-003")
    args = parser.parse_args()

    target_root = Path(args.target_skill_path).expanduser().resolve()
    eval_root = target_root / "eval"
    cases_dir = eval_root / "cases"
    runs_dir = eval_root / "runs"

    if not eval_root.exists():
        raise SystemExit(f"Missing eval workspace: {eval_root}")

    runs_dir.mkdir(parents=True, exist_ok=True)
    run_id = args.run_id or next_run_id(runs_dir)
    run_root = runs_dir / run_id
    if run_root.exists():
        raise SystemExit(f"Run already exists: {run_root}")

    selected_cases = collect_cases(cases_dir, args.cases)
    manifest = {
        "run_id": run_id,
        "target_skill": target_root.name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "attempts": args.attempts,
        "cases": selected_cases,
    }

    write_text(
        run_root / "plan.md",
        "\n".join(
            [
                "# Eval Plan",
                "",
                f"- target skill: {target_root.name}",
                f"- attempts: {args.attempts}",
                f"- cases: {len(selected_cases)}",
            ]
        ),
    )
    write_text(run_root / "results.md", "# Results\n\nRecord outputs, grader notes, and failures here.\n")
    write_text(run_root / "feedback.md", "# Feedback\n\nRecord user or human-review feedback here.\n")
    write_text(run_root / "patch-plan.md", "# Patch Plan\n\nList concrete edits motivated by this run.\n")
    (run_root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(run_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
