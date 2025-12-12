from selenium.webdriver.common.by import By

class BasePageLocators:
    """Локаторы, общие для всех страниц"""
    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")