#!/usr/bin/env python3
"""Validate the workshop setup without modifying the project."""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STARTER = ROOT / "examples" / "starter_article"


@dataclass
class CheckResult:
    label: str
    status: str
    detail: str


def run_version(label: str, command: list[str], required: bool = True) -> CheckResult:
    executable = shutil.which(command[0])
    if executable is None:
        status = "MISSING" if required else "INFO"
        detail = f"{command[0]} not found"
        return CheckResult(label, status, detail)

    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except Exception as exc:  # pragma: no cover - diagnostic path
        return CheckResult(label, "WARN", f"{command[0]} exists but failed: {exc}")

    output = (completed.stdout or completed.stderr).strip().splitlines()
    detail = output[0] if output else f"{command[0]} found at {executable}"
    status = "OK" if completed.returncode == 0 else "WARN"
    return CheckResult(label, status, detail)


def check_python_package(module_name: str, label: str) -> CheckResult:
    if importlib.util.find_spec(module_name) is None:
        return CheckResult(label, "MISSING", f"Python package '{module_name}' not installed")
    return CheckResult(label, "OK", f"Python package '{module_name}' importable")


def check_starter_article() -> CheckResult:
    required = [
        STARTER / "AGENTS.md",
        STARTER / "docs" / "project_brief.md",
        STARTER / "src" / "estimate_did.py",
        STARTER / "data" / "raw" / "city_month_panel.csv",
        STARTER / ".cursor" / "skills" / "replication-checker" / "SKILL.md",
    ]
    missing = [p.relative_to(ROOT) for p in required if not p.exists()]
    if missing:
        return CheckResult(
            "starter_article",
            "MISSING",
            f"missing paths: {', '.join(str(m) for m in missing)}",
        )
    return CheckResult("starter_article", "OK", "core harness paths present")


def main() -> int:
    checks = [
        check_starter_article(),
        CheckResult("python", "OK", sys.version.split()[0]),
        run_version("git", ["git", "--version"]),
        run_version("node", ["node", "--version"]),
        run_version("npm", ["npm", "--version"]),
        run_version("codex", ["codex", "--version"], required=False),
        run_version("claude", ["claude", "--version"], required=False),
        run_version("cursor", ["cursor", "--version"], required=False),
        run_version("cursor-agent", ["cursor-agent", "--version"], required=False),
        check_python_package("playwright", "playwright-python"),
        check_python_package("pandas", "pandas"),
        check_python_package("statsmodels", "statsmodels"),
    ]

    for check in checks:
        print(f"{check.status}: {check.label} - {check.detail}")

    optional_tools = {"codex", "claude", "cursor", "cursor-agent"}
    required_failures = [c for c in checks if c.status == "MISSING" and c.label not in optional_tools]
    if required_failures:
        print("\nSetup is incomplete. Revisit SETUP.md for the missing required items.")
        return 1

    print(
        "\nINFO: desktop-app - Codex and Claude Code app installs cannot be "
        "verified here. On macOS/Windows, open the app on this repository folder "
        "and run one test prompt (see examples/codex-app/ or examples/claude-app/)."
    )
    print("\nSetup check complete. Optional agent tools may still need sign-in.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
