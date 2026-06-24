# Verification Report

Date: 2026-06-24.

Issue: #14, reviewer verification for examples, slides, and harness install
paths.

## Environment

This verification was **not** run in a Codex cloud environment. The issue was
delegated to Codex cloud first, but the connector returned a usage-limit block.
The checks below were run as the approved local fallback on branch
`review/14-cloud-verification`, starting from main commit
`77ab58af77093432cbfd044500653caddebfa3a4`.

Observed local tool versions:

- Python 3.12.9 in `/tmp/ac4e-padova-verify-venv`
- Node v24.16.0 and npm 11.13.0
- TeX Live 2025, `latexmk` 4.86a
- Codex CLI 0.141.0, Claude Code 2.1.119, Cursor 3.8.23, cursor-agent
  2026.04.17

## Blockers

No open blockers remain after the fixes in this PR.

Blockers found and fixed:

- Root Python install failed because `requirements.txt` required
  `playwright>=1.61.1`, while the available Python package index only exposed
  Playwright through 1.60.0. Fixed by pinning Python and Node Playwright to the
  1.60.x workshop line.
- `package.json` exposed `docs:*` scripts for the excluded `website/` folder.
  Fixed by removing those npm scripts and deleting the stale site-generation
  scripts.
- `scripts/validate_setup.py` failed because the starter article referenced a
  synthetic raw CSV that was not committed. Fixed by adding the small synthetic
  starter panel and updating its documented sample size.
- Root-level `pytest examples/card-krueger/tests examples/starter_article/tests`
  failed because starter tests assumed the working directory was
  `examples/starter_article`. Fixed by making the starter tests importable from
  repo root and from the starter directory.
- The Playwright Python demo produced a raw traceback when Chromium was not
  installed. Fixed with a participant-facing missing-browser message.

## Warnings

- This report is local fallback evidence, not cloud-agent evidence, because the
  cloud connector was quota-blocked.
- Desktop app workflows cannot be fully verified by command line. The setup
  validator can detect local CLI/app binaries, but participants still need to
  sign in and open the repository in the apps.
- Browser-backed Playwright checks required the documented Chromium install
  step. After `python -m playwright install chromium`, both Python and Node
  browser checks passed.
- `npm run validate` uses whichever `python3` is first on `PATH`; it passes
  after the workshop Python requirements are installed and the environment is
  active, and correctly fails if required packages such as Playwright are absent.

## Command Evidence

| Check | Command | Status | Evidence |
| --- | --- | --- | --- |
| Python dependency install | `python -m venv /tmp/ac4e-padova-verify-venv`; `python -m pip install -r requirements.txt`; `python -m pip install -r examples/card-krueger/requirements.txt` | Pass after Playwright pin fix | Installed Playwright 1.60.0, pytest 9.1.1, pandas 3.0.3, statsmodels 0.14.6, matplotlib 3.11.0, rich 15.0.0. |
| Setup validator | `/tmp/ac4e-padova-verify-venv/bin/python scripts/validate_setup.py` | Pass after starter data fix | All required setup checks OK; optional agent tools detected; desktop app sign-in remains manual. |
| Package validate script | `PATH=/tmp/ac4e-padova-verify-venv/bin:$PATH npm run validate` | Pass | Same setup checks passed through the npm script when the documented Python environment was active. |
| Card-Krueger analysis | `/tmp/ac4e-padova-verify-venv/bin/python examples/card-krueger/src/did_analysis.py` | Pass | Printed `Toy DID estimate: 3.0 FTE workers`; wrote `examples/card-krueger/outputs/baseline_did_summary.md`. |
| Card-Krueger and starter tests | `/tmp/ac4e-padova-verify-venv/bin/python -m pytest examples/card-krueger/tests examples/starter_article/tests` | Pass | 12 tests passed in 1.36s. |
| Starter analysis | `/tmp/ac4e-padova-verify-venv/bin/python examples/starter_article/src/estimate_did.py` | Pass | Printed `DiD estimate (Treat x Post): -0.0550`; wrote `examples/starter_article/tables/main_did.tex`. |
| Playwright Python compile fallback | `/tmp/ac4e-padova-verify-venv/bin/python -m py_compile examples/playwright/fill_demo_form.py` | Pass | No syntax errors. |
| Playwright browser install | `/tmp/ac4e-padova-verify-venv/bin/python -m playwright install chromium` | Pass | Downloaded Chromium/headless shell for Playwright 1.60.0. |
| Playwright Python demo | `/tmp/ac4e-padova-verify-venv/bin/python examples/playwright/fill_demo_form.py` | Pass | Wrote ignored `outputs/playwright_form_evidence.md` and `outputs/playwright_confirmation.png`; confirmation was Card-Krueger public data page. |
| Node dependency install | `npm install --no-package-lock` | Pass | Added 3 packages; audit reported 0 vulnerabilities. |
| Playwright TypeScript spec | `npm run serve:form`; `npm run pw:test` | Pass | 1 test passed in 1.2s against the local form. |
| Slide build | `npm run slides:build` | Pass | `latexmk` built `slides/workshop/workshop_slides.pdf`; output is 37 pages. |
| FRED MCP tests | `/tmp/ac4e-padova-verify-venv/bin/python -m pytest agent-harness/mcp/fred/tests` | Pass | 4 tests passed in 0.03s. |
| FRED MCP smoke | `/tmp/ac4e-padova-verify-venv/bin/python agent-harness/mcp/fred/scripts/smoke.py --offline` | Pass | `initialize ok`, `tools/list ok`, `tools/call fred_get_series_info ok`, `offline smoke ok`. |
| Harness config parse | Python `json.loads` / `tomllib.loads` over Codex, Claude, and Cursor MCP/hook/settings examples | Pass | JSON and TOML examples parsed for `examples/` and `agent-harness/` copies. |
| Harness tree inventory | Python path inventory for Codex, Claude Code, and Cursor examples | Pass | Skills, subagents/agents, hooks, MCP config, goals, and orchestration paths present for all three lanes. |
| Forbidden import check | `find . -maxdepth 2 -type d \( -name follow_up -o -name followup -o -name website \)` and `git ls-files \| rg '(^|/)(follow_up|followup|website)(/|$)'` | Pass | No forbidden folders or tracked files under those paths. |
| Secret/path scan | Strict `rg` scan for API-key assignments, private-key markers, and absolute local user paths | Pass | No matches after excluding ignored generated outputs and dependency folders. |

## Files Fixed By Verification

- `.gitignore`
- `requirements.txt`
- `package.json`
- `scripts/build_site_tabs.py` and `scripts/build_concepts_site.py` deleted
- `examples/starter_article/data/raw/city_month_panel.csv`
- `examples/starter_article/docs/research_design_memo.md`
- `examples/starter_article/src/estimate_did.py`
- `examples/starter_article/tables/main_did.tex`
- `examples/starter_article/tests/test_estimate_did.py`
- `examples/playwright/fill_demo_form.py`
- `agent-harness/codex/hooks/post_tool_use_review.py`
- `examples/codex/.codex/hooks/post_tool_use_review.py`
- `slides/workshop/workshop_slides.pdf`

## Follow-Up Issues

No new blocker issue is required from this verification pass. Remaining risks
are environment warnings: cloud quota, desktop app sign-in, and local browser
binary installation.
