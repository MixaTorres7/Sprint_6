from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    # Базовые методы для работы с элементами
    def find_element(self, locator):
        """Найти элемент по локатору"""
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """Найти элементы по локатору"""
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def fill_field(self, locator, text):
        """Заполнить текстовое поле"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Получить текст элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def wait_for_element_visible(self, locator):
        """Ожидать видимость элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def scroll_to_element(self, locator):
        """Прокрутить до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
    
    def switch_to_new_window(self):
        """Переключиться на новую вкладку"""
        self.driver.switch_to.window(self.driver.window_handles[1])