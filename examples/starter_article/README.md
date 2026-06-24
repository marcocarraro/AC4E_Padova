# Starter Article (Workshop Mini Repo)

Shared economics research project for the LSE PhD workshop. **All five tool lanes**
copy this tree, then merge harness files from your lane folder:

- Codex: `examples/codex/` or `examples/codex-app/`
- Claude: `examples/claude/` or `examples/claude-app/`
- Cursor: `examples/cursor/`

## Teaching thread

Applied micro DiD: remote-work policy pilot and local service employment (synthetic data).

## Quick start

```bash
cd examples/starter_article
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/estimate_did.py
python .cursor/skills/replication-checker/scripts/check_replication.py .
```

## Layout

```text
docs/           project brief, design memo, data source map
paper/          LaTeX skeleton
src/            panel DiD estimation
data/raw/       synthetic CSV (safe to share)
replication/    clean-run instructions
notes/          orchestration and review logs
.cursor/        Cursor harness (copy to lane paths for Codex/Claude)
```

See [`docs/research_article_harness.md`](../../docs/research_article_harness.md) for the completion checklist.
