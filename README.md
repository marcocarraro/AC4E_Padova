# Agentic Coding for Economists: LSE PhD Short Course

Four-hour hands-on version for LSE PhD students in Economics.

This repository adapts the full [Agentic Coding for Economists](https://github.com/antoniomele/AgenticCodingForEconomists)
course into one compressed workshop. The emphasis is a **research-article harness**:
participants copy a mini repo, install reusable skills and review agents, run a
bounded empirics or writing pipeline, verify with replication and referee checks,
and leave with a checklist they can apply to a dissertation or job market paper.

## Course Snapshot

- Format: 4 hours, in person
- Audience: LSE PhD students in Economics
- Style: short demos followed by guided exercises
- Primary platforms: Codex, Claude Code, Cursor, GitHub, Playwright
- Output: a forkable [`examples/starter_article/`](examples/starter_article/) harness
  plus lane-specific installs in five tool tracks

## Start Here

**Workshop website:** run `npm run docs:dev` and open the local URL. Deploy via [Vercel](website/README.md) with root directory `website/`.

1. Complete the [setup guide](SETUP.md) before the workshop.
2. Read the [syllabus](SYLLABUS.md) for outcomes and timing.
3. Read the [research article harness](docs/research_article_harness.md) checklist.
4. Use the [instructor runbook](INSTRUCTOR_RUNBOOK.md) to deliver the session.
5. Build projector slides from [`slides/workshop/workshop_slides.tex`](slides/workshop/workshop_slides.tex) (see [`slides/README.md`](slides/README.md); `npm run slides:build`).
6. Pick a lane in the [five-track plan](materials/tool_tracks.md) (Codex CLI/app,
   Claude CLI/app, or Cursor).
7. Work through the modules in order:

| Module | Topic | Time |
| --- | --- | ---: |
| 1 | [Scaffold the article repo](materials/module_01_foundations.md) | 50 min |
| 2 | [Harness stack: skills, subagents, hooks, goals](materials/module_02_hooks_goals.md) | 55 min |
| 3 | [Research pipeline sprint](materials/module_03_referee_review.md) | 55 min |
| 4 | [Quality, replication, and data acquisition](materials/module_04_playwright.md) | 55 min |
| 5 | [Harness sign-off and adoption plan](materials/module_05_capstone.md) | 25 min |

The timing includes a 10 minute break after Module 2.

## What Changed From The Full Course

The full course covers multi-day SDD, GitHub swarms, cloud agents, and a large
capstone. This short version compresses the article lifecycle into one path:

1. Copy `starter_article` and set `AGENTS.md`, brief, and privacy boundaries.
2. Install skills, subagents, hooks, and optional MCP from your tool lane.
3. Update the research design memo and one code or LaTeX artifact.
4. Run referee + replication checks and one Playwright data-acquisition demo.
5. Sign off with the [harness checklist](docs/research_article_harness.md).

## Five Workshop Lanes

Same harness artifacts, different control surface ([`materials/tool_tracks.md`](materials/tool_tracks.md)):

| Lane | Surface |
| --- | --- |
| A1 | Codex CLI |
| A2 | Codex desktop app |
| B1 | Claude Code CLI |
| B2 | Claude Code desktop app |
| C | Cursor IDE |

Merge lane files from `examples/{codex,codex-app,claude,claude-app,cursor}/` into your
`starter_article` copy. Playwright always runs from a terminal.

## Repository Structure

```text
.
+-- README.md
+-- SETUP.md
+-- SYLLABUS.md
+-- INSTRUCTOR_RUNBOOK.md
+-- docs/
|   +-- research_article_harness.md
|   +-- inspiration_notes.md
|   +-- sources.md
+-- materials/
+-- templates/
+-- examples/
|   +-- starter_article/     # shared mini repo (all lanes)
|   +-- codex/ codex-app/ claude/ claude-app/ cursor/
|   +-- hooks/ paper/ playwright/ web-form/
+-- slides/                  # Beamer deck for in-room delivery
+-- website/                 # VitePress + five track tabs
+-- scripts/
```

## Ethical Boundary

Use AI referee tools on your own work, public papers, or material where you have
permission. Do not upload a confidential manuscript that you are reviewing for a
journal, conference, or editor unless the venue explicitly permits it and the
relevant confidentiality obligations are satisfied.
