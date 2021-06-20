from .pages.main_page import MainPage
from .pages.locators import UrlPages
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
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


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, UrlPages.MAIN_PAGE_URL)
    page.open()
    page.should_be_login_link()      # проверяет, что есть ссылка, которая ведет на логин
