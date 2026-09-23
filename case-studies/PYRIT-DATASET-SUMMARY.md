# PyRIT — Dataset Summary API

**Upstream:** [microsoft/PyRIT #2762](https://github.com/microsoft/PyRIT/pull/2762)  
**Status:** Open upstream as of 2026-09-23

## Problem

Add a read-only dataset-summary surface without hydrating seed values, reading media, or invoking provider fetches.

## Implementation

The endpoint adds memory-backed summaries for loaded/provider availability, logical examples, seed pieces, objectives, modalities, harm categories, unlabeled-harm presence, and stable selection keys.

The implementation uses a narrow metadata projection over existing seed storage rather than introducing a new schema.

## Review-driven correctness

Maintainer feedback exposed edge cases around:

- NULL versus empty dataset names
- named `__unnamed__` versus the unnamed population
- logical-example double counting
- SQLite collation semantics
- metadata join cardinality
- fixture modality ordering
- `loaded_only=true` with empty memory

## Verification

Maintainer verification covered real stored seeds, unnamed grouping, selection-key isolation, NOCASE/RTRIM collation, metadata query-size reduction, a 1,200-seed probe producing three metadata rows, and empty-memory `loaded_only` behavior.

## Lesson

Aggregate APIs over relational data need explicit identity, null/empty semantics, collation, and join-cardinality contracts. Correctness is more than returning the right fields.

The PR remains open pending final upstream disposition.
