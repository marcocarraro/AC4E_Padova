"""Minimal MCP JSON-RPC server for bounded FRED public-data tools."""

from __future__ import annotations

import json
import sys
from typing import Any, TextIO

from . import __version__
from .fred_client import FredApiError, FredClient

PROTOCOL_VERSION = "2025-06-18"


class FredMcpServer:
    def __init__(self, client: FredClient | None = None) -> None:
        self.client = client or FredClient.from_env()

    def list_tools(self) -> list[dict[str, Any]]:
        return [
            {
                "name": "fred_search_series",
                "description": (
                    "Search public FRED series metadata by text. Returns a capped "
                    "set of metadata rows; uses bundled samples when offline."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "search_text": {
                            "type": "string",
                            "description": "Search text such as unemployment.",
                        },
                        "limit": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 25,
                            "default": 5,
                        },
                    },
                    "required": ["search_text"],
                },
            },
            {
                "name": "fred_get_series_info",
                "description": (
                    "Fetch public FRED metadata for a single series ID, such as UNRATE."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "series_id": {
                            "type": "string",
                            "description": "FRED series ID such as UNRATE.",
                        }
                    },
                    "required": ["series_id"],
                },
            },
            {
                "name": "fred_get_observations",
                "description": (
                    "Fetch a capped set of public observations for one FRED series."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "series_id": {"type": "string"},
                        "observation_start": {
                            "type": "string",
                            "description": "Optional YYYY-MM-DD start date.",
                        },
                        "observation_end": {
                            "type": "string",
                            "description": "Optional YYYY-MM-DD end date.",
                        },
                        "limit": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 50,
                            "default": 10,
                        },
                    },
                    "required": ["series_id"],
                },
            },
        ]

    def call_tool(self, name: str, arguments: dict[str, Any] | None) -> dict[str, Any]:
        args = arguments or {}
        if name == "fred_search_series":
            return self.client.search_series(
                search_text=str(args.get("search_text", "")),
                limit=int(args.get("limit", 5)),
            )
        if name == "fred_get_series_info":
            return self.client.get_series_info(series_id=str(args.get("series_id", "")))
        if name == "fred_get_observations":
            return self.client.get_observations(
                series_id=str(args.get("series_id", "")),
                observation_start=args.get("observation_start"),
                observation_end=args.get("observation_end"),
                limit=int(args.get("limit", 10)),
            )
        raise ValueError(f"Unknown tool: {name}")

    def handle_request(self, message: dict[str, Any]) -> dict[str, Any] | None:
        method = message.get("method")
        request_id = message.get("id")

        if request_id is None:
            return None

        try:
            if method == "initialize":
                result = {
                    "protocolVersion": PROTOCOL_VERSION,
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {
                        "name": "fred_mcp_server",
                        "version": __version__,
                    },
                }
            elif method == "tools/list":
                result = {"tools": self.list_tools()}
            elif method == "tools/call":
                params = message.get("params") or {}
                data = self.call_tool(
                    name=str(params.get("name", "")),
                    arguments=params.get("arguments") or {},
                )
                result = {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(data, indent=2, sort_keys=True),
                        }
                    ],
                    "isError": False,
                }
            elif method == "shutdown":
                result = None
            else:
                return _error(request_id, -32601, f"Method not found: {method}")
        except (FredApiError, ValueError) as exc:
            return _error(request_id, -32000, str(exc))

        return {"jsonrpc": "2.0", "id": request_id, "result": result}


def run_stdio(server: FredMcpServer, stdin: TextIO, stdout: TextIO) -> int:
    for raw_line in stdin:
        line = raw_line.strip()
        if not line:
            continue
        message: dict[str, Any] | None = None
        try:
            message = json.loads(line)
        except json.JSONDecodeError as exc:
            response = _error(None, -32700, f"Parse error: {exc.msg}")
        else:
            if not isinstance(message, dict):
                response = _error(None, -32600, "Invalid request.")
            else:
                response = server.handle_request(message)

        if response is not None:
            stdout.write(json.dumps(response, separators=(",", ":")) + "\n")
            stdout.flush()

        if isinstance(message, dict) and message.get("method") == "shutdown":
            break

    return 0


def _error(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {"code": code, "message": message},
    }


def log(message: str) -> None:
    print(message, file=sys.stderr)
