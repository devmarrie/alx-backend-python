#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
"""Creating a task
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ASyncio.createtask()
    """
    return asyncio.create_task(wait_random(max_delay))
