---
name: ck-parallel-trends-figure
---

# Goal: Teaching Figure For DiD Intuition

## Description

Create a figure script that plots mean FTE employment for NJ and PA in the before
and after waves of the synthetic teaching panel. The figure illustrates the DiD
visual intuition but cannot test pre-trends because the teaching panel has only two
waves.

## Approach

1. Read `examples/card-krueger/src/did_analysis.py` and
   `examples/card-krueger/data/synthetic_fast_food_panel.csv`.
2. Create `examples/card-krueger/src/make_teaching_figure.py`.
3. Compute mean `fte_employment` by `state` and `wave`.
4. Save `examples/card-krueger/outputs/teaching_did_means.png`.
5. Update `examples/card-krueger/README.md` with the run command and caveat.

## Acceptance Criteria

- [ ] `python3 examples/card-krueger/src/make_teaching_figure.py` runs from the
      repository root.
- [ ] `examples/card-krueger/outputs/teaching_did_means.png` exists after running.
- [ ] The plot labels NJ and PA and uses before/after wave labels.
- [ ] The title or caption contains "synthetic teaching data".
- [ ] `python3 -m pytest examples/card-krueger/tests` passes.
- [ ] No absolute paths appear in the new script.

## Constraints

- Do not modify the synthetic CSV.
- Do not claim the figure demonstrates a real causal effect.
- Add dependencies only if `examples/card-krueger/requirements.txt` is updated.
