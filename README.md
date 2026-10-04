# 🏆 Featured Upstream Contributions — Microsoft PyRIT

> ## **Three PRs — All MERGED UPSTREAM**
>
> **#2762 — Dataset Summary API** · September 24, 2026 · merge commit `47c6151a`
>
> **#2823 — HarmBench context preservation** · September 25, 2026 · merge commit `940a8efabb404d80f6a716c5e641d81809d8972a`
>
> **#2882 — ExactTextMatching empty-target fix** · September 28, 2026 · merge commit `dff83aaab767f9b2b0aee68a20ab277de7e9d289`
>
> Together, these are three separate accepted upstream contributions to Microsoft's open-source AI red-teaming framework, spanning backend feature work and regression-focused behavior preservation.
---

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
| [Machine-readable index](data/contributions.json) | Canonical contribution metadata |
| [Evidence-derived skills](data/skills.json) | Skills mapped to contribution evidence |
| [Case Studies](case-studies/README.md) | Deep evidence-backed analysis |
| [Research](research/README.md) | Reviews, investigations, discussions |
| [Learnings](learnings/README.md) | Reusable engineering lessons |
| [2026-09-27 Ledger](contributions/ALL_PR_HISTORY.md) | Dated contribution-state snapshot |
| [Operating Model](docs/OPERATING_MODEL.md) | Evidence and maintenance rules |
| [Automation](docs/AUTOMATION.md) | GitHub Actions and drift-audit contract |
| [Roadmap](docs/ROADMAP.md) | Atlas implementation plan |


## 📅 October 4, 2026 — Current OSS update

### 🔥 New upstream proposals

- **Inspect AI #5670** — **open upstream** — explicit Google API keys now take precedence over ambient ADC defaults; regression coverage added.
- **Inspect AI #5671** — **open upstream** — structured Pydantic validation failures now flow through retryable tool parsing errors; regression coverage added.
- **Inspect AI #5672** — **open upstream** — cached input tokens are preserved across provider bridges; regression coverage added.
- **Microsoft PyRIT #2976** — **open upstream**; preserves `WordLevelConverter` selection parameters in `StringJoinConverter` identifiers and adds regression coverage for distinct selections, equivalent index sets, and registry registration.
- **NousResearch Hermes Agent #127233** — **open upstream**; fixes MCP `get_prompt` rendering so structured content blocks are rendered correctly.

All five are **open upstream**, not merged. The Atlas keeps upstream acceptance separate from active proposals.


### 🧩 Inspect AI — October 4, 2026

