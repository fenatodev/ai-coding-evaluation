import pytest

from cases.case_05_pr_review_transaction.models import Account
from cases.case_05_pr_review_transaction.repository import (
    AccountNotFound,
    InMemoryRepository,
)
from cases.case_05_pr_review_transaction import service_buggy, service_fixed


def make_repo() -> InMemoryRepository:
    return InMemoryRepository(
        [
            Account(account_id="source", balance=100),
        ]
    )


@pytest.mark.xfail(
    strict=True,
    reason="candidate patch debits and records idempotency before target lookup",
)
def test_buggy_failed_transfer_is_atomic():
    repo = make_repo()

    with pytest.raises(AccountNotFound):
        service_buggy.transfer(
            repo,
            request_id="req-1",
            source_id="source",
            target_id="missing",
            amount=40,
        )

    assert repo.get_account("source").balance == 100
    assert repo.get_processed("req-1") is None


def test_fixed_failed_transfer_is_atomic():
    repo = make_repo()

    with pytest.raises(AccountNotFound):
        service_fixed.transfer(
            repo,
            request_id="req-1",
            source_id="source",
            target_id="missing",
            amount=40,
        )

    assert repo.get_account("source").balance == 100
    assert repo.get_processed("req-1") is None


def test_fixed_retry_after_dependency_is_available_completes_once():
    repo = make_repo()

    with pytest.raises(AccountNotFound):
        service_fixed.transfer(
            repo,
            request_id="req-2",
            source_id="source",
            target_id="target",
            amount=40,
        )

    repo.add_account(Account(account_id="target", balance=10))

    first = service_fixed.transfer(
        repo,
        request_id="req-2",
        source_id="source",
        target_id="target",
        amount=40,
    )
    second = service_fixed.transfer(
        repo,
        request_id="req-2",
        source_id="source",
        target_id="target",
        amount=40,
    )

    assert first == second
    assert repo.get_account("source").balance == 60
    assert repo.get_account("target").balance == 50


def test_fixed_duplicate_request_does_not_double_transfer():
    repo = InMemoryRepository(
        [
            Account(account_id="source", balance=100),
            Account(account_id="target", balance=10),
        ]
    )

    first = service_fixed.transfer(
        repo,
        request_id="req-3",
        source_id="source",
        target_id="target",
        amount=25,
    )
    second = service_fixed.transfer(
        repo,
        request_id="req-3",
        source_id="source",
        target_id="target",
        amount=25,
    )

    assert first == second
    assert repo.get_account("source").balance == 75
    assert repo.get_account("target").balance == 35
