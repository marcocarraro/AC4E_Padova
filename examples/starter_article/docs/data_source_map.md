# Data Source Map

| Source | URL / path | Access | Variables | Notes |
| --- | --- | --- | --- | --- |
| Workshop panel (demo) | `data/raw/city_month_panel.csv` | In repo | `log_emp`, `treat`, `post` | Synthetic — Module 3 empirics |
| Public form demo (Playwright) | `http://127.0.0.1:8000` or script-managed local server | Local form, no external submission | source URL, access note, evidence path | Module 4: run `examples/playwright/fill_demo_form.py` |
| FRED (optional MCP) | <https://fred.stlouisfed.org/> via `agent-harness/mcp/fred/` | API key in env for live calls; offline sample otherwise | e.g. `UNRATE` metadata | Copy your lane MCP example; document any series used |

## Playwright evidence (Module 4)

After running the form demo, copy the row from `outputs/playwright_form_evidence.md`
or record:

| Field | Value |
| --- | --- |
| Evidence file | `outputs/playwright_form_evidence.md` |
| Screenshot path | `outputs/playwright_confirmation.png` |
| Date captured | [YYYY-MM-DD] |
