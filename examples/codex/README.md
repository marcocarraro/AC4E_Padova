# Codex Track (Lanes A1 And A2)

This folder is the project-native Codex example for the Padova workshop. It is
copied from [`../../agent-harness/codex/`](../../agent-harness/codex/README.md)
so participants can install the same harness in a disposable research project.

Official docs checked on 2026-06-24:

- Codex skills: <https://developers.openai.com/codex/skills/>
- Codex subagents: <https://developers.openai.com/codex/subagents/>
- Codex hooks: <https://developers.openai.com/codex/hooks/>
- Codex MCP: <https://developers.openai.com/codex/mcp/>
- Codex app commands: <https://developers.openai.com/codex/app/commands/>

## Merge steps

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

Review hooks before trusting them:

```text
/hooks
```

## Harness Contents

| Need | Path |
| --- | --- |
| Project instructions | `AGENTS.md` |
| Skills | `.agents/skills/` |
| Subagents/reviewers | `.codex/agents/` |
| Hooks | `.codex/hooks.json`, `.codex/hooks/` |
| MCP config example | `.codex/config.toml.example` |
| Goal examples | `goals/` |
| Orchestration prompts | `orchestration/` |

Skills included: `research-sdd`, `replication-checker`, `referee-checklist`,
`data-reviewer`, `paper-polisher`, and `loop-on-verification`.

Reviewer subagents included: `identification-data-reviewer`,
`replication-verifier`, `sdd-orchestrator`, and `pr-scope-reviewer`.

## Card-Krueger Read-Only Prompt

```text
Use the data-reviewer skill on examples/card-krueger. Read only README.md,
docs/data_source_map.md, docs/research_design_memo.md,
data/synthetic_fast_food_panel.csv, and src/did_analysis.py. Do not edit files
or run the analysis. Return PASS/FAIL/UNABLE TO CHECK for source, unit,
treatment group, comparison group, outcome, wave coding, panel balance, missing
values, and synthetic-data caveat.
```

## Long-running work

Use `/goal`, the app goal controls where available, or the goal files in
`goals/`. Keep max iterations bounded and require reviewer evidence before a PR.

Codex app (A2) uses the same files; see
[`../codex-app/README.md`](../codex-app/README.md).
