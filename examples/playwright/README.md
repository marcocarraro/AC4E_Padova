# Playwright Data Evidence Demo

This demo shows how browser automation can create evidence for a data source map
without touching private data or downloading raw external files. It uses the
local form in `examples/web-form/` and records a Card-Krueger public-source row.

The demo is tool-lane independent. Run it from a terminal whether you use Codex,
Claude Code, or Cursor for the rest of the workshop.

## What It Produces

Default command:

```bash
python3 examples/playwright/fill_demo_form.py
```

Expected output:

```text
Saved evidence to .../outputs/playwright_form_evidence.md
Saved screenshot to .../outputs/playwright_confirmation.png
Confirmation: Saved local evidence row for: Card-Krueger public data page
```

Generated files live under `outputs/`, which is ignored by git. The markdown
evidence file contains a row that can be copied into a project
`docs/data_source_map.md`.

## Python Setup

Official Playwright Python docs recommend installing the pytest plugin for tests
and installing browser binaries. For this standalone script, the workshop
`requirements.txt` includes the Playwright library.

```bash
python3 -m pip install -r requirements.txt
python3 -m playwright install chromium
python3 examples/playwright/fill_demo_form.py
```

If browser binaries are unavailable, run:

```bash
python3 -m py_compile examples/playwright/fill_demo_form.py
```

Then record the missing browser install as a yellow verification result.

## Manual Server Mode

The default Python command starts and stops a local static server for you. To run
the server manually:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory examples/web-form
```

In another terminal:

```bash
python3 examples/playwright/fill_demo_form.py --no-server --base-url http://127.0.0.1:8000
```

Stop the server with `Ctrl-C` after the demo.

## Node Smoke Test

The TypeScript spec uses Playwright's user-facing locators and expects the form
server to already be running:

```bash
npm install
npx playwright install chromium
```

Terminal 1:

```bash
npm run serve:form
```

Terminal 2:

```bash
npm run pw:test
```

Stop the server with `Ctrl-C` after the test.

## Data Source Map Exercise

After running the Python script, open `outputs/playwright_form_evidence.md` and
copy the row under "Data Source Map Row" into one of:

- `examples/card-krueger/docs/data_source_map.md`;
- `examples/starter_article/docs/data_source_map.md`;
- your own project `docs/data_source_map.md`.

Human review checks:

- the source URL is public;
- the form did not download raw data;
- the evidence row does not imply a causal result;
- the screenshot, if used, does not expose private data.
