import pytest
from playwright.sync_api import Page


class ReloadPageTestMixin:

    # https://playwright.dev/python/docs/test-runners#using-with-unittesttestcase
    def __init__(self):
        self.page = None
        self.base_url = None

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.page.goto(self.base_url)
