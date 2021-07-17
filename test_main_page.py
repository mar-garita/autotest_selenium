import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.locators import UrlPages, BasketLocators
from .pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        """
        Открывает главную страницу и переходит на страницу логина
        :param browser: фикстура, создает объект WebDriver
        :return:
        """
        page = MainPage(browser, UrlPages.MAIN_PAGE_URL)   # инициализируем Page Object, передаем в конструктор
        # экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()          # переход на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # инициализируем Page Object, передаем в конструктор
        # экземпляр драйвера и текущий! url адрес
        login_page.should_be_login_page()  # проверка страницы логина

    def test_guest_should_see_login_link(self, browser):
        """
        Открывает главную страницу и проверяет, что на ней есть ссылка, которая ведет на логин
        """
        page = MainPage(browser, UrlPages.MAIN_PAGE_URL)
        page.open()
        page.should_be_login_link()      # проверяет ссылку


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Открывает главную страницу и переходит в корзину (пустую) по кнопке в шапке сайта.
    Ожидается, что в корзине нет товаров и что есть текст о том, что корзина пуста
    """
    page = MainPage(browser, UrlPages.MAIN_PAGE_URL)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()
