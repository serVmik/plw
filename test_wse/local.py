import os
import unittest

import pytest
from dotenv import load_dotenv

from test_wse.auth_page import AuthTest
from test_wse.home_page import HomePageTest

load_dotenv()

BASE_URL = 'http://d45400kr.beget.tech/'
USER_NAME = os.getenv('USER_NAME')
USER_PASSWORD = os.getenv('USER_PASSWORD')


@pytest.fixture(scope="class")
def page(browser):
    page = browser.new_page()
    page.goto(BASE_URL)
    print('\nPage created')
    yield page
    page.close()


class TestHomePage(HomePageTest):
    """Home page test."""


class TestAuthPage(AuthTest):
    """Auth page test."""

    base_url = BASE_URL
    user_name = USER_NAME
    user_password = USER_PASSWORD
