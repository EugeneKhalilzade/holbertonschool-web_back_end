#!/usr/bin/env python3
"""
Module that defines task_wait_n, a coroutine that uses task_wait_random
to concurrently wait and return delays in ascending order.
"""

import asyncio
from typing import List
from heapq import heappush, heappop

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random `n` times with `max_delay` and returns the delays
    in ascending order.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in ascending order.
    """
    heap = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in tasks:
        delay = await task
        heappush(heap, delay)

    return [heappop(heap) for _ in range(n)]
