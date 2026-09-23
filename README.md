<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:70a5fd&height=210&section=header&text=OSS%20Atlas&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Open-source%20engineering%20ledger&descAlignY=58&descSize=16" width="100%"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Focus-Open%20Source%20Engineering-70a5fd?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Living%20Ledger-2ea44f?style=for-the-badge"/>
</p>

# OSS Atlas

**OSS Atlas** is my dedicated open-source engineering ledger.

It records what I contribute, what maintainers verify, what gets merged, what remains open, and what I learn from working in unfamiliar codebases.

> **Observed → Implemented → Verified → Documented**

This repository is intentionally **OSS-only**. Personal projects, product prototypes, KIO, AURA, UEA, portfolio material, and unrelated engineering work belong in their own repositories.

---

## 🗺️ Live OSS Dashboard

| Track | Purpose |
|---|---|
| **Merged** | Accepted upstream contributions |
| **Open** | Active upstream and fork-side work |
| **Research** | Architecture reviews and technical investigations |
| **Discussions** | Engineering discussions with maintainers/communities |
| **Case Studies** | Deeper write-ups of significant contributions |
| **Learnings** | Durable lessons extracted from OSS work |
| **Stats** | Historical contribution evidence |

---

## ✅ Merged Upstream Contributions

### aios

- **[PR #2457 — Preserve `length` finish reason across streaming trailers](https://github.com/eumemic/aios/pull/2457)**  
  Preserves provider-reported `finish_reason="length"` through streaming assembly and adds regression coverage.

- **[PR #2460 — Preserve LiteLLM parameter translation](https://github.com/eumemic/aios/pull/2460)**  
  Preserves provider-specific parameter translation while retaining explicit `allowed_openai_params` overrides, with regression coverage.

### GitHub Profile Analyzer

- **[PR #30 — Evidence-weighted impact scoring](https://github.com/0xarchit/github-profile-analyzer/pull/30)**  
  Refined impact scoring with repository-quality evidence and improved viewport-aware factor handling. **Merged upstream on September 23, 2026.**

> These merged records are intentionally kept here even when the profile README only highlights a subset.

---

## 🔥 Active OSS Work

### Microsoft PyRIT

- **[PR #2762 — Dataset Summary API](https://github.com/microsoft/PyRIT/pull/2762)** — **Open upstream**  
  Adds memory-backed dataset summaries. Substantive maintainer concerns were iterated through and verified against real stored data, including:
  - aggregation and logical-example counting
  - SQLite collation behavior
  - unnamed/whitespace dataset identity
  - selection-key isolation
  - metadata query-size behavior
  - `loaded_only` semantics

  A follow-up test-cleanup commit was subsequently pushed to the branch. The PR remains open pending final upstream disposition.

- **[#2782 — Canonical technique names in scenario summaries](https://github.com/aspire488/PyRIT/tree/fix/promptinject-technique-summary)** — **Fork-side**  
  Uses the persisted canonical `technique_name` rather than a potentially goal/objective-bearing display group, with regression coverage.

### NVIDIA garak

- **[PR #1 — Handle unset soft prompt cap in IterativeProbe](https://github.com/aspire488/garak/pull/1)** — **Open fork PR**  
  Treats `soft_probe_prompt_cap=None` as uncapped while preserving existing capped behavior.

### UK AI Security Institute Inspect AI

- **[PR #1 — Base64 encode Google inline image bytes](https://github.com/aspire488/inspect_ai/pull/1)** — **Open fork PR**  
  Encodes raw `Blob.data` bytes before constructing the Google inline-image data URI, with binary-image regression coverage.

### TopoCore

- **[PR #1 — Detect repeated spatial execution states](https://github.com/KARAN-D05/TopoCore/pull/1)** — **Open upstream**  
  Adds deterministic cycle detection using the complete `(X, Y, Direction)` execution state.

---

## 🔎 Upstream Review & Architecture Work

OSS Atlas also records contributions that are not conventional code PRs.

- **[Agent Substrate #1104](https://github.com/agent-substrate/substrate/pull/1104)** — reviewed a dual-stack egress regression test and identified the need to exercise the actual broken-IPv6 → IPv4 fallback condition.
- **[Agent Sandbox #1615](https://github.com/kubernetes-sigs/agent-sandbox/issues/1615)** — discussed responsibility boundaries for routing requests across multiple claimed Sandboxes.

---

## 💬 Technical Discussions

Selected engineering discussions are kept here when they contain reusable implementation reasoning:

- **[Lexical #8771](https://github.com/facebook/lexical/discussions/8771)** — named slots and paginated editor architecture.
- **[MCP Registry #921](https://github.com/modelcontextprotocol/registry/discussions/921)** — published Docker image and PostgreSQL-backed deployment.
- **[VS Code Discussions #3109](https://github.com/microsoft/vscode-discussions/discussions/3109)** — diagnosing Electron main-process hangs.
- **[MVT discussions](https://github.com/mvt-project/mvt/discussions)** — STIX indicator parsing and edge cases.
- **[OpenAI Codex #46658](https://github.com/openai/codex/discussions/46658)** — adaptive allocation, verification, reassessment, and agent feedback loops.

---

## 🧪 Research & Experiments

This repository may contain bounded OSS experiments and investigations when they produce reusable engineering evidence.

The rule is simple:

> An experiment belongs here only when it teaches something about open-source engineering, an upstream codebase, a maintainer workflow, or a reusable technical pattern.

Product prototypes and personal system development are deliberately excluded.

---

## 📁 Repository Structure

```text
oss-atlas/
├── contributions/
│   ├── open/
│   ├── merged/
│   └── closed/
├── research/
├── experiments/
├── case-studies/
├── learnings/
├── stats/
├── templates/
├── docs/
│   ├── OPERATING_MODEL.md
│   └── ROADMAP.md
└── README.md
```

---

## 📐 Evidence Standard

Every record should distinguish:

**Observed** — what GitHub, tests, CI, issues, reviews, or maintainers actually show.

**Implemented** — what exists in a contribution branch or commit.

**Verified** — what was actually tested or explicitly verified.

**Interpretation** — what was learned from the work.

No contribution is described as merged unless GitHub shows it as merged upstream.

Fork-side work is explicitly labelled as fork-side.

---

## 🔭 Direction

OSS Atlas is intended to become a machine-readable and human-readable OSS engineering ledger.

Planned capabilities:

- upstream status tracking
- contribution metadata
- historical snapshots
- broken-link checks
- contribution dashboards
- review/maintainer-response tracking
- skill mapping derived from actual engineering evidence
- automated freshness checks

The goal is **evidence density, not activity-count inflation**.

---

## 🔗 Links

- **Profile:** https://github.com/aspire488
- **OSS automation:** https://github.com/aspire488/gh-ops

<sub>Built in the open. Recorded with evidence. Updated as the work evolves.</sub>
