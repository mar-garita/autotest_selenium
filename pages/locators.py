from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # ссылка на логин


class LoginPageLocators():
    """Класс содержит селекторы к формам регистрации и логина"""
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # форма регистрации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # форма логина


class UrlPages():
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"  # главная страница
