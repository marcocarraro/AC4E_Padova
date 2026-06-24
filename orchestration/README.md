# Cloud Orchestration For Research Tasks

This folder is the participant-facing control plane for longer agent work. Use
it when a task is too large for one prompt but still small enough to be bounded
by one GitHub issue, one branch, one review, and one merge decision.

The running example is the Card-Krueger teaching project in
`examples/card-krueger/`. The same templates also fit a participant's own
research article copy in `examples/starter_article/`.

## Workshop Sequence

1. Open this file to explain the orchestration vocabulary.
2. Copy `cloud_agent_issue_template.md` into a GitHub issue.
3. Pick one stream from `card_krueger_swarm.md`.
4. Paste a matching goal from `goals/` into the issue or cloud-agent prompt.
5. Require the agent to follow `verification_loop.md`.
6. Ask a reviewer to use `reviewer_issue_template.md`.
7. Record the handoff in `../notes/orchestration_log_template.md`.

## Concept Map

| Concept | Meaning in this workshop | Card-Krueger example |
| --- | --- | --- |
| Main agent | The coordinator that reads the repo, scopes tasks, opens issues, and decides what to merge. | Maintains the issue list and merge order. |
| Skill | A reusable procedure that can be invoked inside an agent session. | Replication checker, referee checklist, or research SDD. |
| Subagent or reviewer | A narrower specialist context, preferably read-only for review. | Identification reviewer or replication verifier. |
| MCP | A structured tool server that exposes data or operations through a constrained interface. | Bundled FRED MCP for public macro metadata, not private data. |
| Cloud agent | A background coding agent on an issue or branch, separate from the live workshop machine. | Implement a data-map audit branch and open a PR with evidence. |
| Swarm | Several independent cloud-agent tasks coordinated through dependencies. | Data map and source note run in parallel; estimates wait for data checks. |
| Hook | A deterministic reminder or guardrail triggered by an agent event. | Remind after code edits to run tests and keep synthetic-data caveats visible. |
| Loop | A bounded repeat-review-fix cycle with explicit exit rules. | At most three review iterations before merge, stop, or new issue. |
| Goal | A measurable outcome with acceptance criteria and stop conditions. | "Baseline DID summary exists, tests pass, no causal overclaim." |

## Tool Surfaces

| Tool lane | Use for orchestration | Current participant rule |
| --- | --- | --- |
| Codex | Codex cloud tasks, GitHub `@codex`, `@codex review`, local/app goals, `.codex/agents/` reviewers. | Put branch, allowed files, forbidden files, evidence, and reviewer in the issue. |
| Claude Code | Project subagents in `.claude/agents/`, `/agents`, hooks/settings, and checkpointed goals. | Keep project subagents versioned and make reviewer prompts read-only by default. |
| Cursor | Cloud Agent where available, background subagents, `.cursor/agents/`, rules, hooks, and MCP config. | Treat cloud/background agents as branch workers; keep team/cloud MCP configuration separate from local secrets. |

Official docs for these claims were checked on 2026-06-24. See
`../docs/sources.md` for the exact links and version caveats.

## Safety Defaults

- Use public or synthetic data only unless the issue explicitly authorizes
  access to another source.
- Do not put `.env`, API keys, private data, confidential manuscripts, or raw
  external data into cloud-agent context.
- Every task must list allowed files and forbidden files.
- Every PR must include command output, generated artifacts, or a reviewer note.
- Reviewers are read-only unless a human creates a separate fix issue.
- If a task discovers out-of-scope work, open a new issue instead of expanding
  the active branch.

## Files In This Folder

| File | Purpose |
| --- | --- |
| `cloud_agent_issue_template.md` | Copy-ready issue body for cloud agents. |
| `reviewer_issue_template.md` | Copy-ready read-only review prompt. |
| `card_krueger_swarm.md` | Dependency and merge plan for a Card-Krueger swarm. |
| `verification_loop.md` | Green/yellow/red loop rules and evidence table. |
| `goals/ck-data-map-audit.md` | Goal prompt for data-source documentation. |
| `goals/ck-baseline-estimate-review.md` | Goal prompt for analysis and test evidence. |
| `goals/ck-replication-signoff.md` | Goal prompt for final replication review. |

## Done Standard

An orchestrated task is complete only when the PR shows:

- issue link, branch name, and changed files;
- acceptance criteria checked against real files;
- verification command or reason it could not run;
- reviewer verdict with blockers first;
- remaining risks and any follow-up issue.
