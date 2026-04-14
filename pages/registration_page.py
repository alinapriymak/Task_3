from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators
from utils.urls import REGISTER_PAGE
import allure

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = REGISTER_PAGE
    
    @allure.step("Зарегистрировать пользователя: {name}")
    def register(self, name, email, password):
        self.input_text(RegistrationPageLocators.NAME_INPUT, name)
        self.input_text(RegistrationPageLocators.EMAIL_INPUT, email)
        self.input_text(RegistrationPageLocators.PASSWORD_INPUT, password)
        self.click(RegistrationPageLocators.REGISTER_BTN)
    
    @allure.step("Проверить, что отображается сообщение об ошибке")
    def is_error_message_displayed(self):
        return self.is_element_visible(RegistrationPageLocators.ERROR_MSG)