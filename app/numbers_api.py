"""Numbers API module

Contains a fake API client
"""
import asyncio
from typing import List


class NumbersAPI:
    """Fake API client"""
    async def get(self) -> List[int]:
        """Get a list of numbers with a one second delay"""
        await asyncio.sleep(1)
        return list(range(10000001))

    def __eq__(self, other) -> bool:
        """Implements the == operator. Useful in tests"""
        return type(other) is NumbersAPI
