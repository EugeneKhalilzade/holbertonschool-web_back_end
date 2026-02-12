#!/usr/bin/env python3
"""
This module defines a function that returns the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)
