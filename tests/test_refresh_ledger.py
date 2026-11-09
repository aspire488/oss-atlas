"""Tests for scripts/refresh_ledger.py and scripts/atlas_github.py (stdlib unittest, fake GitHub)."""

import io
import json
import sys
import tempfile
import unittest
import urllib.error
from email.message import Message
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import atlas_github  # noqa: E402
import refresh_ledger as rl  # noqa: E402

BASE = "https://github.com"
A, B, C = f"{BASE}/o/r/pull/1", f"{BASE}/o/r/pull/2", f"{BASE}/o/r/pull/3"
NEW = f"{BASE}/x/y/pull/9"

ARCHIVE = """# Complete External OSS PR History

> Based on GitHub state refreshed on November 1, 2026.

| Status | Count |
|---|---:|
| Merged upstream | 1 |
| Open upstream | 1 |
| Open fork-side | 0 |
| Closed without merge | 1 |
| **External OSS PRs** | **3** |

## Merged upstream
- [o/r #1 — merged one]({A}) — merged 2026-10-01; maintainer confirmed.

## Open upstream
- [o/r #2 — open one]({B}) — opened 2026-10-02; CI pending, reviewer asked for a test.

## Open fork-side OSS work

None.

## Closed without merge
- [o/r #3 — closed one]({C}) — closed without merge on 2026-10-03.

## Status rules
""".format(A=A, B=B, C=C)

README = """<img src="https://img.shields.io/badge/RECORDS-3-171715?style=flat-square" alt="3 tracked records">
<strong><sub>EXTERNAL PRs</sub></strong><br>
<strong><samp>3</samp></strong>
<strong><sub>MERGED UPSTREAM</sub></strong><br>
<strong><samp>1</samp></strong>
<strong><sub>OPEN UPSTREAM</sub></strong><br>
<strong><samp>1</samp></strong>
<strong><sub>CLOSED</sub></strong><br>
<strong><samp>1</samp></strong>
<sub>LEDGER SNAPSHOT · 01 NOVEMBER 2026 · EXCLUDED</sub>
"""


def entry(url, status, summary):
    owner, repo, num = url.split("/")[3], url.split("/")[4], int(url.split("/")[6])
    return {"id": f"{owner}/{repo}#{num}", "title": f"{owner}/{repo} #{num} — t", "url": url, "owner": owner,
            "repository": repo, "pr": num, "status": status, "summary": summary, "source": "github"}


INDEX = {
    "schema_version": "1.0", "generated_from": "x", "observed_at": "2026-11-01", "scope": "s",
    "counts": {"total": 3, "merged": 1, "open_upstream": 1, "open_fork": 0, "closed": 1},
    "contributions": [entry(A, "merged", "merged 2026-10-01"),
                      entry(B, "open_upstream", "opened 2026-10-02; CI pending"),
                      entry(C, "closed", "closed without merge; state verified 2026-10-27")],
}


def item(url, title="t", state="open", merged=None, created="2026-10-02T00:00:00Z", closed=None, draft=False):
    return {"html_url": url, "title": title, "state": state, "draft": draft, "created_at": created,
            "closed_at": closed, "pull_request": {"merged_at": merged}}


BASE_ITEMS = [item(A, state="closed", merged="2026-10-01T00:00:00Z", closed="2026-10-01T00:00:00Z"),
              item(B), item(C, state="closed", closed="2026-10-03T00:00:00Z")]


def fake_get(items, per_page=100, **overrides):
    def get(path, params=None):
        page = int(params["page"])
        data = {"total_count": len(items), "incomplete_results": False,
                "items": items[(page - 1) * per_page: page * per_page]}
        data.update(overrides)
        return data
    return get


class RefreshTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        for rel, text in ((rl.INDEX, json.dumps(INDEX, indent=2, ensure_ascii=False) + "\n"),
                          (rl.ARCHIVE, ARCHIVE), (rl.README, README)):
            (self.root / rel).parent.mkdir(parents=True, exist_ok=True)
            (self.root / rel).write_bytes(text.encode())
        self.addCleanup(self._tmp.cleanup)

    def snapshot(self):
        return {p: (self.root / p).read_bytes() for p in (rl.INDEX, rl.ARCHIVE, rl.README)}

    def run_refresh(self, items, today="2026-11-09", **kw):
        return rl.refresh(self.root, fake_get(items), today, **kw)

    def index(self):
        return json.loads((self.root / rl.INDEX).read_text("utf-8"))

    def test_current_ledger_is_a_noop(self):
        before = self.snapshot()
        self.assertEqual(self.run_refresh(BASE_ITEMS), ["Ledger already current."])
        self.assertEqual(self.snapshot(), before)

    def test_new_pr(self):
        self.run_refresh(BASE_ITEMS + [item(NEW, title="Fix thing", draft=True, created="2026-11-08T10:00:00Z")])
        idx = self.index()
        self.assertEqual(idx["contributions"][-1], {
            "id": "x/y#9", "title": "x/y #9 — Fix thing", "url": NEW, "owner": "x", "repository": "y", "pr": 9,
            "status": "open_upstream", "summary": "opened 2026-11-08; draft", "source": "github"})
        self.assertEqual(idx["counts"], {"total": 4, "merged": 1, "open_upstream": 2, "open_fork": 0, "closed": 1})
        self.assertEqual(idx["observed_at"], "2026-11-09")
        archive = (self.root / rl.ARCHIVE).read_text("utf-8")
        self.assertIn(f"- [x/y #9 — Fix thing]({NEW}) — opened 2026-11-08; draft.\n\n## Open fork-side", archive)
        self.assertIn("| Open upstream | 2 |", archive)
        self.assertIn("| **External OSS PRs** | **4** |", archive)
        self.assertIn("refreshed on November 9, 2026.", archive)
        readme = (self.root / rl.README).read_text("utf-8")
        self.assertIn("RECORDS-4-", readme)
        self.assertIn("LEDGER SNAPSHOT · 09 NOVEMBER 2026", readme)

    def test_self_owned_prs_are_ignored(self):
        self.run_refresh(BASE_ITEMS + [item(f"{BASE}/aspire488/own/pull/1")])
        self.assertEqual(self.index()["counts"]["total"], 3)

    def test_pr_merged_keeps_editorial_prose_and_flags_it(self):
        report = self.run_refresh([BASE_ITEMS[0], item(B, state="closed", merged="2026-11-05T00:00:00Z"), BASE_ITEMS[2]])
        moved = next(e for e in self.index()["contributions"] if e["url"] == B)
        self.assertEqual(moved["status"], "merged")
        self.assertEqual(moved["summary"], "opened 2026-10-02; CI pending")  # editorial: untouched
        self.assertIn(f"Needs editorial review (prose kept as written): {B}", report)
        archive = (self.root / rl.ARCHIVE).read_text("utf-8")
        merged = archive.split("## Merged upstream")[1].split("## Open upstream")[0]
        self.assertIn(f"[o/r #2 — open one]({B}) — opened 2026-10-02; CI pending, reviewer asked for a test.", merged)
        self.assertNotIn(B, archive.split("## Open upstream")[1].split("## Open fork-side")[0])
        self.assertIn("| Merged upstream | 2 |", archive)

    def test_pr_merged_regenerates_auto_prose(self):
        idx = json.loads(json.dumps(INDEX))
        idx["contributions"][1]["summary"] = ""
        (self.root / rl.INDEX).write_text(json.dumps(idx, indent=2, ensure_ascii=False) + "\n", "utf-8")
        (self.root / rl.ARCHIVE).write_text(ARCHIVE.replace("; CI pending, reviewer asked for a test", ""), "utf-8")
        self.run_refresh([BASE_ITEMS[0], item(B, state="closed", merged="2026-11-05T00:00:00Z"), BASE_ITEMS[2]])
        self.assertEqual(next(e for e in self.index()["contributions"] if e["url"] == B)["summary"], "merged 2026-11-05")
        self.assertIn(f"({B}) — merged 2026-11-05.", (self.root / rl.ARCHIVE).read_text("utf-8"))

    def test_pr_closed(self):
        self.run_refresh([BASE_ITEMS[0], item(B, state="closed", closed="2026-11-06T00:00:00Z"), BASE_ITEMS[2]])
        idx = self.index()
        self.assertEqual(next(e for e in idx["contributions"] if e["url"] == B)["status"], "closed")
        self.assertEqual(idx["counts"]["closed"], 2)
        closed = (self.root / rl.ARCHIVE).read_text("utf-8").split("## Closed without merge")[1]
        self.assertIn(B, closed)

    def test_missing_pr_refuses_without_writing(self):
        before = self.snapshot()
        with self.assertRaises(rl.Refusal) as ctx:
            self.run_refresh(BASE_ITEMS[:2] + [item(NEW)])
        self.assertEqual(ctx.exception.code, 3)
        self.assertIn(C, str(ctx.exception))
        self.assertIn(NEW, str(ctx.exception))
        self.assertEqual(self.snapshot(), before)

    def test_api_problems_write_nothing(self):
        before = self.snapshot()
        items = BASE_ITEMS + [item(NEW)]

        def boom(path, params=None):
            raise atlas_github.ApiError("HTTP 500")

        for get in (boom,
                    fake_get(items, incomplete_results=True),
                    fake_get(items, total_count=len(items) + 1),
                    fake_get(items + [item(NEW)])):  # duplicate PR across pages
            with self.assertRaises(atlas_github.ApiError):
                rl.refresh(self.root, get, "2026-11-09")
            self.assertEqual(self.snapshot(), before)

    def test_pagination(self):
        many = BASE_ITEMS + [item(f"{BASE}/x/y/pull/{n}") for n in range(10, 15)]
        self.assertEqual(len(atlas_github.fetch_authored_prs(fake_get(many, per_page=2))), 8)

    def test_second_run_is_byte_identical(self):
        items = [BASE_ITEMS[0], item(B, state="closed", merged="2026-11-05T00:00:00Z"), BASE_ITEMS[2],
                 item(NEW, created="2026-11-08T10:00:00Z")]
        self.run_refresh(items)
        after_first = self.snapshot()
        self.assertEqual(self.run_refresh(items, today="2026-11-10"), ["Ledger already current."])
        self.assertEqual(self.snapshot(), after_first)

    def test_dry_run_writes_nothing(self):
        before = self.snapshot()
        report = self.run_refresh(BASE_ITEMS + [item(NEW)], dry_run=True)
        self.assertTrue(report[-1].startswith("Would update"))
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(sorted(p.name for p in self.root.rglob("*.tmp")), [])

    def test_crlf_files_stay_crlf(self):
        for rel in (rl.ARCHIVE, rl.README):
            path = self.root / rel
            path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.run_refresh(BASE_ITEMS + [item(NEW)])
        for rel in (rl.ARCHIVE, rl.README):
            data = (self.root / rel).read_bytes()
            self.assertEqual(data.count(b"\n"), data.count(b"\r\n"))


