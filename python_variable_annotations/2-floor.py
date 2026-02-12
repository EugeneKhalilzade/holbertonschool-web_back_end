#!/usr/bin/env python3
"""
This module defines a function that returns the floor of a float using
type annotations.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the given float.

    Args:
        n (float): The number to floor.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
