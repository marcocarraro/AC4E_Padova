#!/usr/bin/env python3
"""Claude Code hook example: remind the agent to report verification evidence."""

import json


print(json.dumps({
    "systemMessage": (
        "If this turn changed files or ran commands, summarize the diff, command "
        "result, and remaining risks before claiming completion."
    )
}))

