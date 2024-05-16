import os

import pytest
from playwright.sync_api import Page, expect

from dotenv import load_dotenv

load_dotenv()

BASE_URL = '127.0.0.1:8000'
USER_NAME = os.getenv('USER_NAME')
USER_PASSWORD = os.getenv('USER_PASSWORD')


# https://playwright.dev/python/docs/writing-tests#using-fixtures
@pytest.fixture(scope="function", autouse=True)
def go_to_page(page: Page):
    """Go to ``BASE_URL`` after each function."""
    page.goto(BASE_URL)


class TestHomePage:
    """Home page test."""

    def test_page_content(self, page: Page):
        """Test home page content."""
        expect(page).to_have_title('Домашняя страница')
        headline = page.get_by_test_id('headline')
        expect(headline).to_contain_text('Домашняя страница')


class TestAuth:
    """Auth test.

    The page transition to URL will not be saved for another method.
    """

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, page: Page):
        """Go to login url after each function."""
        page.goto(f'{BASE_URL}/users/login/')

    def test_go_to_login(self, page: Page):
        """Test go to login page via click."""
        page.goto(BASE_URL)
        button = page.locator('#login-nav')
        expect(button).to_contain_text('Войти')
        button.click()

    def test_page_content(self, page: Page):
        """Test login page content."""
        expect(page).to_have_title('Вход в приложение')
        headline = page.get_by_test_id('headline')
        expect(headline).to_contain_text('Вход в приложение')

    def test_login(self, page: Page):
        """Test login and logout."""
        # user data input
        page.locator('#id_username').fill(USER_NAME)
        page.locator('#id_password').fill(USER_PASSWORD)

        # check login button
        button = page.get_by_test_id('login-button')
        button.click()
        assert page.url == f'http://{BASE_URL}/'

        # check logout button
        button = page.locator('#logout-nav')
        expect(button).to_contain_text('Выйти')
        button.click()
        assert page.url == f'http://{BASE_URL}/'

        # check logout status
        button = page.locator('#login-nav')
        expect(button).to_contain_text('Войти')
