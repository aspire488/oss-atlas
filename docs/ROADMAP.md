# OSS Atlas Roadmap

## Phase 1 — Foundation
- [x] Repository identity
- [x] OSS-only scope
- [x] Contribution taxonomy
- [x] Evidence standard
- [x] Complete external OSS PR archive
- [x] Curated contribution index
- [x] Dated snapshot
- [x] Case-study layer
- [x] Research / learning navigation

## Phase 2 — Contribution intelligence
- [x] Separate merged/open/closed lifecycle
- [x] Explicit upstream vs fork-side labeling
- [x] Maintainer-verification notes for major work
- [ ] One canonical metadata record per significant contribution
- [ ] Review timeline per significant PR
- [ ] Automatic upstream-state reconciliation

## Phase 3 — Engineering knowledge
- [x] PyRIT case study
- [x] aios streaming case study
- [x] Profile Analyzer case study
- [ ] TopoCore case study
- [ ] OpenHands case study
- [ ] Additional systems/infrastructure case studies
- [ ] Research note index
- [ ] Learning-to-source backlinks

## Phase 4 — Automation
- [x] PR/push CI validation
- [x] Internal Markdown-link validation
- [x] External OSS archive audit
- [x] Daily scheduled drift detection
- [x] Manual audit dispatch
- [x] Least-privilege workflow permissions
- [x] Pinned GitHub Actions dependencies
- [ ] Machine-readable contribution metadata
- [ ] Automatic dated snapshot generation
- [ ] Broken external-link checker
- [ ] Stale-record detector
- [ ] Reviewed status-refresh PR generation

## Phase 5 — Analytics
- [ ] Contribution dashboard
- [ ] Repository/project index
- [ ] Review/maintainer-response timeline
- [ ] Evidence-derived skill map
- [ ] Historical trend views
- [ ] Contribution-to-learning graph

## Phase 6 — OSS Atlas intelligence
- [ ] Canonical contribution IDs
- [ ] Evidence bundles per contribution
- [ ] Cross-project engineering pattern extraction
- [ ] Maintainer feedback timeline
- [ ] Contribution freshness score based on evidence age, not quality
- [ ] Searchable machine-readable index
- [ ] Static generated Atlas report

## Design constraints

- Never fabricate or infer merge outcomes.
- Never rank contributions by subjective quality.
- Never silently rewrite historical records.
- Keep external OSS work distinct from self-owned project work.
- Automation should detect drift first and mutate the ledger only through reviewable changes.

## Target end state

OSS Atlas should function as a **version-controlled OSS engineering knowledge base**:

**GitHub evidence → contribution record → verification → case study → reusable learning → historical snapshot**

The repository should remain useful even if every decorative portfolio element is removed.
