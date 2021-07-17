from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        self.should_basket_empty()
        self.should_text_of_empty_basket()

    def should_basket_empty(self):
        """Проверяет, что в корзине нет товаров"""
        assert self.is_not_element_present(*BasketLocators.PRODUCT_IN_BASKET), \
            "Product is presented in basket, but should not be"

    def should_text_of_empty_basket(self):
        """Проверяет, что в корзине присутствует уведомление, что корзина пустая"""
        notification = self.get_text_element(*BasketLocators.TEXT_BASKET_EMPTY)
        # определяет язык браузера:
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        if language == "ru-RU":
            assert "Ваша корзина пуста" in notification, \
                "There is no notification that the basket is empty"
        elif language == "en-EN":
            assert "Your basket is empty" in notification, \
                "There is no notification that the basket is empty"
