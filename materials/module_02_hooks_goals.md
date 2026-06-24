# Module 2: Install The Harness Stack

Time: 55 minutes

## Purpose

Install skills, subagents, hooks, and optional MCP into your `starter_article`
copy. Run one long-running goal with explicit stopping conditions.

| Layer | Role |
| --- | --- |
| Skill | Reusable procedure (referee, replication, SDD, prose) |
| Subagent | Isolated reviewer (identification, verifier) |
| Hook | Deterministic reminder after edits |
| Goal | Multi-step task with checkpoints |

Merge instructions: your lane README under `examples/{codex,claude,cursor}/`.

## Install checklist (all lanes)

- [ ] `referee-checklist` skill
- [ ] `replication-checker` skill
- [ ] `research-sdd` or `paper-polisher` skill
- [ ] `identification-data-reviewer` subagent or identification pass via skill
- [ ] `verifier` subagent where supported
- [ ] One hook pack (Codex/Claude/Cursor)
- [ ] (Cursor) Review `mcp.json.example` — optional FRED row in data map

## Step-by-step: skills

```text
List the skills in my project's .agents/skills, .claude/skills, or .cursor/skills folder.
Explain when to use research-sdd vs referee-checklist vs replication-checker.
```

Invoke replication-checker:

```text
Run the replication-checker skill on this repo root. Report green/yellow/red.
```

## Step-by-step: hooks

Use disposable copy first. Codex: `examples/codex/.codex/`. Claude: `settings.example.json`.
Cursor: `examples/cursor/.cursor/hooks.json`.

## Step-by-step: long-running goal

Use [`templates/long_running_goal_prompt.md`](../templates/long_running_goal_prompt.md):

```text
Goal: Complete rig/estimation — run src/estimate_did.py, update paper/main.tex
table reference, run pytest. Stop when tests pass and replication-checker is green.
Allowed: src/, tables/, paper/, docs/. Forbidden: data/raw/.
```

## Tool Notes

### Codex CLI

- Merge `.agents/skills/` and `.codex/agents/` from [`examples/codex/`](../examples/codex/README.md).
- `/hooks` to trust; `/goal` for long tasks.

### Codex app

- Same harness files as CLI; trust hooks in UI.

### Claude Code CLI

- Merge `.claude/skills/` and `.claude/agents/` from [`examples/claude/`](../examples/claude/README.md).
- `/agents` to run identification-reviewer.

### Claude Code app

- Same files; invoke skills from `/` menu.

### Cursor

- Full merge per [`examples/cursor/README.md`](../examples/cursor/README.md).
- Subagents: Task tool or `@identification-reviewer`.
- Optional MCP: copy `mcp.json.example` → `mcp.json` with your API key.

## Debrief

Which harness piece catches errors **before** you read the agent's prose?
