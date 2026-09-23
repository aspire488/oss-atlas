# OpenAI Agents Python — Compaction Session State Clearing

**Project:** [openai/openai-agents-python](https://github.com/openai/openai-agents-python)

**Issue:** #4864

**Status:** Contribution prepared

## Problem

Clearing a compaction session could retain response-chain state that should no longer be reused.

## Change

Successful session clearing resets the stored response identifiers, while a failed clear preserves the existing state. Regression tests cover both behaviors and the requirement for a new response after clearing.

## Validation

The contribution branch was checked with targeted memory tests and static tooling; the full-suite result is intentionally not claimed here.
