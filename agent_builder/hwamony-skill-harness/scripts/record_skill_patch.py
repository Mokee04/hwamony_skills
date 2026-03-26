#!/usr/bin/env python3
"""Record a patch note for a target skill's eval history."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Append a patch note to eval/history.md.")
    parser.add_argument("target_skill_path", help="Path to the target skill directory")
    parser.add_argument("--summary", required=True, help="Short summary of what changed")
    parser.add_argument("--run-id", help="Optional run id that motivated the patch")
    parser.add_argument(
        "--files",
        nargs="*",
        default=[],
        help="Optional list of touched files relative to the target skill",
    )
    args = parser.parse_args()

    target_root = Path(args.target_skill_path).expanduser().resolve()
    history_path = target_root / "eval" / "history.md"
    history_path.parent.mkdir(parents=True, exist_ok=True)
    if not history_path.exists():
        history_path.write_text("# Eval History\n", encoding="utf-8")

    timestamp = datetime.now(timezone.utc).isoformat()
    line = f"- {timestamp}: {args.summary}"
    if args.run_id:
        line += f" (from {args.run_id})"
    if args.files:
        line += f" [files: {', '.join(args.files)}]"

    with history_path.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")

    print(history_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
