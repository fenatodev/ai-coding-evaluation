# Case 05 — Multi-file PR review: transfer idempotency

## Finding 1

**Severity: Critical**

The candidate implementation mutates durable state before confirming that the transfer can complete.

It debits the source account and marks the request as processed before resolving the target account.

If target lookup fails:

- source funds are already reduced;
- the request is already recorded as accepted;
- the transfer is incomplete.

This violates the all-or-nothing invariant.

## Finding 2

**Severity: High**

The early idempotency record corrupts retry behavior.

After the failed attempt, a retry with the same request ID returns the stored `accepted` result immediately, even if the missing target later becomes available.

The retry never credits the target.

The combination creates a particularly bad failure mode:

~~~text
source debited
→ target not credited
→ retry suppressed
→ API may return apparent success
~~~

## Evidence

The proof test verifies two invariants after target lookup fails:

~~~text
source balance remains unchanged
request id is not marked processed
~~~

The buggy implementation violates both.

## Minimal fix

Resolve and validate every dependency before mutating balances or recording idempotency state.

For this in-memory example:

1. check for an already-completed request;
2. validate the amount;
3. resolve source and target;
4. validate funds;
5. mutate balances;
6. record the completed result.

## Production caveat

The fixed example demonstrates ordering, not a complete database transaction design.

In a real service, balance updates and the unique idempotency record should be committed atomically in one transaction, with concurrency handling around duplicate request IDs.

## Why this is a stronger review case

The candidate change is locally plausible: it adds an idempotency check and records progress.

The defect appears only when reviewing:

- mutation ordering;
- exception paths;
- retry semantics;
- state across multiple repository calls.

That is the kind of failure a useful code reviewer or coding-agent evaluator should detect.
