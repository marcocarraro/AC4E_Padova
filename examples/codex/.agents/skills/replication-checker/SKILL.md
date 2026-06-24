---
name: replication-checker
description: >-
  Use when asked to verify reproducibility, audit a replication package, check a
  clean run, validate run instructions, or review before sharing research code.
---

# Replication Checker

This is a clean-room reproducibility checklist for economics research projects.

## Checklist

1. Read `AGENTS.md`, the example or project README, and any data source map.
2. Identify the documented entry point and the smallest safe verification command.
3. Check path hygiene: no `/Users/`, `C:\`, machine names, or hidden local data
   assumptions in runnable code.
4. Check dependencies: requirements are declared and match imports.
5. Check data documentation: source, unit of observation, sample restriction,
   transformations, and caveats are visible.
6. Check generated outputs: outputs are either reproducible or clearly ignored.
7. Run the smallest safe command only when the user or task allows execution.
8. Return GREEN only if runnable evidence supports it; otherwise use YELLOW or RED.

## Card-Krueger Baseline

Expected verification commands from the repository root:

```bash
python3 examples/card-krueger/src/did_analysis.py
python3 -m pytest examples/card-krueger/tests
```

## Output

```markdown
# Replication Report

**Status:** GREEN / YELLOW / RED

## Evidence

| Criterion | Status | Evidence |
| --- | --- | --- |

## Blockers

## Recommendations

## Commands
```

## Constraints

- Do not mark GREEN without command output or equivalent evidence.
- Do not modify data files during an audit.
- Do not treat a successful synthetic-data run as a substantive replication of
  Card and Krueger (1994).
