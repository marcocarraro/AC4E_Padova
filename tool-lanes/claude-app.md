# Lane B2: Claude Code App

Use this lane for the Claude Code desktop app, visual diffs, and app-managed
sessions. The project harness files are the same as the CLI lane.

Official docs checked on 2026-06-24:

- Overview and desktop app: <https://code.claude.com/docs/en/overview>
- Settings: <https://code.claude.com/docs/en/settings>
- Skills: <https://code.claude.com/docs/en/skills>
- Subagents: <https://code.claude.com/docs/en/sub-agents>
- Hooks: <https://code.claude.com/docs/en/hooks>
- MCP: <https://code.claude.com/docs/en/mcp>
- Sessions: <https://code.claude.com/docs/en/manage-sessions>

## Setup

1. Open the Claude desktop app.
2. Use the Code tab and set the project folder to your `starter_article` copy.
3. Start with a read-only prompt.

```text
Read README.md, GUIDE.md, examples/card-krueger/README.md, and
examples/claude-app/README.md. Do not edit files. Explain the app lane and the
files I need from examples/claude/.
```

## Harness Map

| Need | Path or action |
| --- | --- |
| Context file | `CLAUDE.md`, plus shared `AGENTS.md` when useful |
| Skills | `examples/claude/.claude/skills/` |
| Subagents/reviewers | `examples/claude/.claude/agents/` |
| Hooks | `examples/claude/.claude/settings.example.json` and `.claude/hooks/` |
| MCP | project `.claude/settings.json` MCP entries after issue #9; env vars for secrets |
| Loop/goal | app checkpoints, app sessions, `/loop` where available |
| Cloud/background | desktop/web/background sessions where account features allow |
| Review | visual diff, reviewer subagent, PR evidence |

## Merge Steps

Use the same harness files as Lane B1:

```bash
cp -r examples/starter_article /path/to/my-article
mkdir -p /path/to/my-article/.claude/{skills,agents,hooks}
cp -r examples/claude/.claude/skills/* /path/to/my-article/.claude/skills/
cp examples/claude/.claude/agents/*.md /path/to/my-article/.claude/agents/
cp -r examples/claude/.claude/hooks/* /path/to/my-article/.claude/hooks/
cp examples/claude/.claude/settings.example.json /path/to/my-article/.claude/settings.json
cp examples/claude/CLAUDE.md /path/to/my-article/CLAUDE.md
```

## Card-Krueger Prompt

```text
Use examples/card-krueger as the running case. Do not edit data. Draft a
checkpointed plan for adding a robustness-note section to the research design
memo. Stop after the plan and wait for my approval.
```

## Reviewer Prompt

```text
Run the verifier or identification-reviewer subagent on the current diff. Check
that the synthetic data caveat, data source, treatment/control groups, timing,
and verification commands remain correct. Return blockers first. Do not edit
files.
```

## Notes

- App UI labels and session handoff features change. Use the official docs and
  the installed app menus as the source of truth.
- Use app sessions for app work unless you deliberately hand off to another
  surface through a documented command.
