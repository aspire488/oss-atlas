#!/usr/bin/env python3
"""Refresh the external-OSS ledger from GitHub's authored-PR state.

Updates only API-derived data: entry status (and auto-generated summaries), new entries,
index counts, and the derived counts/dates in ALL_PR_HISTORY.md and README.md. Editorial
prose is never rewritten. All outputs are computed and cross-checked in memory first; on
any problem nothing is written.

Exit codes: 0 ok (changed or already current), 1 internal consistency failure,
2 GitHub API problem / no token, 3 ledger PRs that GitHub no longer returns.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from atlas_github import ApiError, fetch_authored_prs, make_get

ROOT = Path(__file__).resolve().parents[1]
OWN = "aspire488"
INDEX = "data/contributions.json"
ARCHIVE = "contributions/ALL_PR_HISTORY.md"
README = "README.md"
SECTIONS = {"merged": "Merged upstream", "open_upstream": "Open upstream", "closed": "Closed without merge"}
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
# Prose this script itself generates; anything else is editorial and is kept verbatim.
AUTO = re.compile(
    r"^(|opened \d{4}-\d\d-\d\d(; draft)?|merged( upstream)? \d{4}-\d\d-\d\d"
    r"|closed without merge( on \d{4}-\d\d-\d\d)?(\s*\(state (verified|observed) \d{4}-\d\d-\d\d\))?"
    r"|closed without merge; state verified \d{4}-\d\d-\d\d)\.?$"
)
PR_URL = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/pull/(\d+)$")
BULLET = re.compile(r"^(- \[.*\]\(\S+\))(?: — (.*))?$")


class Refusal(Exception):
    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code = code


def load_prs(items: list[dict]) -> dict[str, dict]:
    """Authored external PRs keyed by URL, with the API-derived fields we track."""
    prs = {}
    for item in items:
        match = PR_URL.match(item.get("html_url", ""))
        if not match or match.group(1) == OWN:
            continue
        merged_at = (item.get("pull_request") or {}).get("merged_at")
        status = "merged" if merged_at else "open_upstream" if item["state"] == "open" else "closed"
        stamp = merged_at if status == "merged" else item.get("created_at") if status == "open_upstream" else item.get("closed_at")
        prs[item["html_url"]] = {
            "owner": match.group(1), "repository": match.group(2), "pr": int(match.group(3)),
            "title": item["title"], "status": status, "draft": bool(item.get("draft")),
            "date": (stamp or "")[:10],
        }
    return prs


def prose(pr: dict, today: str) -> tuple[str, str]:
    """(index summary, archive note) generated for a PR's current state."""
    if pr["status"] == "merged":
        return f"merged {pr['date']}", f"merged {pr['date']}."
    if pr["status"] == "open_upstream":
        note = f"opened {pr['date']}" + ("; draft" if pr["draft"] else "")
        return note, note + "."
    return f"closed without merge; state verified {today}", f"closed without merge on {pr['date']}."


def plan(index: dict, prs: dict[str, dict], today: str):
    """Return (new index, added urls, status moves, urls whose prose was kept). Refusal(3) on missing PRs."""
    known = {entry["url"] for entry in index["contributions"]}
    missing = sorted(known - set(prs))
    if missing:
        extra = sorted(set(prs) - known)
        raise Refusal(3, "In the ledger but not returned by GitHub (renamed, transferred, deleted or "
                         "re-authored?); resolve by hand: " + ", ".join(missing)
                         + (f" | also new on GitHub: {', '.join(extra)}" if extra else ""))
    new_index = json.loads(json.dumps(index))
    added, moved, kept = [], [], []
    for entry in new_index["contributions"]:
        pr = prs[entry["url"]]
        if entry["status"] != pr["status"]:
            moved.append((entry["url"], entry["status"], pr["status"]))
            entry["status"] = pr["status"]
            if AUTO.match(entry["summary"]):
                entry["summary"] = prose(pr, today)[0]
            else:
                kept.append(entry["url"])
    for url in sorted(set(prs) - known):
        pr = prs[url]
        added.append(url)
        new_index["contributions"].append({
            "id": f"{pr['owner']}/{pr['repository']}#{pr['pr']}",
            "title": f"{pr['owner']}/{pr['repository']} #{pr['pr']} — {pr['title']}",
            "url": url, "owner": pr["owner"], "repository": pr["repository"], "pr": pr["pr"],
            "status": pr["status"], "summary": prose(pr, today)[0], "source": "github",
        })
    return new_index, added, moved, kept


