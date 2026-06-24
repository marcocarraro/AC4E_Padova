# Research Article Harness

This workshop builds one **agentic harness** for an economics research article: a
forkable project where context, skills, subagents, hooks, and verification gates
work together across the article lifecycle.

Canonical project: [`examples/starter_article/`](../examples/starter_article/).

Pick one tool lane in [`materials/tool_tracks.md`](../materials/tool_tracks.md)
and merge lane-specific harness files from `examples/{codex,codex-app,claude,claude-app,cursor}/`
into your copy of `starter_article`.

## Article lifecycle (workshop spine)

| Phase | Module | Primary artifacts |
| --- | --- | --- |
| Scaffold | 1 | `docs/project_brief.md`, `AGENTS.md`, `.cursorignore`, issue list |
| Harness stack | 2 | Skills, subagents, hooks, optional MCP; long-running goal |
| Pipeline | 3 | `docs/research_design_memo.md`, `src/` or `paper/` update |
| Quality + data | 4 | Referee report, replication check, Playwright evidence |
| Sign-off | 5 | Harness checklist + `outputs/adoption_plan.md` |

## Harness components

| Component | Role | Example paths (Cursor) |
| --- | --- | --- |
| Project context | Always-on instructions | `AGENTS.md`, `.cursor/rules/*.mdc` |
| Research spec | Plan before code | `docs/project_brief.md`, `spec/intent.md` (via research-sdd skill) |
| Skills | Reusable procedures | `.cursor/skills/referee-checklist/`, `replication-checker/`, `paper-polisher/`, `research-sdd/` |
| Subagents | Isolated review (avoid self-bias) | `.cursor/agents/verifier.md`, `identification-reviewer.md` |
| Hooks | Deterministic lifecycle checks | `.cursor/hooks.json` |
| MCP (optional) | External tools (data APIs) | `.cursor/mcp.json` from `mcp.json.example` |
| Orchestration log | Lightweight coordination | `notes/orchestration_log.md` |
| Replication gate | Clean-run evidence | `replication/README.md` + replication-checker skill |

## Workshop completion checklist

Mark each row before you leave. Use your lane’s native paths (`.codex/`, `.claude/`, `.cursor/`).

### Scaffold (Module 1)

- [ ] Copied `examples/starter_article/` to a working folder (or forked on GitHub).
- [ ] Personalized `docs/project_brief.md` for your research question.
- [ ] `AGENTS.md` (or `CLAUDE.md`) lists repo map, verification commands, and “Do not” rules.
- [ ] `.cursorignore` or equivalent excludes raw/confidential data from agent context.
- [ ] At least three GitHub issues (or markdown issue list) for memo, estimation, and review.

### Harness stack (Module 2)

- [ ] Installed **referee-checklist** skill from lane examples.
- [ ] Installed **replication-checker** skill.
- [ ] Installed **research-sdd** or **paper-polisher** skill (at least one writing/spec skill).
- [ ] Configured at least one **hook** (Codex, Claude, or Cursor).
- [ ] Created or invoked one **subagent** (verifier or identification-reviewer).
- [ ] (Cursor lane) Reviewed `mcp.json.example`; optional: one FRED series logged in memo.
- [ ] Ran one **long-running goal** or checkpointed session with explicit stopping conditions.

### Pipeline (Module 3)

- [ ] Updated `docs/research_design_memo.md` (hypotheses, data, identification).
- [ ] One bounded change in `src/` **or** `paper/` with verification (test, script run, or `latexmk`).

### Quality + acquisition (Module 4)

- [ ] Referee-style report on non-confidential text (`templates/referee_report.md`).
- [ ] Replication-checker report (green/yellow/red) for `starter_article`.
- [ ] Playwright script or spec that fills `examples/web-form` and saves evidence for `data_source_map.md`.

### Sign-off (Module 5)

- [ ] `notes/orchestration_log.md` lists what you delegated vs reviewed yourself.
- [ ] `outputs/adoption_plan.md` maps one dissertation workflow to harness rows above.
- [ ] You can explain which tasks agents should **not** own (identification claims, novel contribution).

## Ethics

- Referee skills: own work, public papers, or material you may use with AI tools only.
- Do not upload confidential referee assignments or unreleased third-party manuscripts.
- You remain responsible for citations, identification, and numerical results.

## Follow-on

The full [Agentic Coding for Economists](https://github.com/antoniomele/AgenticCodingForEconomists)
course adds multi-day SDD, GitHub swarms, and cloud agents. This four-hour workshop
delivers the **minimum harness** you can extend on your dissertation repo.
