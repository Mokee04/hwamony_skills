#!/usr/bin/env python3
"""Compare baseline and mutation outputs shard by shard using deterministic checks."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


PLACEHOLDER_MARKER = "Replace this placeholder with the actual output for this case."


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


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


def parse_bullet_sections(case_path: Path) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {"Must Have": [], "Must Not": []}
    current_section: str | None = None
    for raw_line in case_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            current_section = line[3:].strip()
            continue
        if current_section in sections and line.startswith("- "):
            sections[current_section].append(line[2:].strip())
    return sections


def normalize_response(text: str) -> str:
    return text.replace(PLACEHOLDER_MARKER, "").strip()


def is_placeholder_response(text: str) -> bool:
    return PLACEHOLDER_MARKER in text or not normalize_response(text)


def match_rule(rule: str, text: str) -> bool:
    if rule.startswith("literal:"):
        return rule[len("literal:") :].strip() in text
    if rule.startswith("regex:"):
        pattern = rule[len("regex:") :].strip()
        return re.search(pattern, text, flags=re.MULTILINE) is not None
    return rule in text


def score_case(case_path: Path, response_path: Path) -> dict[str, Any]:
    sections = parse_bullet_sections(case_path)
    response_text = response_path.read_text(encoding="utf-8") if response_path.exists() else ""
    placeholder = is_placeholder_response(response_text)
    normalized = normalize_response(response_text)

    missing = []
    violated = []
    if not placeholder:
        for rule in sections["Must Have"]:
            if not match_rule(rule, normalized):
                missing.append(rule)
        for rule in sections["Must Not"]:
            if match_rule(rule, normalized):
                violated.append(rule)

    passed = response_path.exists() and not placeholder and not missing and not violated
    notes = []
    if not response_path.exists():
        notes.append("response file missing")
    elif placeholder:
        notes.append("response file still contains placeholder content")
    if missing:
        notes.append("missing must-have checks")
    if violated:
        notes.append("triggered must-not checks")

    return {
        "case_group": case_path.parent.name,
        "case_name": case_path.name,
        "response_path": str(response_path),
        "passed": passed,
        "missing": missing,
        "violated": violated,
        "notes": "; ".join(notes) if notes else "deterministic checks passed",
    }


def evaluate_phase(run_dir: Path, assignments: list[dict[str, Any]], worker: str, phase: str, rubric: dict[str, Any]) -> dict[str, Any]:
    worker_assignment = next((item for item in assignments if item.get("worker") == worker), None)
    if worker_assignment is None:
        raise SystemExit(f"No worker assignment found for {worker}")

    case_results = []
    evidence_files_present = True
    regression_pass = True

    for record in worker_assignment.get("assigned_cases", []):
        case_path = run_dir.parent.parent / "cases" / record["case_group"] / record["case_name"]
        response_key = f"{phase}_response_path"
        response_path = run_dir / record[response_key]
        result = score_case(case_path, response_path)
        case_results.append(result)

        response_text = response_path.read_text(encoding="utf-8") if response_path.exists() else ""
        evidence_files_present = evidence_files_present and response_path.exists() and not is_placeholder_response(response_text)
        if record["case_group"] == "regression" and not result["passed"]:
            regression_pass = False

    total_cases = len(case_results)
    passed_cases = sum(1 for item in case_results if item["passed"])
    dimensions: dict[str, float] = {}

    for check in rubric.get("deterministic_checks", []):
        check_type = check.get("type")
        dimension = check.get("dimension")
        weight = float(check.get("weight", 1))
        if check_type == "response_files_present":
            dimensions[dimension] = weight if evidence_files_present else 0.0
        elif check_type == "case_requirements_match":
            ratio = (passed_cases / total_cases) if total_cases else 0.0
            dimensions[dimension] = round(ratio * weight, 3)

    if "regression_guard" in rubric.get("dimensions", {}):
        dimensions["regression_guard"] = float(1 if regression_pass else 0)

    total = round(sum(value for value in dimensions.values() if isinstance(value, (int, float))), 3)
    return {
        "dimensions": dimensions,
        "case_results": case_results,
        "regression_pass": regression_pass,
        "total": total,
        "passed_cases": passed_cases,
        "total_cases": total_cases,
    }


def verdict_for_delta(baseline_total: float | None, mutation_total: float | None) -> str:
    if baseline_total is None or mutation_total is None:
        return "pending"
    if mutation_total > baseline_total:
        return "improved"
    if mutation_total < baseline_total:
        return "worse"
    return "same"


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare baseline and mutation outputs shard by shard.")
    parser.add_argument("target_skill_path", help="Path to the target skill directory")
    parser.add_argument("--run-id", help="Optional run id such as run-20260327-001; defaults to the latest run")
    parser.add_argument(
        "--worker",
        action="append",
        default=[],
        help="Worker shard to grade, such as worker-a. Repeat to limit grading.",
    )
    args = parser.parse_args()

    target_root = Path(args.target_skill_path).expanduser().resolve()
    run_dir = resolve_run_dir(target_root, args.run_id)
    manifest = load_json(run_dir / "manifest.json")
    rubric = load_json(run_dir / "rubric.json")
    assignments = load_json(run_dir / "assignments.json").get("workers", [])

    workers = args.worker or manifest.get("workers", [])
    for worker in workers:
        baseline_eval = evaluate_phase(run_dir, assignments, worker, "baseline", rubric)
        mutation_eval = evaluate_phase(run_dir, assignments, worker, "mutation", rubric)
        delta = None
        if baseline_eval["total"] is not None and mutation_eval["total"] is not None:
            delta = round(mutation_eval["total"] - baseline_eval["total"], 3)
        verdict = verdict_for_delta(baseline_eval["total"], mutation_eval["total"])

        rationale = (
            f"Mutation {verdict} for {worker}: baseline {baseline_eval['passed_cases']}/{baseline_eval['total_cases']} passes, "
            f"mutation {mutation_eval['passed_cases']}/{mutation_eval['total_cases']} passes."
        )
        write_json(
            run_dir / "grades" / f"{worker}.json",
            {
                "worker": worker,
                "baseline_total": baseline_eval["total"],
                "mutation_total": mutation_eval["total"],
                "delta": delta,
                "verdict": verdict,
                "baseline_dimensions": baseline_eval["dimensions"],
                "mutation_dimensions": mutation_eval["dimensions"],
                "baseline_case_results": baseline_eval["case_results"],
                "mutation_case_results": mutation_eval["case_results"],
                "baseline_regression_pass": baseline_eval["regression_pass"],
                "mutation_regression_pass": mutation_eval["regression_pass"],
                "rationale": rationale,
            },
        )

    print(run_dir / "grades")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
