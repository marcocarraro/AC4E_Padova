#!/usr/bin/env python3
"""Post-tool-use reminder to run verification (Cursor hook demo)."""

from __future__ import annotations

import json
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    tool = payload.get("tool_name") or payload.get("tool") or ""
    if tool in {"edit", "write", "search_replace"}:
        print(
            "Hook reminder: after edits to src/ or paper/, run "
            "python src/estimate_did.py or pytest tests/ -q",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
