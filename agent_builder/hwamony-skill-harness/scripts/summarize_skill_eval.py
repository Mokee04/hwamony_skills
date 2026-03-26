#!/usr/bin/env python3
"""Summarize target-skill eval runs into eval/summary.md."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh eval/summary.md from recorded runs.")
    parser.add_argument("target_skill_path", help="Path to the target skill directory")
    args = parser.parse_args()

    target_root = Path(args.target_skill_path).expanduser().resolve()
    eval_root = target_root / "eval"
    runs_dir = eval_root / "runs"
    summary_path = eval_root / "summary.md"

    if not runs_dir.exists():
        raise SystemExit(f"Missing runs directory: {runs_dir}")

    run_dirs = sorted(path for path in runs_dir.iterdir() if path.is_dir() and path.name.startswith("run-"))

    lines = [
        "# Eval Summary",
        "",
        f"- target skill: {target_root.name}",
        f"- total runs: {len(run_dirs)}",
    ]

    if not run_dirs:
        lines.extend(["", "No runs recorded yet."])
    else:
        lines.extend(["", "## Runs"])
        for run_dir in run_dirs:
            manifest_path = run_dir / "manifest.json"
            if manifest_path.exists():
                manifest = load_manifest(manifest_path)
                lines.append(
                    f"- {manifest['run_id']}: {len(manifest.get('cases', []))} cases, attempts={manifest.get('attempts', 1)}, created_at={manifest.get('created_at', 'unknown')}"
                )
            else:
                lines.append(f"- {run_dir.name}: manifest missing")

    summary_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(summary_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
