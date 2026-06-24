# Example Provenance

Sanitized copies for teaching. No API keys or personal paths.

| Workshop path | Source | Notes |
| --- | --- | --- |
| `examples/card-krueger/` | Adapted from Pavia `examples/card-krueger-toy/` plus verified public Card-Krueger source links | Synthetic teaching data; cleaned for Padova path and tests |
| `starter_article/.cursor/skills/research-sdd/` | `~/.cursor/skills/sdd/` | Trimmed for research `spec/intent.md` |
| `starter_article/.cursor/skills/paper-polisher/` | `~/.cursor/skills/deslop-prose/` | Short prose rules for economics papers |
| `starter_article/.cursor/skills/replication-checker/` | AgenticCodingForEconomists `skills/course/replication-checker/` | Script + criteria |
| `starter_article/.cursor/agents/verifier.md` | `~/.cursor/agents/verifier.md` | Readonly completion check |
| `starter_article/.cursor/agents/identification-reviewer.md` | ACE `subagents/templates/reviewer.md` | Identification focus |
| `starter_article/.cursor/hooks/` | LSE `examples/claude/hooks/` + Cursor hook pattern | Verification reminder |
| `examples/hooks/.codex/` | Course-authored | SessionStart / PreToolUse / PostToolUse |
| `agent-harness/codex/` | Adapted from Pavia harness and checked against official Codex docs on 2026-06-24 | Portable Codex skills, subagents, hooks, MCP config, goals, orchestration |
| `examples/cursor/.cursor/mcp.json.example` | Template only | Replace `YOUR_FRED_API_KEY_HERE` |
| `examples/plugins/README.md` | Cursor marketplace docs | Optional superpowers / doc-sync plugins |

Lane folders (`codex/`, `claude/`, `cursor/`) mirror harness **skills and agents** in native paths; merge into a copy of `starter_article/`.
