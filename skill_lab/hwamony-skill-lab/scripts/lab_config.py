#!/usr/bin/env python3
"""Helpers for loading skill-lab configuration."""

from __future__ import annotations

import json
from pathlib import Path


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def config_root() -> Path:
    return skill_root() / "config"


def load_json_config(name: str) -> dict:
    path = config_root() / name
    return json.loads(path.read_text(encoding="utf-8"))


def load_role_config() -> dict:
    return load_json_config("roles.json")


def load_lifecycle_config() -> dict:
    return load_json_config("lifecycle.json")


def load_artifact_schema() -> dict:
    return load_json_config("artifact-schema.json")


def case_groups() -> list[str]:
    return list(load_lifecycle_config().get("case_groups", []))


def default_worker_names() -> list[str]:
    role_config = load_role_config()
    for role in role_config.get("roles", []):
        if role.get("id") != "worker":
            continue
        count = int(role.get("count", 0))
        pattern = role.get("name_pattern", "worker-{index}")
        names = []
        for index in range(1, count + 1):
            index_letter = chr(ord("a") + index - 1)
            names.append(
                pattern.format(
                    index=index,
                    index_letter=index_letter,
                )
            )
        return names
    return []


def results_header() -> str:
    schema = load_artifact_schema()
    return "\t".join(schema.get("results_columns", []))


def run_dirs() -> list[str]:
    schema = load_artifact_schema()
    return list(schema.get("run_dirs", []))


def eval_dirs() -> list[str]:
    schema = load_artifact_schema()
    return list(schema.get("eval_dirs", []))
