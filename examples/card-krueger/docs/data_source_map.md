# Card-Krueger Data Source Map

Checked on 2026-06-24.

## Public Source

| Field | Detail |
| --- | --- |
| Study | Card and Krueger, "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania" |
| Public data page | <https://davidcard.berkeley.edu/data_sets.html> |
| Public data readme | <https://davidcard.berkeley.edu/readme/njmin-readme.txt> |
| NBER working paper | <https://www.nber.org/papers/w4509> |
| Paper PDF | <https://davidcard.berkeley.edu/papers/njmin-aer.pdf> |
| Access note | The David Card data page lists an associated data archive and readme. This workshop repository does not bundle that archive. |

## Bundled Teaching Data

| Field | Detail |
| --- | --- |
| File | `examples/card-krueger/data/synthetic_fast_food_panel.csv` |
| Status | Synthetic teaching data created for the workshop |
| Unit of observation | Store-wave pair |
| Treatment group | New Jersey fast-food stores, coded `NJ` |
| Comparison group | Eastern Pennsylvania fast-food stores, coded `PA` |
| Outcome | Full-time-equivalent employment in workers, `fte_employment` |
| Timing | `before` and `after` waves around the April 1992 New Jersey minimum wage increase |
| Sample restriction | Balanced panel with exactly one before and one after observation per store |
| Transformations | Create `treated` and `post` indicators; compute group means; compare the NJ employment change with the PA employment change |
| Raw/private data | None included |
| Research caveat | The synthetic data are not Card and Krueger's raw data, do not reproduce the published estimates, and cannot support a substantive causal claim. |

## Variables

| Variable | Type | Meaning |
| --- | --- | --- |
| `store_id` | string | Synthetic store identifier |
| `state` | string | `NJ` for treatment, `PA` for comparison |
| `wave` | string | `before` or `after` |
| `fte_employment` | numeric | Full-time-equivalent employment in workers |

## Baseline Estimand For The Teaching CSV

The teaching script computes:

```text
(mean NJ after - mean NJ before) - (mean PA after - mean PA before)
```

This is a simple before/after comparison across the two groups. It illustrates
the mechanics of difference-in-differences; it is not a complete replication of
the paper.
