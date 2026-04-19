from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import LOGIN_PAGE
import allure
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = LOGIN_PAGE
    
    @allure.step("Войти с email: {email}")
    def login(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BTN)

        time.sleep(2)

        if "login" in self.driver.current_url:
            self.driver.get("https://stellarburgers.education-services.ru/")
        self.wait.until(EC.url_contains("stellarburgers"))

    
    @allure.step("Кликнуть на ссылку 'Восстановить пароль'")
    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)


    @allure.step("Кликнуть на ссылку 'Зарегистрироваться'")
    def click_register(self):
        self.click(LoginPageLocators.REGISTER_LINK)

    
    @allure.step("Проверить, что пользователь авторизован")
    def is_user_logged_in(self):
        return self.is_element_visible(MainPageLocators.CHECKOUT_BTN)
    

    @allure.step("Проверить, что открыта страница логина")
    def is_login_page(self):
        return "login" in self.driver.current_url
    