import pytest
from playwright.sync_api import Page


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
        def test_header(self, page: Page):
            expect(page).to_have_title('GitHub')
    """
    page.goto('base_url')


class PageFixtureMixin:
    """Page fixture mixin.

    Use reloaded ``page`` (`Page`) fixture for each class method.
    """

    page = None
    base_url = None

    # https://playwright.dev/python/docs/test-runners#using-with-unittesttestcase
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Reload page for each class method."""
        self.page = page
        self.page.goto(self.base_url)
