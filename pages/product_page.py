from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Класс описывает страниуц продкута"""
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT)
        button.click()
        self.solve_quiz_and_get_code()

        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_product_description()
        self.should_be_add_button()
        self.should_be_success()

    def should_be_product_name(self):
        """Проверяет наличие названия продукта"""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name not found"

    def should_be_product_price(self):
        """Проверяет наличие цены продукта"""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price not found"

    def should_be_product_description(self):
        """Проверяет наличие описания продукта"""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Product description not found"

    def should_be_add_button(self):
        """Проверяет наличие кнопки 'Добавить в корзину'"""
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_PRODUCT), "Button 'Добавить в корзину' is not " \
                                                                                 "presented"

    def should_be_success(self):
        """Проверяет наличие сообщения об успешном добавлении товара в корзину"""
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES_PRODUCT_NAME), "The message about the " \
                                                                                            "successful addition of " \
                                                                                            "the product to the " \
                                                                                            "basket was not found "

    def should_match_product_name(self):
        """Проверяет, что название товара в сообщении об успешном добавлении
        товара в корзину соответствует заголовку товара"""
        product_name = self.get_text_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_basket = self.get_text_element(*ProductPageLocators.SUCCESS_MESSAGES_PRODUCT_NAME)
        assert product_name == product_name_in_basket, "The product name doesn't match the product name in the basket"

    def should_match_product_price(self):
        """Проверяет, что цена товара в сообщении об успешном добавлении
        товара в корзину соответствует цене, указанной в заголовке товара"""
        product_price = self.get_text_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_basket = self.get_text_element(*ProductPageLocators.SUCCESS_MESSAGES_PRODUCT_PRICE)
        assert product_price == product_price_in_basket, "The product price doesn't match the product price in the " \
                                                         "basket "

    def go_to_basket_from_product_page(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_SEE_BASKET)
        button_basket.click()

