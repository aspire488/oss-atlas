# VS Code Discussions #3109 — Electron main-process hang diagnostics

**Atlas tag:** TECHNICAL DISCUSSION  
**Activity:** Discussion comment and threaded reply  
**Author:** `aspire488`  
**Discussion:** [How do you diagnose Electron main process hangs in VS Code-like apps?](https://github.com/microsoft/vscode-discussions/discussions/3109)  
**Comment:** [Joel's reply](https://github.com/microsoft/vscode-discussions/discussions/3109#discussioncomment-19530051)  
**Date:** 2026-09-21

## Context

The discussion asks how Electron-based desktop applications can diagnose intermittent main-process hangs when the main event loop is blocked and normal IPC/UI debugging paths are unavailable.

## Contribution recorded

Joel's response contributes a practical diagnostic architecture and investigation workflow:

- Treat intermittent hangs as an observability problem; pre-arm diagnostics instead of depending on attaching a debugger after the failure.
- Track event-loop delay, CPU, RSS/heap, process/window IDs, recent IPC activity, and extension/plugin activity.
- Capture Node diagnostic reports where supported, while accounting for platform limitations (notably Windows signal-report limitations).
- Use an out-of-process watchdog to detect missed heartbeats and collect OS-level dumps when the main process cannot service its own diagnostics.
- Use Electron's inspector and live V8 profiling for JavaScript-level hangs, but use native OS tools for threads blocked in native calls.
- Distinguish event-loop starvation, synchronous/native blocking, IPC overload, and extension-host pressure using CPU posture, stacks, and process activity.
- Keep the Electron main process thin and move expensive or failure-prone work into utility/shared processes where possible.

The linked threaded reply engages with another participant's detailed technical explanation, emphasizing the boundary between JS-level and native-level inspection, the limits of SIGUSR1 when native code is blocking, and an escalation design of heartbeat/telemetry → external watchdog → OS-level capture.

## Attribution and ledger boundary

This is a **technical community discussion contribution**, not an authored pull request, merged code contribution, or formal GitHub PR review. It must not be added to `data/contributions.json`, `data/reviews.json`, or authored/merged PR totals. This research record preserves the technical discussion separately from code contributions.
