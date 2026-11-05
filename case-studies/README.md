# Engineering Case Studies

<sub>THE RECORD / 03</sub>

Deep technical narratives reserved for work with meaningful implementation reasoning, review feedback, debugging, architecture, or reusable engineering patterns.

---

## Case study collection

| Project | Engineering theme | Read |
|:--|:--|:--|
| Microsoft PyRIT | Dataset API design and query correctness | [Dataset Summary API](PYRIT-DATASET-SUMMARY.md) |
| aios | Streaming termination semantics | [Streaming semantics](AIOS-STREAMING-SEMANTICS.md) |
| GitHub Profile Analyzer | Evidence-weighted impact scoring | [Impact scoring](PROFILE-ANALYZER-IMPACT-SCORING.md) |
| TopoCore | Deterministic cycle detection | [Cycle detection](TOPOCORE-CYCLE-DETECTION.md) |
| OpenHands | Settings contract alignment | [Settings contract](OPENHANDS-SETTINGS-CONTRACT.md) |

## Case study standard

Every case study should answer:

1. **Problem** — What was wrong upstream, and how was it observed?
2. **Constraints** — What behavior or compatibility had to be preserved?
3. **Implementation** — What changed, and why?
4. **Verification** — Which tests or checks ran, and in what environment?
5. **Review** — What did maintainers challenge, request, or accept?
6. **Outcome** — What happened upstream?
7. **Transfer** — What reusable lesson remains?

An open PR is never presented as merged. Missing validation is stated explicitly.

---

<sub>Only work with enough evidence and engineering depth earns a full case study.</sub>
