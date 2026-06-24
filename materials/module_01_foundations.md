# Module 1: Scaffold The Article Repo

Time: 50 minutes

## Purpose

Copy the workshop mini repo, set project context, privacy boundaries, and a
small issue list. Every later module edits the **same** `starter_article` tree.

Pick one lane in [`tool_tracks.md`](tool_tracks.md) (Codex CLI/app, Claude CLI/app, Cursor).

## Concepts

| Concept | Definition | Economics example |
| --- | --- | --- |
| Agent loop | Read context, plan, act, verify | DiD pipeline + table check |
| Harness | Skills + subagents + hooks + gates | See [`docs/research_article_harness.md`](../docs/research_article_harness.md) |
| Artifact | Reviewable file | Design memo, `tables/main_did.tex` |
| Guardrail | Persistent rule | Never edit `data/raw/` |

## Exercise 1: Copy `starter_article`

```bash
cp -r examples/starter_article ~/my-article-workshop
cd ~/my-article-workshop
```

Open that folder in your agent tool (not only the course repo).

1. Edit `docs/project_brief.md` for your research question (or keep the demo).
2. Personalize `AGENTS.md` from [`templates/AGENTS_economics.md`](../templates/AGENTS_economics.md).
3. Add `.cursorignore` or equivalent exclusions for confidential paths.

## Exercise 2: Issue list

Create three tasks (GitHub issues or `notes/orchestration_log.md`):

- `rig/memo` — design memo
- `rig/estimation` — run `src/estimate_did.py`
- `rig/referee-pass` — pre-submission review

Prompt:

```text
Read docs/project_brief.md and AGENTS.md. Turn the three rig/* tasks into
agent-friendly issues with allowed files and verification commands.
```

## Demo prompt

```text
Read examples/starter_article/README.md and docs/research_article_harness.md.
What should I complete in Module 1 before installing skills in Module 2?
```

## Tool Notes

### Codex CLI

- `cd` to your `starter_article` copy; run `codex`.
- `/init` if you need a fresh `AGENTS.md` scaffold.

### Codex app

- Open the **project folder** = your copy (not the course repo only).
- Same `AGENTS.md` and `.codex/` merge steps as CLI.

### Claude Code CLI

- `CLAUDE.md` optional; keep `AGENTS.md` for collaborators.
- Project memory should point at your article copy.

### Claude Code app

- Code tab → set folder to your `starter_article` copy.

### Cursor

- Copy `examples/cursor/.cursor` into your project per [`examples/cursor/README.md`](../examples/cursor/README.md).
- Rules: `.cursor/rules/economics-research.mdc`.

## Debrief

1. Which file should agents read first?
2. Which folder is never edited without permission?
3. What command proves estimation output is real?
