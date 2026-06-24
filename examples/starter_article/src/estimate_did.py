"""Panel DiD demo for the starter article workshop repo."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

RANDOM_SEED = 42
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "city_month_panel.csv"
TABLES_DIR = PROJECT_ROOT / "tables"


def load_panel(csv_path: Path = DATA_PATH) -> pd.DataFrame:
    """Load city-month panel and build Treat x Post."""
    df = pd.read_csv(csv_path)
    required = {"city_id", "month", "log_emp", "treat", "post"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    out = df.copy()
    out["did"] = out["treat"] * out["post"]
    return out


def estimate_twfe(df: pd.DataFrame):
    """Two-way fixed effects via city and month dummies."""
    model = smf.ols(
        "log_emp ~ did + C(city_id) + C(month)",
        data=df,
    )
    return model.fit(cov_type="cluster", cov_kwds={"groups": df["city_id"]})


def write_main_table(results, path: Path = TABLES_DIR / "main_did.tex") -> None:
    """Write a minimal booktabs row for the DiD coefficient."""
    path.parent.mkdir(parents=True, exist_ok=True)
    coef, se = 0.0, float("nan")
    for key in results.params.index:
        if key == "did" or "did" in str(key).lower():
            coef = float(results.params[key])
            se = float(results.bse[key])
            break
    text = "\n".join(
        [
            r"\begin{tabular}{lcc}",
            r"\toprule",
            r" & Coefficient & Std. err. \\",
            r"\midrule",
            f"Treat $\\times$ Post & {coef:.3f} & ({se:.3f}) \\\\",
            r"\bottomrule",
            r"\end{tabular}",
        ]
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    np.random.seed(RANDOM_SEED)
    df = load_panel()
    results = estimate_twfe(df)
    write_main_table(results)
    if "did" in results.params.index:
        print(f"DiD estimate (Treat x Post): {results.params['did']:.4f}")
    print(f"Wrote {TABLES_DIR / 'main_did.tex'}")


if __name__ == "__main__":
    main()
