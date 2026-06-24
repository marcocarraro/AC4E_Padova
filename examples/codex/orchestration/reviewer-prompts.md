# Reviewer Prompts

## Identification And Data Reviewer

```text
Use identification-data-reviewer. Review examples/card-krueger read-only.
Check source status, unit of observation, treatment/comparison coding, before/after
timing, fte_employment coding, panel balance, sample restriction, and whether any
text overclaims beyond synthetic teaching data. Return blockers first with file
references. Do not edit files.
```

## Replication Verifier

```text
Use replication-verifier. Review the current diff against the issue acceptance
criteria. Check dependencies, path hygiene, data provenance, verification commands,
and generated outputs. Do not infer that tests passed unless command output is
present. Return GREEN/YELLOW/RED with evidence. Do not edit files.
```

## PR Scope Reviewer

```text
Use pr-scope-reviewer. Review this PR against its issue. Confirm allowed files,
privacy, no secrets, no raw-data changes, no unsupported causal claims, and exact
verification evidence. Return blockers first. Do not approve or merge.
```
