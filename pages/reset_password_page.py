from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators
import allure

class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Кликнуть на кнопку показать/скрыть пароль")
    def click_show_password_button(self):
        self.click(ResetPasswordPageLocators.SHOW_PASSWORD_BTN)
    
    @allure.step("Проверить, что поле пароля активно (подсвечено)")
    def is_password_field_active(self):
        return self.is_element_visible(ResetPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
    
    @allure.step("Ввести новый пароль")
    def enter_new_password(self, password):
        self.input_text(ResetPasswordPageLocators.PASSWORD_INPUT, password)
