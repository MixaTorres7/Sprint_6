import pytest
from constants import MAIN_PAGE_URL, ORDER_PAGE_URL, TEST_DATA
from pages.main_page import MainPage
from pages.order_form_page import OrderFormPage
from pages.rent_form_page import RentFormPage

class TestOrderScooter:
    """Тесты заказа самоката"""
    
    @pytest.mark.parametrize("name,surname,address,phone,comment", TEST_DATA)
    def test_order_scooter_via_header_button(self, main_page, name, surname, address, phone, comment):
        """Тест заказа самоката через кнопку 'Заказать' в header"""
        # Шаг 1: Кликнуть на кнопку 'Заказать' в header
        main_page.click_header_order_button()
        
        # Шаг 2: Заполнить первую форму
        order_form = OrderFormPage(main_page.driver)
        order_form.fill_first_form(name, surname, address, phone)
        
        # Шаг 3: Заполнить вторую форму и подтвердить заказ
        rent_form = RentFormPage(main_page.driver)
        rent_form.fill_second_form(period="сутки", comment=comment)
        
        # Шаг 4: Проверить успешное оформление заказа
        assert rent_form.check_success_order() is True, "Заказ не был успешно оформлен"
    
    @pytest.mark.parametrize("name,surname,address,phone,comment", TEST_DATA)
    def test_order_scooter_via_middle_button(self, main_page, name, surname, address, phone, comment):
        """Тест заказа самоката через кнопку 'Заказать' в середине страницы"""
        # Шаг 1: Кликнуть на кнопку 'Заказать' в середине страницы
        main_page.click_middle_order_button()
        
        # Шаг 2: Заполнить первую форму
        order_form = OrderFormPage(main_page.driver)
        order_form.fill_first_form(name, surname, address, phone)
        
        # Шаг 3: Заполнить вторую форму и подтвердить заказ
        rent_form = RentFormPage(main_page.driver)
        rent_form.fill_second_form(period="сутки", comment=comment)
        
        # Шаг 4: Проверить успешное оформление заказа
        assert rent_form.check_success_order() is True, "Заказ не был успешно оформлен"
    
    def test_logo_samokat_redirect(self, main_page):
        """Тест редиректа по логотипу Самоката"""
        # Шаг 1: Открыть страницу заказа
        main_page.driver.get(ORDER_PAGE_URL)
        rent_form = RentFormPage(main_page.driver)
        
        # Шаг 2: Кликнуть на логотип Самоката
        rent_form.click_element(rent_form.locators.SAMOKAT_LOGO)
        
        # Шаг 3: Проверить редирект на главную страницу
        current_url = rent_form.get_current_url()
        assert current_url == MAIN_PAGE_URL, f"Неверный URL после клика на лого Самоката: {current_url}"
    
    def test_new_window_opened_after_yandex_logo_click(self, main_page):
        """Тест открытия новой вкладки по клику на логотип Яндекс"""
        # Шаг 1: Открыть страницу заказа
        main_page.driver.get(ORDER_PAGE_URL)
        rent_form = RentFormPage(main_page.driver)
        
        # Шаг 2: Сохранить текущую вкладку
        original_window = main_page.driver.current_window_handle
        
        # Шаг 3: Кликнуть на логотип Яндекс
        rent_form.click_element(rent_form.locators.YANDEX_LOGO)
        
        # Шаг 4: Проверить, что открылась новая вкладка
        rent_form.wait_for_new_window(original_window, timeout=10)
        window_count = len(rent_form.driver.window_handles)
        assert window_count > 1, f"Новая вкладка не открылась. Количество вкладок: {window_count}"
    
    def test_yandex_logo_redirects_to_dzen(self, main_page):
        """Тест редиректа на Дзен по клику на логотип Яндекс"""
        # Шаг 1: Открыть страницу заказа
        main_page.driver.get(ORDER_PAGE_URL)
        rent_form = RentFormPage(main_page.driver)
        
        # Шаг 2: Сохранить текущую вкладку
        original_window = main_page.driver.current_window_handle
        
        # Шаг 3: Кликнуть на логотип Яндекс и переключиться на новую вкладку
        rent_form.click_element(rent_form.locators.YANDEX_LOGO)
        rent_form.wait_for_new_window(original_window, timeout=10)
        rent_form.switch_to_new_window()
        
        # Шаг 4: Подождать загрузки страницы (просто подождем пока URL не будет about:blank)
        from selenium.webdriver.support.ui import WebDriverWait
        
        # Ждем максимум 10 секунд пока URL не изменится с about:blank
        wait = WebDriverWait(rent_form.driver, 10)
        wait.until(lambda driver: driver.current_url != "about:blank")
        
        # Шаг 5: Проверить, что открылся Дзен
        current_url = rent_form.get_current_url()
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, f"Не открылся Дзен/Яндекс. URL: {current_url}"