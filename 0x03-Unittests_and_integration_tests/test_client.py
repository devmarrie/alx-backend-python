#!/usr/bin/env python3
"""
Testing the client.py
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    class to implement the tests
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json",)
    def test_org(self, org_name: str, mock_get_json: Mock):
        """
        Tests the org method
        """
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name))
