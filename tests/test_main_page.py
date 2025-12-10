import pytest
from pages.main_page import MainPage
from constants import MAIN_PAGE_URL

class TestMainPage:
    """Тесты главной страницы"""
    
    def test_click_header_order_button(self, main_page):
        """Тест клика по кнопке 'Заказать' в header"""
        main_page.click_header_order_button()
        current_url = main_page.get_current_url()
        assert "order" in current_url, f"Не перешли на страницу заказа. URL: {current_url}"
    
    def test_click_middle_order_button(self, main_page):
        """Тест клика по кнопке 'Заказать' в середине страницы"""
        main_page.click_middle_order_button()
        current_url = main_page.get_current_url()
        assert "order" in current_url, f"Не перешли на страницу заказа. URL: {current_url}"