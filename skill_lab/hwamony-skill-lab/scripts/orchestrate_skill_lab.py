#!/usr/bin/env python3
"""Supervisor wrapper for interactive single-mutation skill-lab runs."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def script_root() -> Path:
    return Path(__file__).resolve().parent


def script_path(name: str) -> Path:
    return script_root() / name


def run_script(name: str, *args: str) -> None:
    subprocess.run([sys.executable, str(script_path(name)), *args], check=True)


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


def ensure_eval_workspace(target_root: Path) -> None:
    if (target_root / "eval").exists():
        return
    run_script("init_skill_eval.py", str(target_root))


def supervisor_packet(target_root: Path, run_dir: Path, mutation: dict[str, Any], assignments: list[dict[str, Any]], next_command: str) -> str:
    workers = [item["worker"] for item in assignments]
    mutation_path = Path(run_dir / mutation["skill_snapshot_path"]).resolve()
    lines = [
        "# Supervisor Packet",
        "",
        "Start the run by defining the improvement plan before any worker executes anything.",
        "",
        "## Your Job",
        "",
        "- decide what behavior should improve in this iteration",
        "- decide how the test should be run",
        "- write the rubric evaluators should use",
        "- apply exactly one bounded mutation to the mutation snapshot",
        "",
        "## Files To Fill",
        "",
        f"- live skill: {target_root / 'SKILL.md'}",
        f"- mutation snapshot to edit: {mutation_path}",
        f"- plan: {run_dir / 'plan.md'} and {run_dir / 'plan.json'}",
        f"- rubric: {run_dir / 'rubric.json'}",
        f"- mutation record: {run_dir / 'mutation.json'}",
        "",
        "## Worker Shards",
        "",
        *[f"- {worker}" for worker in workers],
        "",
        "## Guardrails",
        "",
        "- one mutation only",
        "- do not change case files during the run",
        "- do not edit the live skill directly",
        "- keep the mutation narrow enough that the result is attributable",
        "",
        "## Next Command",
        "",
        f"`{next_command}`",
    ]
    return "\n".join(lines) + "\n"


def worker_packet(run_dir: Path, worker_assignment: dict[str, Any], baseline: dict[str, Any], mutation: dict[str, Any]) -> str:
    worker = worker_assignment["worker"]
    lines = [
        f"# Worker Packet: {worker}",
        "",
        "You are a naive executor. Do not judge the mutation. Do not edit either skill snapshot.",
        "",
        "## Skill Snapshots",
        "",
        f"- baseline snapshot: {Path(run_dir / baseline['skill_snapshot_path']).resolve()}",
        f"- mutation snapshot: {Path(run_dir / mutation['skill_snapshot_path']).resolve()}",
        "",
        "## Your Shard",
        "",
    ]
    for item in worker_assignment.get("assigned_cases", []):
        lines.extend(
            [
                f"- {item['case_group']}/{item['case_name']}",
                f"  baseline response file: {run_dir / item['baseline_response_path']}",
                f"  mutation response file: {run_dir / item['mutation_response_path']}",
            ]
        )
    lines.extend(
        [
            "",
            "## Checklist",
            "",
            "- run the baseline snapshot on your shard and write the outputs into the baseline response files",
            "- run the mutation snapshot on the same shard and write the outputs into the mutation response files",
            "- do not edit the skill snapshots",
            "- do not change cases, rubric, or scoring files",
            "- do not decide whether the mutation should be kept",
        ]
    )
    return "\n".join(lines) + "\n"


def evaluator_packet(run_dir: Path, worker_assignment: dict[str, Any], mutation: dict[str, Any]) -> str:
    worker = worker_assignment["worker"]
    lines = [
        f"# Evaluator Packet: {worker}",
        "",
        "Compare the baseline and mutation outputs for this shard using the supervisor's rubric.",
        "",
        "## Files",
        "",
        f"- plan: {run_dir / 'plan.md'} and {run_dir / 'plan.json'}",
        f"- rubric: {run_dir / 'rubric.json'}",
        f"- mutation record: {run_dir / 'mutation.json'}",
        f"- deterministic evidence: {run_dir / 'grades' / f'{worker}.json'}",
        f"- judgment to fill: {run_dir / 'judgments' / f'{worker}.json'}",
        "",
        "## Shard Outputs",
        "",
    ]
    for item in worker_assignment.get("assigned_cases", []):
        lines.extend(
            [
                f"- {item['case_group']}/{item['case_name']}",
                f"  baseline output: {run_dir / item['baseline_response_path']}",
                f"  mutation output: {run_dir / item['mutation_response_path']}",
            ]
        )
    lines.extend(
        [
            "",
            "## Required Judgment Fields",
            "",
            "- `status`: set to `completed` when done",
            "- `verdict`: one of `mutation_better`, `baseline_better`, `tie`, `incomplete`",
            "- `confidence`: low, medium, or high",
            "- `baseline_better_on`, `mutation_better_on`, `tie_on`: rubric dimensions or observations",
            "- `rationale`: short explanation grounded in the rubric and evidence",
            "- `risks`: any caveats or rollout concerns",
        ]
    )
    return "\n".join(lines) + "\n"


def coordinator_packet(target_root: Path, run_dir: Path, run_id: str, assignments: list[dict[str, Any]], final_summary: str) -> str:
    workers = [item["worker"] for item in assignments]
    lines = [
        "# Coordinator Packet",
        "",
        "This run is ready for supervisor planning, worker execution, evaluator review, and closeout.",
        "",
        "## Sequence",
        "",
        "1. Complete the supervisor phase first: plan, improvement target, rubric, and one bounded mutation.",
        "2. Dispatch the worker packets so each worker executes baseline and mutation on its shard.",
        "3. Run the review command to generate deterministic evidence and refresh evaluator packets.",
        "4. Dispatch evaluator packets and wait for all `judgments/*.json` files to be completed.",
        "5. Finalize the run with the command below.",
        "",
        "## Commands",
        "",
        f"- review: `python3 scripts/orchestrate_skill_lab.py review {target_root} --run-id {run_id}`",
        f"- finalize: `python3 scripts/orchestrate_skill_lab.py finalize {target_root} --run-id {run_id} --summary {json.dumps(final_summary)}`",
        "",
        "## Packets",
        "",
        "- `packets/supervisor.md`",
        *[f"- `packets/{worker}.md`" for worker in workers],
        *[f"- `packets/evaluator-{worker}.md`" for worker in workers],
        "",
        "## Guardrails",
        "",
        "- workers execute only",
        "- evaluators judge only",
        "- only promote through the finalize step",
    ]
    return "\n".join(lines) + "\n"


def refresh_packets(target_root: Path, run_dir: Path, final_summary: str) -> None:
    assignments = load_json(run_dir / "assignments.json").get("workers", [])
    baseline = load_json(run_dir / "baseline.json")
    mutation = load_json(run_dir / "mutation.json")
    packets_dir = run_dir / "packets"
    packets_dir.mkdir(parents=True, exist_ok=True)
    write_text(
        packets_dir / "supervisor.md",
        supervisor_packet(
            target_root,
            run_dir,
            mutation,
            assignments,
            f"python3 scripts/orchestrate_skill_lab.py review {target_root} --run-id {run_dir.name}",
        ),
    )
    for assignment in assignments:
        write_text(packets_dir / f"{assignment['worker']}.md", worker_packet(run_dir, assignment, baseline, mutation))
        write_text(packets_dir / f"evaluator-{assignment['worker']}.md", evaluator_packet(run_dir, assignment, mutation))
    write_text(
        packets_dir / "coordinator.md",
        coordinator_packet(target_root, run_dir, run_dir.name, assignments, final_summary),
    )


def start_command(args: argparse.Namespace) -> int:
    target_root = Path(args.target_skill_path).expanduser().resolve()
    if not (target_root / "SKILL.md").exists():
        raise SystemExit(f"Target skill is missing SKILL.md: {target_root}")
    ensure_eval_workspace(target_root)

    command_args = [str(target_root), "--attempts", str(args.attempts)]
    for case_name in args.case:
        command_args.extend(["--case", case_name])
    for worker in args.worker:
        command_args.extend(["--worker", worker])
    if args.run_id:
        command_args.extend(["--run-id", args.run_id])

    run_script("run_skill_eval.py", *command_args)
    run_dir = resolve_run_dir(target_root, args.run_id)

    plan = load_json(run_dir / "plan.json")
    if args.goal:
        plan["goal"] = args.goal
    if args.hypothesis:
        plan["hypothesis"] = args.hypothesis
    if args.improvement_target:
        plan["improvement_target"] = args.improvement_target
    write_json(run_dir / "plan.json", plan)

    mutation = load_json(run_dir / "mutation.json")
    mutation["mutation_brief"] = args.mutation or "Fill in one bounded mutation."
    mutation["mutation_hypothesis"] = args.hypothesis or args.mutation or ""
    write_json(run_dir / "mutation.json", mutation)

    final_summary = args.summary or f"Finalize {run_dir.name} after baseline and mutation shard outputs are recorded."
    refresh_packets(target_root, run_dir, final_summary)
    print(run_dir)
    return 0


def review_command(args: argparse.Namespace) -> int:
    target_root = Path(args.target_skill_path).expanduser().resolve()
    run_dir = resolve_run_dir(target_root, args.run_id)
    run_script("auto_grade_skill_eval.py", str(target_root), "--run-id", run_dir.name)
    refresh_packets(target_root, run_dir, f"Finalize {run_dir.name} after evaluator judgments are recorded.")
    print(run_dir / "packets")
    return 0


def finalize_command(args: argparse.Namespace) -> int:
    target_root = Path(args.target_skill_path).expanduser().resolve()
    run_dir = resolve_run_dir(target_root, args.run_id)

    run_script("grade_skill_eval.py", str(target_root), "--run-id", run_dir.name)

    decision = load_json(run_dir / "decision.json")
    mutation = load_json(run_dir / "mutation.json")
    promoted = False
    if decision.get("status") == "keep" and not args.no_promote:
        run_script("promote_skill_candidate.py", str(target_root), "--run-id", run_dir.name)
        promoted = True
        decision = load_json(run_dir / "decision.json")

    if args.summary:
        summary = args.summary
    elif promoted:
        summary = f"Promoted mutation from {run_dir.name}."
    elif decision.get("status") == "keep":
        summary = f"Mutation passed majority in {run_dir.name} but promotion was skipped."
    elif decision.get("status") == "pending":
        summary = f"Run {run_dir.name} is still pending because evaluator judgments are incomplete."
    else:
        summary = f"No promotion from {run_dir.name}; final status was {decision.get('status')}."

    patch_args = [str(target_root), "--run-id", run_dir.name, "--summary", summary]
    changed_files = mutation.get("changed_files", [])
    if changed_files:
        patch_args.extend(["--files", *changed_files])
    run_script("record_skill_patch.py", *patch_args)
    run_script("summarize_skill_eval.py", str(target_root))
    refresh_packets(target_root, run_dir, summary)
    print(run_dir / "decision.json")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Supervisor wrapper for interactive single-mutation skill-lab runs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    start = subparsers.add_parser("start", help="Create a run and generate supervisor/worker/evaluator packets.")
    start.add_argument("target_skill_path", help="Path to the target skill directory")
    start.add_argument("--attempts", type=int, default=1, help="Planned pass@k attempt count")
    start.add_argument("--run-id", help="Optional explicit run id such as run-20260327-001")
    start.add_argument("--goal", help="Short run goal to store in plan.json")
    start.add_argument("--hypothesis", help="Short hypothesis to store in plan.json")
    start.add_argument("--improvement-target", help="Optional improvement target to seed into plan.json")
    start.add_argument("--mutation", help="One bounded mutation to test in this iteration")
    start.add_argument("--summary", help="Optional finalize-summary hint to place in the coordinator packet")
    start.add_argument("--case", action="append", default=[], help="Specific case filename to include; repeat for multiple cases")
    start.add_argument("--worker", action="append", default=[], help="Worker shard identifier to scaffold; repeat for multiple workers")
    start.set_defaults(func=start_command)

    review = subparsers.add_parser("review", help="Generate deterministic evidence and refresh evaluator packets.")
    review.add_argument("target_skill_path", help="Path to the target skill directory")
    review.add_argument("--run-id", help="Optional run id such as run-20260327-001; defaults to the latest run")
    review.set_defaults(func=review_command)

    finalize = subparsers.add_parser("finalize", help="Grade, optionally promote, and summarize a prepared run.")
    finalize.add_argument("target_skill_path", help="Path to the target skill directory")
    finalize.add_argument("--run-id", help="Optional run id such as run-20260327-001; defaults to the latest run")
    finalize.add_argument("--summary", help="Optional patch summary to record in eval/history.md")
    finalize.add_argument("--no-promote", action="store_true", help="Compute the decision but skip promotion into the live SKILL.md")
    finalize.set_defaults(func=finalize_command)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
