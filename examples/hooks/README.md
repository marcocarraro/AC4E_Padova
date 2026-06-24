# Hook Examples

These examples are for teaching. Review them before installing.

Hooks run deterministic scripts during the agent lifecycle. They are useful
for:

- blocking risky shell commands,
- reminding agents about data boundaries,
- adding context at session start,
- checking outputs after a tool runs,
- writing a review log.

## Files

```text
examples/hooks/
+-- .codex/
    +-- hooks.json
    +-- hooks/
        +-- session_start_context.py
        +-- pre_tool_use_policy.py
        +-- post_tool_use_review.py
```

The files in this directory use Codex hook layout. **Codex CLI:** copy then run
`/hooks` in the terminal. **Codex app:** copy then run `/hooks` in the thread to
review and trust. Claude Code examples live in `examples/claude/.claude/`.
Cursor users should verify hook support in their installed editor or CLI version
before installing.

## Install In A Disposable Test Repo

From a test repository root:

```bash
mkdir -p .codex
cp -R /path/to/AC4E_LSE_PhD_Students/examples/hooks/.codex/* .codex/
codex
```

Inside Codex:

```text
/hooks
```

Review the hooks before trusting them.

## What The Hooks Do

- `SessionStart`: adds a short reminder about workshop data boundaries.
- `PreToolUse` on Bash: warns or blocks risky commands such as `rm -rf`, edits
  to `data/raw`, or attempts to print `.env`.
- `PostToolUse` on Bash: reminds the agent to report verification evidence
  after commands that look like tests or browser automation.

## Exercise

Ask your agent:

```text
Read the hook scripts in examples/hooks/.codex/hooks. Suggest one change that
would make them more appropriate for a confidential empirical research project.
Do not apply the change.
```
