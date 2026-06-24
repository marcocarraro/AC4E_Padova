# Replication Package

## Requirements

- Python 3.10+
- Packages in `requirements.txt`

## Clean run (from repo root)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/estimate_did.py
python -m pytest tests/ -q
```

Expected outputs:

- `tables/main_did.tex`
- Console print of Treat × Post coefficient

## Replication check

```bash
python .cursor/skills/replication-checker/scripts/check_replication.py .
```

(Codex/Claude: adjust path to your lane’s `replication-checker` skill folder.)
