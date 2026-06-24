#!/usr/bin/env python3
"""Split workshop materials into shared + per-track slices for the VitePress site."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATERIALS = ROOT / "materials"
OUT = ROOT / "website" / "docs" / "modules" / "_generated"

TRACK_SLUGS = ("codex-cli", "codex-app", "claude-cli", "claude-app", "cursor")

MODULES = [
    ("01-foundations", "module_01_foundations.md", ["## Tool Notes"]),
    ("02-hooks-goals", "module_02_hooks_goals.md", ["### Codex CLI"]),
    ("03-referee-review", "module_03_referee_review.md", ["## Tool Notes"]),
    ("04-playwright", "module_04_playwright.md", ["## Tool Notes"]),
    ("05-capstone", "module_05_capstone.md", []),
]

# Map repo-relative markdown links to VitePress routes (cleanUrls, no .html).
_TEMPLATE_ANCHORS = {
    "AGENTS_economics.md": "agents-economics",
    "skill_referee_checklist.md": "referee-checklist",
    "long_running_goal_prompt.md": "long-running-goal",
    "referee_report.md": "referee-report",
    "review_log.md": "review-log",
    "research_design_memo.md": "research-design-memo",
    "project_brief.md": "project-brief",
    "data_source_map.md": "data-source-map",
    "response_to_referees.md": "response-to-referees",
    "prompts_research_article.md": "prompts-research-article",
    "app_track_quickstart.md": "app-track-quickstart",
}


def rewrite_links_for_vitepress(text: str) -> str:
    """Turn materials/ docs/ examples/ links into site routes."""
    text = re.sub(r"\]\(\.\./docs/research_article_harness\.md\)", "](/harness)", text)
    text = re.sub(r"\]\(docs/research_article_harness\.md\)", "](/harness)", text)
    text = re.sub(r"\]\(\.\./docs/sources\.md\)", "](/sources)", text)
    text = re.sub(r"\]\(docs/sources\.md\)", "](/sources)", text)
    text = re.sub(r"\]\(\.\./docs/inspiration_notes\.md\)", "](/sources)", text)
    text = re.sub(r"\]\(\.\./examples/starter_article/?\)", "](/starter-article)", text)
    text = re.sub(r"\]\(examples/starter_article/?\)", "](/starter-article)", text)
    text = re.sub(r"\]\(\.\./examples/codex/README\.md\)", "](/examples#codex-cli-a1)", text)
    text = re.sub(r"\]\(\.\./examples/codex/\)", "](/examples#codex-cli-a1)", text)
    text = re.sub(r"\]\(\.\./examples/codex-app/README\.md\)", "](/examples#codex-app-a2)", text)
    text = re.sub(r"\]\(\.\./examples/claude/README\.md\)", "](/examples#claude-cli-b1)", text)
    text = re.sub(r"\]\(\.\./examples/claude/\)", "](/examples#claude-cli-b1)", text)
    text = re.sub(r"\]\(\.\./examples/claude-app/README\.md\)", "](/examples#claude-app-b2)", text)
    text = re.sub(r"\]\(\.\./examples/cursor/README\.md\)", "](/examples#cursor-c)", text)
    text = re.sub(r"\]\(\.\./examples/cursor/\)", "](/examples#cursor-c)", text)
    text = re.sub(
        r"\]\(\.\./examples/paper/working_paper_excerpt\.md\)",
        "](/examples#sample-paper)",
        text,
    )
    text = re.sub(r"\]\(\.\./examples/hooks/README\.md\)", "](/examples#hooks-codex)", text)
    text = re.sub(r"\]\(\.\./examples/PROVENANCE\.md\)", "](/examples#provenance)", text)
    text = re.sub(r"\]\(\.\./examples/plugins/README\.md\)", "](/examples#plugins)", text)
    text = re.sub(
        r"\]\(\.\./materials/tool_tracks\.md\)|\]\(materials/tool_tracks\.md\)|\]\(tool_tracks\.md\)",
        "](/tracks)",
        text,
    )

    def _template_link(match: re.Match[str]) -> str:
        filename = match.group(1)
        anchor = _TEMPLATE_ANCHORS.get(filename, filename.replace(".md", "").lower())
        return f"](/templates#{anchor})"

    text = re.sub(r"\]\(\.\./templates/([^)]+)\)", _template_link, text)
    text = re.sub(r"\]\(templates/([^)]+)\)", _template_link, text)
    return text


TRACK_HEADINGS = {
    "codex-cli": re.compile(r"^### Codex CLI\s*$", re.MULTILINE),
    "codex-app": re.compile(r"^### Codex app\s*$", re.MULTILINE),
    "claude-cli": re.compile(r"^### Claude Code CLI\s*$", re.MULTILINE),
    "claude-app": re.compile(r"^### Claude Code app\s*$", re.MULTILINE),
    "cursor": re.compile(r"^### Cursor\s*$", re.MULTILINE),
}


def strip_leading_title(text: str, *, strip_time: bool = True) -> str:
    """Remove leading # title and optional 'Time:' line for page-level includes."""
    lines = text.splitlines()
    start = 0
    if lines and lines[start].startswith("# "):
        start += 1
    while start < len(lines) and not lines[start].strip():
        start += 1
    if strip_time and start < len(lines) and re.match(r"^time:", lines[start], re.I):
        start += 1
    while start < len(lines) and not lines[start].strip():
        start += 1
    return "\n".join(lines[start:]).strip() + "\n"


