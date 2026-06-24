---
name: ck-robustness-note
---

# Goal: Add A Robustness Planning Note

## Description

Add a short planning note to `examples/card-krueger/docs/research_design_memo.md`
describing one plausible robustness check for the synthetic Card-Krueger teaching
example. This is a planning note only; it does not implement a new estimator.

## Approach

1. Read the research design memo and data source map.
2. Add one paragraph under `Limitations` or a new `Potential Robustness Checks`
   section.
3. State the allowed robustness idea, why it matters, and what command would verify
   it if implemented later.
4. Preserve the synthetic-data caveat.

## Acceptance Criteria

- [ ] The memo contains one robustness planning paragraph or short bullet list.
- [ ] The text names the target file(s) for a future implementation.
- [ ] The text says the bundled data are synthetic teaching data.
- [ ] The text does not claim a substantive causal result.
- [ ] No data files are modified.

## Constraints

- Do not implement code for this goal.
- Do not edit `examples/card-krueger/data/synthetic_fast_food_panel.csv`.
- Keep the change under 200 words.
