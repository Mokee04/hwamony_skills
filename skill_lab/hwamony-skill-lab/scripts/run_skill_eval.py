#!/usr/bin/env python3
"""Create a dated single-mutation skill-lab run with worker shard assignments."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from lab_config import case_groups, default_worker_names, eval_dirs, load_artifact_schema, load_lifecycle_config, load_role_config, run_dirs


def next_run_id(runs_dir: Path) -> str:
    date_prefix = datetime.now().strftime("%Y%m%d")
    prefix = f"run-{date_prefix}-"
    existing = sorted(path.name for path in runs_dir.iterdir() if path.is_dir() and path.name.startswith(prefix))
    if not existing:
        return f"{prefix}001"
    last = existing[-1].split("-")[-1]
    return f"{prefix}{int(last) + 1:03d}"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def snapshot_skill(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def collect_cases(eval_root: Path, selected: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    wanted = set(selected)
    for case_group in case_groups():
        case_dir = eval_root / "cases" / case_group
        case_files = sorted(path.name for path in case_dir.glob("*.md"))
        case_files = [name for name in case_files if name != "case-template.md"]
        if wanted:
            case_files = [name for name in case_files if name in wanted]
        groups[case_group] = case_files
    return groups


def role_map() -> dict[str, dict[str, Any]]:
    config = load_role_config()
    return {role["id"]: role for role in config.get("roles", [])}


def shard_assignments(workers: list[str], selected_cases: dict[str, list[str]]) -> list[dict[str, Any]]:
    assignments = [{"worker": worker, "assigned_cases": [], "notes": ""} for worker in workers]
    if not workers:
        return assignments

    for group in case_groups():
        for index, case_name in enumerate(selected_cases.get(group, [])):
            target = assignments[index % len(assignments)]
            target["assigned_cases"].append(
                {
                    "case_group": group,
                    "case_name": case_name,
                }
            )
    return assignments


def response_placeholder(worker: str, phase: str, case_group: str, case_name: str) -> str:
    return "\n".join(
        [
            f"# Response Record: {worker} / {phase} / {case_group}/{case_name}",
            "",
            "Replace this placeholder with the actual output for this case.",
            "",
            "## Response",
            "",
            "",
            "## Notes",
            "",
            "- capture anything relevant about this output here",
        ]
    ) + "\n"


def response_path(phase: str, worker: str, case_group: str, case_name: str) -> str:
    case_id = Path(case_name).stem
    return f"outputs/{phase}/{worker}/{case_group}__{case_id}.md"


def phase_records(assignments: list[dict[str, Any]], phase: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for assignment in assignments:
        worker = assignment["worker"]
        for item in assignment["assigned_cases"]:
            records.append(
                {
                    "worker": worker,
                    "case_group": item["case_group"],
                    "case_name": item["case_name"],
                    "response_path": response_path(phase, worker, item["case_group"], item["case_name"]),
                }
            )
    return records


def grade_template(worker: str) -> dict[str, Any]:
    return {
        "worker": worker,
        "baseline_total": None,
        "mutation_total": None,
        "delta": None,
        "verdict": "pending",
        "baseline_dimensions": {},
        "mutation_dimensions": {},
        "baseline_case_results": [],
        "mutation_case_results": [],
        "baseline_regression_pass": None,
        "mutation_regression_pass": None,
        "rationale": "",
    }


def judgment_template(worker: str) -> dict[str, Any]:
    return {
        "worker": worker,
        "status": "pending",
        "verdict": "",
        "confidence": "",
        "baseline_better_on": [],
        "mutation_better_on": [],
        "tie_on": [],
        "rationale": "",
        "risks": [],
        "deterministic_evidence_path": f"grades/{worker}.json",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a dated single-mutation run for skill-lab.")
    parser.add_argument("target_skill_path", help="Path to the target skill directory")
    parser.add_argument("--attempts", type=int, default=1, help="Planned pass@k attempt count")
    parser.add_argument(
        "--case",
        action="append",
        dest="cases",
        default=[],
        help="Specific case filename to include; repeat for multiple cases",
    )
    parser.add_argument(
        "--worker",
        action="append",
        dest="workers",
        default=[],
        help="Worker shard identifier to scaffold; repeat for multiple workers",
    )
    parser.add_argument("--run-id", help="Optional explicit run id such as run-20260327-001")
    args = parser.parse_args()

    target_root = Path(args.target_skill_path).expanduser().resolve()
    eval_root = target_root / "eval"
    runs_dir = eval_root / "runs"
    backups_dir = eval_root / "backups"
    skill_path = target_root / "SKILL.md"

    if not skill_path.exists():
        raise SystemExit(f"Target skill is missing SKILL.md: {skill_path}")
    if not eval_root.exists():
        raise SystemExit(f"Missing eval workspace: {eval_root}")

    for dirname in eval_dirs():
        (eval_root / dirname).mkdir(parents=True, exist_ok=True)

    runs_dir.mkdir(parents=True, exist_ok=True)
    run_id = args.run_id or next_run_id(runs_dir)
    run_root = runs_dir / run_id
    if run_root.exists():
        raise SystemExit(f"Run already exists: {run_root}")
    backup_root = backups_dir / run_id

    selected_cases = collect_cases(eval_root, args.cases)
    workers = args.workers or default_worker_names()
    assignments = [item for item in shard_assignments(workers, selected_cases) if item["assigned_cases"]]
    workers = [item["worker"] for item in assignments]
    lifecycle = load_lifecycle_config()
    loop_steps = lifecycle.get("loop", [])
    roles = role_map()

    for dirname in run_dirs():
        (run_root / dirname).mkdir(parents=True, exist_ok=True)

    snapshot_skill(skill_path, backup_root / "original" / "SKILL.md")
    snapshot_skill(skill_path, backup_root / "mutation" / "SKILL.md")

    manifest = {
        "run_id": run_id,
        "target_skill": target_root.name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "attempts": args.attempts,
        "roles": {role_id: role.get("count", 1) for role_id, role in roles.items()},
        "workers": workers,
        "cases": selected_cases,
        "status": "planned",
        "skill_path": str(skill_path),
        "backup_root": str(backup_root),
        "majority_threshold": (len(workers) // 2) + 1 if workers else 0,
    }

    write_text(
        run_root / "plan.md",
        "\n".join(
            [
                "# Eval Plan",
                "",
                f"- target skill: {target_root.name}",
                f"- attempts: {args.attempts}",
                f"- worker count: {len(workers)}",
                f"- evaluator count: {len(workers)}",
                f"- workers: {', '.join(workers)}",
                f"- train cases: {len(selected_cases['train'])}",
                f"- regression cases: {len(selected_cases['regression'])}",
                f"- holdout cases: {len(selected_cases['holdout'])}",
                f"- majority threshold: {manifest['majority_threshold']}",
                "",
                "## Audit Questions",
                "",
                "- what should improve in this run?",
                "- what one mutation are we testing in this run?",
                "- what rubric should evaluators use?",
                "- which shard was assigned to each worker?",
                "- how did evaluators compare the mutation against baseline on each shard?",
                "- did a majority of evaluator judgments improve over baseline?",
                "",
                "## Loop",
                "",
                *[f"{index}. {step}" for index, step in enumerate(loop_steps, start=1)],
            ]
        ),
    )
    write_json(
        run_root / "plan.json",
        {
            "run_id": run_id,
            "goal": "",
            "hypothesis": "",
            "improvement_target": "",
            "baseline_required": True,
            "selected_case_groups": selected_cases,
            "majority_threshold": manifest["majority_threshold"],
            "loop": loop_steps,
        },
    )

    rubric_json = {
        "profile_snapshot_path": str(eval_root / "profile.yaml"),
        "comparison_mode": "majority_over_baseline",
        "dimensions": {
            "evidence_hygiene": {
                "description": "Every assigned response file exists and is not a placeholder.",
                "weight": 1,
            },
            "requirement_match": {
                "description": "Case-level must-have and must-not checks pass.",
                "weight": 1,
            },
            "regression_guard": {
                "description": "Regression cases inside the shard still pass.",
                "weight": 1,
            },
        },
        "pass_thresholds": {
            "evidence_hygiene": 1,
            "requirement_match": 1,
            "regression_guard": 1,
        },
        "deterministic_checks": [
            {
                "id": "response_files_present",
                "type": "response_files_present",
                "dimension": "evidence_hygiene",
                "weight": 1,
            },
            {
                "id": "case_requirements_match",
                "type": "case_requirements_match",
                "dimension": "requirement_match",
                "weight": 1,
            },
        ],
        "notes": "Compare the baseline snapshot and the mutation snapshot shard by shard. Promotion depends on majority improvement over baseline.",
    }
    write_json(run_root / "rubric.json", rubric_json)

    baseline_records = phase_records(assignments, "baseline")
    mutation_records = phase_records(assignments, "mutation")
    write_json(
        run_root / "baseline.json",
        {
            "status": "pending",
            "skill_snapshot_path": f"../../backups/{run_id}/original/SKILL.md",
            "records": baseline_records,
            "notes": "",
        },
    )
    write_json(
        run_root / "mutation.json",
        {
            "status": "draft",
            "skill_snapshot_path": f"../../backups/{run_id}/mutation/SKILL.md",
            "mutation_brief": "",
            "mutation_hypothesis": "",
            "changed_files": [],
            "summary": "",
            "records": mutation_records,
            "notes": "",
        },
    )

    assignments_payload = {
        "workers": [
            {
                "worker": assignment["worker"],
                "assigned_cases": [
                    {
                        **item,
                        "baseline_response_path": response_path("baseline", assignment["worker"], item["case_group"], item["case_name"]),
                        "mutation_response_path": response_path("mutation", assignment["worker"], item["case_group"], item["case_name"]),
                    }
                    for item in assignment["assigned_cases"]
                ],
                "notes": assignment["notes"],
            }
            for assignment in assignments
        ]
    }
    write_json(run_root / "assignments.json", assignments_payload)

    for phase, records in (("baseline", baseline_records), ("mutation", mutation_records)):
        write_text(
            run_root / "outputs" / phase / "responses.md",
            f"# {phase.title()} Responses\n\nRecord shard outputs under the worker folders in this directory.\n",
        )
        for record in records:
            write_text(
                run_root / record["response_path"],
                response_placeholder(record["worker"], phase, record["case_group"], record["case_name"]),
            )

    for worker in workers:
        write_json(run_root / "grades" / f"{worker}.json", grade_template(worker))

    scores = {
        "judgment_votes": {worker: {"verdict": "pending"} for worker in workers},
        "baseline_average": None,
        "mutation_average": None,
        "improved_votes": 0,
        "same_votes": 0,
        "worse_votes": 0,
        "pending_votes": len(workers),
        "majority_threshold": manifest["majority_threshold"],
        "decision": "pending",
    }
    write_json(run_root / "scores.json", scores)

    write_text(
        run_root / "decision.md",
        "# Decision\n\nRecord whether evaluator judgments say the single mutation beat baseline by majority across worker shards.\n",
    )
    write_json(
        run_root / "decision.json",
        {
            "status": "pending",
            "majority_threshold": manifest["majority_threshold"],
            "improved_votes": 0,
            "same_votes": 0,
            "worse_votes": 0,
            "pending_votes": len(workers),
            "selected_mutation": "mutation.json",
            "changed_files": [],
            "decision_rationale": "",
            "evidence_consulted": [
                "plan.json",
                "rubric.json",
                "baseline.json",
                "mutation.json",
                "assignments.json",
                "grades/*.json",
                "judgments/*.json",
                "scores.json",
            ],
        },
    )

    write_text(run_root / "artifact-guide.md", "# Artifact Guide\n\nThis file is refreshed later with a run-specific explanation of each generated artifact.\n")
    write_text(run_root / "feedback.md", "# Feedback\n\nRecord operator or user feedback here.\n")
    write_text(run_root / "patch-plan.md", "# Patch Plan\n\nRecord the supervisor's proposed mutation and any follow-up ideas here.\n")
    write_json(run_root / "manifest.json", manifest)

    for worker in workers:
        write_json(run_root / "judgments" / f"{worker}.json", judgment_template(worker))

    print(run_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
