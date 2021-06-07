class BasePage():
    def __init__(self, browser, url):
        """Конструктор класса
        :param browser: фикстура, которая создает объект WebDriver
        :param url: url страницы
        """
        self.browser = browser
        self.url = url

    def open(self):
        """Открывает нужную страницу, используя метод get()"""
        self.browser.get(self.url)
