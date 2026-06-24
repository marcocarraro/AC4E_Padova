#!/usr/bin/env python3
"""
Replication checker script for economics research pipelines.

Checks:
- No hardcoded paths in Python files
- requirements.txt or pyproject.toml exists
- replication/README.md exists
- All imported packages are declared in requirements
- Reports pass/fail for each check

Usage:
    python check_replication.py /path/to/repo
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path


def check_hardcoded_paths(repo_root: Path) -> tuple[bool, list[str]]:
    """Scan Python files for hardcoded paths. Returns (pass, list of findings)."""
    patterns = [
        (r"/Users/[^/\s'\"]+", "Unix /Users path"),
        (r"/home/[^/\s'\"]+", "Unix /home path"),
        (r"C:\\[^\s'\"]+", "Windows drive path"),
        (r"localhost(:\d+)?", "localhost reference"),
        (r"/tmp/[^\s'\"]+", "Hardcoded /tmp path"),
    ]
    findings: list[str] = []
    python_files = list(repo_root.rglob("*.py"))
    if not python_files:
        return True, []  # No Python files, nothing to check

    for py_file in python_files:
        if "__pycache__" in str(py_file) or "venv" in str(py_file):
            continue
        if "check_replication" in py_file.name:
            continue
        try:
            text = py_file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for pattern, label in patterns:
            for match in re.finditer(pattern, text):
                rel = py_file.relative_to(repo_root)
                findings.append(f"{rel}:{label} — {match.group()[:60]}")

    return len(findings) == 0, findings


def check_deps_file(repo_root: Path) -> tuple[bool, str]:
    """Check that requirements.txt or pyproject.toml exists."""
    if (repo_root / "requirements.txt").exists():
        return True, "requirements.txt"
    if (repo_root / "pyproject.toml").exists():
        return True, "pyproject.toml"
    return False, "Neither requirements.txt nor pyproject.toml found"


def check_replication_readme(repo_root: Path) -> tuple[bool, str]:
    """Check that replication/README.md exists."""
    path = repo_root / "replication" / "README.md"
    if path.exists():
        return True, str(path.relative_to(repo_root))
    return False, "replication/README.md not found"


def get_declared_packages(repo_root: Path) -> set[str]:
    """Extract package names from requirements.txt or pyproject.toml."""
    declared: set[str] = set()

    req_path = repo_root / "requirements.txt"
    if req_path.exists():
        for line in req_path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.split("#")[0].strip()
            if not line or line.startswith("-"):
                continue
            # Handle package[extra]==1.0 -> package
            name = re.split(r"[=<>\[]", line)[0].strip().lower()
            declared.add(name)

    # Minimal pyproject.toml parsing for dependencies
    py_path = repo_root / "pyproject.toml"
    if py_path.exists():
        text = py_path.read_text(encoding="utf-8", errors="replace")
        # Simple regex for dependencies section
        for m in re.finditer(r'["\']([a-zA-Z0-9_-]+)["\']\s*(?:\[|==|>=|<=|~=)?', text):
            declared.add(m.group(1).lower())

    return declared


def get_imported_packages(repo_root: Path) -> set[str]:
    """Parse Python files and extract top-level import names."""
    imported: set[str] = set()
    stdlib = {
        "abc", "argparse", "ast", "collections", "csv", "dataclasses", "datetime",
        "glob", "importlib", "io", "json", "math", "os", "pathlib", "re",
        "shutil", "subprocess", "sys", "typing", "__future__",
    }

    for py_file in repo_root.rglob("*.py"):
        if "__pycache__" in str(py_file) or "venv" in str(py_file):
            continue
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    top = alias.name.split(".")[0]
                    if top not in stdlib:
                        imported.add(top.lower())
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    top = node.module.split(".")[0]
                    if top not in stdlib:
                        imported.add(top.lower())

    return imported


def check_imports_declared(repo_root: Path) -> tuple[bool, list[str]]:
    """Check that all imported packages appear in requirements."""
    declared = get_declared_packages(repo_root)
    imported = get_imported_packages(repo_root)
    missing = imported - declared
    return len(missing) == 0, sorted(missing)


def main() -> int:
    parser = argparse.ArgumentParser(description="Replication checker for research pipelines")
    parser.add_argument("repo", type=Path, nargs="?", default=Path.cwd())
    args = parser.parse_args()

    repo = args.repo.resolve()
    if not repo.is_dir():
        print(f"Error: not a directory: {repo}", file=sys.stderr)
        return 1

    results: list[tuple[str, bool, str]] = []

    # 1. Hardcoded paths
    ok, findings = check_hardcoded_paths(repo)
    if ok:
        results.append(("No hardcoded paths", True, "pass"))
    else:
        results.append(("No hardcoded paths", False, f"fail: {len(findings)} found\n  " + "\n  ".join(findings[:5])))

    # 2. Dependencies file
    ok, msg = check_deps_file(repo)
    results.append(("Dependencies file exists", ok, "pass" if ok else f"fail: {msg}"))

    # 3. Replication README
    ok, msg = check_replication_readme(repo)
    results.append(("Replication README exists", ok, "pass" if ok else f"fail: {msg}"))

    # 4. Imports in requirements (only if deps file exists)
    deps_ok, _ = check_deps_file(repo)
    if deps_ok:
        ok, missing = check_imports_declared(repo)
        results.append(("Imports in requirements", ok, "pass" if ok else f"fail: {missing}"))
    else:
        results.append(("Imports in requirements", False, "skip: no deps file"))

    # Print report
    print("# Replication Check Report")
    print(f"\n**Repo:** {repo}\n")
    all_pass = all(r[1] for r in results)
    print(f"**Overall:** {'PASS' if all_pass else 'FAIL'}\n")
    print("| Check | Result |")
    print("|-------|--------|")
    for name, passed, msg in results:
        status = "pass" if passed else "fail"
        print(f"| {name} | {status} |")
    print()
    for name, passed, msg in results:
        if not passed and "fail" in msg:
            print(f"**{name}:** {msg}\n")

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
