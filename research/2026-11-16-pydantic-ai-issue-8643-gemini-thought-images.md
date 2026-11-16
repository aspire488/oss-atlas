# Pydantic AI #8643 — Gemini interim thought images in non-streaming responses

> **Outcome: upstream issue resolved · not an authored/merged PR by Joel.** Observed November 16, 2026.

## Issue

- Repository: [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
- Issue: [#8643 — `GoogleModel` returns Gemini's interim thought images as output when not streaming](https://github.com/pydantic/pydantic-ai/issues/8643)
- Original reporter: `mosafariuk`
- Closed: November 16, 2026
- Closing PR: [#8644 — Drop Gemini's interim thought images from non-streaming `GoogleModel` responses](https://github.com/pydantic/pydantic-ai/pull/8644)

## Joel's participation

Joel (`aspire488`) commented on the issue offering to implement the matching `thought=True` handling and regression tests, and asked to be assigned if the proposed approach was acceptable.

That comment records interest and a willingness to contribute. It does **not** establish that Joel implemented the fix or authored the closing PR.

## Upstream resolution

GitHub reports issue #8643 as closed via PR #8644. The PR metadata identifies its author as `pydanty[bot]`; its description says it was posted by Claude Code on behalf of David. It was merged upstream.

The merged change filters Gemini inline image parts marked `thought=True` from the non-streaming response mapping, matching the existing streaming behavior. The PR adds recorded regression coverage for non-streaming image output and a hand-built streaming guard test.

- PR: https://github.com/pydantic/pydantic-ai/pull/8644
- Merge commit: `afefc5c292e371996903e6ab89aa9bc6af1d36ef`

## Ledger treatment

- Record this as **issue participation / volunteered implementation**, with the upstream issue now resolved.
- Do **not** add PR #8644 to Joel's authored contribution ledger or merged-PR totals.
- Do **not** count this as a code review: the available evidence is an issue comment offering to take the work, not a review of someone else's PR.

## Evidence checked

- Issue #8643: closed; original author `mosafariuk`; closed November 16, 2026.
- Issue comment by `aspire488`: offers to implement the fix and requests assignment.
- PR #8644: merged; author `pydanty[bot]`; merge commit recorded above.
