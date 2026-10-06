from cases.case_05_pr_review_transaction.repository import InMemoryRepository


class InsufficientFunds(Exception):
    pass


class InvalidAmount(Exception):
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

    if amount <= 0:
        raise InvalidAmount(amount)

    # Resolve every required dependency before mutating state.
    source = repo.get_account(source_id)
    target = repo.get_account(target_id)

    if source.balance < amount:
        raise InsufficientFunds(source_id)

    source.balance -= amount
    target.balance += amount

    result = {
        "request_id": request_id,
        "status": "completed",
        "amount": amount,
    }
    repo.mark_processed(request_id, result)
    return result
