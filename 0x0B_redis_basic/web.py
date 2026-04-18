#!/usr/bin/env python3
"""Web page cache and access tracker using Redis."""

from functools import wraps
from typing import Callable

import redis
import requests

redis_client = redis.Redis()


def count_url_access(method: Callable) -> Callable:
    """Track URL accesses and cache fetched HTML for 10 seconds."""

    @wraps(method)
    def wrapper(url: str) -> str:
        redis_client.incr(f"count:{url}")

        cached = redis_client.get(f"cached:{url}")
        if cached:
            return cached.decode("utf-8")

        html = method(url)
        redis_client.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """Fetch and return HTML content for a URL."""
    return requests.get(url).text