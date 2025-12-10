from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators  # Импортировать базовые локаторы

class RentFormLocators(BasePageLocators):  # Наследовать от BasePageLocators
    """Локаторы формы аренды (вторая страница)"""
    DATE_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    CALENDAR = (By.CLASS_NAME, "react-datepicker__current-month")
    DATE_DAY = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day')]")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-placeholder")
    DROPDOWN_MENU = (By.CLASS_NAME, "Dropdown-menu")
    BLACK_COLOR_CHECKBOX = (By.XPATH, ".//label[@for='black']")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    
    # Подтверждение заказа
    CONFIRM_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    
    # Успешный заказ
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_TEXT = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")