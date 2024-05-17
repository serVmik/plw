import pytest


@pytest.fixture(scope="class")
def page(browser):
    """Yield testing page at the specified address.

    The page goes to the specific url. Url is required.

    Parameters
    ----------
    browser : `Browser`
        Pytest fixture.
    Yields
    ------
    page : `Page`
        Playwright page at the specified address.
    """
    page = browser.new_page()
    base_url = 'BASE_URL'
    page.goto(base_url)
    yield page
    page.close()
