#!/usr/bin/env python3
"""Redis basic cache module."""

from typing import Union
from uuid import uuid4

import redis


class Cache:
    """Represents a Redis cache."""

    def __init__(self) -> None:
        """Initialize Redis client and reset the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return a generated key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key