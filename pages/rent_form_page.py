from pages.base_page import BasePage
from locators.rent_form_locators import RentFormLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class RentFormPage(BasePage):
    """Класс для работы со второй формой заказа"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RentFormLocators()
    
    def select_date(self):
        """Выбрать дату доставки"""
        self.click_element(self.locators.DATE_FIELD)
        self.wait_for_element_visible(self.locators.CALENDAR)
        
        # Выбираем первый доступный день
        dates = self.find_elements(self.locators.DATE_DAY)
        for day in dates:
            if day.is_displayed() and day.text.strip().isdigit():
                day.click()
                break
        
        # Закрываем календарь
        date_field = self.find_element(self.locators.DATE_FIELD)
        date_field.send_keys(Keys.ESCAPE)
    
    def select_rental_period(self, period="сутки"):
        """Выбрать период аренды"""
        self.click_element(self.locators.RENTAL_PERIOD_FIELD)
        self.wait_for_element_visible(self.locators.DROPDOWN_MENU)
        
        period_locator = (By.XPATH, f"//div[text()='{period}']")
        self.click_element(period_locator)
    
    def select_black_color(self):
        """Выбрать черный цвет"""
        self.click_element(self.locators.BLACK_COLOR_CHECKBOX)
    
    def fill_comment(self, comment):
        """Заполнить комментарий"""
        self.fill_field(self.locators.COMMENT_FIELD, comment)
    
    def click_order_button(self):
        """Нажать кнопку 'Заказать'"""
        self.click_element(self.locators.ORDER_BUTTON)
    
    def confirm_order(self):
        """Подтвердить заказ"""
        self.wait_for_element_visible(self.locators.CONFIRM_MODAL)
        self.click_element(self.locators.YES_BUTTON)
    
    def check_success_order(self):
        """Проверить успешное оформление заказа"""
        self.wait_for_element_visible(self.locators.SUCCESS_MODAL)
        success_element = self.find_element(self.locators.SUCCESS_TEXT)
        return success_element.is_displayed()
    
    def fill_second_form(self, period="сутки", comment=""):
        """Заполнить всю вторую форму"""
        self.select_date()
        self.select_rental_period(period)
        self.select_black_color()
        if comment:
            self.fill_comment(comment)
        self.click_order_button()
        self.confirm_order()