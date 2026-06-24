# Instructor Runbook

## Delivery Principles

- Demo for at most 8 minutes before hands-on work.
- Every block produces a file in the participant's `starter_article` copy.
- Economics thread: remote-work DiD demo; identification threats are teachable.
- No confidential manuscripts in AI tools.
- Human owns identification and contribution claims.

## Room Setup

- Projector slides: build [`slides/workshop/workshop_slides.pdf`](slides/workshop/workshop_slides.pdf) (`cd slides/workshop && latexmk -pdf workshop_slides.tex`).
- Backup tab on [`docs/sources.md`](docs/sources.md).
- [`docs/research_article_harness.md`](docs/research_article_harness.md) open.
- [`materials/tool_tracks.md`](materials/tool_tracks.md) for five lanes.
- Venv active; `python scripts/validate_setup.py`.
- Form server: `python3 -m http.server 8000 --directory examples/web-form`.

## Timing

| Time | Action |
| --- | --- |
| 00:00 | Harness spine diagram; five lanes, one mini repo |
| 00:10 | Demo copy `examples/starter_article`; edit brief + AGENTS |
| 00:40 | Three issues / orchestration log |
| 00:50 | Demo five harness installs (skill, subagent, hook) |
| 01:05 | Lane merge paths; CLI/App toggle on site |
| 01:20 | Long-running goal on `rig/estimation` |
| 01:45 | Break |
| 01:55 | Design memo + `python src/estimate_did.py` |
| 02:30 | identification-reviewer optional demo |
| 02:50 | Referee on sample excerpt; replication-checker |
| 03:10 | Playwright + data_source_map row |
| 03:45 | Harness checklist + adoption plan |

## Demo Prompts

### Scaffold

```text
Read examples/starter_article/docs/project_brief.md and AGENTS.md. List Module 1
outputs I must commit before Module 2.
```

### Harness

```text
Run replication-checker on examples/starter_article. Explain one red or yellow
item a student might see.
```

### Pipeline

```text
Update docs/research_design_memo.md identification section for the DiD demo.
Then run src/estimate_did.py and report the Treat x Post coefficient.
```

### Quality

```text
Use referee-checklist on examples/paper/working_paper_excerpt.md. One major issue
must cite parallel trends or pre-trends. Save outputs/referee_report_sample.md.
```

### Playwright

```text
After fill_demo_form.py, what row should I add to docs/data_source_map.md?
```

## Failure Modes

| Problem | Fix |
| --- | --- |
| Student edits course repo only | Require copy to `~/my-article-workshop` |
| DiD script fails | `pip install -r requirements.txt`; check CSV exists |
| Replication checker path | Point to `.cursor/skills/replication-checker/scripts/...` |
| MCP key missing | Optional; skip FRED row |
| Hook untrusted | Codex `/hooks`; Claude settings |
| Generic referee prose | Require evidence + identification section |
