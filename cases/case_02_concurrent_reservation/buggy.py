import asyncio


class Inventory:
    def __init__(self, available: int):
        self.available = available

    async def reserve(self, quantity: int) -> bool:
        snapshot = self.available

        # Simulate an I/O boundary between read and write.
        await asyncio.sleep(0)

        if snapshot < quantity:
            return False

        self.available = snapshot - quantity
        return True
