from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import FORGOT_PASSWORD_PAGE
import allure

class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = FORGOT_PASSWORD_PAGE
    
    @allure.step("Ввести email для восстановления: {email}")
    def enter_email(self, email):
        self.input_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)
    
    @allure.step("Кликнуть на кнопку 'Восстановить'")
    def click_recover_button(self):
        self.click(ForgotPasswordPageLocators.RECOVER_BTN)
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("reset-password")
        )
