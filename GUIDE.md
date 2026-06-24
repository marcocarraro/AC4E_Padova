# Padova Participant Guide

This guide is the live reference for the 5-hour Padova version of **Agentic
Coding for Economists**. It adapts the longer Pavia guide into one compact
sequence centered on a research-article harness.

## The Core Idea

An AI coding agent can read files, draft plans, edit code or documents, run
commands when allowed, and report results. That is useful for economics research
only when the work is bounded.

Every important agent task needs:

1. **Scope** - what the agent may read, edit, run, or create.
2. **Evidence** - what diff, output, table, log, screenshot, or review note
   proves what happened.
3. **Review** - what the human checks before accepting the result.

The human owns the research question, identification argument, data access
rights, confidentiality decisions, interpretation, and final claims.

## Running Case: Card And Krueger

The workshop uses Card and Krueger's minimum-wage study as the running example.
The simple question is:

```text
What happened to fast-food employment in New Jersey relative to eastern
Pennsylvania after New Jersey raised its minimum wage in April 1992?
```

Starting references:

- David Card data page: <https://davidcard.berkeley.edu/data_sets.html>
- NBER working paper page: <https://www.nber.org/papers/w4509>
- Paper PDF: <https://davidcard.berkeley.edu/papers/njmin-aer.pdf>

Workshop translation:

1. document the public data source;
2. state treatment, comparison group, timing, outcome, and sample limits;
3. draft a project brief and research design memo;
4. estimate or inspect a baseline difference-in-differences result;
5. run a reviewer or replication check;
6. record what the agent did and what the human reviewed.

The runnable workshop version lives in [`examples/card-krueger/`](examples/card-krueger/).
It uses clearly labeled synthetic teaching data, not Card and Krueger's raw
data.

## Five-Hour Path

| Block | What you learn | What you produce |
| --- | --- | --- |
| Orientation | Tool lanes, repo map, research boundary | Tool lane choice |
| Foundations | Agent loop, context, privacy | Scoped read-only prompt |
| Card-Krueger scaffold | Brief, memo, data map | Draft research artifact |
| Harness pieces | Skills, subagents, hooks, MCP | Harness component plan |
| Orchestration | Issues, branches, cloud agents, swarms, loops, goals | Issue or goal prompt |
| Sprint | One bounded research task | Changed artifact |
| Verification | Replication, referee review, Playwright evidence | Review or evidence log |
| Transfer | Checklist and adoption | 7-day plan |

See [`SCHEDULE.md`](SCHEDULE.md) for timing.

## Tool Lanes

Pick one tool family and follow the matching examples.

| Lane | Files to inspect first |
| --- | --- |
| Codex CLI | `tool-lanes/codex-cli.md`, `examples/codex/README.md`, `agent-harness/codex/README.md` |
| Codex app | `tool-lanes/codex-app.md`, then Codex CLI files as reference |
| Claude Code CLI | `tool-lanes/claude-cli.md`, `examples/claude/README.md`, `agent-harness/claude/README.md` |
| Claude Code app | `tool-lanes/claude-app.md`, then Claude CLI files as reference |
| Cursor | `tool-lanes/cursor.md`, `examples/cursor/README.md`, `agent-harness/cursor/README.md` |

Version-sensitive UI labels, settings, and feature names change. Use
[`docs/sources.md`](docs/sources.md) for official docs and verify in your
installed version.

## First Agent Prompt

Use this before editing anything:

```text
Read README.md, START_HERE.md, SCHEDULE.md, GUIDE.md, and
examples/card-krueger/README.md and examples/starter_article/README.md. Do not
edit files. Explain:
1. the workshop path;
2. the Card-Krueger running example;
3. which files I should copy or personalize;
4. which files or folders I should not expose to agents.
```

## Card-Krueger Scaffold Prompt

```text
Use examples/card-krueger as the running example and examples/starter_article as
the project skeleton. Do not edit raw data.
Draft a project brief for the Card-Krueger minimum-wage example with research
question, data source, method, expected outputs, and out-of-scope items. Save the
draft in docs/project_brief.md or show me the diff first.
```

## Harness Pieces

The workshop uses six reusable pieces.

| Piece | What it does | Economist example |
| --- | --- | --- |
| Project instructions | Persistent context and boundaries | "Do not claim causality beyond the design." |
| Skill | Repeatable procedure | Replication checker or referee checklist |
| Subagent or reviewer role | Independent specialist context | Identification reviewer |
| Hook | Deterministic reminder or guardrail | Remind after code edits to run verification |
| MCP | Structured external tool access | FRED or scoped filesystem tool |
| Goal/loop/cloud agent | Longer bounded task | Work one issue until acceptance criteria pass |

Use the smallest piece that fits. A read-only prompt is often enough.

## Orchestration Pattern

Use GitHub issues as task cards:

```text
Title: Draft Card-Krueger design memo

Allowed files:
- docs/research_design_memo.md
- docs/data_source_map.md

Do not edit:
- data/raw/
- paper/main.tex

Acceptance criteria:
- treatment, comparison group, post period, and outcome are explicit;
- data source URL is recorded;
- limitations include at least two threats to identification;
- no claims go beyond the design.
```

For multiple agents, split work into separate branches and require a PR with
verification evidence before merging.

Use the complete orchestration pack in [`orchestration/`](orchestration/):

- [`orchestration/cloud_agent_issue_template.md`](orchestration/cloud_agent_issue_template.md)
  for issue bodies and cloud-agent triggers;
- [`orchestration/card_krueger_swarm.md`](orchestration/card_krueger_swarm.md)
  for parallel/sequential/blocked-by task order;
- [`orchestration/verification_loop.md`](orchestration/verification_loop.md)
  for green/yellow/red loop exits;
- [`orchestration/reviewer_issue_template.md`](orchestration/reviewer_issue_template.md)
  for read-only reviewer agents;
- [`notes/orchestration_log_template.md`](notes/orchestration_log_template.md)
  for evidence logs.

The Card-Krueger goal prompts in [`orchestration/goals/`](orchestration/goals/)
are designed to be mechanically checkable and safe without private data or live
secrets.

## Verification Prompts

Referee-style review:

```text
Act as an economics referee. Review the design memo only. Return blockers first:
identification, data source, sample definition, outcome units, and overclaiming.
Do not edit files.
```

Replication-style review:

```text
Use the replication-checker workflow on examples/starter_article. Do not edit
files. Report missing data, dependency, path, and output blockers before
suggestions.
```

Playwright evidence:

```text
Read examples/playwright/README.md, examples/playwright/fill_demo_form.py, and
examples/web-form/index.html. Explain how the script starts and stops the local
server, what evidence file it creates, and what row should be copied into a data
source map.
```

## Final Checklist

Before you transfer the harness to your own project, check:

- Did I define scope before asking for edits?
- Did I keep private data and secrets out of agent context?
- Did I record the data source and assumptions?
- Did I run or inspect a verification step?
- Did I review the claim myself?
- Do I know the next small issue for the project?

Use [`docs/research_article_harness.md`](docs/research_article_harness.md) for
the full checklist.
