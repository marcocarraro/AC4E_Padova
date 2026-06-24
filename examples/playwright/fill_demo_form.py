#!/usr/bin/env python3
"""Fill the local LSE workshop form with Playwright."""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import expect, sync_playwright


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "outputs"


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://localhost:8000", wait_until="networkidle")

        page.get_by_role("button", name="Start").click()
        page.get_by_label("Project title").fill("Job market paper robustness workflow")
        page.get_by_label("Field").select_option("Applied microeconomics")
        page.get_by_label("Referee-style review").check()
        page.get_by_label("Browser automation").check()
        page.get_by_role("button", name="Next").click()

        page.get_by_label("Review target").fill("Introduction and main results table")
        page.get_by_label("Data sensitivity").select_option("Confidential data excluded")
        page.get_by_label("Notes for agent").fill(
            "Do not inspect raw data. Focus on claims, tables, and reproducibility notes."
        )
        page.get_by_role("button", name="Submit request").click()

        heading = page.get_by_role("heading", name="Workshop request received")
        expect(heading).to_be_visible()

        screenshot_path = OUTPUT_DIR / "playwright-confirmation.png"
        page.screenshot(path=str(screenshot_path), full_page=True)
        confirmation = heading.text_content()

        browser.close()

    print(f"Saved screenshot to {screenshot_path}")
    print(f"Confirmation: {confirmation}")


if __name__ == "__main__":
    main()

