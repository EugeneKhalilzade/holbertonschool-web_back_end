#!/usr/bin/env python3
"""
This module defines a function that returns the sum of a list of integers
and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of mixed integers and
        floats.

    Returns:
        float: The sum of the elements in the list.
    """
    return float(sum(mxd_lst))
