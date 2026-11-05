# PyRIT: General scorer identifier configuration

**Observed:** November 5, 2026  
**Status:** Draft fork-side proposal; not submitted upstream  
**Repository:** [aspire488/PyRIT](https://github.com/aspire488/PyRIT)  
**PR:** [#5](https://github.com/aspire488/PyRIT/pull/5)  
**Target issue:** [microsoft/PyRIT #3839](https://github.com/microsoft/PyRIT/issues/3839)  
**Branch:** `fix/self-ask-output-keys-3839`

## Problem

The general True/False and float-scale scorers wrap their configured response handlers. Their component identifiers included the requested JSON schema, but did not include the wrapped handler's replay identifier. Different parser configurations—especially custom response output-key names—could therefore produce indistinguishable scorer identifiers.

## Change

The draft adds `self._response_handler._get_replay_identifier()` to the identifier parameters of:

- `SelfAskGeneralTrueFalseScorer`
- `SelfAskGeneralFloatScaleScorer`

This captures stable parser configuration from the wrapped response handler while retaining the existing response-schema field.

## Regression coverage

A parameterized test module covers five constructor output-key options for each scorer:

- `score_value_output_key`
- `rationale_output_key`
- `description_output_key`
- `metadata_output_key`
- `category_output_key`

The tests assert that changing each configured key changes the scorer identifier. This produces ten parameterized cases.

## Validation and limitations

- The code and test changes were committed to the personal fork.
- The draft PR was checked through GitHub and is currently open.
- **The test suite has not been executed in this environment.** No passing-test claim is made.
- The PR targets the fork's `main`, not `microsoft/PyRIT` upstream. It is a prepared fork-side proposal only.
- It is excluded from the external upstream contribution totals until an actual upstream PR exists.

## Evidence

- [Draft PR #5](https://github.com/aspire488/PyRIT/pull/5)
- [Upstream issue #3839](https://github.com/microsoft/PyRIT/issues/3839)
- [True/False scorer implementation](https://github.com/aspire488/PyRIT/blob/fix/self-ask-output-keys-3839/pyrit/score/true_false/self_ask_general_true_false_scorer.py)
- [Float-scale scorer implementation](https://github.com/aspire488/PyRIT/blob/fix/self-ask-output-keys-3839/pyrit/score/float_scale/self_ask_general_float_scale_scorer.py)
- [Regression tests](https://github.com/aspire488/PyRIT/blob/fix/self-ask-output-keys-3839/tests/unit/score/test_general_scorer_output_key_identifiers.py)
