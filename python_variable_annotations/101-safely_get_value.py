#!/usr/bin/env python3
"""
Module that provides a function to safely retrieve
a value from a mapping with a default fallback.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value associated with a key in a mapping
    if the key exists, otherwise returns the default value.

    Args:
        dct (Mapping): A mapping object (e.g., dict).
        key (Any): The key to look for in the mapping.
        default (Union[T, None], optional): The value to return
            if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the mapping if the key exists,
        otherwise the provided default value.
    """
    if key in dct:
        return dct[key]
    return default
