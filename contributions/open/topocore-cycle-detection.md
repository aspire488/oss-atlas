# TopoCore — Spatial Execution Cycle Detection

**Project:** [KARAN-D05/TopoCore](https://github.com/KARAN-D05/TopoCore)

**Pull request:** [#1](https://github.com/KARAN-D05/TopoCore/pull/1)

**Status:** Open upstream

## Problem

The spatial execution visualizer could continue indefinitely when execution entered a deterministic cycle.

## Change

Added visited-state tracking using `(X, Y, Direction)` and a step counter. When a previously visited spatial state is encountered, autoplay stops and the simulator reports the cycle.

## Design rationale

Because TopoCore defines execution through spatial position and traversal direction, the complete execution state must include all three values rather than position alone.

## Validation

The fork branch was compared against `main` and contained the intended focused simulator change without unrelated divergence.
