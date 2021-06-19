from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        """Реализует проверку страницы логина"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Реализует проверку, что подстрока "login" есть в текущем url браузера"""
        print(f'CURRENT URL', self.browser.current_url)
        assert "/login" in self.browser.current_url, "login is absent in current url"

    def should_be_login_form(self):
        """Реализует проверку, что есть форма логина на странице"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Реализует проверку, что есть форма регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