- [Inspect AI #5670 — Google API key / ADC precedence](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5670) — **OPEN UPSTREAM**; fixes #5358 by making an explicit API key win over ambient `GOOGLE_USE_ADC`, while preserving explicit `use_adc=true` behavior. Adds focused regression coverage.
- [Inspect AI #5671 — structured tool validation errors](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5671) — **OPEN UPSTREAM**; fixes #5403 by converting Pydantic structured-parameter `ValidationError` into the normal retryable `ToolParsingError` path. Adds focused regression coverage.
- [Inspect AI #5672 — cached input-token preservation](https://github.com/UKGovernmentBEIS/inspect_ai/pull/5672) — **OPEN UPSTREAM**; fixes #5364 by preserving cached-read/write input tokens across OpenAI Responses and Gemini provider bridges. Adds round-trip regression coverage.

All three are **open upstream** and are not counted as merged until upstream acceptance.

## 📊 External OSS snapshot

| State | Count |
|---|---:|
|  Merged upstream | **11** |
| Open upstream | **23** |
| Open fork-side | **0** |
| Closed without merge | **8** |
| **External OSS PRs** | **42** |

Snapshot date: **October 4, 2026**.

## 📈 OSS Atlas Dashboard

The Atlas now has a **first-party GitHub Actions dashboard**. These cards are generated from the canonical OSS ledger and refreshed automatically on pushes and on a daily schedule.

<p align="center">
<a href="https://github.com/aspire488/oss-atlas/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/aspire488/oss-atlas/ci.yml?branch=main&style=for-the-badge&label=Atlas%20CI"/></a>
<a href="https://github.com/aspire488/oss-atlas/actions/workflows/atlas-audit.yml"><img src="https://img.shields.io/github/actions/workflow/status/aspire488/oss-atlas/atlas-audit.yml?branch=main&style=for-the-badge&label=Ledger%20Audit"/></a>
<a href="https://github.com/aspire488/oss-atlas/actions/workflows/dashboard.yml"><img src="https://img.shields.io/github/actions/workflow/status/aspire488/oss-atlas/dashboard.yml?branch=main&style=for-the-badge&label=Dashboard"/></a>
</p>

<p align="center">
<img src="assets/dashboard/overview.svg" alt="OSS Atlas engineering overview" width="100%"/>
</p>

<p align="center">
<img src="assets/dashboard/status.svg" alt="OSS Atlas contribution state" width="92%"/>
</p>

<p align="center">
<img src="assets/dashboard/repositories.svg" alt="OSS Atlas repository concentration" width="92%"/>
</p>

<p align="center">
<img src="assets/dashboard/actions.svg" alt="OSS Atlas GitHub Actions health" width="92%"/>
</p>

**Dashboard pipeline:** data/contributions.json → scripts/generate_dashboard.py → SVG cards → Git commit via GitHub Actions.

## 🏆 Recent upstream merges

### 🔥 Microsoft PyRIT — current upstream track
- **Microsoft PyRIT #2882 — ExactTextMatching empty-target fix** — **MERGED UPSTREAM on September 28, 2026**; rejects empty and whitespace-only exact-match targets, with `DecodingScorer` regression coverage and explicit `ignore_whitespace=False` coverage. Merge commit: `dff83aaab767f9b2b0aee68a20ab277de7e9d289`.
- **Microsoft PyRIT #2885 — Prompt Shield parser** — **CLOSED AS DUPLICATE on September 28, 2026**; maintainer directed the fix/review to earlier #2838, which addresses the same parsing bug.
- **New open proposals:** [Hermes Agent #123846](https://github.com/NousResearch/hermes-agent/pull/123846) and [#123850](https://github.com/NousResearch/hermes-agent/pull/123850) — **open upstream on September 26, 2026**; the first fixes Fire CLI tuple/numeric argument normalization, while the second preserves Tool Search bridge trajectories during batch validation. #123850 now also has behavioral regression coverage through `_combine_batch_files()` verifying a `tool_call` bridge trajectory is retained rather than filtered as invalid.
- **Hermes Agent #126144** — **MERGED UPSTREAM on September 28, 2026**; broader desktop/session routing work incorporates and credits #121771's stale gateway-ref recovery, alongside session-owner pinning, profile-switch PTY cleanup, secondary-window routing, and live gateway recovery.
- **Prepared fork-side fix:** [PyRIT #2839](https://github.com/microsoft/PyRIT/issues/2839) — fixes `TemplateSegmentConverter` sampling when a prompt has fewer words than template parameters, with focused regression coverage. Branch: [aspire488/PyRIT `fix/template-segment-short-prompts`](https://github.com/aspire488/PyRIT/tree/fix/template-segment-short-prompts). Upstream PR creation is currently blocked by the GitHub integration permission boundary, so this remains fork-side prepared work.
- **Open fork proposal:** [PyRIT #3](https://github.com/aspire488/PyRIT/pull/3) — targets upstream issue [#2835](https://github.com/microsoft/PyRIT/issues/2835), fixing ObjectiveScorerEvaluator so `[user, assistant]` conversations retain all turns in memory but score only the assistant response, with regression coverage.

- [PicadoLabs Agent-Bench #8 — Global command palette](https://github.com/PicadoLabs/agent-bench/pull/8)  
  **Merged upstream on September 26, 2026** after maintainer review. The command palette implementation was approved with the build passing; the maintainer also pushed a small refactor switching the trigger from `useEffect` to `onClick`.

- [Agent-Field AgentField #1073 — Go harness factory tests](https://github.com/Agent-Field/agentfield/pull/1073)  
  **Merged upstream on September 26, 2026.** Adds focused `factory_test.go` coverage for explicit Claude Code and OpenCode provider construction, with the table driving concrete type assertions. Maintainer review approved the change and confirmed focused factory tests plus `go vet` pass locally.
- [PyRIT #2762 — Dataset Summary API](https://github.com/microsoft/PyRIT/pull/2762) — **MERGED UPSTREAM · September 24, 2026**; memory-backed dataset summaries with multiple substantive review rounds covering aggregation, dataset identity, SQLite behavior, selection-key isolation, metadata query controls, `loaded_only`, and regression coverage. Merge commit `47c6151a`.
- [PyRIT #2882 — ExactTextMatching empty-target fix](https://github.com/microsoft/PyRIT/pull/2882) — **MERGED UPSTREAM · September 28, 2026**; rejects empty/whitespace-only targets with scorer-level and `ignore_whitespace=False` regression coverage. Merge commit `dff83aaab767f9b2b0aee68a20ab277de7e9d289`.
- [PyRIT #2823 — HarmBench context preservation](https://github.com/microsoft/PyRIT/pull/2823) — **MERGED UPSTREAM · September 25, 2026**; preserves non-empty HarmBench `ContextString` in behavior prompts, retains context metadata, and adds regression coverage. Merge commit `940a8efabb404d80f6a716c5e641d81809d8972a`.
- [Microsoft RAMPART #2 — Generic PyRIT converter bridge](https://github.com/aspire488/RAMPART/pull/2) — **open upstream fork-side proposal · September 25, 2026**; implements the documented PyRIT PromptConverter → RAMPART PayloadConverter bridge for text-to-text converters, preserving payload identity/metadata with focused regression coverage.

**PyRIT track record:** 3 separate upstream PRs merged into Microsoft's AI red-teaming framework.

- [aios #2457](https://github.com/eumemic/aios/pull/2457) — preserved streaming length termination semantics
- [aios #2460](https://github.com/eumemic/aios/pull/2460) — preserved LiteLLM parameter translation
- [aios #2459](https://github.com/eumemic/aios/pull/2459) — preserved the timeout bound (`deadline` vs `spend`) in child outcomes while keeping `kind="timeout"` compatible
- [github-profile-analyzer #30](https://github.com/0xarchit/github-profile-analyzer/pull/30) — refined evidence-weighted impact scoring
- [GitFut #125](https://github.com/Younesfdj/gitfut/pull/125) — open upstream; derives active years from annual GitHub contribution windows instead of owned-repository timestamps, with focused regression coverage.

## 📌 September 28, 2026 update

### 🔥 Current OSS state

- **NVIDIA garak #2234** — **open upstream**; fixes paraphrase compatibility with newer Transformers by removing the deprecated custom-generation dependency and `trust_remote_code`, with focused regression coverage.
- **Microsoft PyRIT #2762** — **merged upstream**; dataset summary API accepted after multiple substantive review rounds. Merge commit: `47c6151a`.
- **Microsoft PyRIT #2823** — **merged upstream**; preserves non-empty HarmBench contextual behavior prompts with regression coverage. Merge commit: `940a8efabb404d80f6a716c5e641d81809d8972a`.
- **NousResearch Hermes Agent #126144** — **merged upstream** on September 28, 2026; broader desktop/session routing work incorporates and credits #121771's stale gateway-ref recovery. **#121771 was closed as superseded after the fix landed in #126144.**
- **collective/icalendar #1835** — **open upstream**; resolves inconsistent `DTEND` + `DURATION` handling with focused regression coverage.
- **NVIDIA garak #2234** — **open upstream**; removes the deprecated `transformers-community/group-beam-search` custom-generation path and `trust_remote_code` requirement from the `Fast` paraphrase buff, retaining native group-beam-search parameters with regression coverage.
- **aios #2458** — **merged upstream** on September 24, 2026; records provider `finish_reason="length"` as `output_truncated=true` with streaming regression coverage. Merge commit: `fe051b2c`.
- **RisingWave #27181** — **open upstream**; correlated-reference regression now exercises the real `LogicalApply → ApplyEliminateRule → to_batch()` boundary, including a non-first-row `LogicalValues` reference.
- **KiroCrew #12861** — **open upstream**; bounded PDF extraction and child-process protocol handling hardened.
- **TopoCore #1** — **open upstream**; deterministic cycle detection added for repeated spatial execution states.
- **LlamaIndex #23201** — **open upstream**; retrieved scores preserved during prev-next expansion.
- **OpenHands #17579** — **open upstream**; condenser metadata aligned with the agent-server minimum.
- **Coder #29668** — **open upstream**; unknown AI Gateway client deduplication.
- **Cloudflare quiche #2758 / #2759** — **open upstream**; custom-CA peer verification and Reno non-in-flight ACK handling.
- **IntelliJ PowerShell #506** — **open upstream**; PowerShell executable reparse-point resolution.
- **N3MO #39** — **open upstream**; Ruby/Kotlin routing regression coverage.

### 🧪 Fork-side / prepared work

- **SiYuan #1** — expired Streamable HTTP MCP session recovery with exactly one safe replay for `mcp.ErrSessionMissing`.
- **garak #1** — unset `soft_probe_prompt_cap=None` handling in `IterativeProbe`.
- **Inspect AI #1** — base64 encoding for Google inline-image bytes.
- **RAMPART #1** — adaptive multi-turn XPIA execution.
- **RAMPART #2** — generic PyRIT converter bridge; text-to-text adapter with focused regression coverage.
- **PyRIT fork #1** — canonical technique names in scenario run summaries.
- **PyRIT fork — #2839 fix** — short-prompt handling in `TemplateSegmentConverter`, prepared on September 26, 2026.

> **Evidence rule:** merged means upstream accepted it; open means the PR is still under review/CI; fork-side means the work exists on a fork and is not represented as upstream acceptance.


## 📅 September 26, 2026 — Ledger refresh

### GitFut #125 opened upstream

- **Younesfdj/gitfut #125** — **open upstream on September 26, 2026**; derives `active_years` from annual GitHub contribution windows rather than owned-repository timestamps, covering organization-only activity and unavailable annual windows with focused tests.


### Agent-Bench #8 merged upstream

- **PicadoLabs/agent-bench #8** — **merged upstream on September 26, 2026** after approval. The reviewer confirmed the command palette implementation looked good and the build passed; a small `useEffect` → `onClick` trigger refactor was pushed before merge.

### New prepared PyRIT work

- **PyRIT #2839** — prepared fork-side fix for `TemplateSegmentConverter` when the prompt has fewer words than template parameters. The production change is one line; regression coverage was added for the two-word/three-parameter case. It is not labeled as upstream acceptance because the PR could not be created through the current integration.

## 📅 September 25, 2026 — Ledger refresh

- **collective/icalendar #1835** — **open upstream**; fixes the start/end/duration mismatch reported in #1796. The implementation prefers explicit `DURATION` when both `DTEND` and `DURATION` are present and adds regression coverage.

The Atlas has been reconciled against the current PR state.

- **PyRIT #2823** — **merged upstream** on September 25, 2026. Merge commit: `940a8efabb404d80f6a716c5e641d81809d8972a`. Preserves non-empty HarmBench ContextString in behavior prompts, retains context metadata, and adds regression coverage.
- **Hermes Agent #121771 → #126144** — the standalone stale-gateway recovery PR was closed as superseded after #126144 incorporated and credited the fix. The upstream PR now carries the recovery logic as part of the broader desktop/session routing change.
- **RisingWave #27181** — latest requested regression and ctx.clone() compile issue were addressed; no new actionable review work is visible.
- **SiYuan #1, TopoCore #1, Inspect AI #1, MVT #939, quiche #2756/#2758/#2759, Linguist #1, AI Platform AWS #4, GoalAI #1** — no new code changes required from the latest review/status pass; these remain maintainer/deployment waiting states.

### Evidence boundary

- **Merged upstream** is reserved for upstream-accepted work.
- **Open upstream** means the contribution remains under review or CI.
- **Fork-side** means the work exists on a fork without an upstream acceptance claim.
- **Waiting** is not presented as a technical failure.

The ledger is intentionally evidence-first: no activity is manufactured just to make the contribution count look larger.
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

GitHub Actions validates the Atlas on pushes and pull requests, audits the external OSS ledger daily, and refreshes the dashboard cards automatically. Standard Actions are pinned to immutable commit SHAs.

## 🧱 Repository architecture

```text
oss-atlas/
├── contributions/
│   ├── INDEX.md
│   ├── ALL_PR_HISTORY.md
│   ├── merged/
│   ├── open/
│   └── closed/
├── data/
│   ├── contributions.json
│   └── skills.json
├── case-studies/
├── research/
├── experiments/
├── learnings/
├── assets/\n│   └── dashboard/\n│       ├── overview.svg\n│       ├── status.svg\n│       ├── repositories.svg\n│       └── actions.svg\n├── stats/
├── templates/
├── docs/
│   ├── OPERATING_MODEL.md
│   ├── AUTOMATION.md
│   └── ROADMAP.md
└── .github/workflows/
    ├── ci.yml
    └── atlas-audit.yml
```

## 📐 Evidence standard

**Observed** — GitHub state, issue/PR text, CI, tests, reviews, or maintainer statements.

**Implemented** — code or documentation actually present in a contribution branch/commit.

**Verified** — validation actually run or explicitly confirmed by an upstream maintainer.

**Interpretation** — engineering lessons inferred from evidence.

An open PR is never called merged. A targeted test run is never called a full-suite pass. Fork-side work is never presented as upstream acceptance.

## 🔭 Direction

OSS Atlas is evolving from a contribution list into a version-controlled OSS engineering knowledge base.

The current implementation already has:

- canonical machine-readable contribution metadata
- evidence-derived skill mapping
- deterministic structure/link validation
- GitHub-state drift auditing
- daily scheduled auditing
- dated historical snapshots
- deep contribution case studies
- explicit upstream/fork provenance

Next layers are review timelines, stale-record detection, generated snapshots, evidence bundles, and analytics.

**Evidence density over activity-count inflation.**

---

**Profile:** https://github.com/aspire488  
**OSS automation:** https://github.com/aspire488/gh-ops

<sub>Built in the open. Recorded with evidence. Updated as the work evolves.</sub>
