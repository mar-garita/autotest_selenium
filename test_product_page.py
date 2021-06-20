from .pages.locators import UrlPages
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    """Добавляет товар в корзину"""
    page = ProductPage(browser, UrlPages.PRODUCT_PAGE_URL)   # инициализируем Page Object, передаем в конструктор
    # экземпляр драйвера и url адрес (ссылку на страницу товара)
    page.open()
    page.add_product_to_basket()  # выполняем метод страницы — добавление товара в корзину
