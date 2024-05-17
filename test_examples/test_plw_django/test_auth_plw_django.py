# Rase exceptions when run pytest:
# - django.core.exceptions.SynchronousOnlyOperation: You cannot call
# this from an async context - use a thread or sync_to_async.
# or
# ```settings.py
#    if DEBUG:
#        os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'```
# - playwright._impl._errors.Error: It looks like you are
# using Playwright Sync API inside the asyncio loop.
import os
from urllib.parse import urljoin

import pytest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import expect, sync_playwright

LOGIN_PATH = 'users/login/'

TEST_USERNAME = os.getenv('TEST_USERNAME')
TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD')


class TestAuth(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()

    @pytest.mark.django_db()
    def test_user_authentication_page(self):
        """Test user authentication page."""
        page = self.browser.new_page()
        page.goto(urljoin(self.live_server_url, LOGIN_PATH))
        expect(page).to_have_title('Вход в приложение')

        page.locator('#id_username').fill(TEST_USERNAME)
        page.locator('#id_password').fill(TEST_USER_PASSWORD)
        submit = page.get_by_test_id('login-button')
        submit.click()
        expect(page).to_have_title('Домашняя страница')
