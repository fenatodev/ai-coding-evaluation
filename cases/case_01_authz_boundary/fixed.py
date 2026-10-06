ORDERS = {
    101: {"id": 101, "tenant_id": "alpha", "total": 120},
    202: {"id": 202, "tenant_id": "beta", "total": 450},
}


def get_order(order_id: int, actor_tenant_id: str) -> dict:
    """Return an order only when it belongs to the caller's tenant."""
    order = ORDERS[order_id]
    if order["tenant_id"] != actor_tenant_id:
        raise PermissionError("order is outside caller tenant")
    return dict(order)
