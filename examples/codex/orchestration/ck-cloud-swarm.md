# Card-Krueger Cloud Swarm Prompt

Use GitHub issues as the control plane. Each cloud task gets one issue, one
branch, clear allowed files, mechanical acceptance criteria, and a reviewer role.

## Waves

| Wave | Stream | Branch | Reviewer |
| --- | --- | --- | --- |
| 1 | Data documentation and panel validation | `ck/data-validation` | `identification-data-reviewer` |
| 1 | Literature/source note | `ck/source-note` | `pr-scope-reviewer` |
| 2 | Estimation or robustness implementation | `ck/robustness` | `replication-verifier` |
| 3 | Teaching figure | `ck/teaching-figure` | `pr-scope-reviewer` |
| 3 | Replication audit | `ck/replication-audit` | `replication-verifier` |

## Issue Template

```markdown
## Objective

## Allowed Files

## Out Of Scope

## Acceptance Criteria

- [ ] Mechanically checkable criterion.
- [ ] Verification command and expected artifact.
- [ ] Synthetic-data caveat remains visible.

## Reviewer

Use [reviewer subagent name] read-only before requesting merge.
```

## Merge Rules

1. Do not merge a stream until its acceptance criteria pass.
2. Do not merge a stream that modifies data unless the issue explicitly allowed it.
3. Run the relevant tests from `main` after each merge.
4. Record gaps as new issues rather than expanding an active stream.
