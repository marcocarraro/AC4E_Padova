---
name: replication-checker
description: >-
  Runs a clean-room replication check on economics research pipelines. Verifies
  dependencies are declared, no hardcoded paths exist, data sources are
  documented, and the pipeline runs from a clean state. Use when checking
  replication readiness, validating run instructions, before sharing code, or
  when the user asks to verify reproducibility.
---

# Replication Checker

Performs a clean-room replication check on research pipelines. Ensures a colleague can run the code from scratch.

## When to Use

- User asks to "verify replication," "check pipeline," "validate reproducibility"
- Before sharing code or submitting a replication package
- After major pipeline changes

## Workflow

1. **Identify entry point** — Script, notebook, or Make target in `src/`, `replication/`, or `scripts/`
2. **Run checks** — Execute `scripts/check_replication.py` from repo root
3. **Review criteria** — See `references/replication_criteria.md` for pass/fail definitions
4. **Run pipeline** — Attempt a clean run from repo root; note success/failure and any errors
5. **Produce report** — Output using the template below

## What to Check

| Check | Action |
|-------|--------|
| **Hardcoded paths** | Run script; grep for `/Users/`, `C:\\`, `localhost`, machine names |
| **Dependencies** | `requirements.txt` or `pyproject.toml` exists and lists all imports |
| **Replication docs** | `replication/README.md` exists with setup and run instructions |
| **Data sources** | `docs/data_source_map.md` or equivalent documents data access |
| **Clean run** | Pipeline executes from fresh clone + venv without manual edits |

## Output Format

```markdown
# Replication Report — [Project/Root]

**Status:** green / yellow / red

## Summary
[1–2 sentence verdict]

## Checks
| Check | Status | Notes |
|-------|--------|-------|
| Dependencies declared | pass/fail | |
| No hardcoded paths | pass/fail | |
| Replication README | pass/fail | |
| Data documented | pass/fail | |
| Imports in requirements | pass/fail | |
| Clean run | pass/fail | |

## Blockers (must fix)
- [ ]

## Recommendations
- [ ]

## Run Command
\`\`\`bash
[exact command to run from repo root]
\`\`\`
```

## Scripts

**check_replication.py** — Run from repo root:
```bash
python skills/course/replication-checker/scripts/check_replication.py /path/to/repo
```

Reports pass/fail for each check. For full pass/fail definitions, see `references/replication_criteria.md`.