class HttpRetryTest(unittest.TestCase):
    def error(self, code, **headers):
        msg = Message()
        for key, value in headers.items():
            msg[key.replace("_", "-")] = value
        return urllib.error.HTTPError("u", code, "x", msg, io.BytesIO(b"{}"))

    def getter(self, outcomes, sleeps):
        outcomes = iter(outcomes)

        def opener(request, timeout):
            outcome = next(outcomes)
            if isinstance(outcome, Exception):
                raise outcome
            return io.BytesIO(json.dumps(outcome).encode())

        return atlas_github.make_get("t", opener=opener, sleep=sleeps.append, now=lambda: 1000.0)

    def test_retry_after_is_honoured(self):
        sleeps = []
        get = self.getter([self.error(429, Retry_After="3"), {"ok": 1}], sleeps)
        self.assertEqual(get("/x"), {"ok": 1})
        self.assertEqual(sleeps, [3.0])

    def test_ratelimit_reset_is_honoured_when_short(self):
        sleeps = []
        get = self.getter([self.error(403, x_ratelimit_remaining="0", x_ratelimit_reset="1010"), {"ok": 1}], sleeps)
        self.assertEqual(get("/x"), {"ok": 1})
        self.assertEqual(sleeps, [11.0])

    def test_long_wait_fails_instead_of_sleeping(self):
        sleeps = []
        get = self.getter([self.error(403, x_ratelimit_remaining="0", x_ratelimit_reset="9999")], sleeps)
        with self.assertRaises(atlas_github.ApiError):
            get("/x")
        self.assertEqual(sleeps, [])

    def test_plain_403_and_404_fail_immediately(self):
        for code in (403, 404):
            get = self.getter([self.error(code)], [])
            with self.assertRaises(atlas_github.ApiError):
                get("/x")

    def test_gives_up_after_bounded_attempts(self):
        sleeps = []
        get = self.getter([self.error(503) for _ in range(3)], sleeps)
        with self.assertRaises(atlas_github.ApiError):
            get("/x")
        self.assertEqual(len(sleeps), 2)


if __name__ == "__main__":
    unittest.main()
