#!/usr/bin/env python3
"""
This module defines a function that takes a string and a number (int or float),
and returns a tuple with the string and the square of the number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k and the square of v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The number to square.

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of v.
    """
    return (k, float(v ** 2))
