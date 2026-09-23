# OSS Atlas Data

Machine-readable artifacts are version-controlled alongside the human-facing Atlas.

## Files

### `contributions.json`

Canonical contribution inventory.

Schema:
- `schema_version`
- `generated_from`
- `observed_at`
- `scope`
- `counts`
- `contributions[]`

Each contribution includes:
- stable `id`
- upstream owner/repository
- PR number
- GitHub URL
- lifecycle status
- optional summary
- source

### `skills.json`

Evidence-derived skill categories. These are not proficiency scores or rankings. Each category points back to concrete PR evidence.

## Invariants

- URLs are unique.
- Contribution IDs are unique.
- Self-owned repositories are excluded from the external OSS inventory.
- Skill evidence must resolve to a contribution in `contributions.json`.
- Counts are derived from entries and validated in CI.

Future schema additions should remain backwards-readable where practical.
