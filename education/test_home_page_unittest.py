import unittest

import pytest
from playwright.sync_api import Page, expect, sync_playwright


@unittest.skip
class TestHomePage(unittest.TestCase):
    """Playwright test with unittest.TestCase without changing the page state.

    The page transition to URL will not be saved for another method.
    """

    base_url = None

    # https://playwright.dev/python/docs/test-runners#using-with-unittesttestcase
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.page.goto(self.base_url)

    def test_title(self):
        expect(self.page).to_have_title('Домашняя страница')

    def test_headline(self):
        locator = self.page.get_by_test_id('headline')
        expect(locator).to_contain_text('Домашняя страница')


class TestAuth(unittest.TestCase):
    """Playwright test with unittest.TestCase with changing the page state.

    Notes
    -----

    Has a single attribute ``page`` for all methods.
    The ``page`` transition to another URL will be saved for another method.
    """

    @classmethod
    def setUpClass(cls):
        """Start playwright."""
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()
        cls.page = cls.browser.new_page()
        cls.page.goto('127.0.0.1:8000')

    @classmethod
    def tearDownClass(cls):
        """Stop playwright."""
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()

    def test_click_login(self):
        locator = self.page.locator('#login-nav')
        expect(locator).to_contain_text('Войти')
        locator.click()

    def test_title(self):
        expect(self.page).to_have_title('Вход в приложение')

    def test_headline2(self):
        locator = self.page.get_by_test_id('headline')
        expect(locator).to_contain_text('Вход в приложение')

