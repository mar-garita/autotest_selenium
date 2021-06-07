import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Метод позволяет запускать тест, который зависит от опции командной строки
    (в данном случае - от выбранного языка браузера),
    parser - это (в данном случае) атрибут, который считывает значения из строки"""
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура инициализации браузера (создает объект WebDriver),
    который затем можно использовать в тестах для взаимодействия с браузером"""
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
