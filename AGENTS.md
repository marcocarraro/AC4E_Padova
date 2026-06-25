# Agent Instructions

## Project

This is the participant-facing repository for the Padova 5-hour version of
Agentic Coding for Economists.

The repository started from `AC4E_LSE_PhD_Students` and is being adapted using
`AC4E_Pavia` as the main reference. The workshop sequence, guide, examples,
slides, and harnesses must all point to the Padova session and to the
Card-Krueger running example.

If you are in doubt about the details of the project, refer to @templates/project_brief.md and @templates/research_design_memo.md. 

## Scope Rules

- Keep this repository participant-facing.
- Do not add `followup/`, `follow_up/`, or `website/`.
- Do not add private data, raw confidential data, API keys, secrets, or local
  absolute paths.
- Prefer small issue-scoped branches and pull requests.
- Keep downstream work coordinated through GitHub issues unless a GitHub/cloud
  operation fails; if it fails, do the smallest local fallback and explain it.
- Do not append to `cursor_chat_recording.md` unless the current issue
  explicitly asks for that file.

## Workshop Shape

- Format: 5 hours, in person, University of Padova.
- Audience: economists and economics researchers.
- Running example: Card and Krueger's minimum-wage study.
- Core output: a personalized research-article harness with project brief,
  design memo, skills, subagents, hooks, optional MCP, orchestration log,
  verification evidence, and adoption checklist.

## Important Paths

- `START_HERE.md` - participant navigation.
- `SCHEDULE.md` - 5-hour live sequence.
- `GUIDE.md` - main participant guide.
- `materials/` - timed module notes.
- `slides/workshop/` - projector deck source and PDF.
- `examples/starter_article/` - shared mini research repo.
- `examples/{codex,codex-app,claude,claude-app,cursor}/` - tool-lane harnesses.
- `templates/` - reusable participant templates.
- `docs/import_manifest.md` - LSE source import record.
- `docs/sources.md` - official documentation and provenance links.

## Agent Workflow

1. Read this file, `README.md`, `START_HERE.md`, `SCHEDULE.md`, and the issue.
2. Confirm the issue number, branch name, allowed files, and acceptance criteria.
3. Make the smallest coherent change for that issue.
4. Verify with commands that match the issue. If dependencies or network access
   block verification, report the blocker with the exact command and error.
5. Open a PR with changed files, verification evidence, and remaining risks.

## Research Boundary

The agent can draft, inspect, transform, test, and review bounded artifacts.
The human owns the research question, identification argument, data access
rights, confidentiality decisions, interpretation of results, and final claims.
