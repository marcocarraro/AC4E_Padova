# Inspiration Notes (Peer Workshops)

How external economist resources inform this LSE workshop. We cite and adapt
**patterns**, not slides.

| Resource | Link | Mapped to |
| --- | --- | --- |
| AI in Business & Economic Research wiki | <https://velikov-mihail.github.io/ai-econ-wiki/> | Skills vs subagents, Git-first workflow, plan/execute split → Modules 2–3 |
| Golub: Cursor for economics research | <https://velikov-mihail.github.io/ai-econ-wiki/summaries/using-llms-cursor/> | Repo-wide context, Overleaf/Git sync → Module 1 scaffold |
| Panjwani: AI agents for econ research | <https://velikov-mihail.github.io/ai-econ-wiki/summaries/ai-agents-econ-research/> | Issue lists, verification before merge → Module 1, 5 |
| Markus Academy: Claude Code for Economists | <https://velikov-mihail.github.io/ai-econ-wiki/summaries/getting-started-economists/> | PhD toolchain narrative → README, five lanes |
| Spina: Claude Code for academics | <https://velikov-mihail.github.io/ai-econ-wiki/summaries/spina-paper/> | “Jagged frontier” → Module 4 identification review |
| Periklis: Claude Code for economic research | <https://perikl.is/posts/2026/claude-code-for-econ/> | Repo layout → `starter_article` |
| AI Economist benchmark | <https://claude-code-economist.com/> | Optional reading; causal task limits → Module 4 |
| Agentic Coding for Economists (parent course) | <https://github.com/antoniomele/AgenticCodingForEconomists> | `starter_repo`, replication-checker, research prompts |

## Design choices from this literature

1. **Separate planning from execution** — research design memo and `spec/intent.md` before large code edits (Module 3).
2. **Subagents for review** — identification-reviewer and verifier run in fresh context (Module 2, 4).
3. **Skills for repetition** — referee, replication, prose polish (Module 2).
4. **Human owns identification** — referee skill flags threats; agents do not certify causality (Module 4).

See also [`docs/sources.md`](sources.md) for live product documentation links.
