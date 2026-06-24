# Replication Criteria — Pass/Fail Definitions

This document defines what passes and what fails a replication check for economics research pipelines.

---

## 1. Dependencies Declared

**PASS:** `requirements.txt` or `pyproject.toml` exists at repo root and lists project dependencies.

**FAIL:**
- No dependency file present
- File exists but is empty or contains only comments
- File is a stub (e.g., "add your packages here") with no actual packages

**Note:** `environment.yml` (conda) may substitute; add support if the project uses conda.

---

## 2. No Hardcoded Paths

**PASS:** No Python files contain:
- Absolute Unix paths: `/Users/...`, `/home/...`
- Absolute Windows paths: `C:\...`, `D:\...`
- `localhost` or `127.0.0.1` with non-configurable ports (config via env vars is OK)
- Machine-specific paths that assume a particular setup

**FAIL:** Any of the above appear in source code. Common failures:
- `"/Users/jane/data/file.csv"`
- `os.path.join("/home/user", "output")`
- `"localhost:5432"` without being read from config/env

**Exception:** Paths constructed from env vars (e.g., `os.environ["DATA_DIR"]`) are acceptable.

---

## 3. Replication README Exists

**PASS:** `replication/README.md` exists and contains:
- Setup instructions (clone, venv, pip install)
- How to obtain/configure data
- Exact run commands in order
- Expected outputs (figures, tables)

**FAIL:**
- File does not exist
- File exists but is empty or a bare template with no real instructions
- Instructions are outdated or refer to non-existent scripts

---

## 4. Data Sources Documented

**PASS:** Data access is documented in one of:
- `docs/data_source_map.md`
- `replication/README.md` (data section)
- A clearly linked external document

The document should describe:
- Where data comes from (URL, API, manual download)
- Access requirements (API key, registration)
- Key variables and coverage

**FAIL:** No documentation of data sources; a reader cannot determine how to obtain the data.

---

## 5. Imports in Requirements

**PASS:** Every top-level package imported in Python files appears in `requirements.txt` or `pyproject.toml` dependencies.

**FAIL:** One or more imported packages are not declared. Common omissions:
- `pandas`, `numpy`, `matplotlib` used but not listed
- Project uses `statsmodels` but it is missing from requirements

**Note:** Standard library modules (`os`, `sys`, `json`, etc.) are not required.

---

## 6. Clean Run

**PASS:** A fresh clone + new virtual environment + following `replication/README.md` yields:
- All run commands complete without error
- Expected output files are generated

**FAIL:**
- Commands fail due to missing deps, wrong paths, or environment assumptions
- Output files are missing or differ from documented expectations
- Manual edits are required beyond what the README describes

---

## Severity Tiers

- **Blockers (red):** Must fix before sharing. Dependencies missing, hardcoded paths, no replication README.
- **Warnings (yellow):** Should fix. Data docs incomplete, imports partially missing.
- **Green:** Replication-ready; a colleague can run from scratch.
