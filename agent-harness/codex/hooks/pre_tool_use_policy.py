#!/usr/bin/env python3
"""Warn before risky shell commands in an economics research project."""

from __future__ import annotations

import json
import re
import sys


def _command_from_payload(payload: dict) -> str:
    tool_input = payload.get("tool_input") or {}
    return str(tool_input.get("command") or tool_input.get("cmd") or "")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    command = _command_from_payload(payload)
    warnings = [
        (r"\brm\s+-rf\b", "Recursive force deletion is out of scope for the workshop."),
        (r"\b(cat|sed|less|head|tail)\b\s+.*\.env\b", "Do not print .env files or secrets."),
        (
            r"\b(open|cat|sed|less|head|tail|python3?)\b.*data/(raw|private)",
            "Raw or private data require explicit human approval before inspection.",
        ),
        (
            r">\s*examples/card-krueger/data/synthetic_fast_food_panel\.csv\b",
            "The Card-Krueger teaching CSV should not be overwritten by harness tasks.",
        ),
    ]

    for pattern, reason in warnings:
        if re.search(pattern, command):
            print(json.dumps({"systemMessage": f"Research safety policy warning: {reason}"}))
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
