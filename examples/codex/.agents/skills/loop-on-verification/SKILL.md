---
name: loop-on-verification
description: >-
  Use when a task has explicit, mechanically checkable acceptance criteria and
  the agent should iterate implement, verify, and revise until GREEN or a maximum
  of three iterations is reached.
---

# Loop On Verification

Run a bounded execution loop against acceptance criteria.

## Checklist

1. Read the issue, goal file, or task prompt and copy the acceptance criteria.
2. Set `max_iterations = 3`.
3. Implement only the smallest change needed for the current criterion.
4. Evaluate with a reviewer role such as `replication-verifier` or
   `identification-data-reviewer`.
5. Record each criterion as PASS, FAIL, or UNABLE TO CHECK.
6. If all pass, stop with GREEN and request human diff review.
7. If a minor gap remains, revise only that gap and continue.
8. If a blocker cannot be resolved within scope, stop with RED and draft a new
   issue for the blocker.

## Card-Krueger Example

Use this loop for a robustness task only if the goal states:

- allowed files;
- required command output;
- required tests;
- raw or synthetic data files that must remain unchanged;
- explicit caveat that synthetic data do not support a causal claim.

## Output

```markdown
# Verification Loop

| Iteration | Verdict | Evidence | Next Action |
| --- | --- | --- | --- |

## Final Status

## Remaining Human Checks
```

## Constraints

- Do not loop indefinitely.
- Do not auto-merge after GREEN.
- Do not broaden scope; new findings become new issues.
