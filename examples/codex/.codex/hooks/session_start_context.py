#!/usr/bin/env python3
"""Provide lightweight economics-research context for a Codex session."""

from __future__ import annotations

import json

MESSAGE = (
    "Economics research context: protect confidential data and secrets; do not "
    "edit raw or synthetic data without explicit scope; do not invent citations "
    "or results; report verification evidence before claiming completion."
)

print(
    json.dumps(
        {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": MESSAGE,
            }
        }
    )
)
