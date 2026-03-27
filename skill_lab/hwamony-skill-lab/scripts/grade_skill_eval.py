#!/usr/bin/env python3
"""Aggregate evaluator judgments into a majority-over-baseline decision."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


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


def render_decision_markdown(
    run_id: str,
    mutation_total: float | None,
    baseline_total: float | None,
    improved_votes: int,
    same_votes: int,
    worse_votes: int,
    pending_votes: int,
    majority_threshold: int,
    decision_status: str,
    rationale: str,
    worker_votes: dict[str, dict[str, Any]],
) -> str:
    lines = [
        "# Decision",
        "",
        f"- run: {run_id}",
        f"- baseline average: {baseline_total if baseline_total is not None else 'pending'}",
        f"- mutation average: {mutation_total if mutation_total is not None else 'pending'}",
        f"- evaluator votes for mutation: {improved_votes}",
        f"- evaluator tie votes: {same_votes}",
        f"- evaluator votes for baseline: {worse_votes}",
        f"- pending evaluator votes: {pending_votes}",
        f"- majority threshold: {majority_threshold}",
        f"- final status: {decision_status}",
        "",
        "## Worker Shards And Evaluator Judgments",
        "",
    ]
    for worker, result in worker_votes.items():
        lines.append(
            f"- {worker}: evaluator_verdict={result.get('verdict', 'pending')}, confidence={result.get('confidence', 'unknown')}, baseline_total={result.get('baseline_total')}, mutation_total={result.get('mutation_total')}, delta={result.get('delta')}"
        )
    lines.extend(["", "## Final Rationale", "", rationale])
    return "\n".join(lines) + "\n"


def average(values: list[float]) -> float | None:
    if not values:
        return None
    return round(sum(values) / len(values), 3)


def judgment_vote(status: str, verdict: str) -> str:
    if status != "completed":
        return "pending"
    if verdict == "mutation_better":
        return "improved"
    if verdict == "baseline_better":
        return "worse"
    if verdict == "tie":
        return "same"
    return "pending"


def main() -> int:
    parser = argparse.ArgumentParser(description="Aggregate evaluator judgments into a majority-over-baseline decision.")
    parser.add_argument("target_skill_path", help="Path to the target skill directory")
    parser.add_argument("--run-id", help="Optional run id such as run-20260327-001; defaults to the latest run")
    args = parser.parse_args()

    target_root = Path(args.target_skill_path).expanduser().resolve()
    run_dir = resolve_run_dir(target_root, args.run_id)

    manifest = load_json(run_dir / "manifest.json")
    mutation = load_json(run_dir / "mutation.json")
    scores = load_json(run_dir / "scores.json")
    decision = load_json(run_dir / "decision.json")

    improved_votes = 0
    same_votes = 0
    worse_votes = 0
    pending_votes = 0
    baseline_totals: list[float] = []
    mutation_totals: list[float] = []
    worker_votes: dict[str, dict[str, Any]] = {}
    deterministic_concerns: list[str] = []

    for worker in manifest.get("workers", []):
        grade_path = run_dir / "grades" / f"{worker}.json"
        judgment_path = run_dir / "judgments" / f"{worker}.json"
        grade = load_json(grade_path)
        judgment = load_json(judgment_path)
        judgment_status = judgment.get("status", "pending")
        verdict = judgment_vote(judgment_status, judgment.get("verdict", ""))
        baseline_total = grade.get("baseline_total")
        mutation_total = grade.get("mutation_total")
        delta = grade.get("delta")

        if isinstance(baseline_total, (int, float)):
            baseline_totals.append(float(baseline_total))
        if isinstance(mutation_total, (int, float)):
            mutation_totals.append(float(mutation_total))

        if verdict == "improved":
            improved_votes += 1
        elif verdict == "same":
            same_votes += 1
        elif verdict == "worse":
            worse_votes += 1
        else:
            pending_votes += 1

        if grade.get("mutation_regression_pass") is False:
            deterministic_concerns.append(f"{worker}: mutation failed at least one regression check")
        if grade.get("baseline_regression_pass") is False:
            deterministic_concerns.append(f"{worker}: baseline failed at least one regression check")

        worker_votes[worker] = {
            "verdict": verdict,
            "raw_judgment_verdict": judgment.get("verdict", ""),
            "judgment_status": judgment_status,
            "confidence": judgment.get("confidence", ""),
            "baseline_total": baseline_total,
            "mutation_total": mutation_total,
            "delta": delta,
            "judgment_rationale": judgment.get("rationale", ""),
            "deterministic_rationale": grade.get("rationale", ""),
            "mutation_better_on": judgment.get("mutation_better_on", []),
            "baseline_better_on": judgment.get("baseline_better_on", []),
            "tie_on": judgment.get("tie_on", []),
            "risks": judgment.get("risks", []),
        }

    majority_threshold = int(decision.get("majority_threshold") or manifest.get("majority_threshold") or 0)
    baseline_average = average(baseline_totals)
    mutation_average = average(mutation_totals)

    if improved_votes >= majority_threshold and majority_threshold > 0:
        decision_status = "keep"
        rationale = f"The mutation won {improved_votes} evaluator shard judgment(s), which meets the majority threshold of {majority_threshold}."
    elif pending_votes > 0:
        decision_status = "pending"
        rationale = "At least one evaluator judgment is still incomplete, so the run cannot be closed yet."
    else:
        decision_status = "no_change"
        rationale = f"The mutation won only {improved_votes} evaluator shard judgment(s), which does not reach the majority threshold of {majority_threshold}."

    if deterministic_concerns:
        rationale += " Deterministic evidence raised these concerns: " + "; ".join(deterministic_concerns) + "."

    scores.update(
        {
            "worker_votes": worker_votes,
            "baseline_average": baseline_average,
            "mutation_average": mutation_average,
            "improved_votes": improved_votes,
            "same_votes": same_votes,
            "worse_votes": worse_votes,
            "pending_votes": pending_votes,
            "majority_threshold": majority_threshold,
            "decision": decision_status,
            "deterministic_concerns": deterministic_concerns,
        }
    )

    decision.update(
        {
            "status": decision_status,
            "improved_votes": improved_votes,
            "same_votes": same_votes,
            "worse_votes": worse_votes,
            "pending_votes": pending_votes,
            "changed_files": mutation.get("changed_files", []),
            "decision_rationale": rationale,
            "mutation_brief": mutation.get("mutation_brief", ""),
            "mutation_hypothesis": mutation.get("mutation_hypothesis", ""),
        }
    )

    write_json(run_dir / "scores.json", scores)
    write_json(run_dir / "decision.json", decision)
    (run_dir / "decision.md").write_text(
        render_decision_markdown(
            manifest.get("run_id", run_dir.name),
            mutation_average,
            baseline_average,
            improved_votes,
            same_votes,
            worse_votes,
            pending_votes,
            majority_threshold,
            decision_status,
            rationale,
            worker_votes,
        ),
        encoding="utf-8",
    )

    print(run_dir / "decision.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
