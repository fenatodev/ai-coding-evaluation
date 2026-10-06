# Candidate change summary

The candidate patch attempted to add request-level idempotency.

Conceptually, it changed the transfer flow from:

~~~text
validate
→ debit source
→ credit target
→ return
~~~

to:

~~~text
check request id
→ validate source
→ debit source
→ mark request accepted
→ resolve target
→ credit target
→ mark request completed
~~~

The intended goal was to prevent duplicate transfers.

The review challenge is to determine whether the new ordering preserves atomicity and retry semantics.
