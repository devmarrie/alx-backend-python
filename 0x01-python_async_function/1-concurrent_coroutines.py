#!/usr/bin/env python3
import asyncio
from typing import List
from queue import PriorityQueue
wait_random = __import__('0-basic_async_syntax').wait_random
"""Let's execute multiple coroutines at the same time with async
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.
    """
    delay = PriorityQueue()
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    for r in results:
        delay.put(r)
    return [delay.get() for _ in range(n)]
