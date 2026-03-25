#!/usr/bin/env python3
"""Wrapper around Codex's GitHub skill installer."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys


def find_installer() -> Path | None:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()
    candidates = [
        codex_home / "skills/.system/skill-installer/scripts/install-skill-from-github.py",
        Path.home() / ".codex/skills/.system/skill-installer/scripts/install-skill-from-github.py",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install a skill from GitHub via the Codex installer.")
    parser.add_argument("--repo", help="GitHub repo in owner/repo format")
    parser.add_argument("--url", help="GitHub repo or tree URL")
    parser.add_argument("--path", nargs="+", help="Path(s) to skill directories inside the repo")
    parser.add_argument("--ref", default="main", help="Git ref to install from")
    parser.add_argument("--dest", help="Destination skills directory")
    parser.add_argument("--name", help="Override installed skill name")
    parser.add_argument("--method", default="auto", choices=("auto", "download", "git"))
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    installer = find_installer()
    if installer is None:
        print("Could not find the global skill installer script.", file=sys.stderr)
        return 1

    cmd = [sys.executable, str(installer)]
    if args.repo:
        cmd.extend(["--repo", args.repo])
    if args.url:
        cmd.extend(["--url", args.url])
    if args.path:
        cmd.append("--path")
        cmd.extend(args.path)
    if args.ref:
        cmd.extend(["--ref", args.ref])
    if args.dest:
        cmd.extend(["--dest", args.dest])
    if args.name:
        cmd.extend(["--name", args.name])
    if args.method:
        cmd.extend(["--method", args.method])

    result = subprocess.run(cmd)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
