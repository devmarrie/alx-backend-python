#!/usr/bin/env python3
"""Takes a string k , int or float
as an argument and returns a tuple
Args:
    - k: A string representing the key of the tuple.
    - v: An integer or a float representing the value of the tuple.

    Returns:
    - A tuple containing the string k and the square of v as a float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return string k  and the square of v """
    return (k, v**2)
