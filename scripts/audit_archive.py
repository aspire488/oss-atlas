#!/usr/bin/env python3
"""Audit the external-OSS archive against GitHub's current authored PR state."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "contributions" / "ALL_PR_HISTORY.md"
INDEX = ROOT / "data" / "contributions.json"
TOKEN = os.environ.get("GITHUB_TOKEN")

if not TOKEN:
    print("GITHUB_TOKEN is required", file=sys.stderr)
    raise SystemExit(2)

API = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "oss-atlas-audit",
}


def get(path: str, params: dict[str, str] | None = None):
    url = API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def archive_links() -> set[str]:
    text = ARCHIVE.read_text(encoding="utf-8")
    return {
        f"https://github.com/{owner}/{repo}/pull/{number}"
        for owner, repo, number in re.findall(
            r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)", text
        )
        if owner != "aspire488"
    }


def github_links() -> tuple[set[str], dict[str, str]]:
    items = get(
        "/search/issues",
        {"q": "is:pr author:aspire488", "per_page": "100"},
    ).get("items", {})

    links: set[str] = set()
    states: dict[str, str] = {}
    for item in items:
        url = item.get("html_url", "")
        match = re.match(
            r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)$", url
        )
        if not match:
            continue
        owner = match.group(1)
        if owner == "aspire488":
            continue

        merged_at = item.get("pull_request", {}).get("merged_at")
        status = "merged" if merged_at else item.get("state", "unknown")
        links.add(url)
        states[url] = status

    return links, states


archive = archive_links()
indexed = {
    item["url"]
    for item in json.loads(INDEX.read_text(encoding="utf-8"))["contributions"]
}

if archive != indexed:
    print("Archive/index mismatch.")
    print("Missing from machine index:", sorted(archive - indexed))
    print("Not in archive:", sorted(indexed - archive))
    raise SystemExit(1)

current, states = github_links()

if current != archive:
    print("OSS contribution drift detected.")
    print("New/missing GitHub PRs:", sorted(current ^ archive))
    print("Refresh the archive and machine index intentionally.")
    raise SystemExit(1)

counts = {
    "merged": sum(value == "merged" for value in states.values()),
    "open": sum(value == "open" for value in states.values()),
    "closed": sum(value == "closed" for value in states.values()),
}

snapshot = json.loads(INDEX.read_text(encoding="utf-8"))
indexed_counts = snapshot["counts"]

if counts["merged"] != indexed_counts["merged"]:
    print(f"Merged-state drift: GitHub={counts['merged']} index={indexed_counts['merged']}")
    raise SystemExit(1)

if counts["open"] != indexed_counts["open_upstream"] + indexed_counts["open_fork"]:
    print(
        "Open-state drift: "
        f"GitHub={counts['open']} "
        f"index={indexed_counts['open_upstream'] + indexed_counts['open_fork']}"
    )
    raise SystemExit(1)

if counts["closed"] != indexed_counts["closed"]:
    print(f"Closed-state drift: GitHub={counts['closed']} index={indexed_counts['closed']}")
    raise SystemExit(1)

print(
    "External OSS audit OK: "
    f"{len(current)} PRs; merged={counts['merged']}, "
    f"open={counts['open']}, closed={counts['closed']}."
)
