# OSS Contributions Index

> Canonical navigation layer for Joel Jigo's open-source engineering record.

## Contribution lifecycle

| Layer | Meaning | Location |
|---|---|---|
| **Merged upstream** | Accepted by an upstream repository | `contributions/merged/` |
| **Active upstream** | Open PRs against upstream projects | `contributions/open/` |
| **Fork-side active** | Open work in personal forks | `contributions/open/` |
| **Closed / historical** | Closed without merge | `contributions/closed/` |
| **Review / architecture** | Reviews, issue analysis, design feedback | `research/` |
| **Discussions** | Technical community discussions | `research/` |
| **Case studies** | Deep evidence-backed narratives | `case-studies/` |
| **Learnings** | Reusable engineering lessons | `learnings/` |

## Featured merged work

- [aios #2457](https://github.com/eumemic/aios/pull/2457) — preserve streaming `finish_reason="length"`
- [aios #2458](https://github.com/eumemic/aios/pull/2458) — record streaming length as truncated output
- [Microsoft PyRIT #2762](https://github.com/microsoft/PyRIT/pull/2762) — Dataset Summary API
- [aios #2460](https://github.com/eumemic/aios/pull/2460) — preserve LiteLLM parameter translation
- [github-profile-analyzer #30](https://github.com/0xarchit/github-profile-analyzer/pull/30) — evidence-weighted impact scoring
- [gh-ops #1](https://github.com/aspire488/gh-ops/pull/1) — GitHub Actions CI validation

## Featured active work

- [Hermes Agent #134658](https://github.com/NousResearch/hermes-agent/pull/134658) — **open upstream** — fixes type-only imports for session source types under `verbatimModuleSyntax`.

- [Microsoft PyRIT #3429](https://github.com/microsoft/PyRIT/pull/3429) — **merged upstream · October 26, 2026** — adds XXE output-scorer detection for external XInclude resources. Merge commit [`0735f4c1`](https://github.com/microsoft/PyRIT/commit/0735f4c1077db4b3042495bb821fa33a625482a5); full suite was not run locally.
- [cmux #21749](https://github.com/manaflow-ai/cmux/pull/21749) — **draft fork-side** — OpenCode database snapshot sidecar/missing-file tests; native macOS/Xcode validation pending.

- [Inspect AI #5675](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5675) — **open upstream · CI rerunning** — preserve eval-level errors during streamed log conversion; follow-up commit `fb9a400` restores the existing test parametrization after a Python 3.14 fixture setup error
- [Inspect AI #5670](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5670) — **merged upstream · October 4, 2026**
- [Inspect AI #5671](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5671) — **open upstream**
- [Inspect AI #5672](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5672) — **open upstream**
- [Microsoft PyRIT #2976](https://github.com/microsoft/PyRIT/pull/2976) — **open upstream**
- [NousResearch Hermes Agent #127233](https://github.com/NousResearch/hermes-agent/pull/127233) — **closed without merge** (duplicate of #122824)
- [Hermes Agent #135229](https://github.com/NousResearch/hermes-agent/pull/135229) — **closed without merge**

## Recently closed / superseded

- [Microsoft PyRIT #3558](https://github.com/microsoft/PyRIT/pull/3558) — closed without merge on October 27, 2026; superseded by #3557, which was merged from another contributor's branch.
- [Microsoft PyRIT #3335](https://github.com/microsoft/PyRIT/pull/3335) — closed without merge on October 19, 2026.
- [Microsoft PyRIT #3309](https://github.com/microsoft/PyRIT/pull/3309) — closed without merge on October 20, 2026; the requested 50-run comparison was not completed.
- [Kestra #21225](https://github.com/kestra-io/kestra/pull/21225) — closed without merge on October 21, 2026; required Vitest evidence was not recorded.

### AI / security / agent tooling
- [Microsoft PyRIT #2762](https://github.com/microsoft/PyRIT/pull/2762) — merged upstream
- [Microsoft PyRIT #2885](https://github.com/microsoft/PyRIT/pull/2885) — Prompt Shield parser fix, upstream open
- [TopoCore #1](https://github.com/KARAN-D05/TopoCore/pull/1) — upstream, open
- [garak #1](https://github.com/aspire488/garak/pull/1) — fork-side, open
- [Inspect AI #1](https://github.com/aspire488/inspect_ai/pull/1) — fork-side, open
- [RAMPART #1](https://github.com/aspire488/RAMPART/pull/1) — fork-side, open
- [PyRIT fork #1](https://github.com/aspire488/PyRIT/pull/1) — fork-side, open

### Systems / infrastructure / developer tooling
- [aios #2458](https://github.com/eumemic/aios/pull/2458) — merged upstream
- [aios #2459](https://github.com/eumemic/aios/pull/2459)
- [llama_index #23201](https://github.com/run-llama/llama_index/pull/23201)
- [quiche #2756](https://github.com/cloudflare/quiche/pull/2756)
- [quiche #2758](https://github.com/cloudflare/quiche/pull/2758)
- [quiche #2759](https://github.com/cloudflare/quiche/pull/2759)
- [OpenHands #17579](https://github.com/OpenHands/OpenHands/pull/17579) — open; latest CI passed after review fixes
- [opentelemetry-erlang-contrib #822](https://github.com/open-telemetry/opentelemetry-erlang-contrib/pull/822)
- [RisingWave #27181](https://github.com/risingwavelabs/risingwave/pull/27181)
- [Coder #29668](https://github.com/coder/coder/pull/29668)

## Full history

[ALL_PR_HISTORY.md](ALL_PR_HISTORY.md) is the exhaustive authored-PR archive.

## Rule

Highlighting is navigation, **not a quality ranking**. No open PR is described as successful until upstream evidence shows it.
