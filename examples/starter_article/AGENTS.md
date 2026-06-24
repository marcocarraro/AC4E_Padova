# Agent Instructions — Starter Article

## Project context

Applied micro paper (workshop demo): effect of a 2020 remote-work policy pilot on
local service employment using city-month panel data and two-way fixed effects.
Stage: seminar draft; empirics in `src/estimate_did.py`, manuscript in `paper/main.tex`.

## Repository map

```text
data/raw/              # Synthetic demo data only — do not replace without permission
data/processed/        # Agent may write cleaned outputs here
docs/                  # Brief, design memo, data source map
src/                   # Estimation code
tables/ figures/       # Generated outputs
paper/                 # LaTeX manuscript
references/            # bibliography.bib
replication/           # Clean-run README
notes/                 # orchestration_log, review_log
spec/                  # Optional research SDD (research-sdd skill)
```

## Coding standards

- Python 3.10+, PEP 8, type hints on public functions.
- Relative paths from repo root; no machine-specific paths.
- Seeds: `RANDOM_SEED = 42` in `src/estimate_did.py`.
- LaTeX: `natbib`, `booktabs`; cite all external claims.

## Verification commands

```bash
python src/estimate_did.py
python -m pytest tests/ -q
python .cursor/skills/replication-checker/scripts/check_replication.py .
# latexmk -pdf paper/main.tex   # if latexmk installed
```

## Preferred agent workflow

1. Read this file, `docs/project_brief.md`, and the task issue.
2. Restate allowed files and stopping conditions.
3. Propose a short plan before editing.
4. Make the smallest useful change; run verification.
5. Summarize diff, test result, and remaining risks.

## Do not

- Do not edit `data/raw/` except to fix documented workshop bugs.
- Do not upload confidential manuscripts or restricted data to external APIs.
- Do not invent citations or robustness results.
- Do not claim causal identification without stating assumptions explicitly.
- Do not merge or accept changes before human review.

## Harness (Module 2)

Install skills and agents from your lane’s `examples/{codex,claude,cursor}/` folder.
Cursor paths use `.cursor/`; Codex uses `.codex/`; Claude uses `.claude/`.
