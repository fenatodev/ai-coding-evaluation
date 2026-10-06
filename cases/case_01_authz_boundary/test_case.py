import pytest

from cases.case_01_authz_boundary import buggy, fixed


@pytest.mark.xfail(
    strict=True,
    reason="buggy implementation ignores the caller tenant",
)
def test_buggy_blocks_cross_tenant_read():
    with pytest.raises(PermissionError):
        buggy.get_order(202, actor_tenant_id="alpha")


def test_fixed_blocks_cross_tenant_read():
    with pytest.raises(PermissionError):
        fixed.get_order(202, actor_tenant_id="alpha")


def test_fixed_allows_same_tenant_read():
    order = fixed.get_order(101, actor_tenant_id="alpha")
    assert order["id"] == 101
    assert order["tenant_id"] == "alpha"
