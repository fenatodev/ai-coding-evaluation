from cases.case_05_pr_review_transaction.repository import InMemoryRepository


class InsufficientFunds(Exception):
    pass


def transfer(
    repo: InMemoryRepository,
    *,
    request_id: str,
    source_id: str,
    target_id: str,
    amount: int,
) -> dict:
    existing = repo.get_processed(request_id)
    if existing is not None:
        return existing

    source = repo.get_account(source_id)
    if source.balance < amount:
        raise InsufficientFunds(source_id)

    # Candidate patch added idempotency here, before the operation is complete.
    source.balance -= amount
    repo.mark_processed(
        request_id,
        {
            "request_id": request_id,
            "status": "accepted",
            "amount": amount,
        },
    )

    target = repo.get_account(target_id)
    target.balance += amount

    result = {
        "request_id": request_id,
        "status": "completed",
        "amount": amount,
    }
    repo.mark_processed(request_id, result)
    return result
