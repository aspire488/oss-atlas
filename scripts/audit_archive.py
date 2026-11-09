#!/usr/bin/env python3
"""Audit the external-OSS archive against GitHub's current authored PR state."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

from atlas_github import ApiError, fetch_authored_prs, make_get

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "contributions" / "ALL_PR_HISTORY.md"
INDEX = ROOT / "data" / "contributions.json"
TOKEN = os.environ.get("GITHUB_TOKEN")

if not TOKEN:
    print("GITHUB_TOKEN is required", file=sys.stderr)
    raise SystemExit(2)


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
    try:
        items = fetch_authored_prs(make_get(TOKEN))
    except ApiError as exc:
        # Exit 2 = could not audit (API problem); exit 1 is reserved for real drift.
        print(exc, file=sys.stderr)
        raise SystemExit(2)

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

expected_status = {item["url"]: item["status"] for item in json.loads(INDEX.read_text(encoding="utf-8"))["contributions"]}
actual_status = {url: ("merged" if state == "merged" else "open_upstream" if state == "open" and "/aspire488/" not in url else "open_fork" if state == "open" else "closed") for url, state in states.items()}

drift = False
if current != archive:
    drift = True
    print("OSS contribution drift detected.")
    print("On GitHub but not in archive:", sorted(current - archive))
    print("In archive but not on GitHub:", sorted(archive - current))

if actual_status != expected_status:
    drift = True
    print("Per-contribution status drift detected.")
    for url in sorted(set(actual_status) | set(expected_status)):
        if actual_status.get(url) != expected_status.get(url):
            print(f"  {url}: GitHub={actual_status.get(url)} index={expected_status.get(url)}")

if drift:
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
