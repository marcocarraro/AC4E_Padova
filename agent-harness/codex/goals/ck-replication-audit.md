---
name: ck-replication-audit
---

# Goal: Replication Audit Of The Card-Krueger Teaching Example

## Description

Audit `examples/card-krueger/` for clean-run reproducibility. The result is a
written report that says whether a participant can reproduce the documented group
means, toy DiD estimate, and tests from the repository root.

## Approach

1. Read `examples/card-krueger/README.md`,
   `examples/card-krueger/docs/data_source_map.md`, and
   `agent-harness/codex/skills/replication-checker/SKILL.md`.
2. Check for hardcoded absolute paths in `examples/card-krueger/src/`.
3. Confirm the README documents setup, analysis command, tests, and synthetic-data
   caveat.
4. Run the documented commands only if the session allows local execution.
5. Write a report to `notes/replication_audit_ck.md`.

## Acceptance Criteria

- [ ] `notes/replication_audit_ck.md` exists.
- [ ] The report contains a per-criterion table with PASS/FAIL/UNABLE TO CHECK.
- [ ] The report includes exact command evidence if commands were run.
- [ ] The report states GREEN, YELLOW, or RED and explains the status.
- [ ] The audit does not modify `examples/card-krueger/data/synthetic_fast_food_panel.csv`.
- [ ] The report distinguishes workflow reproducibility from a substantive
      replication of Card and Krueger (1994).

## Constraints

- Do not edit files inside `examples/card-krueger/`; this is a read-only audit.
- Do not mark GREEN unless command evidence exists and passes.
- Do not claim the synthetic estimate is a research finding.
