#!/usr/bin/env python3
"""Completing a type annotation function
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')
Res = Union[T, Any]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    if key in dct:
        return dct[key]
    else:
        return default
