# Cursor Track (Lane C)

Merge these files into your copy of [`starter_article/`](../starter_article/).

## Merge steps

```bash
cp -r examples/starter_article /path/to/my-article
cp -r examples/cursor/.cursor /path/to/my-article/
cp examples/cursor/AGENTS.md /path/to/my-article/AGENTS.md   # if starting fresh
```

Optional: `cp examples/cursor/.cursor/mcp.json.example /path/to/my-article/.cursor/mcp.json` and add a FRED API key.

## Harness files

| Path | Role |
| --- | --- |
| `.cursor/skills/referee-checklist/` | Pre-submission review |
| `.cursor/skills/replication-checker/` | Clean-run gate |
| `.cursor/skills/research-sdd/` | Plan before empirics/LaTeX edits |
| `.cursor/skills/paper-polisher/` | Prose polish |
| `.cursor/agents/verifier.md` | Skeptical completion check |
| `.cursor/agents/identification-reviewer.md` | DiD/IV/RD critique |
| `.cursor/hooks.json` | Post-edit verification reminder |
| `.cursor/rules/economics-research.mdc` | Scoped rules |

## Exercise

```text
Read examples/starter_article/AGENTS.md and merge examples/cursor/.cursor into my
starter_article copy. List the five harness components I should invoke in Module 2.
```

Playwright: always from a terminal (`examples/playwright/`).
