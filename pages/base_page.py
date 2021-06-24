import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


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

    def is_element_present(self, method, selector):
        """Вспомогательный метод поиска элемента,
        который перехватывает исключения
        :param how: как искать элемент на странице (css, id, xpath и тд)
        :param what: что искать (строку-селектор)
        :return: True или False
        """
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def get_text_element(self, method, selector):
        """
        Вспомогательный метод получает текст элемента,
        который перехватывает исключения
        :param how: как искать элемент на странице (css, id, xpath и тд)
        :param what: что искать (строку-селектор)
        :return: текст элемента
        """
        try:
            text = self.browser.find_element(method, selector).text
        except NoSuchElementException:
            return False
        return text

    def solve_quiz_and_get_code(self):
        """Считает результат математического выражения, которое появляется после нажатия на кнопку
        'Добавить в корзину' на странице товара, и вводит ответ"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
