"""Tests for starter article DiD pipeline."""

from pathlib import Path

import pandas as pd

from src.estimate_did import DATA_PATH, estimate_twfe, load_panel

ROOT = Path(__file__).resolve().parents[1]


def test_data_exists():
    assert DATA_PATH.exists()


def test_load_panel_builds_did():
    df = load_panel()
    assert "did" in df.columns
    assert len(df) > 100


def test_twfe_runs():
    df = load_panel()
    results = estimate_twfe(df)
    assert results.nobs > 0
