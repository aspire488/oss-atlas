# OpenHands — Settings Contract Alignment

**Upstream:** [OpenHands/OpenHands #17579](https://github.com/OpenHands/OpenHands/pull/17579)  
**Status:** Open upstream as of 2026-09-23

## Problem

The Condenser Max Number of Events setting had a mismatch between the frontend metadata and the backend contract.

The PR identifies two concrete defects:

- the frontend metadata key used `condenser.condenser_max_size` while the real setting key is `condenser.max_size`
- the frontend minimum was `0` while the backend contract requires `ge=20`

## Implementation

The contribution:

- aligns the metadata key with the actual setting
- raises the minimum to 20
- aligns MSW mocks with the backend settings shape
- adds regression coverage for -1, 19, and 20
- preserves blank input coercion to `null`

## Verification recorded in the PR

The author reports local Windows/Node 24 validation using npm and Vitest, including lint/typecheck/prettier checks and 113 tests across four files.

## Lesson

Configuration systems are contracts across layers. A constraint is ineffective when the UI key does not reach the actual field, and a UI constraint is misleading when it diverges from the backend domain contract.

The PR remains open; the recorded local verification is not represented as upstream acceptance.
