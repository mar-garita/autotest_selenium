from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    """

    :param browser: фикстура, создает объект WebDriver
    :return:
    """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()      # выполняем метод страницы — проверяем, что есть ссылка, которая ведет на логин
