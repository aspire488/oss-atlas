# PyRIT — Canonical Technique Names in Scenario Summaries

**Project:** [microsoft/PyRIT](https://github.com/microsoft/PyRIT)

**Status:** Open / fork-side

## Problem

Scenario run summaries could expose a display-oriented grouping value where consumers need the persisted canonical technique identifier.

## Change

Updated response construction to use the persisted canonical `technique_name`, with the existing scenario-derived fallback when a plan is unavailable.

## Regression coverage

The regression distinguishes `display_group` from `technique_name` and verifies that the canonical identifier is returned.

## Evidence

The fork-side implementation and its tests are the source of truth for the current state.
