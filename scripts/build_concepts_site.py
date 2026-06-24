#!/usr/bin/env python3
"""Split agentic_coding_concepts_guide.md into VitePress pages with per-tool tabs."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "followup" / "agentic_coding_concepts_guide.md"
OUT = ROOT / "website" / "docs" / "concepts" / "_generated"
PAGES = ROOT / "website" / "docs" / "concepts"
SIDEBAR_JSON = ROOT / "website" / ".vitepress" / "concepts-sidebar.json"

TOPIC_HEADING = re.compile(r"^## (\d+)\. (.+)$", re.MULTILINE)
PLAYBOOK_HEADING = re.compile(r"^### (\d+)\. (.+)$", re.MULTILINE)
EXAMPLE_MARKERS = (
    ("codex", re.compile(r"^\*\*Codex\b", re.MULTILINE)),
    ("claude", re.compile(r"^\*\*Claude Code\b", re.MULTILINE)),
    ("cursor", re.compile(r"^\*\*Cursor\b", re.MULTILINE)),
)


def slugify(num: str, title: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f"{int(num):02d}-{base}"[:72].rstrip("-")


def split_at_heading(text: str, heading: str) -> tuple[str, str]:
    marker = f"### {heading}"
    idx = text.find(marker)
    if idx == -1:
        return text.strip(), ""
    before = text[:idx].strip()
    after = text[idx + len(marker) :].strip()
    return before, after


def split_examples_block(block: str) -> dict[str, str]:
    empty = {key: "" for key, _ in EXAMPLE_MARKERS}
    if not block.strip():
        return empty

    matches: list[tuple[int, str]] = []
    for key, pattern in EXAMPLE_MARKERS:
        m = pattern.search(block)
        if m:
            matches.append((m.start(), key))

    if not matches:
        empty["codex"] = block.strip()
        return empty

    matches.sort(key=lambda x: x[0])
    sections = dict(empty)
    for i, (start, key) in enumerate(matches):
        end = matches[i + 1][0] if i + 1 < len(matches) else len(block)
        body = block[start:end].strip()
        body = re.sub(r"^\*\*[^*]+\*\*\.?\s*", "", body, count=1).strip()
        sections[key] = body
    return sections


def parse_topics(main: str) -> list[dict]:
    matches = list(TOPIC_HEADING.finditer(main))
    topics: list[dict] = []
    for i, m in enumerate(matches):
        num, title = m.group(1), m.group(2).strip()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(main)
        body = main[m.end() : end].strip()
        shared, rest = split_at_heading(body, "Tool documentation")
        tool_docs, examples_block = split_at_heading(rest, "Examples by tool")
        examples = split_examples_block(examples_block)
        topics.append(
            {
                "num": int(num),
                "title": title,
                "slug": slugify(num, title),
                "shared": shared,
                "tool_docs": tool_docs,
                "examples": examples,
            }
        )
    return topics


def parse_playbook(playbook: str) -> list[dict]:
    matches = list(PLAYBOOK_HEADING.finditer(playbook))
    items: list[dict] = []
    for i, m in enumerate(matches):
        num, title = m.group(1), m.group(2).strip()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(playbook)
        body = playbook[m.end() : end].strip()
        items.append(
            {
                "num": int(num),
                "title": title,
                "slug": slugify(num, title),
                "body": body,
            }
        )
    return items


def write_slice(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = content.strip()
    if not text:
        text = "_No content in this section for the source guide._"
    path.write_text(text + "\n", encoding="utf-8")


def topic_page_frontmatter(
    topic: dict, *, prev_link: str | None, next_link: str | None
) -> str:
    lines = [
        "---",
        f'title: "{topic["num"]}. {topic["title"]}"',
    ]
    if prev_link:
        lines.append(f"prev: {prev_link}")
    if next_link:
        lines.append(f"next: {next_link}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def render_topic_page(
    topic: dict, *, prev_link: str | None, next_link: str | None
) -> str:
    slug = topic["slug"]
    fm = topic_page_frontmatter(topic, prev_link=prev_link, next_link=next_link)
    return (
        fm
        + f"# {topic['num']}. {topic['title']}\n\n"
        + f"<!--@include: ./_generated/{slug}/shared.md-->\n\n"
        + "## Tool documentation\n\n"
        + f"<!--@include: ./_generated/{slug}/tool-docs.md-->\n\n"
        + "## Examples by tool\n\n"
        + "Choose **Codex**, **Claude Code**, or **Cursor**. Your choice is remembered in this browser.\n\n"
        + "<ConceptToolTabs>\n\n"
        + "<template #codex>\n\n"
        + f"<!--@include: ./_generated/{slug}/codex.md-->\n\n"
        + "</template>\n\n"
        + "<template #claude>\n\n"
        + f"<!--@include: ./_generated/{slug}/claude.md-->\n\n"
        + "</template>\n\n"
        + "<template #cursor>\n\n"
        + f"<!--@include: ./_generated/{slug}/cursor.md-->\n\n"
        + "</template>\n\n"
        + "</ConceptToolTabs>\n"
    )


def main() -> None:
    if not GUIDE.is_file():
        raise SystemExit(f"Guide not found: {GUIDE}")

    raw = GUIDE.read_text(encoding="utf-8")
    intro_end = TOPIC_HEADING.search(raw)
    if not intro_end:
        raise SystemExit("No numbered topics found in guide")

    intro = raw[: intro_end.start()].strip()
    intro = re.sub(r"^#\s+.+\n+", "", intro, count=1).strip()

    playbook_start = raw.find("## Implementation Playbook By Topic")
    resources_start = raw.find("## Web Resources Checked")
    if playbook_start == -1 or resources_start == -1:
        raise SystemExit("Guide missing playbook or resources section")

    main_body = raw[intro_end.start() : playbook_start].strip()
    playbook_body = raw[playbook_start:resources_start].strip()
    playbook_body = re.sub(
        r"^## Implementation Playbook By Topic\s*",
        "",
        playbook_body,
        count=1,
    ).strip()
    resources_body = raw[resources_start:].strip()
    resources_body = re.sub(
        r"^## Web Resources Checked\s*",
        "",
        resources_body,
        count=1,
    ).strip()

    topics = parse_topics(main_body)
    playbook = parse_playbook(playbook_body)

    OUT.mkdir(parents=True, exist_ok=True)
    PAGES.mkdir(parents=True, exist_ok=True)

    for topic in topics:
        slug = topic["slug"]
        topic_dir = OUT / slug
        write_slice(topic_dir / "shared.md", topic["shared"])
        write_slice(topic_dir / "tool-docs.md", topic["tool_docs"])
        for track in ("codex", "claude", "cursor"):
            write_slice(topic_dir / f"{track}.md", topic["examples"].get(track, ""))

    nav_topics = [{"num": t["num"], "title": t["title"], "slug": t["slug"]} for t in topics]
    nav_playbook = [{"num": p["num"], "title": p["title"], "slug": p["slug"]} for p in playbook]

    sidebar = [
        {"text": "Concept guide home", "link": "/concepts/"},
        {
            "text": "Concepts (1–19)",
            "collapsed": False,
            "items": [
                {"text": f'{t["num"]}. {t["title"]}', "link": f'/concepts/{t["slug"]}'}
                for t in nav_topics
            ],
        },
        {
            "text": "Implementation playbook",
            "collapsed": False,
            "items": [
                {"text": "Playbook overview", "link": "/concepts/playbook"},
                *[
                    {
                        "text": f'{p["num"]}. {p["title"]}',
                        "link": f'/concepts/playbook/{p["slug"]}',
                    }
                    for p in nav_playbook
                ],
            ],
        },
        {"text": "Web resources", "link": "/concepts/resources"},
    ]
    SIDEBAR_JSON.write_text(json.dumps(sidebar, indent=2) + "\n", encoding="utf-8")

    write_slice(OUT / "intro.md", intro)
    write_slice(OUT / "resources.md", resources_body)

    for item in playbook:
        write_slice(OUT / "playbook" / f"{item['slug']}.md", item["body"])

    topic_links = [f'/concepts/{t["slug"]}' for t in topics]
    for i, topic in enumerate(topics):
        prev_link = "/concepts/" if i == 0 else topic_links[i - 1]
        next_link = topic_links[i + 1] if i + 1 < len(topics) else "/concepts/playbook/"
        page_path = PAGES / f'{topic["slug"]}.md'
        page_path.write_text(
            render_topic_page(
                topic,
                prev_link=prev_link,
                next_link=next_link,
            ),
            encoding="utf-8",
        )

    (PAGES / "index.md").write_text(
        "---\ntitle: Concept guide\nnext: /concepts/01-agentic-coding\n---\n\n"
        "# Agentic Coding For Economists\n\n"
        "<!--@include: ./_generated/intro.md-->\n\n"
        "## Topics\n\n"
        + "\n".join(
            f'- [{t["num"]}. {t["title"]}](/concepts/{t["slug"]})' for t in topics
        )
        + "\n\n"
        "## Also on this site\n\n"
        "- [Implementation playbook](/concepts/playbook/) — step-by-step setup per concept\n"
        "- [Web resources](/concepts/resources) — official docs checked for this guide\n",
        encoding="utf-8",
    )

    playbook_links = [f'/concepts/playbook/{p["slug"]}' for p in playbook]
    for i, item in enumerate(playbook):
        prev_link = "/concepts/playbook" if i == 0 else playbook_links[i - 1]
        next_link = (
            playbook_links[i + 1] if i + 1 < len(playbook) else "/concepts/resources"
        )
        fm_lines = [
            "---",
            f'title: "Playbook — {item["num"]}. {item["title"]}"',
            f"prev: {prev_link}",
            f"next: {next_link}",
            "---",
            "",
            f"# {item['num']}. {item['title']}",
            "",
            f"<!--@include: ./_generated/playbook/{item['slug']}.md-->",
            "",
        ]
        pb_page = PAGES / "playbook" / f'{item["slug"]}.md'
        pb_page.parent.mkdir(parents=True, exist_ok=True)
        pb_page.write_text("\n".join(fm_lines), encoding="utf-8")

    (PAGES / "playbook" / "index.md").write_text(
        "---\ntitle: Implementation playbook\nprev: /concepts/19-seven-day-adoption-pattern\nnext: /concepts/playbook/01-agentic-coding\n---\n\n"
        "# Implementation Playbook By Topic\n\n"
        "This section adds implementation guidance, examples, and online resources for each concept. "
        "Prefer the official docs linked in each page when tool UI names differ from this guide.\n\n"
        + "\n".join(
            f'- [{p["num"]}. {p["title"]}](/concepts/playbook/{p["slug"]})'
            for p in playbook
        )
        + "\n",
        encoding="utf-8",
    )

    (PAGES / "resources.md").write_text(
        "---\ntitle: Web resources\nprev: /concepts/playbook/19-seven-day-adoption-pattern\n---\n\n"
        "# Web Resources Checked\n\n"
        "<!--@include: ./_generated/resources.md-->\n",
        encoding="utf-8",
    )

    print(f"Wrote {len(topics)} concept pages and {len(playbook)} playbook pages to {PAGES}")


if __name__ == "__main__":
    main()