def counts_of(entries: list[dict]) -> dict[str, int]:
    def count(status: str) -> int:
        return sum(e["status"] == status for e in entries)

    return {"total": len(entries), "merged": count("merged"), "open_upstream": count("open_upstream"),
            "open_fork": count("open_fork"), "closed": count("closed")}


def sub_once(pattern: str, repl: str, text: str, what: str) -> str:
    new, n = re.subn(pattern, repl, text)
    if n != 1:
        raise Refusal(1, f"{what}: expected exactly one match, found {n}")
    return new


def pretty(today: str, fmt: str) -> str:
    y, m, d = (int(x) for x in today.split("-"))
    return fmt.format(y=y, m=MONTHS[m - 1], d=d)


def add_line(lines: list[str], status: str, line: str) -> None:
    """Append after the last bullet of the status' section."""
    start = lines.index(f"## {SECTIONS[status]}")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    last = max((i for i in range(start + 1, end) if lines[i].startswith("- [")), default=None)
    if last is None:  # section was emptied by earlier moves
        lines[start + 1:start + 1] = ["", line]
    else:
        lines.insert(last + 1, line)


def update_archive(text: str, prs: dict, new_index: dict, added, moved, today: str, changed: bool) -> str:
    lines = text.split("\n")
    for url, _, new_status in moved:
        i = next((i for i, l in enumerate(lines) if l.startswith("- [") and f"]({url})" in l), None)
        if i is None:
            raise Refusal(1, f"archive has no line for {url}")
        match = BULLET.match(lines.pop(i))
        rest = match.group(2) or ""
        if AUTO.match(rest):
            rest = prose(prs[url], today)[1]
        add_line(lines, new_status, match.group(1) + (f" — {rest}" if rest else ""))
    for url in added:
        pr = prs[url]
        add_line(lines, pr["status"],
                 f"- [{pr['owner']}/{pr['repository']} #{pr['pr']} — {pr['title']}]({url}) — {prose(pr, today)[1]}")
    text = "\n".join(lines)
    c = counts_of(new_index["contributions"])
    for label, key in (("Merged upstream", "merged"), ("Open upstream", "open_upstream"),
                       ("Open fork-side", "open_fork"), ("Closed without merge", "closed")):
        text = sub_once(rf"(\| {label} \| )\d+( \|)", rf"\g<1>{c[key]}\g<2>", text, f"archive row {label}")
    text = sub_once(r"(\| \*\*External OSS PRs\*\* \| \*\*)\d+(\*\* \|)", rf"\g<1>{c['total']}\g<2>", text, "archive total")
    if changed:
        text = sub_once(r"refreshed on [A-Z][a-z]+ \d{1,2}, \d{4}\.", pretty(today, "refreshed on {m} {d}, {y}."), text, "archive date")
    return text


def update_readme(text: str, c: dict[str, int], today: str, changed: bool) -> str:
    text = sub_once(r"(badge/RECORDS-)\d+(-)", rf"\g<1>{c['total']}\g<2>", text, "README badge")
    text = sub_once(r'alt="\d+ tracked records"', f'alt="{c["total"]} tracked records"', text, "README alt")
    for label, key in (("EXTERNAL PRs", "total"), ("MERGED UPSTREAM", "merged"),
                       ("OPEN UPSTREAM", "open_upstream"), ("CLOSED", "closed")):
        text = sub_once(rf"(<sub>{label}</sub></strong><br>\s*<strong><samp>)\d+(</samp>)",
                        rf"\g<1>{c[key]}\g<2>", text, f"README {label}")
    if changed:
        text = sub_once(r"LEDGER SNAPSHOT · \d\d [A-Z]+ \d{4}",
                        pretty(today, "LEDGER SNAPSHOT · {d:02d} {m} {y}").upper(), text, "README date")
    return text


