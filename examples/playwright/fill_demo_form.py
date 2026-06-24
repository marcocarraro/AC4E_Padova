#!/usr/bin/env python3
"""Fill the local public-data evidence form with Playwright."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable
from urllib.error import URLError
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[2]
WEB_FORM_DIR = ROOT / "examples" / "web-form"
DEFAULT_OUTPUT = ROOT / "outputs" / "playwright_form_evidence.md"
DEFAULT_SCREENSHOT = ROOT / "outputs" / "playwright_confirmation.png"


@dataclass(frozen=True)
class Evidence:
    """Structured evidence captured from the local form."""

    base_url: str
    confirmation: str
    output_path: Path
    screenshot_path: Path | None


def wait_for_server(url: str, timeout_seconds: float = 8.0) -> None:
    """Wait until the local HTTP server returns a response."""

    deadline = time.monotonic() + timeout_seconds
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        try:
            with urlopen(url, timeout=1):
                return
        except URLError as exc:
            last_error = exc
            time.sleep(0.2)
    raise RuntimeError(f"Timed out waiting for {url}: {last_error}")


def start_server(host: str, port: int) -> subprocess.Popen[str]:
    """Start a local static server for the form."""

    command = [
        sys.executable,
        "-m",
        "http.server",
        str(port),
        "--bind",
        host,
        "--directory",
        str(WEB_FORM_DIR),
    ]
    return subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def stop_server(process: subprocess.Popen[str] | None) -> None:
    """Terminate the local server started by this script."""

    if process is None or process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=3)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=3)


def display_path(path: Path) -> str:
    """Return a repo-relative path when possible."""

    candidate = path if path.is_absolute() else ROOT / path
    try:
        return candidate.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def build_evidence_note(evidence: Evidence) -> str:
    """Render the data-source-map evidence note."""

    screenshot = (
        display_path(evidence.screenshot_path)
        if evidence.screenshot_path is not None
        else "not captured"
    )
    output = display_path(evidence.output_path)
    row = (
        "| Card-Krueger public source metadata (Playwright evidence) "
        "| <https://davidcard.berkeley.edu/data_sets.html> "
        "| Public source page, documented through local form automation "
        "| source URL, readme URL, access note, evidence path "
        f"| Evidence: `{output}`; screenshot: `{screenshot}` |"
    )
    return "\n".join(
        [
            "# Playwright Form Evidence",
            "",
            f"Date captured: {date.today().isoformat()}",
            f"Local form URL: {evidence.base_url}",
            f"Confirmation text: {evidence.confirmation}",
            f"Screenshot: `{screenshot}`",
            "",
            "## Data Source Map Row",
            "",
            "Copy this row into a project `docs/data_source_map.md` when the",
            "evidence belongs to that project.",
            "",
            "| Source | URL / path | Access | Variables | Notes |",
            "| --- | --- | --- | --- | --- |",
            row,
            "",
            "## Human Review",
            "",
            "- Confirm the URL is public.",
            "- Confirm the row does not imply the local form downloaded data.",
            "- Confirm any research claim remains tied to the documented source.",
        ]
    )


def write_evidence(evidence: Evidence) -> None:
    """Write the evidence note to disk."""

    evidence.output_path.parent.mkdir(parents=True, exist_ok=True)
    evidence.output_path.write_text(build_evidence_note(evidence) + "\n", encoding="utf-8")


def run_playwright(
    base_url: str,
    output_path: Path,
    screenshot_path: Path | None,
    headed: bool,
) -> Evidence:
    """Fill the local form and capture evidence."""

    try:
        from playwright.sync_api import expect, sync_playwright
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Playwright Python package is not installed. Run "
            "`python3 -m pip install -r requirements.txt` and "
            "`python3 -m playwright install chromium`, then retry."
        ) from exc

    if screenshot_path is not None:
        screenshot_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not headed)
        page = browser.new_page()
        page.goto(base_url, wait_until="domcontentloaded")

        page.get_by_role("button", name="Start").click()
        page.get_by_label("Source title").fill("Card-Krueger public data page")
        page.get_by_label("URL or path").fill("https://davidcard.berkeley.edu/data_sets.html")
        page.get_by_label("Access type").select_option("Public source page")
        page.get_by_label("Variables or fields").fill(
            "study page URL, data readme URL, access note"
        )
        page.get_by_label("Use in data source map").check()
        page.get_by_role("button", name="Next").click()

        page.get_by_label("Project").select_option("Card-Krueger teaching example")
        page.get_by_label("Data sensitivity").select_option("Public metadata only")
        page.get_by_label("Evidence note").fill(
            "Record a source-map row; do not download or redistribute raw data."
        )
        page.get_by_role("button", name="Submit evidence").click()

        heading = page.get_by_role("heading", name="Evidence request received")
        expect(heading).to_be_visible()
        expect(page.get_by_text("Card-Krueger public data page")).to_be_visible()

        if screenshot_path is not None:
            page.screenshot(path=str(screenshot_path), full_page=True)
        confirmation = page.get_by_test_id("confirmation-detail").text_content() or ""
        browser.close()

    evidence = Evidence(
        base_url=base_url,
        confirmation=confirmation,
        output_path=output_path,
        screenshot_path=screenshot_path,
    )
    write_evidence(evidence)
    return evidence


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", help="Host for the local server.")
    parser.add_argument("--port", type=int, default=8000, help="Port for the local server.")
    parser.add_argument(
        "--base-url",
        default=None,
        help="Existing form URL. Defaults to http://HOST:PORT.",
    )
    parser.add_argument(
        "--no-server",
        action="store_true",
        help="Use an already-running form server instead of starting one.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Markdown evidence file to write.",
    )
    parser.add_argument(
        "--screenshot",
        type=Path,
        default=DEFAULT_SCREENSHOT,
        help="Screenshot path. Use --no-screenshot to skip.",
    )
    parser.add_argument(
        "--no-screenshot",
        action="store_true",
        help="Do not capture a screenshot.",
    )
    parser.add_argument("--headed", action="store_true", help="Show the browser window.")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> None:
    args = parse_args(argv)
    base_url = args.base_url or f"http://{args.host}:{args.port}"
    server: subprocess.Popen[str] | None = None
    screenshot_path = None if args.no_screenshot else args.screenshot

    try:
        if not args.no_server:
            server = start_server(args.host, args.port)
        wait_for_server(base_url)
        evidence = run_playwright(
            base_url=base_url,
            output_path=args.output,
            screenshot_path=screenshot_path,
            headed=args.headed,
        )
    finally:
        stop_server(server)

    print(f"Saved evidence to {evidence.output_path}")
    if evidence.screenshot_path is not None:
        print(f"Saved screenshot to {evidence.screenshot_path}")
    print(f"Confirmation: {evidence.confirmation}")


if __name__ == "__main__":
    main()
