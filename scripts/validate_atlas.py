#!/usr/bin/env python3
"""Validate OSS Atlas structure, metadata, and internal Markdown links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)[[^\]]+]\(([^)]+)\)")


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
    "docs/AUTOMATION.md",
    "templates/CONTRIBUTION_RECORD.md",
    "data/contributions.json",
    "data/skills.json",
    "data/reviews.json",
]

missing = [path for path in required if not (ROOT / path).is_file()]
if missing:
    fail("missing required files: " + ", ".join(missing))

try:
    index = json.loads((ROOT / "data/contributions.json").read_text(encoding="utf-8"))
    skills = json.loads((ROOT / "data/skills.json").read_text(encoding="utf-8"))
except json.JSONDecodeError as exc:
    fail(f"invalid JSON metadata: {exc}")

if index.get("schema_version") != "1.0":
    fail("unsupported contributions schema version")

items = index.get("contributions", [])
ids = [item.get("id") for item in items]
urls = [item.get("url") for item in items]

if len(items) != len(set(ids)) or len(items) != len(set(urls)):
    fail("contribution IDs and URLs must be unique")

if any(item.get("owner") == "aspire488" for item in items):
    fail("self-owned repositories must not enter the external OSS index")

expected_counts = {
    "total": len(items),
    "merged": sum(item.get("status") == "merged" for item in items),
    "open_upstream": sum(item.get("status") == "open_upstream" for item in items),
    "open_fork": sum(item.get("status") == "open_fork" for item in items),
    "closed": sum(item.get("status") == "closed" for item in items),
}
if index.get("counts") != expected_counts:
    fail(f"metadata counts do not match entries: {index.get('counts')} != {expected_counts}")

if not isinstance(skills.get("skills"), list) or not skills["skills"]:
    fail("skill map must contain at least one skill")

try:
    reviews = json.loads((ROOT / "data/reviews.json").read_text(encoding="utf-8"))
except json.JSONDecodeError as exc:
    fail(f"invalid review metadata: {exc}")
for record in reviews.get("reviews", []):
    if not record.get("pr") or not record.get("url"):
        fail("review records require pr and url")

indexed_urls = set(urls)
for skill in skills["skills"]:
    for evidence in skill.get("evidence", []):
        owner, rest = evidence.split("/", 1)
        repo, number = rest.rsplit("#", 1)
        url = f"https://github.com/{owner}/{repo}/pull/{number}"
        if url not in indexed_urls:
            fail(f"skill evidence is not in contribution index: {evidence}")

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
print(f"Machine-readable contributions OK: {len(items)} entries.")
print(f"Evidence-derived skills OK: {len(skills['skills'])} categories.")
print("Internal Markdown links OK.")
