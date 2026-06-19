"""Run naive vs defended toy assistants and produce comparison results."""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from run_demo import run  # noqa: E402


def main() -> None:
    naive = run("naive")
    defended = run("defended")
    combined = pd.concat([naive, defended], ignore_index=True)
    out = PROJECT_ROOT / "results" / "comparison_results.csv"
    combined.to_csv(out, index=False)

    summary = (
        combined.groupby("mode")["total_score"]
        .agg(["mean", "min", "max"])
        .reset_index()
    )
    summary_out = PROJECT_ROOT / "results" / "score_summary.csv"
    summary.to_csv(summary_out, index=False)
    print(summary.to_string(index=False))
    print(f"\nSaved combined results to {out}")
    print(f"Saved summary to {summary_out}")


if __name__ == "__main__":
    main()
