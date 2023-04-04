#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
from queue import PriorityQueue
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.
        input - priority queue and tasks
        return - list of tasks
    """
    delay = PriorityQueue()
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    for r in results:
        delay.put(r)
    return [delay.get() for _ in range(n)]
