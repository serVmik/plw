# Playwright with Pytest tests

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from mixins.mixins_pytest import PageFixtureMixin
from test_examples.conditions import HomePageTest

load_dotenv()

BASE_URL = '127.0.0.1:8000'


@pytest.fixture(scope="function", autouse=True)
def setup(page: Page):
    """Reload page for each class method."""
    page.goto(BASE_URL)


class TestHomePage:
    """"""

    def test_page_title(self, page: Page):
        """Test home page title."""
        expect(page).to_have_title('Домашняя страница')

    def test_page_headline(self, page: Page):
        """Test home page title."""
        headline = page.get_by_test_id('headline')
        expect(headline).to_have_text('Домашняя страница')


class TestHomePageFixture(HomePageTest, PageFixtureMixin):
    """"""

    base_url = BASE_URL
