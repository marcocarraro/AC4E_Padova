# Codex, Claude Code, And Cursor Track Plan

This workshop works for participants using Codex, Claude Code, or Cursor. The
research workflow is shared; the control surface differs.

Pick **one tool** and **one surface** (CLI or desktop app where available):

| Lane | Tool | Surface | Best for |
| --- | --- | --- | --- |
| A1 | Codex | CLI | Terminal-first, `codex resume`, instructor demos |
| A2 | Codex | Desktop app | macOS/Windows; same project files, UI threads |
| B1 | Claude Code | CLI | `claude --continue`, `/agents`, terminal hooks |
| B2 | Claude Code | Desktop app | Code tab, parallel sessions, slash menu |
| C | Cursor | IDE | Background agents, rules, review pane |

On **Linux**, Codex and Claude Code desktop apps are not available. Use **A1**
or **B1** instead.

## Teaching Strategy

Teach the concept once, then show the tool-specific implementation:

1. Project context.
2. Reusable workflow.
3. Deterministic guardrail.
4. Long-running work.
5. Review and verification.
6. Browser automation.

Participants choose one lane and complete the same artifacts.

## Feature Map

| Workflow need | Codex (CLI / app) | Claude Code (CLI / app) | Cursor |
| --- | --- | --- | --- |
| Project instructions | `AGENTS.md`, global `~/.codex/AGENTS.md` | `CLAUDE.md`, memory, project files | `AGENTS.md`, `.cursor/rules/*.mdc` |
| Reusable procedure | `.codex/skills/*/SKILL.md` | `.claude/skills/*/SKILL.md` | `.cursor/skills/*/SKILL.md` |
| Research spec (SDD-lite) | `spec/intent.md` + research-sdd skill | same | same |
| Subagents | Subagents in goals | `.claude/agents/*.md` | `.cursor/agents/*.md` |
| MCP (optional) | — | — | `.cursor/mcp.json` |
| Hook or lifecycle script | `.codex/hooks.json`; trust via `/hooks` in CLI or app | `.claude/settings.json`; trust via `/hooks` or settings UI | Hooks where supported; else rules + review |
| Long-running local task | `/goal` or goal UI (app); CLI: `codex resume --last` | Checkpoints; CLI: `claude --continue`; app: same session, no CLI resume | Background agents, Agent checkpoints |
| Parallel work | Subagents, side threads | `/agents`, `.claude/agents/*.md`; app: parallel sessions | Built-in and custom subagents |
| GitHub/cloud handoff | Codex review and cloud workflows | GitHub/CLI workflow by prompt | Background agents create branches/PRs |
| Browser automation | Playwright from terminal (all surfaces) | Playwright from terminal | Playwright, optional browser MCP |
| Review output | `/review`, `/diff`, tests | Hooks, subagents, diff | Review pane, PR review |

**Surface notes:** Codex CLI and app share the same `.codex/` layout. Claude CLI
and app share `.claude/` but **separate session history**—desktop threads do not
resume with `claude --continue`. Playwright exercises always use a terminal
(integrated or external), regardless of lane.

## Common Artifacts

Every participant copies [`examples/starter_article/`](../examples/starter_article/) and merges their lane harness. They should leave with:

- Personalized `docs/project_brief.md` and `AGENTS.md` (or `CLAUDE.md`).
- Four skills: `referee-checklist`, `replication-checker`, `research-sdd`, `paper-polisher`.
- Two subagent roles where supported: `identification-reviewer`, `verifier`.
- One installed hook (or hook plan on Cursor if unsupported).
- Updated `docs/research_design_memo.md` and one `src/` or `paper/` change.
- Referee report + replication-checker output.
- Playwright evidence row in `docs/data_source_map.md`.
- Completed rows in [`docs/research_article_harness.md`](../docs/research_article_harness.md).

## Track A1: Codex CLI

Use this lane for terminal-first workflows, Linux, or the most direct `/goal` and
hook install path.

Entry: `examples/codex/` (see `examples/codex/README.md`)

### Setup

```bash
codex --version
codex
```

Optional config:

```toml
# ~/.codex/config.toml
[features]
goals = true
hooks = true
```

### Project Context

1. Put `templates/AGENTS_economics.md` at `AGENTS.md`.
2. Run `/init` if you want Codex to scaffold instead.
3. Ask Codex to summarize active instructions.

### Skill

Save:

```text
.codex/skills/referee-checklist/SKILL.md
```

Invoke:

```text
Use the referee-checklist skill on examples/paper/working_paper_excerpt.md.
```

### Hook

Use `examples/hooks/.codex/hooks.json` in a disposable test repo. Copy the hook
pack, then inspect and trust in the terminal:

```text
/hooks
```

### Long-Running Work

Use:

```text
/goal
```

Paste an adapted version of `templates/long_running_goal_prompt.md`. Resume
later with:

```bash
codex resume --last
```

### Review

Use:

```text
/diff
/review
/status
```

## Track A2: Codex app

Use this lane on **macOS or Windows** if you prefer the Codex desktop app. Project
files are the same as Track A1.

Entry: `examples/codex-app/` (see `examples/codex-app/README.md`)

### Setup

1. Install the Codex desktop app (see `SETUP.md` and `docs/sources.md`).
2. Sign in with the same account as the CLI if you use both.
3. Open this repository as a Codex **project**.
4. Start a **thread** and confirm the working folder is the repo root.

Enable goals and hooks if your build prompts for feature flags (same
`~/.codex/config.toml` as CLI).

### Project Context

1. Put `templates/AGENTS_economics.md` at `AGENTS.md` (or use `/init` in the
   thread).
