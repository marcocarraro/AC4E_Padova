#!/usr/bin/env python3
"""Provide lightweight session context for the workshop."""

import json


message = (
    "Workshop context: protect confidential data, never edit data/raw without "
    "explicit permission, do not invent citations, and report verification "
    "evidence after edits."
)

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": message,
    }
}))

