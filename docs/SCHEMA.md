# OSS Atlas Data Model

## Contribution

`id` = `owner/repository#pr`

A contribution has:

- identity
- lifecycle status
- provenance
- source URL
- observation date
- optional summary

### Lifecycle

`merged`  
GitHub reports a merge.

`open_upstream`  
Open PR against a repository outside `aspire488/*`.

`open_fork`  
Open PR in an `aspire488/*` fork.

`closed`  
Closed without a merge.

## Evidence graph

The intended graph is:

```text
GitHub PR
   │
   ├── contribution record
   │      ├── status
   │      ├── source
   │      └── evidence
   │
   ├── case study
   │
   ├── research note
   │
   └── learning
```

A downstream artifact must never create a stronger status claim than its source evidence.

## Future extensions

- review events
- maintainer feedback
- commits
- changed-file fingerprints
- validation runs
- issue relationships
- contribution-to-learning edges
