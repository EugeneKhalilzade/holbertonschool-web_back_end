#!/usr/bin/env python3
"""
Async Comprehension module
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    result = [number async for number in async_generator()]
    return result
