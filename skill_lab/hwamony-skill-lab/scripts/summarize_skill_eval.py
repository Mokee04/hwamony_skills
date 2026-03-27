#!/usr/bin/env python3
"""Summarize supervisor/worker/evaluator skill-lab runs into eval artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from lab_config import case_groups, results_header


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def artifact_guide(run_dir: Path, manifest: dict, decision_json: dict, scores: dict) -> str:
    run_id = manifest.get("run_id", run_dir.name)
    workers = manifest.get("workers", [])
    lines = [
        "# Artifact Guide",
        "",
        f"- run: {run_id}",
        "- purpose: explain what each generated artifact means so the run can be reviewed later",
        "",
        "## Core Files",
        "",
        "- `manifest.json`: immutable run metadata such as run id, shard count, and selected case groups",
        "- `plan.md` and `plan.json`: the supervisor's human-readable and structured iteration plan, including the proposed improvement target",
        "- `rubric.json`: the supervisor-authored comparison rubric used by evaluator agents",
        "- `baseline.json`: the baseline snapshot and response record map for this run",
        "- `mutation.json`: the one bounded mutation being tested, plus the mutation snapshot path",
        "- `assignments.json`: the worker shard assignments and the baseline/mutation response paths for each case",
        "- `scores.json`: aggregated evaluator votes, deterministic evidence summaries, and the majority result",
        "- `decision.md` and `decision.json`: final keep/discard rationale, evaluator vote counts, and promotion status",
        "- `feedback.md`: operator or user feedback collected during the run",
        "- `patch-plan.md`: notes on the mutation and any follow-up ideas",
        "- `packets/*.md`: supervisor, worker, evaluator, and coordinator briefing packets for interactive execution",
        "",
        "## Worker Shards",
        "",
    ]
    for worker in workers:
        lines.extend(
            [
                f"- `grades/{worker}.json`: deterministic evidence for {worker}, including baseline total, mutation total, delta, and rubric-aligned requirement checks",
                f"- `judgments/{worker}.json`: evaluator agent judgment for {worker}, including `mutation_better` / `baseline_better` / `tie`, confidence, rationale, and risks",
                f"- `outputs/baseline/{worker}/...`: baseline outputs for {worker}'s shard",
                f"- `outputs/mutation/{worker}/...`: mutation outputs for {worker}'s shard",
                f"- `packets/{worker}.md`: instructions for how {worker} should run its shard",
                f"- `packets/evaluator-{worker}.md`: instructions for how the evaluator should compare {worker}'s baseline and mutation outputs",
            ]
        )

    lines.extend(
        [
            "",
            "## Backups",
            "",
            f"- `../../backups/{run_id}/original/SKILL.md`: the frozen baseline snapshot for the run",
            f"- `../../backups/{run_id}/mutation/SKILL.md`: the mutated snapshot tested in the run",
            "- `../../backups/<run-id>/promotion/*`: promotion-time backups created when the mutation replaces the live `SKILL.md`",
            "",
            "## Review Questions",
            "",
            "- What improvement target and one mutation did the supervisor choose?",
            "- Which shard belonged to each worker?",
            "- What deterministic evidence did each shard generate?",
            "- How did each evaluator judge baseline versus mutation?",
            "- Did the mutation beat baseline by evaluator-majority?",
            "- Which files back up the baseline, mutation, and any promotion?",
        ]
    )

    deterministic_concerns = scores.get("deterministic_concerns", [])
    if deterministic_concerns:
        lines.extend(["", "## Deterministic Concerns", "", *[f"- {item}" for item in deterministic_concerns]])

    if decision_json.get("promoted_mutation"):
        lines.extend(
            [
                "",
                "## Promotion Status",
                "",
                f"- promoted mutation: {decision_json.get('promoted_mutation')}",
                f"- promotion timestamp: {decision_json.get('promotion_timestamp', 'unknown')}",
            ]
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh eval/summary.md from recorded skill-lab runs.")
    parser.add_argument("target_skill_path", help="Path to the target skill directory")
    args = parser.parse_args()

    target_root = Path(args.target_skill_path).expanduser().resolve()
    eval_root = target_root / "eval"
    runs_dir = eval_root / "runs"
    summary_path = eval_root / "summary.md"
    results_path = eval_root / "results.tsv"

    if not runs_dir.exists():
        raise SystemExit(f"Missing runs directory: {runs_dir}")

    run_dirs = sorted(path for path in runs_dir.iterdir() if path.is_dir() and path.name.startswith("run-"))
    lines = [
        "# Eval Summary",
        "",
        f"- target skill: {target_root.name}",
        f"- total runs: {len(run_dirs)}",
    ]
    tsv_rows = [results_header()]

    if not run_dirs:
        lines.extend(["", "No runs recorded yet."])
    else:
        lines.extend(["", "## Runs"])
        for run_dir in run_dirs:
            manifest = load_json(run_dir / "manifest.json") if (run_dir / "manifest.json").exists() else {}
            mutation = load_json(run_dir / "mutation.json") if (run_dir / "mutation.json").exists() else {}
            scores = load_json(run_dir / "scores.json") if (run_dir / "scores.json").exists() else {}
            decision_json = load_json(run_dir / "decision.json") if (run_dir / "decision.json").exists() else {}
            assignments_path = run_dir / "assignments.json"
            rubric_path = run_dir / "rubric.json"
            judgments_dir = run_dir / "judgments"

            case_summary = manifest.get("cases", {})
            decision = scores.get("decision", "pending")
            baseline_average = scores.get("baseline_average")
            mutation_average = scores.get("mutation_average")
            improved_votes = scores.get("improved_votes", 0)
            same_votes = scores.get("same_votes", 0)
            worse_votes = scores.get("worse_votes", 0)
            worker_count = len(manifest.get("workers", []))

            lines.append(
                "- "
                + f"{manifest.get('run_id', run_dir.name)}: "
                + f"workers={worker_count}, "
                + ", ".join(f"{group}={len(case_summary.get(group, []))}" for group in case_groups())
                + ", "
                + f"decision={decision}, "
                + f"baseline={baseline_average if baseline_average is not None else 'pending'}, "
                + f"mutation={mutation_average if mutation_average is not None else 'pending'}, "
                + f"mutation_votes={improved_votes}, "
                + f"baseline_votes={worse_votes}, "
                + f"ties={same_votes}"
            )

            judgment_files = [judgments_dir / f"{worker}.json" for worker in manifest.get("workers", [])]
            audit_ready = all(
                path.exists()
                for path in (run_dir / "manifest.json", assignments_path, rubric_path, run_dir / "decision.json", run_dir / "plan.json")
            ) and all(path.exists() for path in judgment_files)
            notes = mutation.get("mutation_brief", "")
            if notes:
                notes = f"{notes}; audit_ready={audit_ready}"
            else:
                notes = f"audit_ready={audit_ready}"

            tsv_rows.append(
                "\t".join(
                    [
                        manifest.get("run_id", run_dir.name),
                        str(baseline_average if baseline_average is not None else "pending"),
                        str(mutation_average if mutation_average is not None else "pending"),
                        str(improved_votes),
                        str(worker_count),
                        str(decision),
                        ",".join(mutation.get("changed_files", [])),
                        notes,
                    ]
                )
            )

            (run_dir / "artifact-guide.md").write_text(artifact_guide(run_dir, manifest, decision_json, scores), encoding="utf-8")

    summary_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    results_path.write_text("\n".join(tsv_rows).rstrip() + "\n", encoding="utf-8")
    print(summary_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
