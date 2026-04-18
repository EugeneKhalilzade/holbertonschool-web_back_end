#!/usr/bin/env python3
"""Redis basic cache module."""

from functools import wraps
from typing import Callable, Union
from uuid import uuid4

import redis


def count_calls(method: Callable) -> Callable:
    """Count how many times a method is called."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Represents a Redis cache."""

    def __init__(self) -> None:
        """Initialize Redis client and reset the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return a generated key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key