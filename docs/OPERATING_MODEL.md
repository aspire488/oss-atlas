# OSS Atlas Operating Model

OSS Atlas is a factual, continuously maintained record of open-source engineering work.

## 1. Source hierarchy

Use evidence in this order:

1. Upstream GitHub repository, PR, issue, commit, release, or discussion
2. Maintainer/reviewer feedback
3. Verified local test/build output
4. Author notes and interpretation

Primary evidence wins when sources disagree.

## 2. Status discipline

- **Merged** only when GitHub reports a merge.
- **Open** only when GitHub reports the PR open.
- **Closed without merge** when GitHub reports closed with no merge timestamp.
- **Fork-side** must be explicitly labelled.
- Do not infer acceptance from silence, comments, CI, or review activity.

## 3. Verification discipline

Record the exact scope of validation:

- command or test suite
- environment when material
- result
- known gaps

Never turn a targeted run into a full-suite claim.

## 4. Record hierarchy

Use the repository layers consistently:

`contributions/` → contribution lifecycle  
`research/` → investigations, reviews, discussions  
`case-studies/` → deep narratives  
`learnings/` → reusable lessons  
`stats/` → dated snapshots  
`templates/` → repeatable record format

## 5. Highlighting rule

Featured items are selected for recency, upstream relevance, technical substance, review depth, or reusable lessons.

They are **not rankings** and do not receive quality scores.

## 6. Update loop

When an upstream artifact changes state:

1. Refresh the contribution record/index.
2. Refresh the current status snapshot when the change is material.
3. Update the case study if the contribution is significant.
4. Add a learning when the work exposes a durable pattern.
5. Keep the exhaustive archive intact.

## 7. Historical integrity

Do not rewrite history to make outcomes look cleaner.

Closed, superseded, rejected, and fork-side work can remain valuable evidence of iteration and learning.

## 8. Scope boundary

OSS Atlas contains OSS engineering work only. Personal product development, KIO, AURA, UEA, portfolio design, and unrelated system work belong elsewhere unless they are directly relevant to an OSS contribution being documented.

## 9. Core principle

> **Evidence density over activity-count inflation.**
