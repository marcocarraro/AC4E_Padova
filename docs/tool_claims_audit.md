# Tool Claims Audit

Audit date: 2026-06-24.

Scope: participant-facing tool lanes, harness files, orchestration templates,
and source notes. This audit checks documentation claims against official docs;
it does not certify that each participant account has the relevant plan,
feature flag, quota, or local install.

Cloud-agent note: issue #13 was first delegated as a cloud task, but the Codex
connector reported a usage-limit block. The audit below was completed locally as
the fallback path for the same issue.

## Audit Table

| Tool or area | Official docs checked | Claims checked | Files corrected | Unresolved caveats |
| --- | --- | --- | --- | --- |
| Codex | <https://developers.openai.com/codex/>, `/cloud/`, `/integrations/github/`, `/guides/agents-md/`, `/hooks`, `/mcp`, `/subagents`, `/skills` | Codex cloud/GitHub handoff, `@codex review`, `AGENTS.md`, `.agents/skills/`, `.codex/agents/`, `.codex/hooks.json`, `.codex/config.toml`, MCP approval boundaries | `docs/sources.md` | Cloud task availability depends on account quota, repository connection, trust settings, and active Codex product behavior. |
| Claude Code | <https://code.claude.com/docs/en/overview>, `/settings`, `/cli-reference`, `/skills`, `/sub-agents`, `/hooks`, `/hooks-guide`, `/mcp`, `/goal`, `/scheduled-tasks`, `/agent-view` | `.claude/skills/`, `.claude/agents/`, `/agents`, hooks/settings, `.mcp.json`, `/goal`, `/loop`, app/web/background session wording | `docs/sources.md` | `/goal` requires Claude Code v2.1.139+; `/loop` and scheduled tasks require v2.1.72+; availability of desktop, web, and background-session surfaces depends on installation and account. |
| Cursor | <https://cursor.com/docs>, `/cli/overview`, `/cli/headless`, `/rules`, `/rules.md`, `/skills`, `/subagents`, `/mcp`, `/hooks`, `/cloud-agent`, `/cloud-agent/setup`, `/cloud-agent/best-practices`, `/cloud-agent/security-network`, `/cloud-agent/capabilities`, `/integrations/github`, `/bugbot` | `.cursor/rules/*.mdc`, `AGENTS.md`, `.cursor/skills/`, `.cursor/agents/`, `.cursor/mcp.json`, MCP interpolation, Cloud Agent prompts, Bugbot and `/review` wording | `docs/sources.md`, `materials/tool_tracks.md`, `tool-lanes/README.md`, `tool-lanes/cursor.md`, `orchestration/README.md` | Cursor cloud, hooks, Bugbot, and review commands are plan, repository-integration, version, and workspace-setting sensitive. Cursor docs state `/review` and `/review-bugbot` are available in Cursor 3.7+ and on `cursor.com/agents`; verify in class before relying on them. |
| MCP and FRED | <https://modelcontextprotocol.io/docs/getting-started/intro>, <https://modelcontextprotocol.io/specification/2025-06-18>, <https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices>, FRED API docs | MCP as a host-client-server protocol, public FRED-only MCP example, environment-only `FRED_API_KEY`, no arbitrary URL or local path access, user consent and data privacy cautions | `docs/sources.md` | MCP servers can expose data, run code, or call APIs depending on implementation. Keep workshop servers bounded and avoid confidential data unless explicitly approved. |
| Playwright | <https://playwright.dev/docs/intro>, <https://playwright.dev/python/docs/intro>, <https://playwright.dev/docs/best-practices>, <https://playwright.dev/docs/codegen> | Node and Python install pattern, browser-binary install step, local static form, locators/assertions over implementation details | `docs/sources.md` | Browser-backed checks require installed Playwright packages and browser binaries. The fallback environment for issue #11 lacked those binaries, so browser execution remains a participant setup check. |
| GitHub workflow | GitHub issues, pull requests, and linked PR docs | One issue per task, one branch per task, PR evidence, reviewer handoff, closing keywords on PRs targeting the default branch | `docs/sources.md` | Branch protection, merge permissions, Actions availability, and automatic issue closing depend on repository settings and PR target branch. |

## Targeted Changes Made

- Added official Claude `/goal`, `/loop`, and agent-view sources and version
  requirements to `docs/sources.md`.
- Added Cursor headless CLI, Cloud Agent, GitHub integration, and Bugbot sources
  to `docs/sources.md`.
- Narrowed Cursor review language to "`/review` or Bugbot where enabled" and
  documented the Cursor 3.7+ caveat.
- Softened Cursor cloud-entry-point wording to avoid promising a specific UI or
  command that may vary by release.
- Added MCP security best-practices and GitHub issue/PR workflow sources.
- Fixed the stale "four-hour workshop" wording in `examples/plugins/README.md`.

## Caveats To Carry Into The Workshop

- Do not promise that cloud/background agents are available for every account;
  confirm quota, repository connection, trust prompts, and institutional rules.
- Do not put raw/private data, secrets, or unpublished manuscripts in MCP tools
  or cloud-agent contexts unless the participant explicitly approves that data
  path.
- Treat Cursor hook and review-command behavior as version-sensitive; have a
  CLI or plain prompt fallback ready.
- Keep the Playwright exercise deterministic by using the local static form and
  by installing browser binaries before browser-backed demos.

## Follow-Up Review

Issues #14 and #15 should verify the complete repository after this audit:
examples, links, workshop sequence, and stale imported wording that is not part
of the tool-claims surface.
