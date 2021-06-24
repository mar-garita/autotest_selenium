import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


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

    def go_to_login_page(self):
        """Метод осуществляет переходит на страницу логина"""
        # символ * указывает на то, что передаем именно пару, и этот кортеж нужно распаковать
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        """Метод проверяет наличие ссылки, которая ведет на логин"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, method, selector):
        """Вспомогательный метод поиска элемента,
        который перехватывает исключения
        :param method: как искать элемент на странице (css, id, xpath и тд)
        :param selector: что искать (строку-селектор)
        :return: True или False
        """
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, method, selector, timeout=4):
        """
        Метод проверяет, что элемент не появляется на странице в течение заданного времени
        (использует явное ожидание)
        :param method: как искать элемент на странице (css, id, xpath и тд)
        :param selector: что искать (строку-селектор)
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, selector, timeout=4):
        """
        Метод проверяет, что какой-то элемент на странице исчезает
        (использует явное ожидание вместе с функцией until_not)
        :param method:
        :param selector:
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            return False
        return True

    def get_text_element(self, method, selector):
        """
        Вспомогательный метод получает текст элемента,
        который перехватывает исключения
        :param method: как искать элемент на странице (css, id, xpath и тд)
        :param selector: что искать (строку-селектор)
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
