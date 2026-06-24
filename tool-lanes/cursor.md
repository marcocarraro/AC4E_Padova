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
- Cursor headless CLI: <https://cursor.com/docs/cli/headless>
- Cloud Agent: <https://cursor.com/docs/cloud-agent>
- GitHub integration and review: <https://cursor.com/docs/integrations/github>
- Bugbot: <https://cursor.com/docs/bugbot>

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
| Context file | `AGENTS.md`, `examples/cursor/AGENTS.md`, `.cursor/rules/*.mdc` |
| Skills | `examples/cursor/.cursor/skills/` |
| Subagents/reviewers | `examples/cursor/.cursor/agents/` |
| Hooks | `examples/cursor/.cursor/hooks.json` and `.cursor/hooks/`, version-sensitive |
| MCP | `examples/cursor/.cursor/mcp.json.example`; shared server in `agent-harness/mcp/fred/`; secrets through env vars |
| Loop/goal | `agent-harness/cursor/goals/`, checkpoints, Cursor CLI resume, Cloud Agent handoff |
| Cloud/background | `agent-harness/cursor/cloud-agent-prompts/`, Cursor Cloud Agent, background agents |
| Review | review pane, `/review` or Bugbot where enabled, PR evidence |

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

Portable source pack: [`agent-harness/cursor/`](../agent-harness/cursor/).

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

## Cloud Agent Prompt

Use [`agent-harness/cursor/cloud-agent-prompts/card-krueger-issue.md`](../agent-harness/cursor/cloud-agent-prompts/card-krueger-issue.md)
for issue-scoped tasks. The prompt requires an issue number, branch, allowed
files, out-of-scope list, acceptance criteria, verification evidence, and a
read-only reviewer subagent before PR review.

## Notes

- Cursor rules can be project, user, or team rules. For this workshop, keep
  reusable project rules in `.cursor/rules/*.mdc` and simple shared guidance in
  `AGENTS.md`.
- Cursor docs expose markdown versions of many pages, e.g.
  `https://cursor.com/docs/rules.md`, which are useful for agents auditing
  claims.
- Cursor skills are stored as `SKILL.md` files under `.cursor/skills/`.
- Cursor project subagents are markdown files under `.cursor/agents/` with YAML
  frontmatter. The included reviewers use `model: inherit` and read-only mode.
- Cursor MCP project configuration lives at `.cursor/mcp.json`; the example uses
  `${env:FRED_API_KEY}` and `${workspaceFolder}` interpolation.
- Cloud Agent, Bugbot, hooks, and CLI features can depend on plan, version,
  repository integration, and workspace settings. Cursor's Bugbot docs describe
  `/review` and `/review-bugbot` as available in Cursor 3.7+ and on
  `cursor.com/agents`; verify support in the installed version before using
  those commands in class.
