# Setup Guide

Complete this before the workshop. Allow 45-75 minutes if you are installing
from scratch.

This guide is dedicated to this LSE short-course repository. It gives you the
minimum setup needed for the hands-on exercises, plus optional paths for the
tools you may already use.

## Quick Checklist

- [ ] Git installed and configured.
- [ ] GitHub account available.
- [ ] Python 3.10 or later installed.
- [ ] Node.js 20 or later installed.
- [ ] One primary agentic coding tool chosen: Codex, Claude Code, or Cursor.
- [ ] For that tool, both the CLI and desktop/editor app are installed where
      available.
- [ ] Playwright installed with a browser.
- [ ] This repository opens locally.
- [ ] `python3 scripts/validate_setup.py` runs.

## 1. Get This Repository

If the repository already exists on your machine, open it in your agentic coding
tool. Otherwise clone it from GitHub once the instructor has shared the URL:

```bash
git clone <course-repository-url>
cd AC4E_LSE_PhD_Students
```

If you received the folder directly, open a terminal in that folder and run:

```bash
pwd
ls
```

You should see `README.md`, `SETUP.md`, `materials/`, `templates/`, and
`examples/`.

## 2. Git And GitHub

Check Git:

```bash
git --version
```

Set your identity if needed:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.name@lse.ac.uk"
```

Create or verify your GitHub account at <https://github.com>. SSH keys are
recommended, but HTTPS is acceptable for the workshop.

## 3. Python Environment

Check Python:

```bash
python3 --version
```

Create a virtual environment in the course folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## 4. Node.js And Playwright CLI

The Python Playwright package is enough for the Python exercise. Node.js is
useful for Playwright codegen and the TypeScript test path.

Check Node:

```bash
node --version
npm --version
```

Install project dependencies:

```bash
npm install
npx playwright install chromium
```

Run Playwright codegen against the local exercise page after starting the server:

```bash
python3 -m http.server 8000 --directory examples/web-form
npx playwright codegen http://localhost:8000
```

Stop the server with `Ctrl+C` when finished.

## 5. Install An Agentic Coding Tool

Choose one **tool family** and one **surface** (see `materials/tool_tracks.md`):

| Lane | When to use |
| --- | --- |
| **Codex app** (A2) | macOS/Windows; desktop UI, same `/goal` and hooks as CLI |
| **Codex CLI** (A1) | Linux, terminal-first, `codex resume` |
| **Claude app** (B2) | macOS/Windows; Code tab, slash menu, parallel sessions |
| **Claude CLI** (B1) | Linux, `claude --continue`, terminal hooks |
| **Cursor** (C) | IDE-first; background agents |

You do not need all three tools. Pick the surface you will use for **most**
module exercises.

**Recommended on macOS/Windows:** install the **desktop app** for Codex or Claude
Code and follow **Track A2** or **B2** in the materials. Also install the **CLI**
if you want Playwright codegen, `validate_setup.py` to detect the binary, or
Linux-style resume commands as a backup.

**Linux:** use **Codex CLI** or **Claude CLI** only; desktop apps are not
available.

If you are unsure:

- **Codex app or CLI** — closest to instructor `/goal` demos; shared `.codex/`
  files.
- **Claude app or CLI** — skills, hooks, `/agents`; app uses checkpoints in one
  session (CLI resume does not apply to desktop threads).
- **Cursor** — editor-native review and background agents.

### Option A: Codex (CLI and/or desktop app)

Official docs:

- Codex overview: <https://developers.openai.com/codex/>
- Codex CLI: <https://developers.openai.com/codex/cli>
- Codex desktop app guide:
  <https://openai.com/academy/codex-how-to-start/>

**App track (A2):** follow `examples/codex-app/README.md` and
`templates/app_track_quickstart.md` after installing the desktop app.

**CLI track (A1):** install the CLI:

```bash
npm i -g @openai/codex
codex --version
```

If you already have it, upgrade before the workshop:

```bash
npm i -g @openai/codex@latest
codex --version
```

Start the CLI from this repository:

```bash
cd AC4E_LSE_PhD_Students
codex
```

Install the desktop app next:

1. Open the Codex desktop app guide above.
2. Download the official Codex desktop app for your platform if available.
3. Sign in with the same ChatGPT account you use for the CLI.
4. Open this repository as a Codex project.
5. Create one test thread and ask:

```text
Inspect this folder and tell me what course materials you see. Do not edit files.
```

Codex desktop is available on macOS and Windows. If you are on Linux, use the CLI
for the hands-on exercises and the instructor demo for the desktop-specific
parts.

If you want the `/goal` and hooks exercises, enable the features if your Codex
version asks for feature flags:

```toml
# ~/.codex/config.toml
[features]
goals = true
hooks = true
```

Then start Codex:

```bash
codex
```

Inside Codex, useful slash commands for this course are:

```text
/init
/status
/diff
/hooks
/goal
/review
```

### Option B: Claude Code

Official docs:

- Claude Code setup:
  <https://docs.anthropic.com/en/docs/claude-code/setup>
- Claude Code first-day guide:
  <https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code>
- Claude Code desktop app:
  <https://code.claude.com/docs/en/desktop-quickstart>

Install the CLI first. On macOS, Linux, or WSL:

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```

