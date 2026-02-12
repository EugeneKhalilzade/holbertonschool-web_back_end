#!/usr/bin/env python3
"""
Module that provides a function to safely retrieve
the first element of a sequence using duck typing.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence if it exists.

    Args:
        lst (Sequence[Any]): Any sequence (list, tuple, string, etc.)
            containing elements of unknown type.

    Returns:
        Optional[Any]: The first element of the sequence if it is not empty,
        otherwise None.
    """
    if lst:
        return lst[0]
    return None
