# Case 02 — Concurrent reservation

## Finding

**Severity: High**

The buggy reservation flow performs a read/modify/write across an async scheduling point without synchronization.

With one unit available, two concurrent callers can both read 1, both decide stock is sufficient, and both return success.

The final counter can still look valid at 0, which makes the defect easy to miss if tests inspect only stored state rather than successful allocations.

## Evidence

The test launches two reservations concurrently against inventory with one available unit.

Expected invariant: successful reservations cannot exceed available units.

Buggy result: two callers return success while final available is still 0.

## Root cause

The decision and mutation are not atomic.

## Minimal fix

Protect the check-and-decrement critical section with an async lock.

## Regression coverage

The fixed test asserts both that exactly one caller succeeds and inventory reaches zero.

## Review note

For concurrent workflows, validating only final state may be insufficient. Tests should also validate externally observable outcomes and invariants.