def split_at_first_anchor(text: str, anchors: list[str]) -> tuple[str, str | None]:
    """Return (shared, remainder). Remainder is None if no anchor matched."""
    positions = []
    for anchor in anchors:
        idx = text.find(anchor)
        if idx != -1:
            positions.append((idx, anchor))
    if not positions:
        return text.strip(), None
    idx, _ = min(positions, key=lambda x: x[0])
    return text[:idx].strip(), text[idx:].strip()


def extract_track_sections(remainder: str) -> dict[str, str]:
    """Parse ### headings into per-lane bodies."""
    empty = {slug: "" for slug in TRACK_SLUGS}
    if not remainder:
        return empty

    matches: list[tuple[int, str, str]] = []
    for track, pattern in TRACK_HEADINGS.items():
        for m in pattern.finditer(remainder):
            matches.append((m.start(), track, m.group(0)))

    if not matches:
        empty["codex-cli"] = remainder.strip()
        return empty

    matches.sort(key=lambda x: x[0])
    sections: dict[str, str] = {slug: "" for slug in TRACK_SLUGS}
    for i, (start, track, heading) in enumerate(matches):
        end = matches[i + 1][0] if i + 1 < len(matches) else len(remainder)
        body = remainder[start:end].strip()
        body = re.sub(rf"^{re.escape(heading)}\s*", "", body, count=1).strip()
        sections[track] = body

    return sections


def split_tool_tracks(text: str) -> dict[str, str]:
    """Split tool_tracks.md by Track A1/A2/B1/B2/C."""
    markers = [
        ("codex-cli", "## Track A1: Codex CLI"),
        ("codex-app", "## Track A2: Codex app"),
        ("claude-cli", "## Track B1: Claude Code CLI"),
        ("claude-app", "## Track B2: Claude Code app"),
        ("cursor", "## Track C: Cursor"),
    ]
    tracks: dict[str, str] = {}
    for i, (key, marker) in enumerate(markers):
        start = text.find(marker)
        if start == -1:
            tracks[key] = ""
            continue
        start += len(marker)
        end = len(text)
        if i + 1 < len(markers):
            next_idx = text.find(markers[i + 1][1], start)
            if next_idx != -1:
                end = next_idx
        tracks[key] = text[start:end].strip()
    return tracks


def capstone_track_notes() -> dict[str, str]:
    return {
        "codex-cli": (
            "Pick one workflow from the shared capstone. Use `/goal` or a checkpointed "
            "prompt with `templates/long_running_goal_prompt.md`. Save outputs under "
            "`outputs/` and verify with `/diff`. Resume with `codex resume --last` if needed."
        ),
        "codex-app": (
            "Pick one workflow from the shared capstone. Use `/goal` or the goal UI in a "
            "Codex desktop thread with `templates/long_running_goal_prompt.md`. Save under "
            "`outputs/` and review with `/diff` before accepting edits."
        ),
        "claude-cli": (
            "Pick one workflow from the shared capstone. Use checkpointed prompts and "
            "`claude --continue` after each step. Use `/agents` if the task needs a "
            "separate reviewer subagent."
        ),
        "claude-app": (
            "Pick one workflow from the shared capstone. Use checkpoints in one Code-tab "
            "session—do not rely on CLI resume. Use `/agents` or the slash menu for "
            "referee-reviewer when needed."
        ),
        "cursor": (
            "Pick one workflow from the shared capstone. Use foreground Agent with "
            "checkpoints, or a background agent on a branch for isolated drafts. "
            "Review the diff before merging any branch work."
        ),
    }


