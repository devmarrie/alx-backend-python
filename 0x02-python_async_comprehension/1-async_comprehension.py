#!/usr/bin/env python3
"""Async comprehensions
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Do an asynchronous comprehension of async_generator
    """
    result = [i async for i in async_generator()]
    return result