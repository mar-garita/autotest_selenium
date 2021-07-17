from selenium.webdriver.common.by import By


class UrlPages():
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"  # главная страница
    # страница товара
    PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT2_PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")


class LoginPageLocators():
    """Класс содержит селекторы к формам регистрации и логина"""
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # форма регистрации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # форма логина


class ProductPageLocators():
    BUTTON_SEE_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn-default")  # кнопка "Просмотреть корзину"
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, ".btn-add-to-basket")  # кнопка "Добавить в корзину"
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")  # название товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")  # цена товара
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description + p")  # описание товара
    # уведомление о добавлении товара в корзину
    SUCCESS_MESSAGES_PRODUCT_NAME = (By.XPATH,
                                     "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]//strong")
    SUCCESS_MESSAGES_PRODUCT_PRICE = (By.XPATH,
                                      "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")


class BasketLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
