import os

import pytest
from django.core.management import call_command
from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()

FIXTURE_PATH = 'tests/fixtures/wse-fixtures-3.json'


# https://pytest-django.readthedocs.io/en/latest/database.html#populate-the-test-database-if-you-don-t-use-transactional-or-live-server
# https://pytest-django.readthedocs.io/en/latest/database.html#populate-the-test-database-if-you-use-transactional-or-live-server
@pytest.fixture(scope='class')
def django_db_setup(django_db_blocker):
    """Load fixtures to test database.

    Overrides django_db_setup fixture.
    Mark tests with the @pytest.mark.django_db().
    """
    with django_db_blocker.unblock():
        call_command('loaddata', FIXTURE_PATH)


@pytest.fixture(scope='function')
def test_page(page: Page, live_server) -> Page:
    """Return page with started server."""
    page.goto(live_server.url)
    return page


@pytest.fixture(scope="session", autouse=True)
def set_env():
    """Pass environment variables to pytest."""
    os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
