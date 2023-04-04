#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
   this function takes wait_n and alter it to a new funtion
    task_wait_n that returns float values
"""
import asyncio
from typing import List
from queue import PriorityQueue
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.
       takes two int arguments n : max_delay, wait_random
        returns a list of all delay(float values
    """
    delay = PriorityQueue()
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    for r in results:
        delay.put(r)
    return [delay.get() for _ in range(n)]
