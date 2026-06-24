# Codex Project Instructions For Economics Research

Read the project README, the task or issue, and any relevant data map before
editing. Prefer small, reviewable changes with explicit verification evidence.

## Research Boundaries

- Do not invent citations, data sources, coefficients, or robustness results.
- Keep causal language tied to the stated identification assumptions.
- Treat `data/raw/`, private drafts, and credentials as protected. Do not inspect
  or print them without explicit human approval.
- Use relative paths and document the command that reproduces each output.
- For synthetic teaching data, state that no substantive research claim follows.

## Card-Krueger Running Case

The workshop running case is `examples/card-krueger/`. The bundled CSV is
synthetic teaching data. It illustrates data documentation, DiD mechanics, tests,
agent review, goals, and orchestration. It is not the Card-Krueger raw data and it
does not reproduce the published estimates.

## Review Standard

Before claiming completion, report:

- files changed;
- verification command and result, or why it was not run;
- whether data, assumptions, and caveats stayed consistent;
- residual risks or needed human checks.
