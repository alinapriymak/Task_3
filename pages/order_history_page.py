from pages.base_page import BasePage
from locators.order_history_page_locators import OrderHistoryPageLocators
from selenium.webdriver.support import expected_conditions as EC
import allure

class OrderHistoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Получить список заказов пользователя")
    def get_user_order_numbers(self):
        # Ждем, пока появятся заказы в истории
        self.wait.until(EC.presence_of_element_located(OrderHistoryPageLocators.ORDER_NUMBERS))
        elements = self.driver.find_elements(*OrderHistoryPageLocators.ORDER_NUMBERS)
        # Убираем # и 0 при получении
        return [el.text.replace('#', '').lstrip('0') for el in elements]
    