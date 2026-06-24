"""Command-line entry point for the FRED MCP server."""

from __future__ import annotations

import argparse
import json
import os
import sys

from .server import FredMcpServer, run_stdio


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the Padova FRED MCP server.")
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run an offline in-process smoke check and print JSON.",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Force offline sample responses instead of live FRED API calls.",
    )
    args = parser.parse_args(argv)

    if args.offline:
        os.environ["FRED_MCP_OFFLINE"] = "1"

    server = FredMcpServer()
    if args.self_test:
        result = {
            "tools": [tool["name"] for tool in server.list_tools()],
            "sample": server.call_tool(
                "fred_get_series_info", {"series_id": "UNRATE"}
            ),
        }
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    return run_stdio(server, sys.stdin, sys.stdout)


if __name__ == "__main__":
    raise SystemExit(main())
