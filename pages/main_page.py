from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    """Класс для работы с главной страницей"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
    
    def click_header_order_button(self):
        """Кликнуть по кнопке 'Заказать' в header"""
        self.click_element(self.locators.BUTTON_HEADER_ORDER)
    
    def click_middle_order_button(self):
        """Кликнуть по кнопке 'Заказать' в середине страницы"""
        self.scroll_to_element(self.locators.BUTTON_MIDDLE_ORDER)
        self.click_element(self.locators.BUTTON_MIDDLE_ORDER)
    
    def check_question_and_answer(self, question_locator, answer_locator, expected_answer):
        """Проверить вопрос и ответ"""
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        actual_answer = self.get_text(answer_locator)
        return actual_answer == expected_answer
    
    def check_question_1(self):
        """Проверить вопрос 1"""
        from constants import ANSWER_1_TEXT
        return self.check_question_and_answer(
            self.locators.QUESTION_1, 
            self.locators.ANSWER_1, 
            ANSWER_1_TEXT
        )
    
    def check_question_2(self):
        """Проверить вопрос 2"""
        from constants import ANSWER_2_TEXT
        return self.check_question_and_answer(
            self.locators.QUESTION_2, 
            self.locators.ANSWER_2, 
            ANSWER_2_TEXT
        )
    
    def check_question_3(self):
        """Проверить вопрос 3"""
        from constants import ANSWER_3_TEXT
        return self.check_question_and_answer(
            self.locators.QUESTION_3, 
            self.locators.ANSWER_3, 
            ANSWER_3_TEXT
        )
    
    def check_question_4(self):
        """Проверить вопрос 4"""
        from constants import ANSWER_4_TEXT
        return self.check_question_and_answer(
            self.locators.QUESTION_4, 
            self.locators.ANSWER_4, 
            ANSWER_4_TEXT
        )
    
    def check_question_5(self):
        """Проверить вопрос 5"""
        from constants import ANSWER_5_TEXT
        return self.check_question_and_answer(
            self.locators.QUESTION_5, 
            self.locators.ANSWER_5, 
            ANSWER_5_TEXT
        )
    
    def check_question_6(self):
        """Проверить вопрос 6"""
        from constants import ANSWER_6_TEXT
        return self.check_question_and_answer(
            self.locators.QUESTION_6, 
            self.locators.ANSWER_6, 
            ANSWER_6_TEXT
        )
    
    def check_question_7(self):
        """Проверить вопрос 7"""
        from constants import ANSWER_7_TEXT
        return self.check_question_and_answer(
            self.locators.QUESTION_7, 
            self.locators.ANSWER_7, 
            ANSWER_7_TEXT
        )
    
    def check_question_8(self):
        """Проверить вопрос 8"""
        from constants import ANSWER_8_TEXT
        return self.check_question_and_answer(
            self.locators.QUESTION_8, 
            self.locators.ANSWER_8, 
            ANSWER_8_TEXT
        )