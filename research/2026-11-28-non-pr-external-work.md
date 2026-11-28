# Non-PR External Work and Project Engagements

> Email-verified record of external work, technical evaluations, research participation, and project collaborations. This archive is separate from the authored-PR ledger. It does not change PR counts.

**Evidence cutoff:** 2026-11-28  
**Primary evidence:** Gmail correspondence in the account; links below are included where the correspondence provides a public artifact.

## Completed technical work

### XERJ Reader-1 — independent API evaluation and QA

- **Counterparty:** Ivan Novikov / XERJ
- **Period:** November 2026
- **Status:** Evaluation completed; structured findings delivered.
- **Work:** Tested Reader-1 through approximately 400 API calls and several hundred questions. Evaluated evidence grounding, numerical accuracy, deterministic execution, adversarial inputs, long-document behaviour, and performance. Compared Reader-1 with a general LLM on a 137-question test set.
- **Reported findings:** More than 900 checked evidence spans matched their source text; repeated executions reproduced programs; 0 failures across 23 prompt-injection tests. Reported defects included negative currency values becoming positive, aggregation omitting records above six items, stale corrections being preferred over later email corrections, and overconfident incorrect answers (11/71 answers above 0.9 confidence were wrong). Also reported DOCX table, scanned-PDF, SDK retry, time-calculation, authentication, error-leakage, and confidence-calibration issues.
- **Deliverable:** Structured technical report with reproducible findings, prioritised recommendations, and an offer of synthetic documents and reproduction scripts.
- **Boundary:** These are Joel's reported test results, not independently re-run Atlas measurements. No subsequent confirmation of fixes was found in the reviewed email thread.
- **Classification:** External QA / technical evaluation; not an authored PR or formal code review.

### OpenAI Agents Python SDK — compaction response-state fix (#4864)

