ORDERS = {
    101: {"id": 101, "tenant_id": "alpha", "total": 120},
    202: {"id": 202, "tenant_id": "beta", "total": 450},
}


def get_order(order_id: int, actor_tenant_id: str) -> dict:
    """Return an order visible to the caller.

    BUG: actor_tenant_id is accepted but never enforced.
    """
    order = ORDERS[order_id]
    return dict(order)
