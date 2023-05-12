#!/usr/bin/env python3
"""
Parameterize a unittest
"""
import unittest
from utils import access_nested_map
from typing import Dict, Tuple, Union
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    write the first unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]) -> None:
        """
        Remember to decorate with parameterized
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple,
                                         ) -> None:
        """
        Raises a keyerror
        when the parameterized values are used
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
