from cases.case_05_pr_review_transaction.models import Account


class AccountNotFound(Exception):
    pass


class InMemoryRepository:
    def __init__(self, accounts: list[Account]):
        self.accounts = {account.account_id: account for account in accounts}
        self.processed: dict[str, dict] = {}

    def get_account(self, account_id: str) -> Account:
        try:
            return self.accounts[account_id]
        except KeyError as exc:
            raise AccountNotFound(account_id) from exc

    def add_account(self, account: Account) -> None:
        self.accounts[account.account_id] = account

    def get_processed(self, request_id: str) -> dict | None:
        result = self.processed.get(request_id)
        return dict(result) if result is not None else None

    def mark_processed(self, request_id: str, result: dict) -> None:
        self.processed[request_id] = dict(result)
