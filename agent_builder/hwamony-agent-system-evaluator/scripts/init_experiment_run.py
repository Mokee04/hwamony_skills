#!/usr/bin/env python3
"""Initialize a numbered experiment run folder inside an agent-system project."""

from __future__ import annotations

import argparse
from pathlib import Path


def next_run_id(runs_dir: Path) -> str:
    existing = sorted(p.name for p in runs_dir.iterdir() if p.is_dir() and p.name.startswith("run-"))
    if not existing:
        return "run-001"
    last = existing[-1].split("-")[-1]
    return f"run-{int(last) + 1:03d}"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a run folder for an agent-system project.")
    parser.add_argument("project_path", help="Path to the project root")
    parser.add_argument("--run-id", help="Optional explicit run id such as run-003")
    args = parser.parse_args()

    project_root = Path(args.project_path).expanduser().resolve()
    runs_dir = project_root / "07-runs"
    runs_dir.mkdir(parents=True, exist_ok=True)

    run_id = args.run_id or next_run_id(runs_dir)
    run_root = runs_dir / run_id
    if run_root.exists():
        raise SystemExit(f"Run already exists: {run_root}")

    write_text(run_root / "input.md", "# Input\n")
    write_text(run_root / "output.md", "# Output\n")
    write_text(
        run_root / "metadata.yaml",
        'run_id: ""\nvendor: ""\nmodel: ""\nframework: ""\nhistory_policy: ""\npurpose: ""\n',
    )
    write_text(run_root / "evaluation.md", "# Evaluation\n")
    write_text(run_root / "notes.md", "# Notes\n")

    metadata_path = run_root / "metadata.yaml"
    metadata_path.write_text(
        metadata_path.read_text(encoding="utf-8").replace('run_id: ""', f'run_id: "{run_id}"'),
        encoding="utf-8",
    )

    print(run_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
