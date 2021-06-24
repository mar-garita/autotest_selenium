import pytest

from .pages.locators import UrlPages, ProductPageLocators
from .pages.product_page import ProductPage


@pytest.mark.xfail(reason="the test crashes")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Проверка, что нет сообщение об успехе, после добавления товара в корзину"""
    page = ProductPage(browser, UrlPages.PRODUCT_PAGE_URL)
    page.open()
    page.add_product_to_basket()  # добавление товара в корзину
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES_PRODUCT_NAME), \
        "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    """Проверяем, что нет сообщения об успехе, не добавляя товар в корзину"""
    page = ProductPage(browser, UrlPages.PRODUCT_PAGE_URL)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES_PRODUCT_NAME), \
        "Success message is presented, but should not be"


@pytest.mark.xfail(reason="the test crashes")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Проверяем, что сообщение об успехе, появившееся после добавления товара в корзину, исчезает"""
    page = ProductPage(browser, UrlPages.PRODUCT_PAGE_URL)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES_PRODUCT_NAME), \
        "Success message is presented, but should disappear"


def test_guest_should_see_login_link_on_product_page(browser):
    """Проверка наличия на странице товара ссылки, которая ведет на логин"""
    page = ProductPage(browser, UrlPages.PRODUCT2_PAGE_URL)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """Переход на страницу логина со страницы товара"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, UrlPages.PRODUCT2_PAGE_URL)
    page.open()
    page.go_to_login_page()
