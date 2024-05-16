import os
import unittest

from dotenv import load_dotenv

from mixins.mixins_unittest import MutablePageTestMixin
from test_examples.conditions import HomePageTest, AuthTest

load_dotenv()

BASE_URL = '127.0.0.1:8000'
USER_NAME = os.getenv('USER_NAME')
USER_PASSWORD = os.getenv('USER_PASSWORD')


@unittest.skip
class TestHomePageUnittest(HomePageTest, MutablePageTestMixin):
    """Home page test by mutable playwright page."""

    base_url = BASE_URL


@unittest.skip
class TestAuthUnittest(AuthTest, MutablePageTestMixin):
    """Home page test by reloaded playwright page.

    Don't do that!
    the order of execution of modules is sorted alphabetically by module names.

    Use python fixtures.
    """

    base_url = BASE_URL
    user_name = USER_NAME
    user_password = USER_PASSWORD


if __name__ == '__main__':
    unittest.main()
