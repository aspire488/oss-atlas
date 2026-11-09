"""Shared, fail-loud GitHub access for the Atlas scripts (audit and refresh)."""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
SEARCH = "is:pr author:aspire488"
MAX_WAIT = 90  # seconds we are willing to sleep for a rate limit before failing


class ApiError(Exception):
    """The GitHub data could not be read completely; callers must not act on it."""


def _retry_delay(exc: urllib.error.HTTPError, attempt: int, now) -> float | None:
    """Seconds to wait before retrying, or None if this error is not retryable."""
    headers = exc.headers
    if exc.code in (403, 429):
        if headers.get("Retry-After", "").isdigit():
            return float(headers["Retry-After"])
        if headers.get("x-ratelimit-remaining") == "0" and headers.get("x-ratelimit-reset", "").isdigit():
            return max(0.0, float(headers["x-ratelimit-reset"]) - now()) + 1
        return None  # plain 403/429 without rate-limit headers: permission problem
    if exc.code in (500, 502, 503, 504):
        return 2.0 * (attempt + 1)
    return None


def make_get(token, *, opener=urllib.request.urlopen, sleep=time.sleep, now=time.time, attempts=3):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "oss-atlas",
    }

    def get(path: str, params: dict[str, str] | None = None):
        url = API + path + ("?" + urllib.parse.urlencode(params) if params else "")
        for attempt in range(attempts):
            try:
                with opener(urllib.request.Request(url, headers=headers), timeout=30) as response:
                    return json.load(response)
            except urllib.error.HTTPError as exc:
                wait = _retry_delay(exc, attempt, now)
                body = exc.read()[:300]
                exc.close()
                if wait is not None and wait <= MAX_WAIT and attempt < attempts - 1:
                    print(f"GitHub API {exc.code} for {path}; retrying in {wait:.0f}s.", file=sys.stderr)
                    sleep(wait)
                    continue
                raise ApiError(
                    f"GitHub API error {exc.code} for {path}: {body!r} "
                    f"(x-ratelimit-remaining={exc.headers.get('x-ratelimit-remaining')})"
                ) from exc
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                raise ApiError(f"GitHub API request failed for {path}: {exc!r}") from exc
        raise ApiError(f"GitHub API gave up on {path}")  # pragma: no cover

    return get


def fetch_authored_prs(get) -> list[dict]:
    """Every authored PR from the Search API, or ApiError if the set is not provably complete."""
    items: list[dict] = []
    total = None
    for page in range(1, 11):  # Search API serves at most 1000 results.
        data = get("/search/issues", {"q": SEARCH, "per_page": "100", "page": str(page)})
        if data.get("incomplete_results") or "items" not in data:
            raise ApiError(f"GitHub search returned incomplete data on page {page}.")
        total = data["total_count"]
        items += data["items"]
        if len(items) >= total or not data["items"]:
            break
    if len(items) != total:
        raise ApiError(f"Fetched {len(items)} of {total} authored PRs.")
    urls = [item.get("html_url") for item in items]
    if len(set(urls)) != len(urls):
        raise ApiError("GitHub search returned duplicate PRs (results shifted between pages).")
    return items