On Windows PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
claude --version
```

Alternative install paths from the official guide include Homebrew and npm:

```bash
brew install --cask claude-code
npm install -g @anthropic-ai/claude-code
```

Do not use `sudo` with the npm install path.

Start the CLI from this repository and sign in:

```bash
cd AC4E_LSE_PhD_Students
claude
```

Run `/login` if Claude Code asks you to authenticate, then run `/init` if you
want Claude to generate or refresh a project `CLAUDE.md`.

Install the desktop app next:

1. Open the Claude Code desktop app guide above.
2. Download the desktop app for macOS or Windows.
3. Sign in with your Anthropic account.
4. Open the `Code` tab.
5. Select `Local` and choose this repository folder.
6. Start in the default permission mode so you can review proposed changes.

Claude Code desktop is available for macOS and Windows. The desktop app is not
available on Linux; Linux users should use the CLI for the exercises.

Claude Code supports project instructions, skills, subagents, and hooks. The
workshop includes Claude-specific examples in `examples/claude/`.

Useful Claude Code commands and interfaces for this course:

```text
/agents
/hooks
```

Useful terminal flags:

```bash
claude --continue
claude --resume
```

### Option C: Cursor

Official docs:

- Cursor desktop/editor install:
  <https://docs.cursor.com/en/get-started/installation>
- Cursor CLI install:
  <https://docs.cursor.com/en/cli/installation>
- Cursor shell command:
  <https://docs.cursor.com/tools/cli>

Install the desktop/editor app first:

1. Go to <https://cursor.com>.
2. Click `Download`.
3. Run the installer.
4. Open Cursor and sign in so the AI features are available.
5. Open this repository folder.
6. Wait for codebase indexing to complete.

Install the editor shell command from inside Cursor:

1. Open the Command Palette with `Cmd+Shift+P` on macOS or `Ctrl+Shift+P` on
   Windows/Linux.
2. Run `Shell Command: Install 'cursor' command in PATH`.
3. Optionally run `Shell Command: Install 'code' command in PATH`.
4. Verify from a new terminal:

```bash
cursor --version
cursor .
```

Install Cursor Agent CLI if you want a terminal-native agent:

```bash
curl https://cursor.com/install -fsS | bash
cursor-agent --version
cursor-agent
```

If `cursor-agent` is not found after installation, add `~/.local/bin` to your
PATH. For zsh:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

For bash:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Cursor is the best path if you want an IDE-first workshop experience. Open this
repository folder and use Agent, Ask, or Plan mode.

Cursor examples are in `examples/cursor/`. The course uses:

- `AGENTS.md` for simple project-level instructions.
- `.cursor/rules/*.mdc` for scoped reusable rules.
- `.cursor/skills/*/SKILL.md` for procedural skills.
- Cursor subagents and background agents for parallel or longer work.
- Cursor hooks where supported by the installed editor or CLI version.

## 6. Verify Setup

Run:

```bash
python3 scripts/validate_setup.py
```

Expected output:

```text
OK: python ...
OK: git ...
OK: node ...
OK: npm ...
OK: playwright-python ...
INFO: codex ...
INFO: claude ...
INFO: cursor ...
INFO: cursor-agent ...
```

It is fine if the optional tools you did not choose are missing. For example, a
Cursor student does not need `codex` or `claude`, and a Codex student does not
need `cursor-agent`. The important thing is that your chosen tool has both its
desktop/editor app and CLI path working before the workshop.

If both Python Playwright and Node Playwright are missing, complete sections 3
and 4 before the workshop.

## 7. Data And Privacy Setup

Create a data folder that will not be committed:

```bash
mkdir -p data/raw data/processed outputs
```

The `.gitignore` in this repository excludes `data/`, `.env`, virtual
environments, logs, and generated screenshots. Do not place API keys or private
data in prompts, screenshots, or files committed to GitHub.

## 8. Fallback If Something Breaks

If local setup fails:

1. Use the instructor's projected demo for Codex/Cursor/Claude.
2. Complete the Markdown exercises in `templates/`.
3. For Playwright, read `materials/module_04_playwright.md` and annotate the
   generated script in `examples/playwright/fill_demo_form.py`.
4. After the workshop, rerun `scripts/validate_setup.py` and send the exact
   failing line to the instructor.
