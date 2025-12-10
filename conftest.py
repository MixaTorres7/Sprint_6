import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
from constants import MAIN_PAGE_URL

@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера"""
    # Можно добавить опции для headless режима
    options = Options()
    # options.add_argument("--headless")  # раскомментируйте для headless режима
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    """Фикстура для главной страницы"""
    driver.get(MAIN_PAGE_URL)
    return MainPage(driver)