#!/usr/bin/env python3
"""Promote the run's mutation snapshot to the live SKILL.md with backups."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_run_dir(target_root: Path, run_id: str | None) -> Path:
    runs_dir = target_root / "eval" / "runs"
    if not runs_dir.exists():
        raise SystemExit(f"Missing runs directory: {runs_dir}")
    if run_id:
        run_dir = runs_dir / run_id
        if not run_dir.exists():
            raise SystemExit(f"Run does not exist: {run_dir}")
        return run_dir

    run_dirs = sorted(path for path in runs_dir.iterdir() if path.is_dir() and path.name.startswith("run-"))
    if not run_dirs:
        raise SystemExit(f"No run folders found under: {runs_dir}")
    return run_dirs[-1]


def snapshot(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description="Promote the mutation snapshot to the target SKILL.md.")
    parser.add_argument("target_skill_path", help="Path to the target skill directory")
    parser.add_argument("--run-id", help="Optional run id such as run-20260327-001; defaults to the latest run")
    args = parser.parse_args()

    target_root = Path(args.target_skill_path).expanduser().resolve()
    skill_path = target_root / "SKILL.md"
    if not skill_path.exists():
        raise SystemExit(f"Target skill is missing SKILL.md: {skill_path}")

    run_dir = resolve_run_dir(target_root, args.run_id)
    run_id = run_dir.name
    decision = load_json(run_dir / "decision.json")
    if decision.get("status") != "keep":
        raise SystemExit(f"Run {run_id} is not in keep state; current status is {decision.get('status')}.")

    mutation = load_json(run_dir / "mutation.json")
    snapshot_ref = mutation.get("skill_snapshot_path")
    if not snapshot_ref:
        raise SystemExit("Mutation record has no skill_snapshot_path.")

    snapshot_path = (run_dir / snapshot_ref).resolve()
    if not snapshot_path.exists():
        raise SystemExit(f"Mutation snapshot does not exist: {snapshot_path}")

    backups_root = target_root / "eval" / "backups" / run_id / "promotion"
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    pre_promote = backups_root / f"{timestamp}-pre-promote-SKILL.md"
    adopted = backups_root / f"{timestamp}-mutation-adopted-SKILL.md"

    snapshot(skill_path, pre_promote)
    snapshot(snapshot_path, adopted)
    snapshot(snapshot_path, skill_path)

    decision["promoted_mutation"] = "mutation.json"
    decision["promotion_timestamp"] = datetime.now(timezone.utc).isoformat()
    decision["promotion_backups"] = {
        "pre_promote": str(pre_promote.relative_to(target_root)),
        "adopted_snapshot": str(adopted.relative_to(target_root)),
    }
    (run_dir / "decision.json").write_text(json.dumps(decision, indent=2) + "\n", encoding="utf-8")

    with (run_dir / "decision.md").open("a", encoding="utf-8") as handle:
        handle.write(
            "\n## Promotion\n\n"
            "- promoted artifact: mutation snapshot\n"
            f"- pre-promote backup: {pre_promote.relative_to(target_root)}\n"
            f"- adopted snapshot: {adopted.relative_to(target_root)}\n"
        )

    print(skill_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
