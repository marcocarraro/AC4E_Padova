# Long-Running Goal Prompt Template

Use this with Codex `/goal` or goal UI when available, or as a checkpointed
long-running prompt in Claude Code or Cursor.

## Surface notes

| Lane | How to use this template |
| --- | --- |
| Codex CLI | `/goal`, then paste body; resume with `codex resume --last` |
| Codex app | `/goal` or goal UI in thread; continue in same thread |
| Claude Code CLI | `/goal <condition>` (v2.1.139+); bound with `or stop after N turns`; `claude -p "/goal …"` for scripted runs |
| Claude Code app | `/goal` in the composer when available; otherwise paste template with checkpoints |
| Cursor | Agent with checkpoints, or background agent on a branch |

```text
Goal: [One concrete outcome, not an open-ended wish.]

Context:
- Project: [paper/project description].
- Audience: [coauthor, supervisor, referee, future self].
- Tool constraints: [Codex/Cursor/Claude, local only, no web, web allowed, etc.].
- Data constraints: [public only, confidential raw data excluded, no uploads].

Allowed files:
- Read: [specific files/folders].
- Edit: [specific files/folders].
- Create: [specific outputs].

Forbidden actions:
- Do not edit [files/folders].
- Do not upload [data/manuscripts].
- Do not install dependencies without asking.
- Do not invent citations, results, or data sources.

Done when:
- [Measurable artifact 1].
- [Measurable artifact 2].
- [Verification evidence].
- [Human review questions listed].

Checkpoints:
- Stop after scanning context and report the plan.
- Stop after first draft and report open questions.
- Stop after self-review and report final risks.

Verification:
- Run [command] if edits touch code.
- Otherwise produce [review log / checklist / screenshot / citation audit].

Final response:
- Changed files.
- Evidence reviewed.
- Verification result.
- Remaining risks.
```

Example (Codex CLI):

```text
/goal Create a referee-style pre-submission review pack for my own draft in
paper/main.tex. Create notes/referee_review.md and notes/revision_plan.md.
Do not edit paper/main.tex. Do not invent citations. Done when every major issue
points to a section, table, equation, or missing assumption, and each issue has a
concrete fix and difficulty rating. Stop after context scan, after draft review,
and after final self-review.
```

Example (Claude Code CLI — `/goal`):

```text
/goal notes/referee_review.md exists with major and minor issues for paper/main.tex, every major issue cites a section or table, no citations invented, and paper/main.tex is unchanged or stop after 12 turns
```

Example (Claude Code — checkpoint prompt without `/goal`):

```text
Work toward the following goal. Stop after each checkpoint and wait for my confirmation before continuing.

Goal: Create notes/referee_review.md from paper/main.tex using templates/referee_report.md.
Do not edit the source paper. Done when every major issue cites a line or table.
Checkpoints: after context scan, after draft, after self-review.
```
