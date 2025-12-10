from pages.base_page import BasePage
from locators.order_form_locators import OrderFormLocators

class OrderFormPage(BasePage):
    """Класс для работы с первой формой заказа"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFormLocators()
    
    def fill_name(self, name):
        """Заполнить поле Имя"""
        self.fill_field(self.locators.NAME_FIELD, name)
    
    def fill_surname(self, surname):
        """Заполнить поле Фамилия"""
        self.fill_field(self.locators.SURNAME_FIELD, surname)
    
    def fill_address(self, address):
        """Заполнить поле Адрес"""
        self.fill_field(self.locators.ADDRESS_FIELD, address)
    
    def fill_phone(self, phone):
        """Заполнить поле Телефон"""
        self.fill_field(self.locators.PHONE_FIELD, phone)
    
    def select_metro(self):
        """Выбрать станцию метро"""
        self.click_element(self.locators.METRO_STATION_FIELD)
        self.wait_for_element_visible(self.locators.METRO_STATION_ITEM)
        self.click_element(self.locators.METRO_STATION_ITEM)
    
    def click_next_button(self):
        """Нажать кнопку 'Далее'"""
        self.click_element(self.locators.NEXT_BUTTON)
    
    def fill_first_form(self, name, surname, address, phone):
        """Заполнить всю первую форму"""
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.select_metro()
        self.fill_phone(phone)
        self.click_next_button()