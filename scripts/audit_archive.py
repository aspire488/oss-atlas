#!/usr/bin/env python3
"""Audit the external-OSS PR archive against GitHub's current PR state."""

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


archive = ARCHIVE.read_text(encoding="utf-8")
links = re.findall(r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)", archive)
external_links = {(owner, repo, int(number)) for owner, repo, number in links if owner != "aspire488"}

if len(external_links) != 32:
    print(f"Archive currently contains {len(external_links)} unique external OSS PR links; expected 32.")
    raise SystemExit(1)

items = get("/search/issues", {"q": "is:pr author:aspire488", "per_page": "100"}).get("items", [])
external = []
for item in items:
    url = item.get("html_url", "")
    match = re.match(r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)$", url)
    if not match:
        continue
    owner, repo, number = match.groups()
    if owner == "aspire488":
        continue
    external.append((owner, repo, int(number), item.get("state"), item.get("pull_request", {}).get("merged_at")))

counts = {"merged": 0, "open": 0, "closed": 0}
for owner, repo, number, state, merged_at in external:
    if merged_at:
        counts["merged"] += 1
    elif state == "open":
        counts["open"] += 1
    else:
        counts["closed"] += 1

expected = {"merged": 3, "open": 24, "closed": 5}
if counts != expected:
    print(f"GitHub external OSS state: {counts}")
    print(f"Archive snapshot expects:   {expected}")
    print("Refresh the dated snapshot/archive before merging a status-changing change.")
    raise SystemExit(1)

print(f"External OSS archive audit OK: {len(external)} PRs; {counts}.")
