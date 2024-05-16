from playwright.sync_api import expect


class AuthTest:
    """Auth test."""

    base_url = None
    user_name = None
    user_password = None

    def test_go_to_login(self, page):
        """Test go to login page via click."""
        # check page url
        assert page.url == f'http://{self.base_url}/'
        # button
        button = page.locator('#login-nav')
        expect(button).to_contain_text('Войти')
        button.click()

    def test_login(self, page):
        """Test login and logout."""
        # check page url
        assert page.url == f'http://{self.base_url}/users/login/'
        # user data input
        page.locator('#id_username').fill(self.user_name)
        page.locator('#id_password').fill(self.user_password)
        # submit
        submit = page.get_by_test_id('login-button')
        submit.click()

    def test_login_redirect(self, page):
        """Test redirect login after clock submit."""
        # check page url
        assert page.url == f'http://{self.base_url}/'
        # check link
        link = page.locator('#logout-nav')
        expect(link).to_contain_text('Выйти')
