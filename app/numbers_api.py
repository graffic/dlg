"""Numbers API module

Contains a fake API client
"""
import asyncio
from typing import List

DUMMY_DATA = tuple(range(1000001))


class NumbersAPI:
    """Fake API client"""
    async def get(self) -> List[int]:
        """Get a list of numbers with a one second delay"""
        await asyncio.sleep(1)
        return DUMMY_DATA

    def __eq__(self, other) -> bool:
        """Implements the == operator. Useful in tests"""
        return type(other) is NumbersAPI
