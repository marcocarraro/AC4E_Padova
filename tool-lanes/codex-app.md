# Lane A2: Codex App

Use this lane if you prefer the Codex desktop app for project threads, visual
review, and long-running work. The project files are the same as the CLI lane.

Official docs checked on 2026-06-24:

- Codex app: <https://developers.openai.com/codex/app/>
- App commands: <https://developers.openai.com/codex/app/commands/>
- AGENTS.md: <https://developers.openai.com/codex/guides/agents-md/>
- Hooks: <https://developers.openai.com/codex/hooks/>
- Skills: <https://developers.openai.com/codex/skills/>
- Subagents: <https://developers.openai.com/codex/subagents/>
- MCP: <https://developers.openai.com/codex/mcp/>
- Codex cloud: <https://developers.openai.com/codex/cloud/>
- GitHub integration: <https://developers.openai.com/codex/integrations/github/>

## Setup

1. Open the Codex desktop app.
2. Add this repository or your `starter_article` copy as a project.
3. Start a thread in the repository root.
4. Ask for a read-only summary before allowing edits.

```text
Read README.md, START_HERE.md, GUIDE.md, and examples/card-krueger/README.md.
Do not edit files. Tell me which lane files I should copy for Codex app.
```

## Harness Map

| Need | Path or action |
| --- | --- |
| Context file | `AGENTS.md`, `templates/AGENTS_economics.md`, `examples/codex/AGENTS.md` |
| Skills | `examples/codex/.agents/skills/` copied to `.agents/skills/` |
| Subagents/reviewers | `examples/codex/.codex/agents/` copied to `.codex/agents/` |
| Hooks | `examples/codex/.codex/hooks.json` and `examples/codex/.codex/hooks/`; review and trust with `/hooks` in the app |
| MCP | `examples/codex/.codex/config.toml.example`; secrets stay outside git |
| Loop/goal | app goal controls or `/goal` where available; otherwise checkpoint prompts |
| Cloud/GitHub | Codex cloud tasks and GitHub review when account quota permits |
| Review | `/diff`, `/review`, PR evidence, generated outputs |

## Merge Steps

Use the same files as Lane A1:

```bash
cp -r examples/starter_article /path/to/my-article
mkdir -p /path/to/my-article/.agents /path/to/my-article/.codex
cp -r examples/codex/.agents/skills /path/to/my-article/.agents/
cp -r examples/codex/.codex/agents /path/to/my-article/.codex/
cp examples/codex/.codex/hooks.json /path/to/my-article/.codex/
cp -r examples/codex/.codex/hooks /path/to/my-article/.codex/
cp examples/codex/.codex/config.toml.example /path/to/my-article/.codex/
cp examples/codex/AGENTS.md /path/to/my-article/AGENTS.md
```

## Card-Krueger Prompt

```text
In this Codex app thread, use examples/card-krueger as the shared teaching case.
Do not edit data. Draft a short issue for adding one robustness note to the
research design memo. Include allowed files, acceptance criteria, and
verification evidence. Do not implement.
```

## Reviewer Prompt

```text
Use the review command or reviewer mode on the current diff. Check whether the
Card-Krueger synthetic-data caveat remains visible, tests are mentioned, and no
causal claim is made from the toy estimate. Return blockers first and do not
edit files.
```

## Notes

- App labels and command availability can differ by release; verify in the app
  command menu and official docs.
- App threads are the safest resume path for app work. Use CLI resume only when
  you intentionally started or handed off a CLI session.
