#!/usr/bin/env python3
"""
Module for zooming (duplicating) elements of a sequence.
"""

from typing import List, Tuple, TypeVar

T = TypeVar('T')


def zoom_array(lst: Tuple[T, ...], factor: int = 2) -> List[T]:
    """
    Returns a list where each element of the input tuple
    is repeated `factor` times.

    Args:
        lst (Tuple[T, ...]): A tuple of elements of any type.
        factor (int): Number of times each element is repeated.

    Returns:
        List[T]: A new list with duplicated elements.
    """
    zoomed_in: List[T] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # must be int
