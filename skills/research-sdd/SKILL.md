---
name: research-sdd
description: >-
  Use for planning a nontrivial economics research change before editing:
  empirical specs, data pipeline changes, robustness checks, paper sections, or
  referee-response tasks. Trigger on research-sdd, spec, design memo,
  requirements, robustness plan, or implementation plan.
---

# Research SDD

Plan first, then implement the smallest approved slice.

## Checklist

1. Read `AGENTS.md`, the relevant README, and the task or issue acceptance
   criteria.
2. Identify the research object: data, estimand, specification, figure, table,
   prose section, or review report.
3. Draft requirements using checkable language. Prefer:
   - `WHEN [command runs] THEN [output exists or contains X]`.
   - `IF [data are synthetic] THEN [no causal claim is made]`.
4. Draft a design note with files to read, files allowed to edit, verification
   commands, and identification risks.
5. Stop for approval before broad edits unless the task already authorizes
   implementation.
6. After implementation, verify only the scoped criteria and report exact
   evidence.

## Output

```markdown
# Research SDD Plan

## Scope

## Requirements

## Design

## Verification

## Risks And Human Checks
```

## Constraints

- Do not skip the data-source and sample-restriction check.
- Do not use synthetic teaching data for a substantive claim.
- Do not broaden the task without opening a new issue or asking the user.
