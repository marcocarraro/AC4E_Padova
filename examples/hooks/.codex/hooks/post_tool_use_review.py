#!/usr/bin/env python3
"""Remind the agent to summarize verification evidence after key commands."""

from __future__ import annotations

import json
import re
import sys


def main() -> int:
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input", {})
    command = tool_input.get("command", "")

    verification_commands = [
        r"\bpytest\b",
        r"\bplaywright\b",
        r"\bnpm\s+test\b",
        r"\blatexmk\b",
        r"\bpython\b.*src/",
    ]

    if any(re.search(pattern, command) for pattern in verification_commands):
        print(json.dumps({
            "systemMessage": (
                "Verification command detected. In the final response, report "
                "the command, result, generated files, and any remaining risk."
            )
        }))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

