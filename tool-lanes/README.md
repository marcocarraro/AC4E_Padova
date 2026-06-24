# Tool Lane Manuals

These participant manuals translate the same economics research harness into
the available coding-agent surfaces.

| Lane | Manual | Surface |
| --- | --- | --- |
| A1 | [`codex-cli.md`](codex-cli.md) | Codex CLI |
| A2 | [`codex-app.md`](codex-app.md) | Codex desktop app |
| B1 | [`claude-cli.md`](claude-cli.md) | Claude Code CLI |
| B2 | [`claude-app.md`](claude-app.md) | Claude Code desktop app |
| C | [`cursor.md`](cursor.md) | Cursor IDE and CLI |

Each lane covers setup, context files, skills, subagents or reviewer roles,
hooks, MCP, loops/goals, cloud/background work, PR review, one Card-Krueger
prompt, and one reviewer prompt.

Tool surfaces change quickly. When a label or command differs from these notes,
use the official docs linked in the lane manual and verify in your installed
version.

## Shared Starting Point

1. Run or inspect `examples/card-krueger/`.
2. Copy `examples/starter_article/` to a practice project.
3. Merge only the harness files for your lane.
4. Keep raw/private data and secrets outside agent context.
5. Require command output, diff, PR evidence, or review logs before accepting
   agent work.

## Completion Checklist

| Need | A1 Codex CLI | A2 Codex app | B1 Claude CLI | B2 Claude app | C Cursor |
| --- | --- | --- | --- | --- | --- |
| Setup | yes | yes | yes | yes | yes |
| Context file | `AGENTS.md` | `AGENTS.md` | `CLAUDE.md` | `CLAUDE.md` | `AGENTS.md`, rules |
| Skills | `.agents/skills/` | `.agents/skills/` | `.claude/skills/` | `.claude/skills/` | `.cursor/skills/` |
| Subagents/reviewers | `.codex/agents/` | `.codex/agents/` | `.claude/agents/` | `.claude/agents/` | `.cursor/agents/` |
| Hooks | `.codex/hooks` | `.codex/hooks` | `.claude/hooks` | `.claude/hooks` | `.cursor/hooks.json` |
| MCP | `.codex/config.toml` | `.codex/config.toml` | documented target | documented target | `.cursor/mcp.json.example` |
| Loop/goal | `/goal` | app goal/thread | checkpoint/continue | app session/checkpoint | Agent checkpoints/cloud |
| Cloud/background | Codex cloud/GitHub | Codex cloud/GitHub | web/background where available | desktop/web where available | Cloud Agent/background |
| Review | `/review`, PR | `/review`, PR | subagent/PR | subagent/PR | review pane/Bugbot/PR |