def playwright_track_notes() -> dict[str, str]:
    return {
        "codex-cli": (
            "Run the shared Playwright steps in your terminal. Ask Codex CLI to edit "
            "`examples/playwright/fill_demo_form.py` and run it. Use `/diff` before "
            "accepting script changes."
        ),
        "codex-app": (
            "Run the server and Playwright commands from a system or embedded terminal. "
            "Use the Codex app thread to edit and run `fill_demo_form.py`; review with `/diff`."
        ),
        "claude-cli": (
            "Run the shared Playwright steps from the Claude Code CLI terminal. "
            "Use the same Python script; Claude can help adapt the TypeScript spec."
        ),
        "claude-app": (
            "Run Playwright from an external or integrated terminal. Use the Code tab "
            "to edit the script; keep the committed Playwright file as the artifact."
        ),
        "cursor": (
            "Run the shared Playwright steps from the integrated terminal. "
            "Optional: use Cursor browser or browser MCP if installed—the workshop "
            "artifact remains the committed Playwright script."
        ),
    }


def write_module(slug: str, source: str, anchors: list[str]) -> None:
    text = (MATERIALS / source).read_text(encoding="utf-8")
    shared, remainder = split_at_first_anchor(text, anchors)

    if slug == "05-capstone":
        sections = capstone_track_notes()
    elif slug == "04-playwright":
        extracted = extract_track_sections(remainder or "")
        sections = playwright_track_notes()
        for key in TRACK_SLUGS:
            if extracted.get(key, "").strip():
                sections[key] = extracted[key].strip()
    else:
        sections = extract_track_sections(remainder or "")

    mod_dir = OUT / slug
    mod_dir.mkdir(parents=True, exist_ok=True)
    (mod_dir / "shared.md").write_text(
        rewrite_links_for_vitepress(strip_leading_title(shared)), encoding="utf-8"
    )
    for track in TRACK_SLUGS:
        body = sections.get(track, "").strip()
        if not body:
            body = (
                "_No tool-specific section in the source module. "
                "Use the [Track plan](/tracks) for your lane._"
            )
        else:
            body = rewrite_links_for_vitepress(body)
        (mod_dir / f"{track}.md").write_text(body + "\n", encoding="utf-8")


def remove_stale_track_files() -> None:
    """Drop legacy codex.md / claude.md slices from the three-tab layout."""
    stale_names = {"codex.md", "claude.md"}
    for subdir in OUT.iterdir():
        if not subdir.is_dir():
            continue
        for name in stale_names:
            path = subdir / name
            if path.is_file():
                path.unlink()
    tracks_dir = OUT / "tracks"
    if tracks_dir.is_dir():
        for name in stale_names:
            path = tracks_dir / name
            if path.is_file():
                path.unlink()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, source, anchors in MODULES:
        write_module(slug, source, anchors)
    remove_stale_track_files()

    tracks_text = (MATERIALS / "tool_tracks.md").read_text(encoding="utf-8")
    intro_end = tracks_text.find("## Track A1: Codex CLI")
    intro = tracks_text[:intro_end].strip() if intro_end != -1 else tracks_text.strip()
    tracks_dir = OUT / "tracks"
    tracks_dir.mkdir(parents=True, exist_ok=True)
    (tracks_dir / "intro.md").write_text(
        rewrite_links_for_vitepress(strip_leading_title(intro, strip_time=False)),
        encoding="utf-8",
    )

    for track, body in split_tool_tracks(tracks_text).items():
        (tracks_dir / f"{track}.md").write_text(
            rewrite_links_for_vitepress(body) + "\n", encoding="utf-8"
        )

    harness_src = (ROOT / "docs" / "research_article_harness.md").read_text(encoding="utf-8")
    harness_out = OUT.parent.parent / "_generated"
    harness_out.mkdir(parents=True, exist_ok=True)
    (harness_out / "harness_body.md").write_text(
        rewrite_links_for_vitepress(harness_src), encoding="utf-8"
    )

    print(f"Wrote generated site content to {OUT}")


if __name__ == "__main__":
    main()
