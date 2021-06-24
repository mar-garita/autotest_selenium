from .base_page import BasePage  # импорт базового класса


class MainPage(BasePage):
    """В классе нет методов, поэтому добавляем заглушку"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
