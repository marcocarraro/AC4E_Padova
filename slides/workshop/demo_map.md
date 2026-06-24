# Slide-To-Demo Map

This map keeps the deck aligned with the participant repository sequence.

| Deck section | Demo or action | Repository path |
| --- | --- | --- |
| Start | Read-only orientation prompt | `README.md`, `START_HERE.md`, `SCHEDULE.md`, `GUIDE.md` |
| Running case | Inspect runnable Card-Krueger example | `examples/card-krueger/README.md` |
| Running case | Run baseline DiD and tests | `examples/card-krueger/src/did_analysis.py`, `examples/card-krueger/tests/` |
| Harness | Compare instructions, brief, memo, and templates | `examples/starter_article/`, `templates/` |
| Harness | Inspect skills, subagents, hooks, and MCP placeholders | `examples/codex/`, `examples/claude/`, `examples/cursor/`, `agent-harness/{codex,claude,cursor}/` |
| Tool lanes | Choose Codex, Claude Code, or Cursor path | `materials/tool_tracks.md`, `tool-lanes/`, `examples/{codex,codex-app,claude,claude-app,cursor}/` |
| Orchestration | Turn a task into an issue, swarm, loop, and PR evidence plan | `orchestration/README.md`, `orchestration/cloud_agent_issue_template.md`, `orchestration/card_krueger_swarm.md`, `orchestration/verification_loop.md` |
| Sprint | Edit one bounded artifact and record delegation | `notes/orchestration_log_template.md`, `examples/starter_article/notes/orchestration_log.md` |
| Verification | Run tests, reviewer prompt, or Playwright evidence capture; record result | `docs/research_article_harness.md`, `examples/card-krueger/tests/`, `examples/playwright/README.md`, `examples/web-form/` |

## Build Evidence To Record In PRs

- slide count from the generated PDF;
- the list above, updated if demo order changes;
- `latexmk -pdf -interaction=nonstopmode workshop_slides.tex` result or the
  exact build failure;
- whether the PDF was regenerated.
