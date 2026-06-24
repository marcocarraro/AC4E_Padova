# Codex CLI Track (Lane A1)

Merge harness skills into your [`starter_article/`](../starter_article/) copy.

## Merge steps

```bash
cp -r examples/starter_article /path/to/my-article
mkdir -p /path/to/my-article/.codex/skills
cp -r examples/codex/.codex/skills/* /path/to/my-article/.codex/skills/
cp examples/hooks/.codex/hooks.json /path/to/my-article/.codex/
cp -r examples/hooks/.codex/hooks /path/to/my-article/.codex/
```

Trust hooks: `codex` → `/hooks` in the project root.

## Skills (`.codex/skills/`)

- `referee-checklist`, `replication-checker`, `research-sdd`, `paper-polisher`

## Long-running work

`/goal` or `codex resume --last` with `templates/long_running_goal_prompt.md`.

Codex **app** (A2): same `.codex/` layout; see [`../codex-app/README.md`](../codex-app/README.md).
