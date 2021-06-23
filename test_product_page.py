import pytest
from .pages.product_page import ProductPage


# запуск теста  с параметризацией:
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  # помечаем падающий тест как xfail:
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    """Добавление товара в корзину"""
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор
    page.open()
    page.add_product_to_basket()  # выполняем метод страницы — добавление товара в корзину
