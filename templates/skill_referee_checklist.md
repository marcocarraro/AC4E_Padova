# Referee Checklist Skill Draft

## Purpose

Review an economics paper draft as a pre-submission critic.

## Trigger Phrases

- referee report
- paper review
- pre-submission review
- robustness checklist
- reviewer comments
- response to referees
- identification review

## Procedure

1. Confirm the paper is the user's own work, public, or otherwise approved for
   AI review. If it appears confidential, stop and ask for confirmation.
2. Identify paper type: theory, applied micro, macro, structural, econometrics,
   finance, or other.
3. Read the abstract, introduction, main result section, tables, and conclusion.
4. Summarize the paper in 5-7 sentences.
5. Identify decision-relevant major issues. Each issue must cite evidence from
   the draft.
6. Compare claims in the text with tables, figures, and equations.
7. **Identification:** State the estimand and design (DiD, IV, RD, etc.). Check
   parallel trends / exclusion / continuity as appropriate. Flag pre-trends,
   spillovers, selective attrition, and overclaiming permanence or causality.
8. **Econometrics:** Clustering level, functional form, multiple hypotheses,
   sensitivity to sample restrictions.
9. Suggest robustness checks only when tied to a specific threat.
10. Flag all citation claims that require external verification.
11. Produce a report using `templates/referee_report.md`.

## Output

- Referee-style report.
- Ranked revision plan.
- List of unverifiable claims.
- List of questions for the human author.

## Install paths (after converting to SKILL.md)

| Lane | Path | Invoke |
| --- | --- | --- |
| Codex CLI / app | `.codex/skills/referee-checklist/SKILL.md` | Name in prompt or slash menu (app) |
| Claude CLI / app | `.claude/skills/referee-checklist/SKILL.md` | Name in prompt or `/` menu (app) |
| Cursor | `.cursor/skills/referee-checklist/SKILL.md` | Slash menu or explicit prompt |
