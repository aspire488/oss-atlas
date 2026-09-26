# Complete External OSS PR History

> Historical index of authored pull requests against **external open-source repositories**, based on GitHub state observed on September 26, 2026.

This archive intentionally excludes PRs in repositories owned by `aspire488`. Those belong to the engineering portfolio, not the external OSS contribution ledger.

## Summary

| Status | Count |
|---|---:|
| Merged upstream | 8 |
| Open upstream | 16 |
| Open fork-side | 6 |
| Closed without merge | 6 |
| **External OSS PRs** | **36** |

## Merged upstream

- [0xarchit/github-profile-analyzer #30 — Fix/impact score evidence](https://github.com/0xarchit/github-profile-analyzer/pull/30) — merged 2026-09-23
- [eumemic/aios #2460 — preserve LiteLLM parameter translation](https://github.com/eumemic/aios/pull/2460) — merged 2026-09-23
- [eumemic/aios #2457 — preserve length finish reason across streaming trailers](https://github.com/eumemic/aios/pull/2457) — merged 2026-09-23
- [eumemic/aios #2459 — preserve timeout bound in child outcome](https://github.com/eumemic/aios/pull/2459) — merged 2026-09-24
- [microsoft/PyRIT #2762 — Dataset Summary API](https://github.com/microsoft/PyRIT/pull/2762) — merged 2026-09-24
- [eumemic/aios #2458 — record streaming length as truncated output](https://github.com/eumemic/aios/pull/2458) — merged 2026-09-24 (merge commit `fe051b2c`)
- [microsoft/PyRIT #2823 — preserve HarmBench context string](https://github.com/microsoft/PyRIT/pull/2823) — merged 2026-09-25 (merge commit `940a8efabb404d80f6a716c5e641d81809d8972a`)
- [PicadoLabs/agent-bench #8 — global command palette](https://github.com/PicadoLabs/agent-bench/pull/8) — merged 2026-09-26 (merge commit `2d95c522d95705d332f2e6ddc5929c281e2886b3`)

## Open upstream

- [KARAN-D05/TopoCore #1 — detect repeated spatial execution states](https://github.com/KARAN-D05/TopoCore/pull/1)
- [run-llama/llama_index #23201 — preserve retrieved scores during prev-next expansion](https://github.com/run-llama/llama_index/pull/23201)
- [NousResearch/hermes-agent #121771 — desktop gateway stale-ref recovery](https://github.com/NousResearch/hermes-agent/pull/121771)
- [Agent-Field/agentfield #1073 — Go harness factory tests](https://github.com/Agent-Field/agentfield/pull/1073)
- [cloudflare/quiche #2759 — ignore ACKs for non-in-flight packets](https://github.com/cloudflare/quiche/pull/2759)
- [cloudflare/quiche #2758 — verify peers with a custom CA](https://github.com/cloudflare/quiche/pull/2758)
- [cloudflare/quiche #2756 — unify PTO-based timer duration](https://github.com/cloudflare/quiche/pull/2756)
- [intellij-powershell/intellij-powershell #506 — resolve pwsh reparse point](https://github.com/intellij-powershell/intellij-powershell/pull/506)
- [open-telemetry/opentelemetry-erlang-contrib #822 — isolate spans across retries and redirects](https://github.com/open-telemetry/opentelemetry-erlang-contrib/pull/822)
- [risingwavelabs/risingwave #27181 — inspect correlated refs in LogicalValues](https://github.com/risingwavelabs/risingwave/pull/27181)
- [mvt-project/mvt #939 — STIX indicator equals](https://github.com/mvt-project/mvt/pull/939)
- [coder/coder #29668 — deduplicate Unknown AI Gateway clients](https://github.com/coder/coder/pull/29668)
- [tysoncung/ai-platform-aws #4 — provider routing specificity](https://github.com/tysoncung/ai-platform-aws/pull/4)
- [OpenHands/OpenHands #17579 — align condenser max size with agent-server minimum](https://github.com/OpenHands/OpenHands/pull/17579)
- [adityamallia7/GoalAI-Score-predictor-26 #1 — reproducible Monte Carlo prediction analysis](https://github.com/adityamallia7/GoalAI-Score-predictor-26/pull/1)
- [RajX-dev/N3MO #39 — Ruby/Kotlin language routing regression coverage](https://github.com/RajX-dev/N3MO/pull/39)

## Open fork-side OSS work

- [aspire488/siyuan #1 — recover expired MCP sessions without unsafe replay](https://github.com/aspire488/siyuan/pull/1)
- [aspire488/linguist #1 — trim .example suffix before language detection](https://github.com/aspire488/linguist/pull/1)

- [aspire488/inspect_ai #1 — base64 encode Google inline image bytes](https://github.com/aspire488/inspect_ai/pull/1)
- [aspire488/garak #1 — handle unset soft prompt cap](https://github.com/aspire488/garak/pull/1)
- [aspire488/RAMPART #1 — adaptive multi-turn XPIA execution](https://github.com/aspire488/RAMPART/pull/1)
- [aspire488/PyRIT #1 — canonical technique names in scenario summaries](https://github.com/aspire488/PyRIT/pull/1)

## Closed without merge

- [kirodotdev/KiroCrew #12861 — restore PDF search behind bounded extraction](https://github.com/kirodotdev/KiroCrew/pull/12861) — closed 2026-09-25; superseded by #12925

- [uutils/coreutils #14812 — preserve canonical quoting style in dired metadata](https://github.com/uutils/coreutils/pull/14812)
- [microsoft/PyRIT #2743 — garak exploitation scenario](https://github.com/microsoft/PyRIT/pull/2743)
- [akitaonrails/ai-memory #828 — expand agent-memory comparison coverage](https://github.com/akitaonrails/ai-memory/pull/828)
- [github-linguist/linguist #8220 — add Salam language support](https://github.com/github-linguist/linguist/pull/8220)
- [daniel5151/clicky #72 — revamp contributor quickstart](https://github.com/daniel5151/clicky/pull/72)

## Status rules

- **Merged upstream** means GitHub reports a non-null merge timestamp.
- **Open upstream** means the PR is open and the destination repository is not `aspire488/*`.
- **Open fork-side** means the PR is open in an `aspire488/*` repository.
- **Closed without merge** means GitHub reports closed with no merge timestamp.
- This archive is historical and does not rank contribution quality.
