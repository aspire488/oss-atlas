# OSS Atlas Data

Machine-readable artifacts are version-controlled alongside the human-facing Atlas.

## Files

### `contributions.json`
Canonical external-OSS contribution inventory.

### `skills.json`
Evidence-derived engineering skill categories. These are not proficiency scores or rankings; every category points to concrete PR evidence.

### `reviews.json`
Selected formal GitHub review-submission metadata for significant contributions. It records review states and observation dates without treating review activity as an acceptance prediction.

## Invariants

- URLs and contribution IDs are unique.
- Self-owned repositories are excluded from the external OSS inventory.
- Skill evidence resolves to contributions in `contributions.json`.
- Counts are derived from entries and validated in CI.
- Review metadata is explicitly dated and scoped.

Future schema additions should remain backwards-readable where practical.
