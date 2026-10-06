import asyncio

import pytest

from cases.case_02_concurrent_reservation import buggy, fixed


async def run_two_reservations(inventory):
    return await asyncio.gather(
        inventory.reserve(1),
        inventory.reserve(1),
    )


@pytest.mark.xfail(
    strict=True,
    reason="buggy implementation performs a non-atomic read/modify/write",
)
def test_buggy_prevents_double_allocation():
    inventory = buggy.Inventory(available=1)
    results = asyncio.run(run_two_reservations(inventory))

    assert sum(results) == 1
    assert inventory.available == 0


def test_fixed_prevents_double_allocation():
    inventory = fixed.Inventory(available=1)
    results = asyncio.run(run_two_reservations(inventory))

    assert sum(results) == 1
    assert inventory.available == 0
