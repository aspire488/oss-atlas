# Hermes Agent #148989 — pending-restart banner review

**PR:** [NousResearch/hermes-agent #148989](https://github.com/NousResearch/hermes-agent/pull/148989)  
**Author:** [Wang-Zephyr](https://github.com/Wang-Zephyr)  
**Current status:** Reopened · open as of November 20, 2026  
**Status history:** Closed, then reopened on November 20, 2026; neither event was a merge.  
**Review activity:** One formal GitHub review submission (COMMENTED), followed by an issue-thread review follow-up.

## What changed

The PR proposed improving the pending-fleet-restart startup banner so it identifies stale gateway profiles, their PIDs, and the corresponding per-profile restart command.

The initial review identified a correctness problem in _collect_stale_fleet_rows(): selecting every state except current would incorrectly label external and restart_pending rows as gateways owed a restart.

## Review findings and author response

The review requested:

- An explicit diagnostic-state whitelist (stale, unknown, and down).
- Regression tests proving external and restart_pending are omitted.
- Filtering against profiles covered by the pending update obligation, including multiplexer served_profiles.
- Marker-aware filtering using the marker's own inventory, with fail-closed behavior for empty, legacy, malformed, or unsupported inventories.

The author addressed the feedback in additive commits, culminating in [be7e842](https://github.com/NousResearch/hermes-agent/commit/be7e84248aa2daafe6ae5c0ee3dbd7ffbeb7b422). The author reported 55 tests passing and clean ruff check results on the changed files.

## Final follow-up

On November 9, the updated head and full two-file diff were reviewed. The requested state filtering, obligation scoping, marker-aware behavior, and regression coverage were present; no remaining blocking correctness issue was identified. The GitHub Actions runs associated with that head were action_required, with no jobs available to inspect, so CI execution was not independently confirmed.

The author closed the PR on November 20, then reopened it shortly afterward (as shown by the two GitHub notification emails). GitHub currently reports the PR as **open**, unmerged, and with `aspire488` listed as a requested reviewer. Treat it as active again; the earlier closure is historical, not the current outcome.

## Record boundaries

- This is review work on another contributor's PR, not an authored contribution.
- It does not change the external authored-PR totals.
- The formal review is represented in data/reviews.json; the substantive discussion and final outcome are documented here.

## Sources

- [Pull request and current state](https://github.com/NousResearch/hermes-agent/pull/148989)
- [Review commit with final changes](https://github.com/NousResearch/hermes-agent/commit/be7e84248aa2daafe6ae5c0ee3dbd7ffbeb7b422)
