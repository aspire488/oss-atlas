# Research Library

<sub>THE RECORD / 02</sub>

Technical investigations, issue analysis, reviewer feedback, and design discussions that explain the reasoning behind open-source work.

Research is not a claim of acceptance. Each note should distinguish primary evidence, interpretation, implementation, and what remains unverified.

---

## Recent investigations

### 05 November 2026
- [PyRIT general scorer identifier configuration](2026-11-05-pyrit-scorer-identifier.md) — implementation note for draft fork PR [#5](https://github.com/aspire488/PyRIT/pull/5), targeting upstream issue [#3839](https://github.com/microsoft/PyRIT/issues/3839). Records the identifier gap, code changes, regression scope, and validation boundary.

### 21 October 2026
- [PyRIT XXE output-scorer XInclude coverage](2026-10-21-pyrit-xinclude-xxe.md) — contribution note for upstream PR [#3429](https://github.com/microsoft/PyRIT/pull/3429), following issue [#3324](https://github.com/microsoft/PyRIT/issues/3324). Records detection scope, regression cases, and validation boundaries.

## Research taxonomy

| Track | Questions answered |
|:--|:--|
| Architecture | What constraints shape the system? |
| Issue investigation | What is actually broken, and how is it reproduced? |
| Review analysis | What did maintainers challenge or request? |
| Technical discussion | Which trade-offs were debated? |
| Cross-project patterns | What reusable engineering principle emerges? |

## Evidence standard

1. Link the upstream issue, PR, commit, or discussion.
2. Separate observed behavior from interpretation.
3. Record exact commands and test scope where available.
4. State unresolved questions and validation gaps.
5. Link related contribution records and durable learnings.

---

<sub>Research should make the work easier to inspect, reproduce, and learn from — not merely longer.</sub>