- **Repository:** [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- **Issue:** [#4864](https://github.com/openai/openai-agents-python/issues/4864)
- **Period:** September 23–28, 2026
- **Status:** Patch and regression tests submitted to OpenAI Support for maintainer review; acceptance or merge not confirmed.
- **Work:** Prepared a fix in [Joel's fork branch](https://github.com/aspire488/openai-agents-python/tree/fix/4864-clear-compaction-response-state) to reset `_response_id`, `_deferred_response_id`, and `_last_unstored_response_id` after a successful `clear_session()`, while preserving state if the backend clear fails.
- **Tests:** Regression coverage for successful reset, failed-clear preservation, and preventing stale `previous_response_id` reuse. Joel reported formatting, lint, type-check and relevant memory tests passing.
- **Support handoff:** OpenAI Support case 15670816. Branch tip `0be04a1661dc1e74351bdc054f4481dbf9bf1d94`; commits `5c6cd164dc064966acc69febfb80b81df5a23b1e` and `0be04a1661dc1e74351bdc054f4481dbf9bf1d94`. [Unified patch](https://github.com/aspire488/openai-agents-python/compare/main...fix/4864-clear-compaction-response-state.patch).
- **Boundary:** Support said it would forward the patch to the appropriate internal team / maintainers. This is not evidence of acceptance or implementation.

## External adoption of Joel's own work

### Pipo 3D world — selected for XERJ Corpus Hub

- **Counterparty:** XERJ Corpus Hub
- **Period:** October–November 2026
- **Status:** Selected and published with attribution.
- **Work reused:** Joel's existing Pipo 3D-world implementation, described in the correspondence as a 10-file, approximately 3,800-line JavaScript implementation.
- **Outcome:** Joel approved inclusion under Pipo's MIT licence with attribution; XERJ published a contributor page.
- **Links:** [Contributor page](https://hub.xerj.org/contributors/aspire488) · [Pipo repository](https://github.com/aspire488/Pipo).
- **Boundary:** This was adoption of Joel's existing project work, not a new implementation commissioned by XERJ.

## Completed non-code research participation

### Beihang University — open-source onboarding and generative AI survey

- **Researcher:** Kai Zheng, Beihang University
- **Date:** November 28, 2026
- **Status:** Survey submitted; receipt acknowledged by researcher.
- **Subject:** Newcomer barriers in OSS and how generative AI affects understanding unfamiliar codebases, project conventions, issue selection, implementation and review.
- **Classification:** Research participation based on personal OSS experience; not engineering implementation, research authorship, or a publication.

## Active evaluations and proposed collaborations — not completed deliverables

### ChatSorter — comparison with AURA memory

- **Contact:** Jacob, ChatSorter
- **Thread period:** November 2026
- **Status:** Agreed to begin an evaluation; no completed findings recorded as of November 28.
- **Scope discussed:** Fact extraction, updates and conflict resolution across sessions, retrieval relevance, and operational behaviour. Joel proposed synthetic or redacted conversations and preferred the self-hosted route. He requested clarity on hosted data retention, deletion, model training, and staff access before using real AURA data.
- **Latest recorded step:** On November 28, Joel said he would review the API docs and start with the local trial / updated ChatSorter Local package.

### DSH Hermes Memory — possible memory-panel review and adaptation

- **Contact:** isheng-eqi
- **Status:** Discussion / invitation; no completed review or implementation evidenced.
- **Scope discussed:** Memory panel, persistence failures, editing workflow, and a possible adaptation informed by AURA.

### Kairo / Agensi.io — agent-skill marketplace discussion

- **Contact:** Joeri, Agensi.io
- **Status:** Commercial/product discussion; no published listing or integration evidenced.
- **Scope discussed:** Listing `kairo-email-intelligence` as an agent skill, email and company-data integrations, additional feature ideas, ownership/packaging, and proposed revenue sharing.
- **Boundary:** Kairo was still under development in the correspondence. Do not present the integration as shipped.

### gh-ops and UEA — proposed unpaid outreach trial

- **Contact:** Odeku Omotolani
- **Status:** Trial proposed; no completed campaign or delivered sample evidenced.
- **Scope discussed:** A sample outreach strategy for gh-ops and UEA, including relevant communities, sample posts, and GitHub Discussions with reasons for targeting.
- **Terms:** Joel explicitly stated the arrangement was unpaid and requested honest positioning because gh-ops was still under active development.
- **Boundary:** This was marketing/community outreach, not software engineering.

### Hanzo AI / AgentField — networking and beta invitation

- **Contact:** Hanzo AI co-CEO
- **Status:** Networking / beta invitation; no assigned task or completed deliverable evidenced.
- **Boundary:** Do not count as engineering work.

## Other project outreach — no resulting work evidenced

- **Virtual-companion developer outreach (November 23, 2026):** Joel contacted the developers of Thriveling, Rustle, Tamaweb, Pixel Fish Tank, Pawtiva, and WristPet to exchange product feedback as a fellow Android companion developer. The located messages document introductions and offers to exchange feedback, not completed reviews or code contributions to those projects.
- **Animated web-series collaboration (September 14, 2025):** Joel sent collaboration proposals to three creators around an original multi-season animated-series concept. No replies or resulting collaboration were found in the reviewed threads.
- **OSS Atlas growth discussion:** Discussed visibility/outreach for Joel's own OSS Atlas project. No completed external implementation or campaign evidenced.
- **ZeroApply contractor matching:** A Python contracting profile was said to be active, but no client brief, contract, or paid engagement had been offered in the reviewed correspondence. This is an opportunity lead, not completed work.

## Counting and deduplication rules

1. This file is the canonical home for the non-PR engagements above. Do not copy these entries into `data/contributions.json` or the authored-PR history; that ledger is explicitly PR-only.
2. A project may appear in more than one section only when the relationship is materially different. XERJ Reader-1 QA and XERJ's adoption of Pipo are separate activities and must remain distinct.
3. Do not count invitations, proposals, networking, planned evaluations, or unanswered outreach as completed work.
4. Do not convert the OpenAI support handoff into a merged contribution.
5. Do not count survey participation as engineering or research authorship.
6. Update status in place when new evidence arrives; do not create a second record for the same engagement.
