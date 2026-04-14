from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators
from selenium.webdriver.support import expected_conditions as EC
import allure

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Кликнуть на 'История заказов'")
    def click_order_history(self):
        """Клик на кнопку 'История заказов'"""
        element = self.wait.until(EC.element_to_be_clickable(PersonalAccountPageLocators.ORDER_HISTORY_LINK))
        self.driver.execute_script("arguments[0].click();", element)
        
    
    @allure.step("Кликнуть на кнопку 'Выход'")
    def click_logout(self):
        """Клик на кнопку 'Выход'"""
        element = self.wait.until(EC.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BTN))
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(EC.url_contains("login"))
    

    @allure.step("Проверить, что открылась страница профиля")
    def wait_for_profile_page(self):
        current_url = self.driver.current_url
        self.wait.until(EC.url_contains("account/profile"))
        return "account/profile" in self.driver.current_url
    
    
    @allure.step("Проверить, что открылась страница истории заказов")
    def wait_for_order_history_page(self):
        self.wait.until(EC.url_contains("order-history"))
        return "order-history" in self.driver.current_url
    
    
    @allure.step("Проверить, что пользователь на странице профиля")
    def is_on_profile_page(self):
        return "account/profile" in self.driver.current_url