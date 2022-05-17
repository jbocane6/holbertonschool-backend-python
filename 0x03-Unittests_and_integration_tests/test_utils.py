#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function
and understand its purpose.
Play with it in the Python console to make sure you understand.
First, Write the unit test for utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method to test
that the method returns what it is supposed to.
Decorate the method with @parameterized.expand
to test the function for following inputs:
"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    First unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Use the assertRaises context manager to test that a KeyError is raised.
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Define the TestGetJson(unittest.TestCase) class
    and implement the TestGetJson.test_get_json method to test
    that utils.get_json returns the expected result.
    We don’t want to make any actual external HTTP calls.
    Use unittest.mock.patch to patch requests.get.
    Make sure it returns a Mock object with a json method
    that returns test_payload which you parametrize alongside
    the test_url that you will pass to get_json with the following inputs:
        test_url="http://example.com", test_payload={"payload": True}
        test_url="http://holberton.io", test_payload={"payload": False}
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that utils.get_json returns the expected result.
        """
        with patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
