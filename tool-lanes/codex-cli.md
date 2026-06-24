# Lane A1: Codex CLI

Use this lane for terminal-first work, Linux, or when you want the most direct
local command, goal, and GitHub handoff workflow.

Official docs checked on 2026-06-24:

- Codex docs: <https://developers.openai.com/codex/>
- Codex CLI: <https://developers.openai.com/codex/cli/>
- CLI slash commands: <https://developers.openai.com/codex/cli/slash-commands/>
- AGENTS.md: <https://developers.openai.com/codex/guides/agents-md/>
- Hooks: <https://developers.openai.com/codex/hooks/>
- Skills: <https://developers.openai.com/codex/skills/>
- Subagents: <https://developers.openai.com/codex/subagents/>
- MCP: <https://developers.openai.com/codex/mcp/>
- Codex cloud: <https://developers.openai.com/codex/cloud/>
- GitHub integration: <https://developers.openai.com/codex/integrations/github/>

## Setup

```bash
codex --version
codex
```

Open the project root and start read-only:

```text
Read README.md, START_HERE.md, GUIDE.md, and examples/card-krueger/README.md.
Do not edit files. Explain the workshop path and the first command I should run.
```

## Harness Map

| Need | Path or action |
| --- | --- |
| Context file | `AGENTS.md`, `templates/AGENTS_economics.md`, `examples/codex/AGENTS.md` |
| Skills | `examples/codex/.agents/skills/` copied to `.agents/skills/` |
| Subagents/reviewers | `examples/codex/.codex/agents/` copied to `.codex/agents/` |
| Hooks | `examples/codex/.codex/hooks.json` and `examples/codex/.codex/hooks/`, trusted with `/hooks` |
| MCP | `examples/codex/.codex/config.toml.example`; keep secrets in env vars |
| Loop/goal | `/goal`, `templates/long_running_goal_prompt.md`, `codex resume --last` |
| Cloud/GitHub | Issue comments for Codex cloud tasks; GitHub integration for review |
| Review | `/diff`, `/review`, PR checklist, tests |

## Merge Steps

```bash
cp -r examples/starter_article /path/to/my-article
mkdir -p /path/to/my-article/.agents /path/to/my-article/.codex
cp -r examples/codex/.agents/skills /path/to/my-article/.agents/
cp -r examples/codex/.codex/agents /path/to/my-article/.codex/
cp examples/codex/.codex/hooks.json /path/to/my-article/.codex/
cp -r examples/codex/.codex/hooks /path/to/my-article/.codex/
cp examples/codex/.codex/config.toml.example /path/to/my-article/.codex/
cp examples/codex/AGENTS.md /path/to/my-article/AGENTS.md
```

Inspect hooks before trusting:

```text
/hooks
```

## Card-Krueger Prompt

```text
Use the Card-Krueger teaching example in examples/card-krueger. Do not edit raw
or synthetic data. Add one paragraph to docs/research_design_memo.md explaining
why the synthetic estimate is a workflow demo, not a causal claim. Show me the
diff and the verification command before committing.
```

## Reviewer Prompt

```text
/review

Review only examples/card-krueger/docs/research_design_memo.md and
examples/card-krueger/src/did_analysis.py. Return blockers first: missing data
source, wrong unit, wrong treatment/control, overclaiming, missing test evidence.
Do not edit files.
```

## Notes

- If a slash command is missing, use the equivalent plain prompt and record the
  installed Codex version.
- Codex cloud and GitHub review require account access and quota. If blocked,
  record the exact message and use local fallback for that issue only.
