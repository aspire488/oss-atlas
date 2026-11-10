# Microsoft PyRIT #4108 — reviewed implementation

**Atlas tag:** REVIEWED  
**Review activity:** Issue-thread review comment (not a formal GitHub PR review submission)  
**Review date:** 2026-11-10  
**PR author:** `nniiovoo`  
**PR outcome:** Merged upstream on 2026-11-10  
**Merge commit:** `99f0214f5f8588d0058939dd9bd5876754213fd8`

## Source

- [Microsoft PyRIT PR #4108](https://github.com/microsoft/PyRIT/pull/4108)
- [Joel's review comment](https://github.com/microsoft/PyRIT/pull/4108#issuecomment-6757979223)
- [PR review timeline](https://github.com/microsoft/PyRIT/pull/4108/reviews)

## What was reviewed

The PR fixes `get_seed_groups_async` dropping matching seeds without a `prompt_group_id` when grouped matches are also present.

The implementation retains ungrouped matches and appends them after the expanded grouped results. The regression coverage checks mixed grouped/ungrouped objectives, `group_length=[1]`, and multiple ungrouped plus multiple grouped matches with uniqueness assertions.

## Review recorded

On November 10, 2026, Joel (`aspire488`) posted an issue-thread review comment stating that:

- Preserving ungrouped seeds before expanding grouped matches addresses the reported data-loss scenario.
- The regression test covers the regular objective query and `group_length=[1]`.
- Existing group-expansion behaviour appeared preserved, with no obvious blocking issue in the reviewed diff.
- An additional mixed-case test with multiple ungrouped and grouped seeds was worth considering to verify deduplication.

The PR subsequently merged into upstream `main`.

## Attribution and ledger boundary

This PR was **not authored or opened by aspire488**. The Atlas external-contribution ledger tracks authored PRs, so #4108 must not be added to `data/contributions.json` or counted in contribution totals.

The review was an issue-thread comment, not a formal GitHub PR review submission. The formal-review-only `data/reviews.json` remains unchanged. This research record preserves the review activity without misrepresenting either authorship or review type.
