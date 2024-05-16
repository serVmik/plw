import os
import unittest

from dotenv import load_dotenv
from playwright.sync_api import expect

from mixins.utittest_mixin import (
    MutablePageTestMixin,
)

load_dotenv()


class HomePageTest:
    """Home page test by 'Playwright' with 'unittest'.

    Can use:
        -- without page navigation
        -- without reload page for each method.
    """

    def test_title(self):
        expect(self.page).to_have_title('Домашняя страница')

    def test_header(self):
        expect(self.page).to_have_title('Домашняя страница')


class AuthTest:
    """Auth test by 'Playwright' with 'unittest'.

    Use:
        -- with page navigation.
        -- with load page when going to the new page.
    """
    
    base_url = None
    user_name = None
    user_password = None
    
    def test_go_to_login(self):
        """Test go to login page via click."""
        page = self.page
        assert page.url == f'http://{self.base_url}/'
        # button
        button = page.locator('#login-nav')
        expect(button).to_contain_text('Войти')
        button.click()

    def test_login(self):
        """Test login and logout."""
        page = self.page
        assert page.url == f'http://{self.base_url}/users/login/'
        # user data input
        page.locator('#id_username').fill(self.user_name)
        page.locator('#id_password').fill(self.user_password)
        # submit
        submit = page.get_by_test_id('login-button')
        submit.click()

    def test_login_redirect(self):
        """Test redirect login after clock submit."""
        page = self.page
        assert page.url == f'http://{self.base_url}/'
        # button
        button = page.locator('#logout-nav')
        expect(button).to_contain_text('Выйти')


class TestHomePageMutable(HomePageTest, MutablePageTestMixin):
    """Home page test by mutable playwright page."""

    base_url = '127.0.0.1:8000'


class TestHomePageReloaded(AuthTest, MutablePageTestMixin):
    """Home page test by reloaded playwright page.

    Don't do that!
    the order of execution of modules is sorted alphabetically by module names.

    Use python fixtures.
    """

    base_url = '127.0.0.1:8000'
    user_name = os.getenv('USER_NAME')
    user_password = os.getenv('USER_PASSWORD')


if __name__ == '__main__':
    unittest.main()
