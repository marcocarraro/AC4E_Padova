# Lane B1: Claude Code CLI

Use this lane for terminal-first Claude Code workflows and explicit
checkpointing.

Official docs checked on 2026-06-24:

- Overview: <https://code.claude.com/docs/en/overview>
- CLI reference: <https://code.claude.com/docs/en/cli-reference>
- Settings: <https://code.claude.com/docs/en/settings>
- Skills: <https://code.claude.com/docs/en/skills>
- Subagents: <https://code.claude.com/docs/en/sub-agents>
- Hooks: <https://code.claude.com/docs/en/hooks>
- MCP: <https://code.claude.com/docs/en/mcp>
- Sessions: <https://code.claude.com/docs/en/manage-sessions>

## Setup

```bash
claude --version
claude
```

Start read-only:

```text
Read README.md, GUIDE.md, examples/card-krueger/README.md, and
examples/claude/README.md. Do not edit files. Explain the Claude CLI lane.
```

## Harness Map

| Need | Path or action |
| --- | --- |
| Context file | `examples/claude/CLAUDE.md`, plus shared `AGENTS.md` when collaborating |
| Skills | `examples/claude/.claude/skills/` |
| Subagents/reviewers | `examples/claude/.claude/agents/` |
| Hooks | `examples/claude/.claude/settings.example.json` and `.claude/hooks/` |
| MCP | project `.claude/settings.json` MCP entries after issue #9; secrets in env vars |
| Loop/goal | checkpoint prompts, `/loop` where available, `claude --continue` |
| Cloud/background | Claude web, background sessions, or team workflows when available |
| Review | reviewer subagent, git diff, PR evidence |

## Merge Steps

```bash
cp -r examples/starter_article /path/to/my-article
mkdir -p /path/to/my-article/.claude/{skills,agents,hooks}
cp -r examples/claude/.claude/skills/* /path/to/my-article/.claude/skills/
cp examples/claude/.claude/agents/*.md /path/to/my-article/.claude/agents/
cp -r examples/claude/.claude/hooks/* /path/to/my-article/.claude/hooks/
cp examples/claude/.claude/settings.example.json /path/to/my-article/.claude/settings.json
cp examples/claude/CLAUDE.md /path/to/my-article/CLAUDE.md
```

Review hooks before use:

```text
/hooks
```

## Card-Krueger Prompt

```text
Use examples/card-krueger as the teaching case. Work toward this goal, but stop
after planning and wait for confirmation: add one test that protects the
synthetic-data caveat in the README and data source map. Allowed files are only
examples/card-krueger/tests/test_did_analysis.py and docs under
examples/card-krueger/. Do not edit data.
```

## Reviewer Prompt

```text
Use the identification-reviewer subagent on
examples/card-krueger/docs/research_design_memo.md. Review only identification,
data source, treatment/comparison group, timing, outcome units, and
overclaiming. Do not edit files.
```

## Notes

- Claude Code can work in terminal, IDE, desktop, and web surfaces. Handoff and
  resume behavior is version-sensitive; verify in the installed surface before
  relying on cross-surface history.
- Keep project settings in the project and secrets outside git.