def check(index: dict, archive: str, prs: dict) -> None:
    """The invariants audit_archive.py / validate_atlas.py enforce, checked before anything is written."""
    entries = index["contributions"]
    if index["counts"] != counts_of(entries):
        raise Refusal(1, "index counts do not match entries")
    section, seen = None, []
    for line in archive.split("\n"):
        if line.startswith("## "):
            section = line[3:]
        m = re.match(r"^- \[.*?\]\((https://github\.com/(?!aspire488/)[^)]*/pull/\d+)\)", line)
        if m:
            seen.append(m.group(1))
            if m.group(1) in prs and SECTIONS[prs[m.group(1)]["status"]] != section:
                raise Refusal(1, f"{m.group(1)} is listed under '{section}' but is {prs[m.group(1)]['status']}")
    if sorted(seen) != sorted(prs) or sorted(e["url"] for e in entries) != sorted(prs):
        raise Refusal(1, "archive links / index entries / GitHub PRs disagree after refresh")


def read(path: Path) -> tuple[str, str]:
    raw = path.read_bytes().decode("utf-8")
    return raw.replace("\r\n", "\n"), "\r\n" if "\r\n" in raw else "\n"


def write_atomic(path: Path, text: str, newline: str) -> None:
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(text.replace("\n", newline).encode("utf-8"))
    os.replace(tmp, path)


def refresh(root: Path, get, today: str, dry_run: bool = False) -> list[str]:
    """Returns report lines. Raises Refusal / ApiError before any file is touched."""
    prs = load_prs(fetch_authored_prs(get))
    (index_text, index_nl), (archive_text, archive_nl), (readme_text, readme_nl) = (
        read(root / INDEX), read(root / ARCHIVE), read(root / README))
    new_index, added, moved, kept = plan(json.loads(index_text), prs, today)
    changed = bool(added or moved)
    new_index["counts"] = counts_of(new_index["contributions"])
    if changed:
        new_index["observed_at"] = today
    new_archive = update_archive(archive_text, prs, new_index, added, moved, today, changed)
    new_readme = update_readme(readme_text, new_index["counts"], today, changed)
    check(new_index, new_archive, prs)

    report = [f"New: {u} ({prs[u]['status']})" for u in added]
    report += [f"Status: {u} {a} -> {b}" for u, a, b in moved]
    report += [f"Needs editorial review (prose kept as written): {u}" for u in kept]
    outputs = ((INDEX, index_text, json.dumps(new_index, indent=2, ensure_ascii=False) + "\n", index_nl),
               (ARCHIVE, archive_text, new_archive, archive_nl), (README, readme_text, new_readme, readme_nl))
    todo = [(root / p, new, nl) for p, old, new, nl in outputs if old != new]
    if not dry_run:
        for path, text, nl in todo:
            write_atomic(path, text, nl)
    if todo:
        report.append(("Would update " if dry_run else "Updated ") + f"{len(todo)} file(s): " + ", ".join(p.name for p, _, _ in todo))
    else:
        report.append("Ledger already current.")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--dry-run", action="store_true", help="report changes without writing")
    args = parser.parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN is required", file=sys.stderr)
        return 2
    try:
        today = datetime.now(timezone.utc).date().isoformat()
        print("\n".join(refresh(ROOT, make_get(token), today, args.dry_run)))
    except ApiError as exc:
        print(f"{exc}\nNothing was written.", file=sys.stderr)
        return 2
    except Refusal as exc:
        print(f"{exc}\nNothing was written.", file=sys.stderr)
        return exc.code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
