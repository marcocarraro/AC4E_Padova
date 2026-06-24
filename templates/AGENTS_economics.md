# AGENTS.md Template For Economics Research

Workshop harness checklist: [`docs/research_article_harness.md`](../docs/research_article_harness.md).
Starter repo: [`examples/starter_article/`](../examples/starter_article/).

## Article lifecycle

| Phase | Typical files |
| --- | --- |
| Scaffold | `docs/project_brief.md`, this file, `.cursorignore` |
| Harness | skills, subagents, hooks (see your tool lane README) |
| Pipeline | `docs/research_design_memo.md`, `src/`, `paper/` |
| Quality | referee report, replication README, data source map |
| Sign-off | `notes/orchestration_log.md`, adoption plan |

## Project

[One paragraph describing the research question, paper type, target field, and
current stage. Example: "Applied micro paper estimating the effect of X on Y
using administrative panel data, currently preparing a seminar draft."]

## Tech Stack

- Python 3.12 for data cleaning and analysis.
- `pandas` for data work.
- `statsmodels` or `linearmodels` for inference.
- LaTeX for paper drafts.
- GitHub for issues, branches, pull requests, and review.

## Repository Map

```text
data/raw/          # Raw data, never edited by agents
data/processed/    # Cleaned intermediate data
src/               # Analysis code
tables/            # Generated regression tables
figures/           # Generated figures
paper/             # Manuscript and bibliography
notes/             # Planning, review, and replication notes
docs/              # Brief, design memo, data source map
spec/              # Optional research SDD (research-sdd skill)
replication/       # Clean-run instructions
```

## Research Conventions

- Use relative paths from the repository root.
- Use deterministic random seeds for simulations and bootstrap procedures.
- Report standard errors and clustering choices explicitly.
- Keep variable labels and units visible in tables and figures.
- Do not claim causality unless the identification strategy supports it.
- Do not invent citations or bibliographic entries.

## Verification Commands

```bash
python -m pytest
python src/main.py
latexmk -pdf paper/main.tex
```

Adapt these commands to the actual project. If no command exists yet, ask the
agent to create a replication script before making substantive changes.

## Do Not

- Do not edit files in `data/raw/`.
- Do not upload confidential data or manuscripts to external services.
- Do not delete files without explicit permission.
- Do not change identifying assumptions without explaining the reason.
- Do not hardcode absolute paths.
- Do not fabricate citations, data sources, or robustness results.
- Do not merge or accept changes before human review.

## Preferred Agent Workflow

1. Read this file, the README, and the relevant task file.
2. Restate the task and identify allowed files.
3. Propose a short plan before editing.
4. Make the smallest useful change.
5. Run the relevant verification command.
6. Summarize the diff, test result, and remaining risks.

