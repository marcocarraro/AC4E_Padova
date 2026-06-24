---
name: research-sdd
description: >-
  Spec-driven planning for economics research features (memo, empirics, paper
  sections). Use before large code or LaTeX edits. Triggers on research-sdd, spec,
  design memo, requirements for paper.
---

# Research SDD (Workshop)

Plan in markdown before implementation. Adapted from user-level SDD skill; scoped to research repos.

## When to use

- New empirical specification, robustness block, or paper section
- Multi-file changes touching `src/` and `paper/`

## Workflow

1. Read `docs/project_brief.md`, `docs/research_design_memo.md`, and `spec/intent.md`.
2. If `spec/requirements.md` is missing, draft requirements from the memo (EARS style: WHEN/IF/THEN).
3. Propose a short design note: files to touch, verification commands, risks to identification.
4. **Stop for human approval** before editing code or LaTeX.
5. After approval, implement smallest slice; run `python src/estimate_did.py` or tests.

## Do not

- Skip identification discussion for causal claims
- Edit `data/raw/` without permission
