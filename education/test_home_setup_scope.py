import os
import unittest

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect

load_dotenv()

BASE_URL = '127.0.0.1:8000'
USER_NAME = os.getenv('USER_NAME')
USER_PASSWORD = os.getenv('USER_PASSWORD')


class TestAuthSetUpClass(unittest.TestCase):
    """Apply SetUpClass.

    Don't use with go to urls!

    Notes
    -----
        -- Run methods alphabetically
        -- setUp once, when start class test
        -- tearDown once, when end class test
        -- Reuse page state
        -- Run test not applies --headed
    """

    base_url = BASE_URL

    @classmethod
    def setUpClass(cls):
        """Start playwright."""
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()
        cls.page = cls.browser.new_page()
        cls.page.goto(cls.base_url)

    @classmethod
    def tearDownClass(cls):
        """Stop playwright."""
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()

    def test_order_go_to_login(self):
        """Test go to login page via click."""
        page = self.page
        assert page.url == f'http://{BASE_URL}/'
        # button
        button = page.locator('#login-nav')
        expect(button).to_contain_text('Войти')
        button.click()

    def test_order_2_login(self):
        """Test login and logout."""
        page = self.page
        assert page.url == f'http://{BASE_URL}/users/login/'
        # user data input
        page.locator('#id_username').fill(USER_NAME)
        page.locator('#id_password').fill(USER_PASSWORD)
        # submit
        submit = page.get_by_test_id('login-button')
        submit.click()

    def test_order_3_login_redirect(self):
        """Test redirect login after clock submit."""
        page = self.page
        assert page.url == f'http://{BASE_URL}/'
        # button
        button = page.locator('#logout-nav')
        expect(button).to_contain_text('Выйти')
