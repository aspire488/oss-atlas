# PyRIT XXE output-scorer: XInclude external resources

**Date:** 2026-10-21  
**Upstream issue:** [microsoft/PyRIT #3324](https://github.com/microsoft/PyRIT/issues/3324)  
**Contribution:** [microsoft/PyRIT #3429](https://github.com/microsoft/PyRIT/pull/3429)  
**Status:** Open upstream; not merged.

## Problem

The XXE output scorer's existing patterns did not cover XInclude elements that point to external resources. An emitted XInclude directive can reference a local file or a remote resource, so this is a detection-coverage gap for downstream consumers that process XML.

## Change

The contribution adds a pattern for prefixed or unprefixed include elements whose href uses file:, http:, https:, or ftp:. It also adds regression cases for:

- Local-file XInclude references such as file:///etc/passwd.
- Remote XInclude references.
- Relative href values, which should not match this external-scheme pattern.
- Unrelated XML elements with a file URL, which should not match.

## Validation boundary

A focused regex smoke test passed for local-file, remote-resource, relative-reference, unrelated-element, and unprefixed-include cases. The full PyRIT test suite has **not** been run in this environment. No live XML parser, filesystem access, or remote resource was executed; these are string-detection tests only.

## Evidence rule

This is an open proposal, not an accepted upstream change. Update its status only after GitHub shows a merge or closure.
