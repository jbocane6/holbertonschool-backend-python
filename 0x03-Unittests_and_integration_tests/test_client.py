#!/usr/bin/env python3
"""
Familiarize yourself with the client.GithubOrgClient class.
Declare the TestGithubOrgClient(unittest.TestCase) class
and implement the test_org method.
This method should test that GithubOrgClient.org returns the correct value.
Use @patch as a decorator to make sure get_json is called once
with the expected argument but make sure it is not executed.
Use @parameterized.expand as a decorator to parametrize the test
with a couple of org examples to pass to GithubOrgClient, in this order:
    google
    abc
Of course, no external HTTP calls should be made.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    client.GithubOrgClient class.
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mk_obj):
        """
        Should test that GithubOrgClient.org returns the correct value.
        """
        tst_cls = GithubOrgClient(org_name)
        tst_cls.org()
        mk_obj.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name))

    def test_public_repos_url(self):
        """
        Implement the test_public_repos_url method to
        unit-test GithubOrgClient._public_repos_url.
        Use patch as a context manager to patch GithubOrgClient.org
        and make it return a known payload.
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mk:
            pload = {'repos_url': 'test'}
            mk.return_value = pload
            tst_cls = GithubOrgClient('test')
            rslt = tst_cls._public_repos_url
            self.assertEqual(rslt, pload['repos_url'])
