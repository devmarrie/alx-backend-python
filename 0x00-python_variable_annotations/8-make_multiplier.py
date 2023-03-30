#!/usr/bin/env python3
"""Multiplies float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Args:
    - multiplier: A float multiplier.

    Returns:
    - A function that takes a float as an argument and returns
    the product of that float and the input multiplier.
    """
    def called_multiplier(f: float) -> float:
        return f * multiplier

    return called_multiplier