2. Ask Codex to summarize active instructions before editing.

### Skill

Copy from `examples/codex/` to `.codex/skills/referee-checklist/SKILL.md`. Invoke
via the slash menu or by name in the prompt:

```text
Use the referee-checklist skill on examples/paper/working_paper_excerpt.md.
```

### Hook

Copy `examples/hooks/.codex/` into a disposable test project. In the app, open
`/hooks` from the prompt box to **review and trust** hooks before they run on
real work.

### Long-Running Work

Use `/goal` in the thread or the goal controls in the app UI when available.
Paste `templates/long_running_goal_prompt.md`. During the run, use `/status`,
`/diff`, and `/ps` as needed.

If `/goal` is unavailable, paste the goal as a normal prompt with checkpoints
(see `templates/long_running_goal_prompt.md` surface notes). Resume in the same
thread or use CLI `codex resume --last` if you also use the terminal.

### Review

Use `/diff` and `/review` in the thread before accepting edits.

## Track B1: Claude Code CLI

Use this lane for terminal-first workflows, Linux, or `claude --continue` resume.

Entry: `examples/claude/` (see `examples/claude/README.md`)

### Setup

```bash
claude --version
claude
```

### Project Context

1. Copy `examples/claude/CLAUDE.md` to the root of your project.
2. Keep `AGENTS.md` too if collaborators use Codex or Cursor.
3. Ask Claude to summarize the project instructions before editing.

### Skill

Save:

```text
.claude/skills/referee-checklist/SKILL.md
```

Invoke by name:

```text
Use the referee-checklist skill to review the sample paper excerpt.
```

### Hook

Start from `examples/claude/.claude/settings.example.json`. Copy to
`.claude/settings.json` in a disposable test project and inspect:

```text
/hooks
```

### Long-Running Work

Use a checkpointed prompt (Claude does not need Codex `/goal`):

```text
Work toward this goal, but stop at each checkpoint and wait for confirmation.
[paste goal template]
```

Resume:

```bash
claude --continue
```

### Subagent

Use:

```text
/agents
```

Or create:

```text
.claude/agents/referee-reviewer.md
```

## Track B2: Claude Code app

Use this lane on **macOS or Windows** for the Claude Code desktop app (Code tab).
Hooks and skills use the same paths as B1.

Entry: `examples/claude-app/` (see `examples/claude-app/README.md`)

### Setup

1. Install Claude Code desktop (see `SETUP.md`).
2. Open the **Code** tab.
3. Set the **project folder** to this repository.
4. Start a **session** (sidebar). Each session has its own history and worktree
   when using Git.

### Project Context

1. Copy `examples/claude/CLAUDE.md` to the project root.
2. Ask Claude to summarize instructions before editing.

### Skill

Save to `.claude/skills/referee-checklist/SKILL.md`. Invoke from the **slash
commands** menu (`/` or **+** button) or by name in the prompt.

### Hook

Copy `examples/claude/.claude/settings.example.json` to `.claude/settings.json`
in a disposable project. Review hooks via `/hooks` or project settings. Plugins
can bundle hooks—install only from trusted sources.

### Long-Running Work

Use **checkpoints in the same session**—do not rely on `claude --continue` from
the CLI; desktop sessions are separate from CLI history.

```text
Work toward the following goal, but stop after each checkpoint and wait for my
confirmation before continuing.

[paste templates/long_running_goal_prompt.md]
```

Use **+ New session** for parallel tasks; each Git repo session can use an
isolated worktree.

### Subagent

Use `/agents` or the slash menu to run `referee-reviewer` from
`.claude/agents/referee-reviewer.md`.

## Track C: Cursor

Use this lane for an IDE-first workflow and background agents.

Entry: `examples/cursor/` (see `examples/cursor/README.md`)

### Setup

1. Install Cursor.
2. Open this repository folder.
3. Use Ask for exploration, Agent for implementation, and Plan or Custom modes
   where available for planning.

### Project Context

Use both simple and structured options:

```text
AGENTS.md
.cursor/rules/economics-research.mdc
```

Cursor project rules are better when you need scoped rules, globs, or reusable
context. `AGENTS.md` is better for simple project onboarding.

### Skill

Save:

```text
.cursor/skills/referee-checklist/SKILL.md
```

Invoke from the slash command menu if available, or explicitly in the prompt:

```text
Use the referee-checklist skill to review the sample paper excerpt.
```

### Hook

Cursor supports hooks in current agent/CLI workflows, but exact UI exposure can
vary by release. In the workshop:

1. Show the concept using the Codex or Claude hook example.
2. For Cursor users, create a hook plan rather than requiring install.
3. If their installed Cursor exposes hook configuration, install the hook in a
   disposable project and verify it before using it on real research.

### Long-Running Work

Use one of:

- Background Agent for isolated branch work.
- Agent with checkpoints in the prompt.
- Cursor CLI resume if installed.

Background-agent prompt:

```text
Create a branch that drafts notes/referee_review.md from the sample paper.
Do not edit source paper files. Open a PR or provide a diff for review. Stop if
the task requires confidential data.
```

### Review

Use Cursor's review pane, Git diff, and PR review. For background agents, review
the branch before merging.

## Instructor Demo Order

1. Show the same `AGENTS.md` concept across tools.
2. Show one skill file and explain path differences.
3. Demo long-running work: **Codex app or CLI `/goal`**, then Claude checkpoint
   (app or CLI), then Cursor background agent or checkpoints.
4. Demo one hook in Codex or Claude (app UI when the room is app-heavy); explain
   Cursor hook/version check.
5. Run the Playwright exercise once from a terminal, independent of tool.
