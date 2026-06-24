# Lane C: Cursor

Use this lane for IDE-first work, rules, review panes, and Cursor Cloud Agent or
background-agent workflows.

Official docs checked on 2026-06-24:

- Cursor docs: <https://cursor.com/docs>
- Rules and AGENTS.md: <https://cursor.com/docs/rules>
- Skills: <https://cursor.com/docs/skills>
- Subagents: <https://cursor.com/docs/subagents>
- Hooks: <https://cursor.com/docs/hooks>
- MCP: <https://cursor.com/docs/mcp>
- Cursor CLI: <https://cursor.com/docs/cli/overview>
- Cloud Agent: <https://cursor.com/docs/cloud-agent>
- GitHub integration and review: <https://cursor.com/docs/integrations/github>

## Setup

1. Open this repository or your `starter_article` copy in Cursor.
2. Let indexing finish.
3. Use Ask for read-only exploration and Agent for implementation.
4. If using the CLI, verify `cursor --version` or `agent --help` depending on
   your installed Cursor CLI.

Start read-only:

```text
Read README.md, GUIDE.md, examples/card-krueger/README.md, and
examples/cursor/README.md. Do not edit files. Explain the Cursor lane and the
first harness files to copy.
```

## Harness Map

| Need | Path or action |
| --- | --- |
| Context file | `AGENTS.md`, `examples/cursor/AGENTS.md`, `.cursor/rules/economics-research.mdc` |
| Skills | `examples/cursor/.cursor/skills/` |
| Subagents/reviewers | `examples/cursor/.cursor/agents/` |
| Hooks | `examples/cursor/.cursor/hooks.json` and `.cursor/hooks/` |
| MCP | `examples/cursor/.cursor/mcp.json.example`; secrets through env vars |
| Loop/goal | Agent checkpoints, Cursor CLI resume, Cloud Agent handoff |
| Cloud/background | Cursor Cloud Agent, background agents, worktrees where available |
| Review | review pane, Bugbot/review where configured, PR evidence |

## Merge Steps

```bash
cp -r examples/starter_article /path/to/my-article
cp -r examples/cursor/.cursor /path/to/my-article/
cp examples/cursor/AGENTS.md /path/to/my-article/AGENTS.md
```

Optional MCP config:

```bash
cp examples/cursor/.cursor/mcp.json.example /path/to/my-article/.cursor/mcp.json
```

Edit the MCP config to use environment variables or local ignored files for
secrets. Never commit API keys.

## Card-Krueger Prompt

```text
Use examples/card-krueger as the running case. Do not edit data. In Plan mode,
draft an issue for adding a robustness-check section to the design memo. Include
allowed files, acceptance criteria, verification command, and a note that the
synthetic data do not support a causal claim.
```

## Reviewer Prompt

```text
Use the identification-reviewer subagent or review pane on the current diff.
Check data source, unit, treatment group, comparison group, outcome, timing,
synthetic-data caveat, and test evidence. Return blockers first. Do not edit
files.
```

## Notes

- Cursor rules can be project, user, or team rules. For this workshop, keep
  reusable project rules in `.cursor/rules/*.mdc` and simple shared guidance in
  `AGENTS.md`.
- Cursor docs expose markdown versions of many pages, e.g.
  `https://cursor.com/docs/rules.md`, which are useful for agents auditing
  claims.
- Cloud Agent, Bugbot/review, hooks, and CLI features can depend on plan,
  version, and workspace settings. Verify in the installed version.
