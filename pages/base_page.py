from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        """Конструктор класса
        :param browser: фикстура, которая создает объект WebDriver
        :param url: url страницы
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # команда для неявного ожидания со значением по умолчанию в 10

    def open(self):
        """Открывает нужную страницу, используя метод get()"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Метод поиска элемента на базовой странице
        :param how: как искать элемент на странице (css, id, xpath и тд)
        :param what: что искать (строку-селектор)
        :return:
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
