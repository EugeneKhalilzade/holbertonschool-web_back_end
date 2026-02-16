#!/usr/bin/env python3
"""
Module that defines an async routine which runs wait_random multiple times
and returns the delays in ascending order.
"""

import asyncio
from typing import List
from heapq import heappush, heappop

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns wait_random `n` times with the specified `max_delay`
    and returns a list of delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay allowed for each wait_random call.

    Returns:
        List[float]: List of delays returned from wait_random,
        sorted in ascending order.
    """
    heap = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in tasks:
        delay = await task
        heappush(heap, delay)

    delays = [heappop(heap) for _ in range(n)]
    return delays
