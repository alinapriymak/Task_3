import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from utils.test_data import TestData


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    
    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        
        login_page.open(login_page.url)
        login_page.click_forgot_password()
        
        assert driver.current_url == forgot_password_page.url

    
    @allure.title("Проверка ввода почты и клика по кнопке «Восстановить»")
    def test_enter_email_and_click_recover(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        
        login_page.open(login_page.url)
        login_page.click_forgot_password()
        forgot_password_page.enter_email(TestData.VALID_EMAIL)
        forgot_password_page.click_recover_button()
        
        assert "reset-password" in driver.current_url

    
    @allure.title("Проверка активации поля пароля при клике на кнопку показать/скрыть")
    def test_show_password_button_activates_field(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        
        login_page.open(login_page.url)
        login_page.click_forgot_password()
        forgot_password_page.enter_email(TestData.VALID_EMAIL)
        forgot_password_page.click_recover_button()
        reset_password_page.click_show_password_button()
        
        assert reset_password_page.is_password_field_active()