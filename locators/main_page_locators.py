from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы главной страницы"""
    BUTTON_HEADER_ORDER = (By.CLASS_NAME, "Button_Button__ra12g")
    BUTTON_MIDDLE_ORDER = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")
    
    # Вопросы
    QUESTION_1 = (By.ID, "accordion__heading-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")
    
    # Ответы
    ANSWER_1 = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel'][aria-labelledby='accordion__heading-0']")
    ANSWER_2 = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel'][aria-labelledby='accordion__heading-1']")
    ANSWER_3 = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel'][aria-labelledby='accordion__heading-2']")
    ANSWER_4 = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel'][aria-labelledby='accordion__heading-3']")
    ANSWER_5 = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel'][aria-labelledby='accordion__heading-4']")
    ANSWER_6 = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel'][aria-labelledby='accordion__heading-5']")
    ANSWER_7 = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel'][aria-labelledby='accordion__heading-6']")
    ANSWER_8 = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel'][aria-labelledby='accordion__heading-7']")