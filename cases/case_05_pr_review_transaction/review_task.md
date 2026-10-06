# PR review task

A pull request adds idempotency to a transfer service.

## Product requirements

A transfer must:

1. return the previous successful result when the same `request_id` is retried;
2. never debit the source account if the transfer cannot complete;
3. never report a request as processed before the transfer is complete;
4. support retry after a transient dependency failure;
5. avoid double transfer on duplicate successful requests.

Review `service_buggy.py` against the repository and tests.

Do not limit review to syntax or style. Identify behavioral defects, explain impact, and propose the smallest safe fix plus regression coverage.
