# Evaluation report template

## Summary

One or two sentences describing the observed behavior and why it matters.

## Severity

Critical | High | Medium | Low

Explain severity using reachable impact, not adjectives alone.

## Reproduction

~~~text
precondition
→ action
→ observed result
→ expected result
~~~

## Root cause

Identify the smallest code path or assumption responsible for the defect.

## Evidence

Reference the exact test, assertion, trace, or behavior that demonstrates the finding.

## Proposed fix

Describe the smallest safe correction.

## Regression tests

List the cases that should remain protected after the fix.

## Residual risk / uncertainty

State what was not verified, what requires broader integration testing, or what assumptions remain.
