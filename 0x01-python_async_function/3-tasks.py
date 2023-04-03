#!/usr/bin/env python3
import asyncio
"""Creating a task
"""
wait_random = __import__('0-basic_async_syntax').wait_random



def task_wait_random(max_delay: int) -> asyncio.Task:
    """ASyncio.createtask()
    """
    return asyncio.create_task(wait_random(max_delay))
