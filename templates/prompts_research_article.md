# Research Article Prompts (Copy-Paste)

Replace bracketed text. Use in your `starter_article` copy.

## Theory

```text
Read docs/research_design_memo.md. Draft a LaTeX subsection in paper/main.tex
specifying agents, preferences, and equilibrium for [MODEL]. State assumptions
explicitly. Do not invent citations.
```

```text
Check the FOC derivation in paper/theory_appendix.tex for internal consistency.
List any steps that need human verification.
```

## Empirics and causal inference

```text
Given H1: "[HYPOTHESIS]", propose a baseline regression: dependent variable,
main regressor(s), controls, fixed effects, clustering, and software package.
```

```text
Read docs/research_design_memo.md and update the identification section: state
the estimand, parallel trends assumption, and three concrete threats with
evidence from the draft or summary statistics.
```

```text
Run src/estimate_did.py, confirm tables/main_did.tex matches the coefficient
discussed in paper/main.tex. Report mismatches only with file references.
```

## Writing

```text
Use the paper-polisher skill on paper/main.tex Introduction only. Flag claims
needing \cite{} and do not invent references.
```

## Coding and issues

```text
Turn docs/project_brief.md into three GitHub issues with acceptance criteria:
rig/memo, rig/estimation, rig/referee-pass. Each issue lists allowed paths and
verification commands.
```

```text
Use research-sdd skill: propose requirements for adding event-study figures to
this repo. Stop before editing code until I approve the plan.
```
