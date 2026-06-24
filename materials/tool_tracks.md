# Tool Tracks

Use this file during the live session as the short track selector. The detailed
participant manuals live in [`tool-lanes/`](../tool-lanes/).

## Pick One Lane

| Lane | Tool | Surface | Detailed manual | Best fit |
| --- | --- | --- | --- | --- |
| A1 | Codex | CLI | [`tool-lanes/codex-cli.md`](../tool-lanes/codex-cli.md) | Terminal-first work, goals, GitHub handoff |
| A2 | Codex | Desktop app | [`tool-lanes/codex-app.md`](../tool-lanes/codex-app.md) | App threads, visual review, same harness files |
| B1 | Claude Code | CLI | [`tool-lanes/claude-cli.md`](../tool-lanes/claude-cli.md) | Terminal-first Claude workflow |
| B2 | Claude Code | Desktop app | [`tool-lanes/claude-app.md`](../tool-lanes/claude-app.md) | App sessions, visual diff review |
| C | Cursor | IDE and CLI | [`tool-lanes/cursor.md`](../tool-lanes/cursor.md) | IDE-first work, rules, background/cloud agents |

You do not need every tool. Choose one lane for the workshop and translate the
same harness concepts to your own research project.

## Common Workflow

1. Read the repository orientation.
2. Inspect the runnable Card-Krueger example in `examples/card-krueger/`.
3. Copy `examples/starter_article/` for your own practice project.
4. Merge the harness files for your lane.
5. Run one scoped prompt, one review prompt, and one verification check.
6. Record evidence in a review or orchestration log.

## Harness Matrix

| Harness need | Codex paths | Claude Code paths | Cursor paths |
| --- | --- | --- | --- |
| Project instructions | `AGENTS.md`, `examples/codex/AGENTS.md` | `CLAUDE.md`, `examples/claude/CLAUDE.md` | `AGENTS.md`, `.cursor/rules/*.mdc` |
| Skills | `examples/codex/.agents/skills/` | `examples/claude/.claude/skills/` | `examples/cursor/.cursor/skills/` |
| Subagents or reviewers | `examples/codex/.codex/agents/` | `examples/claude/.claude/agents/` | `examples/cursor/.cursor/agents/` |
| Hooks | `examples/codex/.codex/hooks.json`, `examples/codex/.codex/hooks/` | `examples/claude/.claude/settings.example.json` and hooks | `examples/cursor/.cursor/hooks.json` |
| MCP | `examples/codex/.codex/config.toml.example` now; issue #9 validates the server | `.claude/settings.json` MCP entries after issue #9 | `examples/cursor/.cursor/mcp.json.example` |
| Loop or goal | `/goal`, app goal, `templates/long_running_goal_prompt.md` | checkpoints, `/loop` where available, `claude --continue` | Agent checkpoints, Cursor CLI resume, Cloud Agent |
| Cloud/background | Codex cloud and GitHub review | Claude web/desktop/background sessions where available | Cursor Cloud Agent and background agents |
| Review | `/review`, `/diff`, PR evidence | subagent review, diff, PR evidence | review pane, Bugbot/review where configured, PR evidence |

## OS And Version Caveats

- CLI paths are the fallback when a desktop app is unavailable or blocked.
- Desktop/app labels change; verify UI labels in the installed version.
- Hooks, MCP, cloud/background agents, and review integrations may require
  account features, trust prompts, or quota.
- Store API keys in environment variables or local ignored files, never in the
  repository.

## Demo Order

The deck follows [`slides/workshop/demo_map.md`](../slides/workshop/demo_map.md).
The tool-lane block starts after the Card-Krueger example and before GitHub
orchestration.
