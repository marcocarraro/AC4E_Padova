#!/usr/bin/env python3
"""Warn Codex before risky shell commands in an economics project."""

from __future__ import annotations

import json
import re
import sys


def main() -> int:
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input", {})
    command = tool_input.get("command", "")

    forbidden_patterns = [
        (r"\brm\s+-rf\b", "Do not run recursive force deletion during the workshop."),
        (r"\bcat\s+\.env\b", "Do not print .env files or secrets."),
        (r"\b(open|cat|sed|less|head|tail)\b.*data/raw", "Raw data requires explicit human approval."),
    ]

    for pattern, reason in forbidden_patterns:
        if re.search(pattern, command):
            print(json.dumps({
                "systemMessage": f"Research safety policy warning: {reason}"
            }))
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

