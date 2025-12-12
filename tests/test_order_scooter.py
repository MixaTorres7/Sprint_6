import pytest
from constants import MAIN_PAGE_URL, ORDER_PAGE_URL, TEST_DATA
from pages.main_page import MainPage
from pages.order_form_page import OrderFormPage
from pages.rent_form_page import RentFormPage

class TestOrderScooter:
    """Тесты заказа самоката"""
    
    @pytest.mark.parametrize("button_type", ["header", "middle"])
    @pytest.mark.parametrize("name,surname,address,phone,comment", TEST_DATA)
    def test_order_scooter(self, driver, button_type, name, surname, address, phone, comment):
        """Тест заказа самоката через разные кнопки с разными данными"""
        # Шаг 1: Открыть главную страницу
        driver.get(MAIN_PAGE_URL)
        main_page = MainPage(driver)
        
        # Шаг 2: Кликнуть на кнопку Заказать
        if button_type == "header":
            main_page.click_header_order_button()
        else:
            main_page.click_middle_order_button()
        
        # Шаг 3: Заполнить первую форму
        order_form = OrderFormPage(driver)
        order_form.fill_first_form(name, surname, address, phone)
        
        # Шаг 4: Заполнить вторую форму и подтвердить заказ
        rent_form = RentFormPage(driver)
        rent_form.fill_second_form(period="сутки", comment=comment)
        
        # Шаг 5: Проверить успешное оформление заказа
        assert rent_form.check_success_order() is True, "Заказ не был успешно оформлен"
    
    def test_logo_samokat_redirect(self, driver):
        """Тест редиректа по логотипу Самоката"""
        # Открыть страницу заказа
        driver.get(ORDER_PAGE_URL)
        rent_form = RentFormPage(driver)
        
        # Кликнуть на логотип Самоката
        rent_form.click_element(rent_form.locators.SAMOKAT_LOGO)
        
        # Проверить редирект на главную страницу
        current_url = driver.current_url
        assert current_url == MAIN_PAGE_URL, f"Неверный URL после клика на лого Самоката: {current_url}"
    
    def test_logo_yandex_redirect(self, driver):
        """Тест редиректа по логотипу Яндекс"""
        # Открыть страницу заказа
        driver.get(ORDER_PAGE_URL)
        rent_form = RentFormPage(driver)
        
        # Сохранить текущую вкладку
        original_window = driver.current_window_handle
        
        # Кликнуть на логотип Яндекс
        rent_form.click_element(rent_form.locators.YANDEX_LOGO)
        
        # Подождать открытия новой вкладки
        import time
        time.sleep(2)  # Дать время для открытия новой вкладки
        
        # Проверить, что открылась новая вкладка
        assert len(driver.window_handles) > 1, "Новая вкладка не открылась"
        
        # Переключиться на новую вкладку
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        
        # Подождать загрузки страницы
        time.sleep(3)  # Увеличить время ожидания для загрузки
        
        # Проверить, что открылся Дзен
        current_url = driver.current_url
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, f"Не открылся Дзен/Яндекс. URL: {current_url}"
        
        # Закрыть вкладку и вернуться обратно
        driver.close()
        driver.switch_to.window(original_window)