# Module 3: Research Pipeline Sprint

Time: 55 minutes

## Purpose

Move one **pipeline** step on your article: design memo plus a bounded code or
LaTeX change. Referee and replication depth come in Module 4.

Prompt library: [`templates/prompts_research_article.md`](../templates/prompts_research_article.md).

## Exercise A: Design memo (25 min)

1. Open `docs/research_design_memo.md` in your `starter_article` copy.
2. Use template [`templates/research_design_memo.md`](../templates/research_design_memo.md).
3. Prompt:

```text
Read docs/project_brief.md. Update docs/research_design_memo.md with a clear
identification section for the DiD design: estimand, parallel trends assumption,
and three threats. Do not invent citations.
```

4. Optional: invoke **identification-reviewer** subagent on the memo only.

## Exercise B: One empirics or writing artifact (25 min)

Pick **one**:

| Track | Task | Verify |
| --- | --- | --- |
| Empirics | Run or extend `src/estimate_did.py` | `pytest tests/ -q` |
| Writing | Add one paragraph to `paper/main.tex` | `latexmk` if installed |
| Theory | Extend `paper/theory_appendix.tex` | Human read |

Empirics prompt:

```text
Run src/estimate_did.py. Ensure tables/main_did.tex exists. Summarize the Treat x
Post coefficient and whether paper/main.tex text is consistent.
```

## Plan before code

For larger edits, use **research-sdd**:

```text
Use research-sdd: propose requirements for [FEATURE] in spec/intent.md. Do not
edit src/ until I approve.
```

## Tool Notes

### Codex CLI

- Agent mode in your article copy; `/diff` before accept.

### Codex app

- Same prompts; keep project folder on your copy.

### Claude Code CLI

- `claude --continue` for multi-step pipeline within one session.

### Claude Code app

- Checkpoints between memo and code tasks.

### Cursor

- Plan mode for memo; Agent mode for `src/` with rules applied.

## Debrief

What is one claim only **you** should sign off on after this module?
