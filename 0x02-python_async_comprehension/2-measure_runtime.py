#!/usr/bin/env python3
"""Run time for four parallel comprehensions
using asyncio.gather
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Excecute for time in paralel
    using asyncio.gather and measures the time of execution
    and returns the total execution time
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time() - start
    return end
