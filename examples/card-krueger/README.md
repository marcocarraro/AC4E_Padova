# Card-Krueger Teaching Example

This is the main runnable economics example for the Padova workshop. It mirrors
the Card and Krueger minimum-wage case used in `GUIDE.md`: fast-food employment
in New Jersey and eastern Pennsylvania before and after New Jersey's April 1992
minimum wage increase.

The bundled CSV is **synthetic teaching data**. It is not Card and Krueger's raw
data and must not be used for a research claim. It exists so participants can
practice data maps, difference-in-differences code, tests, and agent review
without downloading external data during the workshop.

## What This Example Shows

- how to document a public data source without bundling raw external data;
- how to state unit, treatment, comparison group, outcome, timing, and sample
  restriction;
- how to run a small baseline difference-in-differences calculation;
- how to attach tests that check the teaching data, caveats, and result path.

## Project Map

```text
examples/card-krueger/
+-- README.md
+-- requirements.txt
+-- data/
|   +-- synthetic_fast_food_panel.csv
+-- docs/
|   +-- data_source_map.md
|   +-- research_design_memo.md
+-- outputs/
|   +-- .gitkeep
+-- src/
|   +-- __init__.py
|   +-- did_analysis.py
+-- tests/
    +-- test_did_analysis.py
```

## Clean Run

From the repository root:

```bash
python3 -m pip install -r examples/card-krueger/requirements.txt
python3 examples/card-krueger/src/did_analysis.py
python3 -m pytest examples/card-krueger/tests
```

The analysis command prints group means and the toy DiD estimate. It also writes
`examples/card-krueger/outputs/baseline_did_summary.md`.

Expected headline result with the bundled synthetic data:

```text
Toy DID estimate: 3.0 FTE workers.
```

## Public References

- David Card data page: <https://davidcard.berkeley.edu/data_sets.html>
- Card-Krueger data readme: <https://davidcard.berkeley.edu/readme/njmin-readme.txt>
- NBER Working Paper 4509: <https://www.nber.org/papers/w4509>
- AER paper PDF: <https://davidcard.berkeley.edu/papers/njmin-aer.pdf>

The public data archive is listed by David Card's data page. This workshop
example does not download or redistribute it.

## Data Documentation Summary

- **Source in this repo:** hand-written synthetic CSV at
  `data/synthetic_fast_food_panel.csv`.
- **Unit of observation:** store-wave pair.
- **Outcome variable:** full-time-equivalent employment, in workers, recorded as
  `fte_employment`.
- **Treatment group:** New Jersey stores, coded `NJ`.
- **Comparison group:** eastern Pennsylvania stores, coded `PA`.
- **Wave labels:** `before` and `after`, around the April 1992 New Jersey
  minimum wage increase.
- **Sample restriction:** balanced teaching panel with one `before` and one
  `after` observation per store and no missing employment values.
- **Research caveat:** the synthetic data illustrate the workflow only. They do
  not reproduce the published estimates and do not establish a causal claim.

See [`docs/data_source_map.md`](docs/data_source_map.md) for the full map and
[`docs/research_design_memo.md`](docs/research_design_memo.md) for the teaching
design memo.

## Practice Prompts

Read-only orientation:

```text
Read examples/card-krueger/README.md,
examples/card-krueger/docs/data_source_map.md, and
examples/card-krueger/src/did_analysis.py. Do not edit files. Explain the unit
of observation, treatment group, comparison group, outcome, timing, sample
restriction, synthetic-data caveat, and verification command.
```

Planning:

```text
Plan one issue that extends examples/card-krueger with a robustness check. Do
not implement. Include allowed files, acceptance criteria, verification
evidence, and an out-of-scope note saying this synthetic example cannot
establish a causal claim.
```

Review:

```text
Review a diff to examples/card-krueger. Check whether data source,
transformations, units, sample restrictions, and research caveats remain
documented. Return blockers first.
```
