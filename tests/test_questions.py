import pytest
from pages.main_page import MainPage
from constants import MAIN_PAGE_URL

class TestQuestions:
    """Тесты вопросов о важном"""
    
    def test_question_1(self, driver):
        """Тест вопроса 1"""
        from pages.main_page import MainPage
        from constants import MAIN_PAGE_URL
        
        driver.get(MAIN_PAGE_URL)
        main_page = MainPage(driver)
        assert main_page.check_question_1() is True
    
    def test_question_2(self, driver):
        """Тест вопроса 2"""
        from pages.main_page import MainPage
        from constants import MAIN_PAGE_URL
        
        driver.get(MAIN_PAGE_URL)
        main_page = MainPage(driver)
        assert main_page.check_question_2() is True
    
    def test_question_3(self, driver):
        """Тест вопроса 3"""
        from pages.main_page import MainPage
        from constants import MAIN_PAGE_URL
        
        driver.get(MAIN_PAGE_URL)
        main_page = MainPage(driver)
        assert main_page.check_question_3() is True
    
    def test_question_4(self, driver):
        """Тест вопроса 4"""
        from pages.main_page import MainPage
        from constants import MAIN_PAGE_URL
        
        driver.get(MAIN_PAGE_URL)
        main_page = MainPage(driver)
        assert main_page.check_question_4() is True
    
    def test_question_5(self, driver):
        """Тест вопроса 5"""
        from pages.main_page import MainPage
        from constants import MAIN_PAGE_URL
        
        driver.get(MAIN_PAGE_URL)
        main_page = MainPage(driver)
        assert main_page.check_question_5() is True
    
    def test_question_6(self, driver):
        """Тест вопроса 6"""
        from pages.main_page import MainPage
        from constants import MAIN_PAGE_URL
        
        driver.get(MAIN_PAGE_URL)
        main_page = MainPage(driver)
        assert main_page.check_question_6() is True
    
    def test_question_7(self, driver):
        """Тест вопроса 7"""
        from pages.main_page import MainPage
        from constants import MAIN_PAGE_URL
        
        driver.get(MAIN_PAGE_URL)
        main_page = MainPage(driver)
        assert main_page.check_question_7() is True
    
    def test_question_8(self, driver):
        """Тест вопроса 8"""
        from pages.main_page import MainPage
        from constants import MAIN_PAGE_URL
        
        driver.get(MAIN_PAGE_URL)
        main_page = MainPage(driver)
        assert main_page.check_question_8() is True
        
        
        
        #добавлено для коммита