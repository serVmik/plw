from playwright.sync_api import expect, Page


class HomePageTest:
    """Home page test by 'Playwright' with 'unittest'.

    Can use:
        -- without page navigation
        -- without reload page for each method
    Can't use:
        -- with pytest ``page`` fixture
    """

    def test_page_title(self):
        """Test home page title."""
        expect(self.page).to_have_title('Домашняя страница')

    def test_page_headline(self):
        """Test home page title."""
        headline = self.page.get_by_test_id('headline')
        expect(headline).to_have_text('Домашняя страница')


class HomePageFixtureTest:
    """"

    Use:
        -- with pytest ``page`` fixture.
    """

    def test_page_title(self, page: Page):
        """Test home page title."""
        expect(page).to_have_title('Домашняя страница')

    def test_page_headline(self, page: Page):
        """Test home page title."""
        headline = page.get_by_test_id('headline')
        expect(headline).to_have_text('Домашняя страница')


class AuthTest:
    """Auth test by 'Playwright' with 'unittest'.

    Use:
        -- with page navigation.
        -- with load page when going to the new page.
    """

    page = None
    base_url = None
    user_name = None
    user_password = None

    def test_go_to_login(self):
        """Test go to login page via click."""
        # check page url
        page = self.page
        assert page.url == f'http://{self.base_url}/'
        # button
        button = page.locator('#login-nav')
        expect(button).to_contain_text('Войти')
        button.click()

    def test_login(self):
        """Test login and logout."""
        # check page url
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
        # check page url
        page = self.page
        assert page.url == f'http://{self.base_url}/'
        # button
        button = page.locator('#logout-nav')
        expect(button).to_contain_text('Выйти')
