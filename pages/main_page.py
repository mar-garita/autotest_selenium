from .base_page import BasePage  # импорт базового класса
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)  # символ * указывает на то, что передаем
        # именно пару, и этот кортеж нужно распаковать
        login_link.click()

    def should_be_login_link(self):
        """Метод проверяет наличие ссылки, которая ведет на логин"""
        # символ * указывает на то, что передаем именно пару, и этот кортеж нужно распаковать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
