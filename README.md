# OSS Atlas 🗺️

> **A living map of open-source engineering work.**

[![Open Source](https://img.shields.io/badge/focus-open%20source-blue)](https://github.com/aspire488)
[![Maintained](https://img.shields.io/badge/status-actively%20maintained-brightgreen)](https://github.com/aspire488/oss-atlas)
[![Evidence First](https://img.shields.io/badge/principle-evidence%20first-purple)](docs/OPERATING_MODEL.md)

**OSS Atlas** is my dedicated record of contributing to, studying, and building around real open-source software.

It is not a vanity contribution counter. The goal is to preserve the **technical substance behind the activity**: the problem, investigation, implementation, validation, review, outcome, and lessons.

## The split

| Repository | Role |
|---|---|
| **[oss-atlas](https://github.com/aspire488/oss-atlas)** | Contribution record, research, case studies, engineering knowledge |
| **[gh-ops](https://github.com/aspire488/gh-ops)** | OSS discovery, monitoring, intelligence, automation |

## 🧭 Navigate

- **[Contribution Ledger](contributions/README.md)** — upstream work and status
- **[Research](research/README.md)** — architecture and codebase investigations
- **[Experiments](experiments/README.md)** — bounded technical experiments
- **[Case Studies](case-studies/README.md)** — deep technical write-ups
- **[Learnings](learnings/README.md)** — transferable engineering lessons
- **[Statistics](stats/README.md)** — sourced, dated metrics
- **[Roadmap](docs/ROADMAP.md)** — what is being built next
- **[Operating Model](docs/OPERATING_MODEL.md)** — evidence and maintenance rules

## 🚀 Contribution Portfolio

### Microsoft PyRIT
**AI red teaming / Python / APIs / data modeling**

- **Dataset Summary API** — dataset metadata aggregation, provider/loaded semantics, collation-safe querying, unnamed datasets, and regression coverage.
- **Scenario Summary Fix** — canonical technique_name handling instead of display-oriented grouping.

### TopoCore
**Spatial execution / simulators / deterministic state**

- Added cycle detection based on the complete spatial execution state: **(X, Y, Direction)**.
- [Upstream PR #1](https://github.com/KARAN-D05/TopoCore/pull/1)

### OpenHands
**SDK metadata / validation / testing**

- Corrected condenser SDK field metadata and associated constraints/tests.

### OpenAI Agents Python
**Agents / compaction / state management**

- Prepared a fix for stale response-chain state after successful compaction-session clearing, with regression coverage.

> Contribution status is tracked in the [open contribution ledger](contributions/open/README.md).

## 🧠 How I Contribute

**Understand → isolate → implement → validate → review → document**

I prefer contributions that are:

- small enough to review
- technically justified
- backed by regression tests when behavior changes
- aligned with the upstream project's conventions
- explicit about limitations and verification
- useful beyond the individual patch

I treat maintainer feedback as part of the engineering process, not as an afterthought.

## 📐 Evidence Standard

OSS Atlas distinguishes between:

**Observed**
> What the repository, tests, CI, issue tracker, or maintainer actually shows.

**Implemented**
> What exists in a contribution branch or commit.

**Verified**
> What was actually tested or otherwise checked.

**Interpretation**
> What I learned or believe the design means.

This keeps the portfolio technically honest and makes individual records auditable.

## 🗂️ Repository Architecture

```text
oss-atlas/
├── contributions/       # upstream contribution ledger
│   ├── open/
│   ├── merged/
│   └── closed/
├── research/            # architecture investigations
├── experiments/         # bounded technical experiments
├── case-studies/        # deep contribution write-ups
├── learnings/           # durable engineering lessons
├── stats/               # sourced historical metrics
├── templates/           # reusable record formats
├── docs/
│   ├── OPERATING_MODEL.md
│   └── ROADMAP.md
└── README.md
```

## 🛠️ Repository Health

This repository follows GitHub's recommended documentation/community practices with:

- contribution guidelines
- code of conduct
- security policy
- pull-request template
- issue templates
- reusable documentation templates
- explicit evidence/status rules

See [CONTRIBUTING.md](CONTRIBUTING.md).

## 🔭 Direction

The long-term goal is for OSS Atlas to become a **machine-readable + human-readable OSS engineering ledger**.

Planned capabilities include:

- automated upstream status tracking
- contribution metadata
- historical snapshots
- broken-link checks
- contribution/project dashboards
- skill mapping derived from actual engineering evidence

The automation should reduce maintenance work without turning the repository into an inflated activity counter.

## 🔗 Elsewhere

- **GitHub:** [@aspire488](https://github.com/aspire488)
- **OSS automation:** [gh-ops](https://github.com/aspire488/gh-ops)

---

<sub>Built in the open. Documented with evidence. Updated as the work evolves.</sub>