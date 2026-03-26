#!/usr/bin/env python3
"""Wrapper around Codex's GitHub skill installer."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
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
    parser.add_argument("--ref", help="Pinned Git ref to install from. Prefer a commit SHA.")
    parser.add_argument("--dest", help="Destination skills directory")
    parser.add_argument("--name", help="Override installed skill name")
    parser.add_argument("--method", default="auto", choices=("auto", "download", "git"))
    parser.add_argument(
        "--allow-unpinned",
        action="store_true",
        help="Allow installation from a mutable branch ref such as main. Use only after review.",
    )
    return parser.parse_args(argv)


def is_commit_sha(ref: str) -> bool:
    return bool(re.fullmatch(r"[0-9a-fA-F]{7,40}", ref))


def is_tag_ref(ref: str) -> bool:
    return ref.startswith("refs/tags/") or bool(re.fullmatch(r"v?\d+(?:\.\d+){0,3}(?:[-._][0-9A-Za-z]+)*", ref))


def ensure_safe_ref(args: argparse.Namespace) -> None:
    if args.allow_unpinned:
        return
    if not args.ref:
        print(
            "Refusing unpinned install. Provide --ref with a commit SHA (preferred) or pass --allow-unpinned after review.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    if is_commit_sha(args.ref) or is_tag_ref(args.ref):
        return
    print(
        "Refusing mutable ref install. Use a commit SHA, an immutable release tag, or pass --allow-unpinned after review.",
        file=sys.stderr,
    )
    raise SystemExit(2)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    ensure_safe_ref(args)
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
