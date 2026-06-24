# Claude Code CLI Track (Lane B1)

Merge harness into your [`starter_article/`](../starter_article/) copy.

## Merge steps

```bash
cp -r examples/starter_article /path/to/my-article
mkdir -p /path/to/my-article/.claude/{skills,agents}
cp -r examples/claude/.claude/skills/* /path/to/my-article/.claude/skills/
cp examples/claude/.claude/agents/*.md /path/to/my-article/.claude/agents/
cp examples/claude/.claude/settings.example.json /path/to/my-article/.claude/settings.json
```

Edit `settings.json` paths if needed. Run `/hooks` to trust.

## Skills and subagents

| Path | Role |
| --- | --- |
| `.claude/skills/referee-checklist/` | Referee report |
| `.claude/skills/replication-checker/` | Replication gate |
| `.claude/skills/research-sdd/` | Research planning |
| `.claude/skills/paper-polisher/` | Prose |
| `.claude/agents/identification-reviewer.md` | Identification |
| `.claude/agents/verifier.md` | Completion check |

## Long-running work

`claude --continue` or checkpoints in-session. See `templates/long_running_goal_prompt.md`.

**App** (B2): same `.claude/` files — [`../claude-app/README.md`](../claude-app/README.md).
