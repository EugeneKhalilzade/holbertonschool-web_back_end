#!/usr/bin/env python3
"""
Module that defines a function returning an asyncio.Task
for the wait_random coroutine.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that wraps wait_random with the given max_delay.

    Args:
        max_delay (int): Maximum number of seconds to wait.

    Returns:
        asyncio.Task: A Task object that will execute wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
