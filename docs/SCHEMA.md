# OSS Atlas Data Model

## Contribution

`id` = `owner/repository#pr`

A contribution has identity, lifecycle status, provenance, source URL, observation date, and optional summary.

### Lifecycle

- `merged` — GitHub reports a merge.
- `open_upstream` — open PR outside `aspire488/*`.
- `open_fork` — open PR inside an `aspire488/*` fork.
- `closed` — closed without a merge.

## Review record

A review record contains:

- PR identity
- source URL
- observation date
- number of formal review submissions
- state counts
- latest formal state

It deliberately does not infer approval, merge probability, or contributor quality from review activity.

## Evidence graph

```text
GitHub PR
   │
   ├── contribution record
   │      ├── status
   │      ├── source
   │      └── evidence
   │
   ├── review timeline
   │
   ├── case study
   │
   ├── research note
   │
   └── learning
```

A downstream artifact must never create a stronger status claim than its source evidence.

## Future extensions

- review comments and threads
- commit fingerprints
- changed-file fingerprints
- validation runs
- issue relationships
- contribution-to-learning edges
- generated historical snapshots
