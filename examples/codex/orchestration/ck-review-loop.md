# Card-Krueger Review Loop Prompt

Use this prompt when a cloud or local agent needs to keep iterating until a narrow
task is verifiably done.

```text
Use the loop-on-verification skill. Read the issue acceptance criteria and set
max_iterations to 3. Work only on the allowed files.

After each iteration:
1. Run or inspect the smallest verification evidence allowed by the task.
2. Ask replication-verifier or identification-data-reviewer to review read-only.
3. Mark each criterion PASS, FAIL, or UNABLE TO CHECK.
4. If all pass, stop and request human diff review.
5. If a blocker remains after three iterations, stop and draft a new issue for the
   blocker.

For examples/card-krueger, preserve the synthetic-data caveat and do not edit
data/synthetic_fast_food_panel.csv unless the issue explicitly allows it.
```

## Evidence To Paste In PR

```text
Loop iterations:
- Iteration 1: [verdict, evidence, change]
- Iteration 2: [verdict, evidence, change]
- Iteration 3: [verdict, evidence, change]

Final status:
Verification commands:
Reviewer role used:
Remaining human checks:
```
