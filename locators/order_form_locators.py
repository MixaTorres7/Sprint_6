from selenium.webdriver.common.by import By

class OrderFormLocators:
    """Локаторы формы заказа (первая страница)"""
    NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[contains(text(),'Далее')]")
    
    # Станция метро в выпадающем списке
    METRO_STATION_ITEM = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Черкизовская']")