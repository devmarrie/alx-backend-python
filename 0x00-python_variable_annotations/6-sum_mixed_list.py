#!/usr/bin/env python3
"""Function
  input:mixed list of integers and floats
  output:sum as floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum it then float it"""
    return float(sum(mxd_lst))
