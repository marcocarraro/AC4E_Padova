#!/usr/bin/env python3
"""Offline smoke test for the FRED MCP stdio server."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run FRED MCP offline smoke test.")
    parser.add_argument("--offline", action="store_true", help="Force offline samples.")
    args = parser.parse_args(argv)

    env = os.environ.copy()
    env["PYTHONPATH"] = str(SRC)
    if args.offline:
        env["FRED_MCP_OFFLINE"] = "1"
        env.pop("FRED_API_KEY", None)

    proc = subprocess.Popen(
        [sys.executable, "-m", "fred_mcp_server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env,
    )
    assert proc.stdin is not None
    assert proc.stdout is not None

    try:
        initialize = request(proc, 1, "initialize", {"protocolVersion": "2025-06-18"})
        assert "result" in initialize, initialize
        print("initialize ok")

        tools = request(proc, 2, "tools/list", {})
        tool_names = {tool["name"] for tool in tools["result"]["tools"]}
        expected = {
            "fred_search_series",
            "fred_get_series_info",
            "fred_get_observations",
        }
        assert expected <= tool_names, tool_names
        print("tools/list ok")

        info = request(
            proc,
            3,
            "tools/call",
            {
                "name": "fred_get_series_info",
                "arguments": {"series_id": "UNRATE"},
            },
        )
        text = info["result"]["content"][0]["text"]
        assert "UNRATE" in text, text
        assert "FRED_API_KEY" not in text, text
        print("tools/call fred_get_series_info ok")

        shutdown = request(proc, 4, "shutdown", {})
        assert "result" in shutdown, shutdown
    finally:
        proc.stdin.close()
        stderr = proc.stderr.read() if proc.stderr else ""
        return_code = proc.wait(timeout=5)

    assert return_code == 0, stderr
    print("offline smoke ok")
    return 0


def request(
    proc: subprocess.Popen[str], request_id: int, method: str, params: dict[str, Any]
) -> dict[str, Any]:
    assert proc.stdin is not None
    assert proc.stdout is not None
    proc.stdin.write(
        json.dumps(
            {"jsonrpc": "2.0", "id": request_id, "method": method, "params": params},
            separators=(",", ":"),
        )
        + "\n"
    )
    proc.stdin.flush()
    line = proc.stdout.readline()
    if not line:
        raise RuntimeError("server closed stdout")
    return json.loads(line)


if __name__ == "__main__":
    raise SystemExit(main())
