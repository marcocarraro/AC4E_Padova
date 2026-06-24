# Research Design Memo

> Fill during Module 3. Use `templates/research_design_memo.md` in the course repo for structure.

## Research question

Does a 2020 remote-work policy pilot reduce local service employment in treated cities?

## Motivation and literature context

Remote work shifts expenditure away from CBD services. [PLACEHOLDER: 3–5 citations on
remote work and local labor markets.]

## Hypotheses

- **H1:** Post-pilot, treated cities have lower log service employment than controls (negative β on Treat × Post).
- **H2:** Effect persists twelve months after pilot (requires event-study extension — homework).

## Data description

| Field | Description |
| --- | --- |
| Source | Synthetic workshop file `data/raw/city_month_panel.csv` |
| Access | Public within repo |
| Key variables | `log_emp`, `treat`, `post`, `city_id`, `month` |
| Sample | 30 cities × 60 months |
| Unit | City-month |

## Empirical strategy

Two-way fixed effects:

```text
y_ct = α_c + γ_t + β (Treat_c × Post_t) + ε_ct
```

Cluster standard errors by city. Main script: `src/estimate_did.py`.

## Identification strategy

**Assumption:** Parallel trends for treated and control cities absent the pilot.

**Threats (workshop teaching):**

- Pre-trends: treated cities had faster service growth before March 2020 (see `figures/` or excerpt).
- Permanent effect claimed in abstract without long-horizon evidence.
- Spillovers across cities not modeled.

## Expected results

Negative β if remote work reduces local service demand; magnitude interpretable as
percent change in employment.

## Limitations and robustness

- Synthetic data for teaching only.
- Robustness (homework): city-specific linear trends, alternative post dates, placebo leads.
