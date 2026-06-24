# FRED Public-Data MCP Example

This is the shared MCP server example for the Padova workshop. It is intentionally
small, stdlib-only, and scoped to public FRED metadata/data lookup.

Official docs checked on 2026-06-24:

- MCP introduction: <https://modelcontextprotocol.io/docs/getting-started/intro>
- MCP 2025-06-18 specification: <https://modelcontextprotocol.io/specification/2025-06-18>
- MCP stdio transport: <https://modelcontextprotocol.io/specification/2025-06-18/basic/transports>
- FRED API: <https://fred.stlouisfed.org/docs/api/fred/>
- FRED API keys: <https://fred.stlouisfed.org/docs/api/api_key.html>
- FRED series metadata: <https://fred.stlouisfed.org/docs/api/fred/series.html>
- FRED series search: <https://fred.stlouisfed.org/docs/api/fred/series_search.html>
- FRED observations: <https://fred.stlouisfed.org/docs/api/fred/series_observations.html>

## Scope

Included tools:

- `fred_search_series`: search FRED series by text.
- `fred_get_series_info`: fetch public metadata for one series.
- `fred_get_observations`: fetch a capped set of observations for one series.

The server does not accept arbitrary URLs, write files, inspect local data, or
read secrets beyond `FRED_API_KEY`.

## Environment

| Variable | Required | Purpose |
| --- | --- | --- |
| `FRED_API_KEY` | No for offline smoke, yes for live FRED calls | Registered FRED API key |
| `FRED_MCP_OFFLINE` | No | Set to `1` to force bundled sample responses |

FRED documentation says web-service requests require an API key. This teaching
server therefore runs in offline sample mode when `FRED_API_KEY` is absent, so
participants can smoke-test configuration without a real key.

## Smoke Test

From the repository root:

```bash
python3 agent-harness/mcp/fred/scripts/smoke.py --offline
```

Expected output includes:

```text
initialize ok
tools/list ok
tools/call fred_get_series_info ok
offline smoke ok
```

## Live Use

```bash
# Set FRED_API_KEY in your shell before live calls.
PYTHONPATH=agent-harness/mcp/fred/src python3 -m fred_mcp_server
```

The server communicates over MCP stdio. It reads newline-delimited JSON-RPC
messages from stdin and writes only JSON-RPC messages to stdout.

## Tool-Lane Configs

- Codex: `agent-harness/codex/mcp/config.toml.example`
- Claude Code: `agent-harness/claude/mcp/mcp.json.example`
- Cursor: `agent-harness/cursor/mcp/mcp.json.example`

The participant mirrors are in `examples/codex/`, `examples/claude/`,
`examples/cursor/`, and `examples/starter_article/`.

## Research Boundary

Use this MCP server to add public macro context rows to a data source map, for
example `UNRATE` metadata. Do not use it to imply that the synthetic
Card-Krueger teaching panel is real FRED data, and do not make causal claims from
metadata lookup alone.
