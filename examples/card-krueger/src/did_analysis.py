"""Synthetic Card-Krueger difference-in-differences teaching example."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parents[1]
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "synthetic_fast_food_panel.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "outputs" / "baseline_did_summary.md"
REQUIRED_COLUMNS = {"store_id", "state", "wave", "fte_employment"}
EXPECTED_STATES = {"NJ", "PA"}
EXPECTED_WAVES = {"before", "after"}


@dataclass(frozen=True)
class DidResult:
    """Compact difference-in-differences result for the teaching example."""

    nj_change: float
    pa_change: float
    did: float
    observations: int
    treated_stores: int
    comparison_stores: int


def load_fast_food_data(csv_path: str | Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load the synthetic fast-food panel and add teaching indicators."""

    path = Path(csv_path)
    data = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(data.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")

    if data[list(REQUIRED_COLUMNS)].isna().any().any():
        raise ValueError("Dataset contains missing values in required columns")

    invalid_states = set(data["state"]) - EXPECTED_STATES
    if invalid_states:
        raise ValueError(f"Unexpected states: {sorted(invalid_states)}")

    invalid_waves = set(data["wave"]) - EXPECTED_WAVES
    if invalid_waves:
        raise ValueError(f"Unexpected waves: {sorted(invalid_waves)}")

    cleaned = data.copy()
    cleaned["fte_employment"] = pd.to_numeric(cleaned["fte_employment"])
    if (cleaned["fte_employment"] < 0).any():
        raise ValueError("fte_employment must be non-negative")

    cleaned["post"] = (cleaned["wave"] == "after").astype(int)
    cleaned["treated"] = (cleaned["state"] == "NJ").astype(int)
    cleaned["state_order"] = cleaned["state"].map({"NJ": 0, "PA": 1})
    return (
        cleaned.sort_values(["state_order", "store_id", "post"])
        .drop(columns="state_order")
        .reset_index(drop=True)
    )


def validate_balanced_panel(data: pd.DataFrame) -> None:
    """Check that each store has one before and one after observation."""

    duplicated_rows = data.duplicated(["store_id", "wave"])
    if duplicated_rows.any():
        duplicated = sorted(data.loc[duplicated_rows, "store_id"].unique())
        raise ValueError(f"Duplicate store-wave observations: {duplicated}")

    unbalanced = [
        store_id
        for store_id, waves in data.groupby("store_id")["wave"].agg(set).items()
        if waves != EXPECTED_WAVES
    ]
    if unbalanced:
        raise ValueError(f"Stores without a before/after pair: {sorted(unbalanced)}")

    changing_state = data.groupby("store_id")["state"].nunique()
    bad_state = sorted(changing_state[changing_state != 1].index)
    if bad_state:
        raise ValueError(f"Stores assigned to multiple states: {bad_state}")


def make_group_means(data: pd.DataFrame) -> pd.DataFrame:
    """Return mean full-time-equivalent employment by state and wave."""

    validate_balanced_panel(data)
    means = (
        data.groupby(["state", "wave"], as_index=False)["fte_employment"]
        .mean()
        .rename(columns={"fte_employment": "mean_fte_employment"})
    )
    means["state_order"] = means["state"].map({"NJ": 0, "PA": 1})
    means["wave_order"] = means["wave"].map({"before": 0, "after": 1})
    return means.sort_values(["state_order", "wave_order"]).drop(
        columns=["state_order", "wave_order"]
    )


def _mean_for(data: pd.DataFrame, state: str, wave: str) -> float:
    mask = (data["state"] == state) & (data["wave"] == wave)
    return float(data.loc[mask, "fte_employment"].mean())


def estimate_difference_in_differences(data: pd.DataFrame) -> DidResult:
    """Estimate the simple NJ-versus-PA before/after comparison."""

    validate_balanced_panel(data)

    nj_change = _mean_for(data, "NJ", "after") - _mean_for(data, "NJ", "before")
    pa_change = _mean_for(data, "PA", "after") - _mean_for(data, "PA", "before")

    return DidResult(
        nj_change=nj_change,
        pa_change=pa_change,
        did=nj_change - pa_change,
        observations=len(data),
        treated_stores=int(data.loc[data["state"] == "NJ", "store_id"].nunique()),
        comparison_stores=int(data.loc[data["state"] == "PA", "store_id"].nunique()),
    )


def _display_path(path: str | Path) -> str:
    """Return a repo-relative path when possible."""

    resolved = Path(path).resolve()
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return Path(path).as_posix()


def render_replication_note(
    result: DidResult, data_path: str | Path = DEFAULT_DATA_PATH
) -> str:
    """Document source, transformations, units, restrictions, and caveats."""

    return "\n".join(
        [
            "# Card-Krueger Synthetic Teaching Example",
            "",
            f"Data source in this repo: {_display_path(data_path)}.",
            "Source status: synthetic teaching data, not Card and Krueger's raw data.",
            "Public reference: https://davidcard.berkeley.edu/data_sets.html.",
            "Unit: store-wave observation.",
            "Outcome: full-time-equivalent employment in workers.",
            "Sample restriction: stores with one before and one after observation in NJ or PA.",
            "Transformation: created treated and post indicators and compared mean changes.",
            f"Observations: {result.observations}.",
            f"NJ stores: {result.treated_stores}.",
            f"PA stores: {result.comparison_stores}.",
            f"NJ change: {result.nj_change:.1f} FTE workers.",
            f"PA change: {result.pa_change:.1f} FTE workers.",
            f"Toy DID estimate: {result.did:.1f} FTE workers.",
            "Research caveat: this synthetic result does not reproduce the "
            "paper and does not certify a causal claim.",
        ]
    )


def write_replication_note(
    note: str, output_path: str | Path = DEFAULT_OUTPUT_PATH
) -> Path:
    """Write the replication note and return the output path."""

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(note + "\n", encoding="utf-8")
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        type=Path,
        default=DEFAULT_DATA_PATH,
        help="CSV path for the teaching panel.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Markdown output path for the replication note.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the teaching analysis and write a compact replication note."""

    args = parse_args()
    data = load_fast_food_data(args.data)
    means = make_group_means(data)
    result = estimate_difference_in_differences(data)
    note = render_replication_note(result, args.data)
    output_path = write_replication_note(note, args.output)

    print("Card-Krueger synthetic teaching example")
    print("=======================================")
    print("Group means")
    print(means.to_string(index=False))
    print()
    print(f"Toy DID estimate: {result.did:.1f} FTE workers.")
    print("Synthetic teaching data: not Card and Krueger's raw data.")
    print(f"Wrote {_display_path(output_path)}")


if __name__ == "__main__":
    main()
