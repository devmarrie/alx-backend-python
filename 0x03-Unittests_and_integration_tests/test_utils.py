#!/usr/bin/env python3
"""
Parameterize a unittest
"""
import unittest
from utils import access_nested_map, get_json
from typing import Dict, Tuple, Union
from parameterized import parameterized
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """
    Handles the get json method
    """
    @patch('test_utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self,
                      mock_get_json: Mock,
                      url: str,
                      test_payload: Dict):
        """
        Use existing requests using patch
        set up mock response and return it
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get_json.return_value = mock_response
        res = get_json(url)
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(res, test_payload)


if __name__ == "__main__":
    unittest.main()