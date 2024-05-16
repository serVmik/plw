from playwright.sync_api import expect, Page


class HomePageTest:
    """Home page test."""

    def test_page_status(self, page: Page):
        """Test page status 200."""
        assert page.goto(page.url).ok

    def test_page_title(self, page: Page):
        """Test home page title."""
        expect(page).to_have_title('Домашняя страница')

    def test_page_headline(self, page: Page):
        """Test home page title."""
        headline = page.get_by_test_id('headline')
        expect(headline).to_have_text('Домашняя страница')

    def test_navbar_contain(self, page: Page):
        """Test navbar contain."""
        navbar = page.get_by_test_id('navbar-list')
        assert 'Регистрация' in navbar.text_content()
        assert 'Войти' in navbar.text_content()

