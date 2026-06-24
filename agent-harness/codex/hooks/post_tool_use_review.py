#!/usr/bin/env python3
"""Remind Codex to report verification evidence after relevant commands or edits."""

from __future__ import annotations

import json
import re
import sys


def _payload_text(payload: dict) -> str:
    tool_input = payload.get("tool_input") or {}
    parts = [
        str(tool_input.get("command") or ""),
        str(tool_input.get("cmd") or ""),
        str(tool_input.get("path") or ""),
        str(tool_input.get("file_path") or ""),
    ]
    return " ".join(parts)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    text = _payload_text(payload)
    verification_patterns = [
        r"\bpytest\b",
        r"\blatexmk\b",
        r"\bpython3?\b.*examples/card-krueger",
        r"examples/card-krueger/.+did_analysis\.py",
        r"\bplaywright\b",
        r"\bnpm\s+(test|run\s+docs:build)\b",
    ]

    if any(re.search(pattern, text) for pattern in verification_patterns):
        print(
            json.dumps(
                {
                    "systemMessage": (
                        "Verification-relevant action detected. In the final response, "
                        "report the command or edited path, result, generated files, "
                        "and any remaining risk."
                    )
                }
            )
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
