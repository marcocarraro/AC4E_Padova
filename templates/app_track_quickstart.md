# App track quickstart (Codex or Claude Code desktop)

One-page checklist for **Track A2** (Codex app) or **Track B2** (Claude Code app).
Artifact paths match the CLI tracks; only setup and resume differ.

## Codex app (A2)

1. Install Codex desktop; sign in.
2. **Open project:** this course repository folder.
3. **New thread**; confirm working directory is the repo root.
4. Copy `examples/codex/AGENTS.md` → root `AGENTS.md`.
5. First prompt: inspect repo; do not edit files.
6. Skills: `.codex/skills/referee-checklist/SKILL.md` (from `examples/codex/`).
7. Hooks: copy `examples/hooks/.codex/`; run `/hooks` to trust in the UI.
8. Outputs: save under `outputs/` (create the folder if needed).

## Claude Code app (B2)

1. Install Claude Code desktop; open **Code** tab.
2. **Project folder:** this course repository.
3. **New session** in the sidebar.
4. Copy `examples/claude/CLAUDE.md` → root `CLAUDE.md`.
5. First prompt: summarize workshop goals; do not edit yet.
6. Skills: `.claude/skills/referee-checklist/SKILL.md`.
7. Hooks: copy `settings.example.json` → `.claude/settings.json`; `/hooks`.
8. Long-running work: use checkpoints **in the same session** (not CLI resume).
9. Outputs: save under `outputs/`.

## Playwright (both app tracks)

Use a system or integrated **terminal** for:

```bash
python3 -m http.server 8000 --directory examples/web-form
npx playwright codegen http://localhost:8000
python examples/playwright/fill_demo_form.py
```

## Linux

Use **Track A1** (Codex CLI) or **Track B1** (Claude CLI) instead; desktop apps
are not available on Linux.
