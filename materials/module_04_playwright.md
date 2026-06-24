# Module 4: Quality, Replication, And Data Acquisition

Time: 55 minutes

## Purpose

Close the quality loop: referee review, replication check, and a short
Playwright step that documents **public data acquisition** in `docs/data_source_map.md`.

Ethical boundary: pre-submission review on **your** draft or public material only—not confidential referee assignments.

## Part A: Referee review (~20 min)

1. Target: `paper/main.tex` or [`examples/paper/working_paper_excerpt.md`](../examples/paper/working_paper_excerpt.md).
2. Use **referee-checklist** skill and [`templates/referee_report.md`](../templates/referee_report.md).

```text
Review paper/main.tex as a pre-submission economics referee. Separate major and
minor issues. Each major issue needs evidence from the text or tables. Check
identification and table/text consistency. Do not invent citations.
```

Second pass with **identification-reviewer** or three-pass panel (identification, tables, contribution).

Save: `outputs/referee_report_sample.md`.

## Part B: Replication check (~10 min)

```text
Run replication-checker on repo root. Fix any red items or document why yellow
is acceptable for the workshop demo.
```

## Part C: Playwright data evidence (~20 min)

Playwright is **terminal-only** for all lanes.

```bash
python3 -m http.server 8000 --directory examples/web-form
python examples/playwright/fill_demo_form.py
```

Add a row to `docs/data_source_map.md` linking the script output or screenshot path.

```text
Read examples/playwright/fill_demo_form.py. Explain locators. Suggest one improvement
if the form layout changes.
```

## AI referee tools (discussion)

See [`docs/sources.md`](../docs/sources.md). Tools are leads, not authorities.

## Tool Notes

### Codex CLI

```text
Use referee-checklist on examples/paper/working_paper_excerpt.md. Write
outputs/referee_report_sample.md. Then replication-checker on repo root.
```

### Codex app

Same in desktop thread; `/review` optional.

### Claude Code CLI

```text
Use identification-reviewer on docs/research_design_memo.md, then referee-checklist
on the sample excerpt. Save outputs/referee_report_sample.md.
```

### Claude Code app

Slash menu for skills; parallel sessions optional.

### Cursor

Referee skill + background agent only on a branch you review before merge.

## Red flags in AI reviews

- Generic robustness laundry lists
- “Clear identification” without checking pre-trends
- Invented citations

## Debrief

Which output would you trust without opening the code: referee prose or replication-checker?
