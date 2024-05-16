import os
import unittest

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from mixins.mixins_pytest import PageFixtureMixin
from test_examples.conditions import HomePageTest, HomePageFixtureTest

load_dotenv()

BASE_URL = '127.0.0.1:8000'
USER_NAME = os.getenv('USER_NAME')
USER_PASSWORD = os.getenv('USER_PASSWORD')


class TestHomePagePytest(HomePageTest, PageFixtureMixin):
    """"""

    base_url = BASE_URL


class TestHomePagePytestFixture(HomePageFixtureTest, PageFixtureMixin):
    """"""

    base_url = BASE_URL


@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    """Reload page for each class method.

    Example
    -------
    URL = 'https://github.com/'

    @pytest.fixture(scope='function', autouse=True)
    def setup(page: Page):
        page.goto('base_url)

    class TestGitHubHomeTitle:

        def test_title(self, page: Page):
            expect(page).to_have_title('GitHub')
    """
    page.goto(BASE_URL)


class TestHomePagePytestFunctionFixture(HomePageFixtureTest):
    """"""

    base_url = BASE_URL


if __name__ == '__main__':
    unittest.main()
