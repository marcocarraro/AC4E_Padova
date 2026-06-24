# Research Design Memo

## Title

Minimum Wage Increase and Fast-Food Employment

## Research Question

What happened to fast-food employment in New Jersey relative to eastern
Pennsylvania after New Jersey raised its minimum wage in April 1992?

## Motivation

The Card-Krueger case is a useful teaching example because the policy change,
comparison group, timing, and employment outcome are easy to explain in a short
workshop. It also gives participants a familiar economics setting for practicing
agent instructions, data maps, tests, and review.

## Data

The public source is the Card-Krueger fast-food survey data listed on David
Card's data page. This repository uses a small synthetic teaching panel instead
of bundling the public archive.

The bundled file is `examples/card-krueger/data/synthetic_fast_food_panel.csv`.
It contains store-wave observations for six synthetic New Jersey stores and six
synthetic eastern Pennsylvania stores. Each store has one `before` row and one
`after` row.

## Design

The treatment group is New Jersey stores. The comparison group is eastern
Pennsylvania stores. The post period is the wave after New Jersey's April 1992
minimum wage increase. The outcome is full-time-equivalent employment.

The teaching estimand is:

```text
(NJ after - NJ before) - (PA after - PA before)
```

## Expected Output

Running `python3 examples/card-krueger/src/did_analysis.py` prints group means,
prints the toy difference-in-differences estimate, and writes
`examples/card-krueger/outputs/baseline_did_summary.md`.

## Limitations

- The bundled data are synthetic teaching data, not Card and Krueger's raw data.
- The toy estimate does not reproduce the published estimates.
- The two-wave teaching panel cannot assess pre-trends.
- This memo does not evaluate alternative specifications, sample restrictions,
  closure handling, wage effects, prices, or broader minimum-wage literature.
- No causal or policy claim should be made from the synthetic result.

## Human Review Checklist

- Confirm the data source and synthetic-data caveat are visible.
- Confirm the treatment, comparison group, timing, outcome, and unit are stated.
- Confirm the command in `README.md` runs and produces the documented output.
- Confirm any agent-generated text does not overclaim beyond the teaching design.
