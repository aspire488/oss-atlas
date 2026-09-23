# aios — Streaming Termination Semantics

**Upstream:** [eumemic/aios #2457](https://github.com/eumemic/aios/pull/2457)  
**Status:** Merged upstream on 2026-09-23

## Problem

A provider can emit `finish_reason="length"` at the streaming boundary. Losing that signal during trailer assembly prevents downstream layers from correctly identifying length-limited output.

## Change

The contribution preserves the provider termination reason through streaming assembly and adds regression coverage while retaining existing content-filter precedence.

## Follow-up

[aios #2458](https://github.com/eumemic/aios/pull/2458) carries the now-reliable signal into loop-level truncation telemetry and adds an end-to-end streaming regression.

## Lesson

A semantic event can span multiple transport messages. Streaming implementations must preserve that meaning until the layer responsible for user-visible interpretation.

## Evidence

GitHub reports #2457 merged upstream. The follow-up #2458 remains open and is recorded separately.
