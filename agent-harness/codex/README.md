# Codex Harness For Economics Research

This folder is the portable source pack for the Padova Codex CLI and Codex app
lanes. Copy the pieces into a research project after reading them.

Official Codex docs checked on 2026-06-24:

- Codex overview: <https://developers.openai.com/codex/>
- AGENTS.md: <https://developers.openai.com/codex/guides/agents-md/>
- Skills: <https://developers.openai.com/codex/skills/>
- Subagents: <https://developers.openai.com/codex/subagents/>
- Hooks: <https://developers.openai.com/codex/hooks/>
- MCP: <https://developers.openai.com/codex/mcp/>
- Codex app commands: <https://developers.openai.com/codex/app/commands/>
- GitHub integration: <https://developers.openai.com/codex/integrations/github/>

The issue template for this pack used older docs URLs such as
`/config/hooks/`, `/config/mcp/`, and `/concepts/subagents/`. The current docs
use `/hooks/`, `/mcp/`, and `/subagents/`; the file layout below follows the
current docs.

## Install Map

| Asset | Portable source | Project-native path |
| --- | --- | --- |
| Project instructions | `AGENTS.md` | `AGENTS.md` |
| Skills | `skills/<name>/SKILL.md` | `.agents/skills/<name>/SKILL.md` |
| Subagents | `agents/<name>.toml` | `.codex/agents/<name>.toml` |
| Hooks config | `hooks/hooks.json` | `.codex/hooks.json` |
| Hook scripts | `hooks/*.py` | `.codex/hooks/*.py` |
| MCP config example | `mcp/config.toml.example` | merge into `.codex/config.toml` |
| Goal examples | `goals/*.md` | paste into `/goal` or app goal controls |
| Orchestration prompts | `orchestration/*.md` | paste into GitHub issues or cloud tasks |

For a disposable copy of the Card-Krueger example:

```bash
cp -R examples/card-krueger /tmp/ck-codex-demo
cd /tmp/ck-codex-demo
mkdir -p .agents/skills .codex/agents .codex/hooks
cp -R /path/to/AC4E_Padova/agent-harness/codex/skills/* .agents/skills/
cp /path/to/AC4E_Padova/agent-harness/codex/agents/*.toml .codex/agents/
cp /path/to/AC4E_Padova/agent-harness/codex/hooks/hooks.json .codex/hooks.json
cp /path/to/AC4E_Padova/agent-harness/codex/hooks/*.py .codex/hooks/
cp /path/to/AC4E_Padova/agent-harness/codex/AGENTS.md AGENTS.md
```

Review hooks before trusting them:

```text
/hooks
```

## CLI And App Notes

The CLI and app use the same repository files. The difference is the surface
where you start, review, and resume the work. In CLI lanes, verify command
availability with `codex --version` and slash-command help. In the app, use the
command menu or documented app commands; do not assume a UI label unless it is
visible in the installed app.

## Included Skills

- `research-sdd`: plan a research task before editing code or prose.
- `data-reviewer`: read-only audit of data source, unit, coding, and caveats.
- `replication-checker`: clean-room reproducibility checklist.
- `referee-checklist`: pre-submission economics paper review.
- `paper-polisher`: prose edit that preserves claims and citations.
- `loop-on-verification`: bounded implement/evaluate/revise loop.

## Included Reviewer Subagents

- `identification-data-reviewer`: checks DiD design, data coding, and
  synthetic-data caveats.
- `replication-verifier`: checks reproducibility and test evidence.
- `sdd-orchestrator`: manages spec-driven planning.
- `pr-scope-reviewer`: reviews PR scope, privacy, and merge readiness.

Use subagents by name in a prompt, for example:

```text
Use identification-data-reviewer to review examples/card-krueger read-only.
Return blockers first and do not edit files.
```

## Read-Only Skill Invocation Prompt

```text
Use the data-reviewer skill on examples/card-krueger. Read only README.md,
docs/data_source_map.md, docs/research_design_memo.md, data/synthetic_fast_food_panel.csv,
and src/did_analysis.py. Do not edit files or run the analysis. Return a table of
PASS/FAIL/UNABLE TO CHECK for source, unit, treatment group, comparison group,
outcome, wave coding, panel balance, missing values, and synthetic-data caveat.
```

## Verification Expectations

For Card-Krueger changes, a PR should normally report:

```bash
python3 examples/card-krueger/src/did_analysis.py
python3 -m pytest examples/card-krueger/tests
```

For harness-only changes, do not launch Codex locally just to test the harness.
Static checks are enough: file tree, hook syntax, JSON/TOML parsing, and a dry-run
read-only prompt like the one above.

## Safety Rules

- Do not edit `examples/card-krueger/data/synthetic_fast_food_panel.csv` unless a
  task explicitly asks for a data fixture change.
- Do not claim the synthetic data replicate Card and Krueger (1994).
- Do not put secrets or API keys in `.codex/config.toml`.
- Hooks are examples. They run commands from your machine after you trust them,
  so read every hook script before enabling it.
