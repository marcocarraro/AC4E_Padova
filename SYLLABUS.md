# Syllabus

## Positioning

This short course teaches economics PhD students how to use agentic coding tools
as disciplined research assistants for a **full research article workflow**—not
isolated prompt tricks. Participants scaffold a mini repo, install a harness
(skills, subagents, hooks), run a pipeline sprint, verify outputs, and sign off
with an adoption plan tied to [`docs/research_article_harness.md`](docs/research_article_harness.md).

## Prerequisites

Participants should bring:

- A laptop with local installation rights, or enough time to use user-space
  installation paths from `SETUP.md`.
- A GitHub account.
- At least one agentic coding tool: Codex, Claude Code, or Cursor.
- Python 3.10 or later.
- Node.js 20 or later if they want the Playwright TypeScript path.

No advanced programming background is assumed. Basic comfort with folders,
files, and a terminal helps.

## Learning Outcomes

By the end, participants can:

1. Explain the agent loop and map it to article phases (scaffold → harness → pipeline → quality).
2. Copy and personalize [`examples/starter_article/`](examples/starter_article/) with `AGENTS.md`, brief, and data boundaries.
3. Install at least three skills and two subagent roles appropriate to their tool lane.
4. Configure a deterministic hook and run one long-running goal with stopping conditions.
5. Produce or update a research design memo with identification and data sections.
6. Run referee-style and replication-checker reviews on non-confidential material.
7. Use Playwright to document one public data-acquisition step for a data source map.
8. Complete the harness checklist and a 7-day adoption plan for one dissertation workflow.

## Four-Hour Schedule

| Time | Block | Activity | Output |
| --- | --- | --- | --- |
| 00:00-00:10 | Kickoff | Article harness overview | Shared vocabulary |
| 00:10-00:50 | Module 1 | Copy `starter_article`, brief, AGENTS, issues | Scaffolded mini repo |
| 00:50-01:45 | Module 2 | Skills, subagents, hooks, goals, optional MCP | Harness stack installed |
| 01:45-01:55 | Break | Reset machines | Working setup |
| 01:55-02:50 | Module 3 | Design memo + one code or LaTeX task | Pipeline artifact |
| 02:50-03:45 | Module 4 | Referee, replication, Playwright data step | Quality + evidence |
| 03:45-04:00 | Module 5 | Harness checklist sign-off | Adoption plan |

## Tool Stance

Five lanes share the same harness artifacts ([`materials/tool_tracks.md`](materials/tool_tracks.md)):

- Codex CLI (A1) and Codex app (A2): `AGENTS.md`, `.codex/skills`, hooks, `/goal`.
- Claude Code CLI (B1) and app (B2): `CLAUDE.md`, `.claude/skills`, subagents, hooks.
- Cursor (C): `AGENTS.md`, `.cursor/skills`, agents, hooks, optional MCP.
- Playwright: terminal-based, all lanes.

## Assessment

There is no formal assessment. A participant has completed the workshop when they
can show the [harness checklist](docs/research_article_harness.md):

- Personalized `starter_article` (or equivalent) with brief and `AGENTS.md`.
- Three+ skills, two subagents, one hook, replication and referee artifacts.
- One Playwright evidence file linked from `docs/data_source_map.md`.
- `outputs/adoption_plan.md` referencing checklist rows.
