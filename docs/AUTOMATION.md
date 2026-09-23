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
- self-owned `aspire488/*` repositories are excluded from the external OSS count

### OSS Atlas Audit
`.github/workflows/atlas-audit.yml`

Runs daily and manually.

Its job is to detect drift between the repository's recorded OSS state and GitHub's current authored-PR state.

## Why the audit is read-only

The Atlas should not silently rewrite its own history based on a scheduled job. A detected state change should produce a visible failure, after which the record can be intentionally refreshed and reviewed.

This preserves historical provenance.

## Security model

Workflows use `contents: read` and do not require a personal access token. The built-in GitHub token is used only for read-only API access.

Third-party actions are kept to the standard checkout/setup actions, and workflow permissions are explicitly restricted.

## Future automation

1. Generate machine-readable contribution metadata.
2. Detect newly merged/open/closed external PRs.
3. Generate dated snapshots as reviewed pull requests.
4. Validate case-study links against source PRs.
5. Add stale-record detection.
6. Add an evidence-derived contribution dashboard.

Automation should detect and surface drift before it attempts to modify the ledger.
