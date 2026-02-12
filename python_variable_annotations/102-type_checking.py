#!/usr/bin/env python3
"""
Module that provides a function to zoom (duplicate)
elements of a tuple.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list where each element of the input tuple
    is repeated `factor` times.

    Args:
        lst (Tuple): A tuple of elements.
        factor (int): Number of times each element is repeated.

    Returns:
        List: A list containing duplicated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
