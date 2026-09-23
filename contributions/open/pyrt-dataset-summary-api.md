# PyRIT — Dataset Summary API

**Project:** [microsoft/PyRIT](https://github.com/microsoft/PyRIT)

**Type:** Feature / API

**Status:** Open upstream

## What changed

Added a read-only dataset summary API that exposes dataset selection keys, loaded/provider state, logical example counts, seed-piece counts, objectives, modalities, harm categories, and related metadata.

## Engineering focus

- Aggregation semantics
- Dataset/provider distinctions
- SQLite collation behavior
- Unnamed dataset handling
- Query-size reduction
- Loaded-only behavior
- Regression coverage

## Upstream review

The implementation was reviewed with regression cases covering collation, unnamed datasets, provider-only datasets, and loaded-only behavior.

## Evidence

See the upstream PyRIT pull request and review discussion for the authoritative state.
