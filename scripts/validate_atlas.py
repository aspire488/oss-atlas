#!/usr/bin/env python3
"""Validate OSS Atlas structure and internal Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


required = [
    "README.md",
    "contributions/INDEX.md",
    "contributions/ALL_PR_HISTORY.md",
    "contributions/merged/README.md",
    "contributions/open/README.md",
    "contributions/closed/README.md",
    "case-studies/README.md",
    "research/README.md",
    "learnings/README.md",
    "stats/2026-09-23.md",
    "docs/OPERATING_MODEL.md",
    "docs/ROADMAP.md",
    "templates/CONTRIBUTION_RECORD.md",
]

missing = [path for path in required if not (ROOT / path).is_file()]
if missing:
    fail("missing required files: " + ", ".join(missing))

errors: list[str] = []
for markdown in ROOT.rglob("*.md"):
    text = markdown.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        target = target.strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        candidate = (markdown.parent / target).resolve()
        if not candidate.is_file():
            errors.append(f"{markdown.relative_to(ROOT)} -> {target}")

if errors:
    for error in errors:
        print(f"BROKEN LINK: {error}")
    raise SystemExit(1)

print(f"Atlas structure OK: {len(required)} required files present.")
print("Internal Markdown links OK.")
