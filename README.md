<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:70a5fd&height=210&section=header&text=OSS%20Atlas&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Open-source%20engineering%20ledger&descAlignY=58&descSize=16" width="100%"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Focus-Open%20Source%20Engineering-70a5fd?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Living%20Ledger-2ea44f?style=for-the-badge"/>
</p>

# OSS Atlas

**OSS Atlas** is the dedicated open-source engineering ledger for my external OSS work.

It records contributions, upstream outcomes, maintainer feedback, technical investigations, discussions, case studies, and durable engineering lessons — while deliberately excluding self-repository portfolio work.

> **Observed → Implemented → Verified → Documented**

## 🧭 Start here

| Surface | Purpose |
|---|---|
| [Contributions Index](contributions/INDEX.md) | Curated map of OSS work |
| [Complete OSS PR History](contributions/ALL_PR_HISTORY.md) | External OSS PR archive |
| [Case Studies](case-studies/README.md) | Deep evidence-backed analysis |
| [Research](research/README.md) | Reviews, investigations, discussions |
| [Learnings](learnings/README.md) | Reusable engineering lessons |
| [2026-09-23 Snapshot](stats/2026-09-23.md) | Dated contribution-state snapshot |
| [Operating Model](docs/OPERATING_MODEL.md) | Evidence and maintenance rules |
| [Roadmap](docs/ROADMAP.md) | Atlas implementation plan |
| [Automation](docs/AUTOMATION.md) | GitHub Actions and drift-audit contract |

## 📊 External OSS snapshot

| State | Count |
|---|---:|
| Merged upstream | **3** |
| Open | **24** |
| Closed without merge | **5** |
| **External OSS PRs** | **32** |

**Important:** 24 open = 20 upstream + 4 fork-side. The archive separates them explicitly.

## 🏆 Recent upstream merges

- [aios #2457](https://github.com/eumemic/aios/pull/2457) — preserved streaming length termination semantics
- [aios #2460](https://github.com/eumemic/aios/pull/2460) — preserved LiteLLM parameter translation
- [github-profile-analyzer #30](https://github.com/0xarchit/github-profile-analyzer/pull/30) — refined evidence-weighted impact scoring

## 🔥 Active OSS work

### Microsoft PyRIT
- [#2762 — Dataset Summary API](https://github.com/microsoft/PyRIT/pull/2762) — open upstream; extensive maintainer verification is recorded in the [case study](case-studies/PYRIT-DATASET-SUMMARY.md).
- [fork #1 — canonical technique names](https://github.com/aspire488/PyRIT/pull/1) — fork-side OSS work.

### AI / security / agent systems
- [TopoCore #1](https://github.com/KARAN-D05/TopoCore/pull/1)
- [garak #1](https://github.com/aspire488/garak/pull/1)
- [Inspect AI #1](https://github.com/aspire488/inspect_ai/pull/1)
- [RAMPART #1](https://github.com/aspire488/RAMPART/pull/1)

### Systems / infrastructure
- [aios #2458](https://github.com/eumemic/aios/pull/2458)
- [aios #2459](https://github.com/eumemic/aios/pull/2459)
- [llama_index #23201](https://github.com/run-llama/llama_index/pull/23201)
- [quiche #2756 / #2758 / #2759](https://github.com/cloudflare/quiche)
- [OpenHands #17579](https://github.com/OpenHands/OpenHands/pull/17579)
- [RisingWave #27181](https://github.com/risingwavelabs/risingwave/pull/27181)
- [opentelemetry-erlang-contrib #822](https://github.com/open-telemetry/opentelemetry-erlang-contrib/pull/822)
- [Coder #29668](https://github.com/coder/coder/pull/29668)

## 🧠 Engineering knowledge

### Case studies
- [PyRIT Dataset Summary API](case-studies/PYRIT-DATASET-SUMMARY.md)
- [aios Streaming Termination Semantics](case-studies/AIOS-STREAMING-SEMANTICS.md)
- [GitHub Profile Analyzer Impact Scoring](case-studies/PROFILE-ANALYZER-IMPACT-SCORING.md)

### Research
Architecture reviews, issue investigations, maintainer reasoning, and technical discussions that are useful beyond one PR.

### Learnings
Durable OSS engineering rules backed by primary evidence.

## ⚙️ Automated verification

GitHub Actions validates the Atlas on pushes and pull requests, and a scheduled audit checks the external OSS ledger for GitHub-state drift. Workflows use read-only repository permissions and pinned standard Actions dependencies.

See [Automation](docs/AUTOMATION.md) for the contract and [Roadmap](docs/ROADMAP.md) for the next automation phases.

## 🧱 Repository architecture

```text
oss-atlas/
├── contributions/
│   ├── INDEX.md
│   ├── ALL_PR_HISTORY.md
│   ├── merged/
│   ├── open/
│   └── closed/
├── case-studies/
├── research/
├── experiments/
├── learnings/
├── stats/
├── templates/
├── docs/
│   ├── OPERATING_MODEL.md
│   └── ROADMAP.md
└── README.md
```

## 📐 Evidence standard

**Observed** — GitHub state, issue/PR text, CI, tests, reviews, or maintainer statements.

**Implemented** — code or documentation actually present in a contribution branch/commit.

**Verified** — validation actually run or explicitly confirmed by an upstream maintainer.

**Interpretation** — engineering lessons inferred from evidence.

An open PR is never called merged. A targeted test run is never called a full-suite pass. Fork-side work is never presented as upstream acceptance.

## 🔭 Direction

OSS Atlas is evolving from a contribution list into a durable OSS engineering knowledge base.

Next priorities:

- canonical contribution metadata
- status and maintainer-feedback history
- machine-readable records
- automated freshness and broken-link checks
- dated snapshots
- contribution/review dashboards
- evidence-derived skill mapping

**Evidence density over activity-count inflation.**

---

**Profile:** https://github.com/aspire488  
**OSS automation:** https://github.com/aspire488/gh-ops

<sub>Built in the open. Recorded with evidence. Updated as the work evolves.</sub>
