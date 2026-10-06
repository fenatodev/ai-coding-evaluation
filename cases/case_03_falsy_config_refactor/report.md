# Case 03 — Falsy configuration refactor

## Finding

**Severity: Medium**

A concise refactor uses user.get(key) or default_value. That expression changes semantics: valid explicit values such as 0, False, and an empty string are treated as though the key were absent.

This represents a common class of generated refactor that looks idiomatic and shorter while silently changing behavior.

## Evidence

The proof test supplies three valid falsy values: retry_count 0, enabled False, and an empty label. The buggy implementation replaces all three with defaults.

## Root cause

Truthiness is being used as a proxy for presence. Those concepts are not equivalent.

## Minimal fix

Test whether the key exists, not whether its value is truthy.

## Regression coverage

The fixed tests verify that explicit falsy values survive the merge and defaults are used only when a key is absent.

## Review note

When reviewing generated refactors, shorter code should not receive a correctness presumption. Compare semantics around None, empty values, zero, false, ordering, exceptions, mutation and boundary conditions.
