from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        """ Конструктор класса
        :param browser: фикстура, которая создает объект WebDriver
        :param url: url страницы
        :param timeout: значение для неявного ожидания
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # команда для неявного ожидания со значением по умолчанию в 10

    def open(self):
        """Открывает нужную страницу"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Вспомогательный метод поиска элемента в базовой странице BasePage,
        который перехватывает исключения
        :param how: как искать элемент на странице (css, id, xpath и тд)
        :param what: что искать (строку-селектор)
        :return: True или False
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
