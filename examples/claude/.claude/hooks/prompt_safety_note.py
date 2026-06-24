#!/usr/bin/env python3
"""Claude Code hook example: add a safety note to prompts."""

import json


print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": (
            "Workshop safety reminder: do not process confidential manuscripts "
            "or raw data unless the user explicitly confirms permission."
        )
    }
}))

