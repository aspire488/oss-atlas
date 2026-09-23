# TopoCore — Deterministic Cycle Detection

**Upstream:** [KARAN-D05/TopoCore #1](https://github.com/KARAN-D05/TopoCore/pull/1)  
**Status:** Open upstream as of 2026-09-23

## Problem

The spatial execution simulator could continue indefinitely when its cursor entered a cycle.

## Implementation

The contribution tracks visited spatial states using:

`(X, Y, Direction)`

Revisiting the same state is treated as deterministic evidence that execution has entered a cycle, allowing autoplay to stop.

The change also adds a visible step counter and resets the execution trace when Reset/Clear is used.

## Compatibility

Existing movement and directional semantics are intentionally preserved.

## Verification recorded in the PR

- visited-state tracking added
- step counter added
- Reset/Clear trace reset covered
- branch verified one commit ahead of `main` with no divergence

## Lesson

When a system's execution state is deterministic, cycle detection can often be expressed as a compact state invariant rather than a time-based escape hatch.

The PR remains open, so Atlas does not treat the change as upstream accepted.
