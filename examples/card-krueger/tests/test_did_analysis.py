from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from did_analysis import (  # noqa: E402
    DEFAULT_DATA_PATH,
    estimate_difference_in_differences,
    load_fast_food_data,
    make_group_means,
    render_replication_note,
    validate_balanced_panel,
)


def test_synthetic_input_file_exists_and_is_named_clearly() -> None:
    assert DEFAULT_DATA_PATH.exists()
    assert "synthetic" in DEFAULT_DATA_PATH.name


def test_load_fast_food_data_adds_teaching_indicators() -> None:
    data = load_fast_food_data(DEFAULT_DATA_PATH)

    assert len(data) == 24
    assert data["store_id"].nunique() == 12
    assert {"post", "treated"}.issubset(data.columns)
    assert set(data["state"]) == {"NJ", "PA"}
    assert set(data["wave"]) == {"before", "after"}
    assert data["fte_employment"].notna().all()


def test_validate_balanced_panel_rejects_missing_wave() -> None:
    data = load_fast_food_data(DEFAULT_DATA_PATH)
    incomplete = data.loc[~((data["store_id"] == "NJ01") & (data["wave"] == "after"))]

    with pytest.raises(ValueError, match="before/after pair"):
        validate_balanced_panel(incomplete)


def test_make_group_means_reports_expected_cells() -> None:
    data = load_fast_food_data(DEFAULT_DATA_PATH)
    means = make_group_means(data)

    assert len(means) == 4
    nj_before = means.loc[
        (means["state"] == "NJ") & (means["wave"] == "before"), "mean_fte_employment"
    ].iloc[0]
    pa_after = means.loc[
        (means["state"] == "PA") & (means["wave"] == "after"), "mean_fte_employment"
    ].iloc[0]

    assert nj_before == pytest.approx(23.3333333333)
    assert pa_after == pytest.approx(23.0)


def test_estimate_difference_in_differences_returns_known_teaching_result() -> None:
    data = load_fast_food_data(DEFAULT_DATA_PATH)
    result = estimate_difference_in_differences(data)

    assert result.observations == 24
    assert result.treated_stores == 6
    assert result.comparison_stores == 6
    assert result.nj_change == pytest.approx(2.0)
    assert result.pa_change == pytest.approx(-1.0)
    assert result.did == pytest.approx(3.0)


def test_render_replication_note_keeps_research_caveat_visible() -> None:
    result = estimate_difference_in_differences(load_fast_food_data(DEFAULT_DATA_PATH))
    note = render_replication_note(result)

    assert "synthetic teaching data" in note
    assert "not Card and Krueger's raw data" in note
    assert "does not certify a causal claim" in note


def test_command_line_analysis_runs_and_writes_summary(tmp_path: Path) -> None:
    output_path = tmp_path / "summary.md"
    completed = subprocess.run(
        [
            sys.executable,
            str(PROJECT_ROOT / "src" / "did_analysis.py"),
            "--output",
            str(output_path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "Toy DID estimate: 3.0 FTE workers." in completed.stdout
    assert "Synthetic teaching data" in completed.stdout
    summary = output_path.read_text(encoding="utf-8")
    assert "Toy DID estimate: 3.0 FTE workers." in summary


def test_docs_contain_required_data_map_fields_and_caveats() -> None:
    readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
    data_map = (PROJECT_ROOT / "docs" / "data_source_map.md").read_text(
        encoding="utf-8"
    )
    combined = f"{readme}\n{data_map}".lower()

    for field in [
        "unit of observation",
        "treatment group",
        "comparison group",
        "outcome",
        "timing",
        "sample restriction",
        "access note",
    ]:
        assert field in combined

    assert "synthetic teaching data" in combined
    assert "not card and krueger's raw data" in combined


def test_loader_rejects_unexpected_state(tmp_path: Path) -> None:
    bad_data = pd.DataFrame(
        {
            "store_id": ["X01", "X01"],
            "state": ["XX", "XX"],
            "wave": ["before", "after"],
            "fte_employment": [10, 11],
        }
    )
    csv_path = tmp_path / "bad.csv"
    bad_data.to_csv(csv_path, index=False)

    with pytest.raises(ValueError, match="Unexpected states"):
        load_fast_food_data(csv_path)
