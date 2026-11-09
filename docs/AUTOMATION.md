# OSS Atlas Automation

OSS Atlas uses GitHub Actions as a verification layer rather than an automatic history editor.

## Workflows

### Atlas CI
`.github/workflows/ci.yml`

Runs on pushes and pull requests to `main`, plus manual dispatch.

Checks:

- required Atlas files exist
- internal Markdown links resolve
- the external OSS archive still matches the dated snapshot
- unit tests for the ledger-refresh tooling pass (`tests/`, stdlib `unittest`)
- self-owned `aspire488/*` repositories are excluded from the external OSS count

### OSS Atlas Audit
`.github/workflows/atlas-audit.yml`

Runs daily and manually.

Its job is to detect drift between the repository's recorded OSS state and GitHub's current authored-PR state.

### Ledger Refresh
`.github/workflows/ledger-refresh.yml`

Runs daily at 02:17 UTC (before the audit) and manually. It runs `scripts/refresh_ledger.py`, then `validate_atlas.py` and `audit_archive.py` on the result, and if the ledger changed it pushes an `automation/ledger-refresh-<run id>` branch and opens a pull request. It never pushes to `main`. If a refresh PR is already open it does nothing, so merge or close it first.

What the refresh changes: new authored PRs (entries with API-derived fields only, no editorial notes), status moves between merged/open/closed, index counts, `observed_at`, the counts table and refresh date in `ALL_PR_HISTORY.md`, and the README counts and snapshot date. It never rewrites editorial prose: a summary or archive note is regenerated only when it is empty or exactly the kind of text the script generates; otherwise it is kept and reported as "Needs editorial review". Run it locally with `GITHUB_TOKEN=... python scripts/refresh_ledger.py --dry-run`.

Guarantees: all-or-nothing (any API error, rate limit longer than 90 s, incomplete or mismatched results exits 2 before anything is written); idempotent (a second run with no upstream change writes nothing, and `observed_at` only moves when entries change); a ledger PR that GitHub no longer returns exits 3 and is never deleted automatically.

Trade-offs and setup:

- Pull requests created with `GITHUB_TOKEN` do not trigger other workflows, so CI does not start on the refresh PR. The job already ran validation and the audit on the same tree; close and reopen the PR to run Atlas CI. A personal access token or GitHub App would remove this limitation at the cost of a stored secret, which this repository avoids.
- The repository setting Settings > Actions > General > "Allow GitHub Actions to create and approve pull requests" must be enabled. Without it the branch is pushed but PR creation fails with a visible error.

## Why the audit is read-only

The Atlas should not silently rewrite its own history based on a scheduled job. A detected state change should produce a visible failure, after which the record can be intentionally refreshed and reviewed.

The audit stays read-only. The refresh workflow is the intentional, reviewable path: it proposes the change as a pull request, so a human approves every ledger update. This preserves historical provenance.

## Security model

Workflows use `contents: read` and do not require a personal access token. The built-in GitHub token is used only for read-only API access.

Third-party actions are kept to the standard checkout/setup actions, and workflow permissions are explicitly restricted.

## Future automation

1. Generate machine-readable contribution metadata.
2. ~~Detect newly merged/open/closed external PRs.~~ (done: Ledger Refresh)
3. ~~Generate dated snapshots as reviewed pull requests.~~ (done: Ledger Refresh)
4. Validate case-study links against source PRs.
5. Add stale-record detection.
6. Add an evidence-derived contribution dashboard.

Automation should detect and surface drift before it attempts to modify the ledger.
