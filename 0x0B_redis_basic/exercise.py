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


def call_history(method: Callable) -> Callable:
    """Store call inputs and outputs for a method."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", output)
        return output

    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls for a particular function."""
    redis_client = redis.Redis()
    name = method.__qualname__
    calls = redis_client.get(name)
    calls_count = int(calls.decode("utf-8")) if calls else 0
    print(f"{name} was called {calls_count} times:")

    inputs = redis_client.lrange(f"{name}:inputs", 0, -1)
    outputs = redis_client.lrange(f"{name}:outputs", 0, -1)

    for arg, output in zip(inputs, outputs):
        print(f"{name}(*{arg.decode('utf-8')}) -> {output.decode('utf-8')}")


class Cache:
    """Represents a Redis cache."""

    def __init__(self) -> None:
        """Initialize Redis client and reset the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return a generated key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key