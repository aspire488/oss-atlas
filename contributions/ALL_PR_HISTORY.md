# Complete External OSS PR History

> Historical index of authored pull requests against **external open-source repositories**, based on GitHub state observed on October 26, 2026.

This archive intentionally excludes PRs in repositories owned by `aspire488`. Those belong to the engineering portfolio, not the external OSS contribution ledger.

## Summary

| Status | Count |
|---|---:|
| Merged upstream | 13 |
| Open upstream | 26 |
| Open fork-side | 3 |
| Closed without merge | 12 |
| **External OSS PRs** | **54** |

## Merged upstream
- [microsoft/PyRIT #3429 — detect external XInclude resources in XXE output scoring](https://github.com/microsoft/PyRIT/pull/3429) — merged 2026-10-26 (merge commit `0735f4c1077db4b3042495bb821fa33a625482a5`); full PyRIT suite was not run locally.

- [0xarchit/github-profile-analyzer #30 — Fix/impact score evidence](https://github.com/0xarchit/github-profile-analyzer/pull/30) — merged 2026-09-23
- [eumemic/aios #2460 — preserve LiteLLM parameter translation](https://github.com/eumemic/aios/pull/2460) — merged 2026-09-23
- [eumemic/aios #2457 — preserve length finish reason across streaming trailers](https://github.com/eumemic/aios/pull/2457) — merged 2026-09-23
- [eumemic/aios #2459 — preserve timeout bound in child outcome](https://github.com/eumemic/aios/pull/2459) — merged 2026-09-24
- [microsoft/PyRIT #2762 — Dataset Summary API](https://github.com/microsoft/PyRIT/pull/2762) — merged 2026-09-24
- [eumemic/aios #2458 — record streaming length as truncated output](https://github.com/eumemic/aios/pull/2458) — merged 2026-09-24 (merge commit `fe051b2c`)
- [microsoft/PyRIT #2823 — preserve HarmBench context string](https://github.com/microsoft/PyRIT/pull/2823) — merged 2026-09-25 (merge commit `940a8efabb404d80f6a716c5e641d81809d8972a`)
- [PicadoLabs/agent-bench #8 — global command palette](https://github.com/PicadoLabs/agent-bench/pull/8) — merged 2026-09-26 (merge commit `2d95c522d95705d332f2e6ddc5929c281e2886b3`)
- [Agent-Field/agentfield #1073 — Go harness factory tests](https://github.com/Agent-Field/agentfield/pull/1073) — merged 2026-09-26 (merge commit `13b44603e2fb09a5d1817e8d2d0f64f3a40041fa`)

## Open upstream
- [microsoft/PyRIT #3558 — assign user roles to social-bias multi-turn seeds](https://github.com/microsoft/PyRIT/pull/3558) — opened 2026-10-26; regression assertion added, tests not yet run.
- [NousResearch/hermes-agent #134658 — use type-only imports for session source types](https://github.com/NousResearch/hermes-agent/pull/134658) — fixes #134632.

- [microsoft/PyRIT #3335 — AzureML extra parameter identifier fix](https://github.com/microsoft/PyRIT/pull/3335)
- [UKGovernmentBEIS/inspect_ai #5675 — preserve eval-level error during stream conversion](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5675) — fixes #5639; follow-up CI fix pushed 2026-10-22 (`fb9a400`) to restore the existing test's `stream`/`to` parametrization after a Python 3.14 fixture setup error; CI rerunning, local `make check`/`make test` not run
- [UKGovernmentBEIS/inspect_ai #5670 — prefer explicit API keys over ambient ADC](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5670) — merged 2026-10-04
- [UKGovernmentBEIS/inspect_ai #5671 — convert structured validation failures to parsing errors](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5671)
- [UKGovernmentBEIS/inspect_ai #5672 — preserve cached input tokens across provider bridges](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5672)
- [microsoft/PyRIT #2976 — preserve word-selection parameters in StringJoinConverter identifiers](https://github.com/microsoft/PyRIT/pull/2976)
- [NVIDIA/garak #2234 — Fix/paraphrase transformers compat](https://github.com/NVIDIA/garak/pull/2234)
- [NousResearch/hermes-agent #123846 — fix(batch): accept Fire tuple args and numeric run names](https://github.com/NousResearch/hermes-agent/pull/123846)
- [NousResearch/hermes-agent #123850 — fix(batch): keep tool-search bridge trajectories](https://github.com/NousResearch/hermes-agent/pull/123850)
- [Younesfdj/gitfut #125 — Fix/active years from contributions](https://github.com/Younesfdj/gitfut/pull/125)
- [collective/icalendar #1835 — Fix/start end duration mismatch](https://github.com/collective/icalendar/pull/1835)
- [microsoft/PyRIT #2882 — Fix/exact text matching empty target](https://github.com/microsoft/PyRIT/pull/2882) — merged 2026-09-28 (merge commit `dff83aaab767f9b2b0aee68a20ab277de7e9d289`)
- [microsoft/PyRIT #2885 — preserve text after Prompt Shield document tags](https://github.com/microsoft/PyRIT/pull/2885) — closed 2026-09-28; duplicate/superseded by earlier #2838
- [run-llama/llama_index #23260 — fix(postprocessor): preserve retrieved scores during prev/next expansion](https://github.com/run-llama/llama_index/pull/23260)

- [KARAN-D05/TopoCore #1 — detect repeated spatial execution states](https://github.com/KARAN-D05/TopoCore/pull/1)
- [run-llama/llama_index #23201 — preserve retrieved scores during prev-next expansion](https://github.com/run-llama/llama_index/pull/23201)
- [NousResearch/hermes-agent #121771 — desktop gateway stale-ref recovery](https://github.com/NousResearch/hermes-agent/pull/121771) — closed as superseded after #126144 incorporated the fix
- [cloudflare/quiche #2759 — ignore ACKs for non-in-flight packets](https://github.com/cloudflare/quiche/pull/2759)
- [cloudflare/quiche #2758 — verify peers with a custom CA](https://github.com/cloudflare/quiche/pull/2758)
- [cloudflare/quiche #2756 — unify PTO-based timer duration](https://github.com/cloudflare/quiche/pull/2756)
- [intellij-powershell/intellij-powershell #506 — resolve pwsh reparse point](https://github.com/intellij-powershell/intellij-powershell/pull/506)
- [open-telemetry/opentelemetry-erlang-contrib #822 — isolate spans across retries and redirects](https://github.com/open-telemetry/opentelemetry-erlang-contrib/pull/822)
- [risingwavelabs/risingwave #27181 — inspect correlated refs in LogicalValues](https://github.com/risingwavelabs/risingwave/pull/27181)
- [mvt-project/mvt #939 — STIX indicator equals](https://github.com/mvt-project/mvt/pull/939)
- [coder/coder #29668 — deduplicate Unknown AI Gateway clients](https://github.com/coder/coder/pull/29668)
- [tysoncung/ai-platform-aws #4 — provider routing specificity](https://github.com/tysoncung/ai-platform-aws/pull/4)
- [OpenHands/OpenHands #17579 — align condenser max size with agent-server minimum](https://github.com/OpenHands/OpenHands/pull/17579) — still open; latest CI passed after review fixes
- [adityamallia7/GoalAI-Score-predictor-26 #1 — reproducible Monte Carlo prediction analysis](https://github.com/adityamallia7/GoalAI-Score-predictor-26/pull/1)
- [RajX-dev/N3MO #39 — Ruby/Kotlin language routing regression coverage](https://github.com/RajX-dev/N3MO/pull/39)

## Open fork-side OSS work

- [aspire488/PyRIT #3309 — prevent role-play prompt preambles](https://github.com/microsoft/PyRIT/pull/3309) — open PR from fork; regression tests added, but tests and the requested 50-run comparison remain pending.
- [aspire488/kestra #21225 — editor content widget lifecycle tests](https://github.com/kestra-io/kestra/pull/21225) — draft fork-side PR; Vitest run and required passing-test screenshot remain pending.
- [aspire488/cmux #21749 — OpenCode database snapshot sidecar tests](https://github.com/manaflow-ai/cmux/pull/21749) — draft fork-side PR; native macOS/Xcode tests and requested CLA signature remain pending.

- [aspire488/siyuan #1 — recover expired MCP sessions without unsafe replay](https://github.com/aspire488/siyuan/pull/1)
- [aspire488/linguist #1 — trim .example suffix before language detection](https://github.com/aspire488/linguist/pull/1)

- [aspire488/inspect_ai #1 — base64 encode Google inline image bytes](https://github.com/aspire488/inspect_ai/pull/1)
- [aspire488/garak #1 — handle unset soft prompt cap](https://github.com/aspire488/garak/pull/1)
- [aspire488/RAMPART #1 — adaptive multi-turn XPIA execution](https://github.com/aspire488/RAMPART/pull/1)
- [aspire488/PyRIT #1 — canonical technique names in scenario summaries](https://github.com/aspire488/PyRIT/pull/1)

## Closed without merge
- [NousResearch/hermes-agent #135229 — update lock custodian partner v2](https://github.com/NousResearch/hermes-agent/pull/135229) — closed without merge (state observed 2026-10-21).

- [NousResearch/hermes-agent #127233 — MCP prompt rendering fix](https://github.com/NousResearch/hermes-agent/pull/127233) — closed 2026-10-01 without merge (duplicate of #122824)
- [microsoft/PyRIT #2919 — inverted score metadata](https://github.com/microsoft/PyRIT/pull/2919) — closed 2026-10-01 without merge

- [pydantic/pydantic-ai #8823 — perf: avoid redundant RunContext copy when validation context is unset](https://github.com/pydantic/pydantic-ai/pull/8823)

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
