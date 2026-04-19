from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import ORDER_FEED_PAGE
import allure

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = ORDER_FEED_PAGE
    
    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order(self):
        self.click(OrderFeedPageLocators.ORDER_ITEMS)
    
    @allure.step("Проверить, что открылось модальное окно с деталями заказа")
    def is_order_details_modal_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(OrderFeedPageLocators.ORDER_DETAILS_MODAL))
            return True
        except:
            return False
    
    @allure.step("Закрыть модальное окно с деталями заказа")
    def close_order_details_modal(self):
        element = self.wait.until(EC.element_to_be_clickable(OrderFeedPageLocators.CLOSE_MODAL_BTN))
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(EC.invisibility_of_element_located(OrderFeedPageLocators.ORDER_DETAILS_MODAL))
    
    @allure.step("Получить список номеров заказов в ленте")
    def get_order_numbers_in_feed(self):
        elements = self.driver.find_elements(*OrderFeedPageLocators.ORDER_NUMBERS)
        return [el.text.replace('#', '').lstrip('0') for el in elements]
    
    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_orders_count(self):
        element = self.wait.until(EC.presence_of_element_located(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))
        text = element.text
        return int(text) if text.isdigit() else 0

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        element = self.wait.until(EC.presence_of_element_located(OrderFeedPageLocators.TODAY_ORDERS_COUNTER))
        text = element.text
        return int(text) if text.isdigit() else 0


    @allure.step("Ожидать обновления счётчиков")
    def wait_for_counters_update(self, initial_total, initial_today, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
        lambda driver: (
            self.get_total_orders_count() > initial_total and 
            self.get_today_orders_count() > initial_today
        )
    )
    
    @allure.step("Получить список номеров заказов в работе")
    def get_orders_in_progress(self):
        elements = self.driver.find_elements(*OrderFeedPageLocators.ORDERS_IN_PROGRESS_LIST)
        orders = []
        for el in elements:
            text = el.text
            if text and text != 'Все текущие заказы готовы!':
                # Убираем ведущий ноль для сравнения с номером из модалки
                orders.append(text.lstrip('0'))
        return orders
    

    @allure.step("Дождаться загрузки ленты заказов")
    def wait_for_feed_loaded(self):
        self.wait.until(EC.presence_of_element_located(OrderFeedPageLocators.ORDER_ITEMS))

    @allure.step("Дождаться появления номера заказа в разделе 'В работе'")
    def wait_for_order_in_progress(self, expected_number):  
        def condition(driver):
            elements = driver.find_elements(*OrderFeedPageLocators.ORDERS_IN_PROGRESS_LIST)
            orders = [el.text for el in elements if el.text]
            print(f"Заказы в работе: {orders}")
            return expected_number in orders
        self.wait.until(condition)
        return True
    

    @allure.step("Дождаться появления номера заказа в ленте")
    def wait_for_order_in_feed(self, expected_number):
        def condition(driver):
            orders = self.get_order_numbers_in_feed()
            return expected_number in orders
        self.wait.until(condition)
        return True
    
    
    @allure.step("Ожидать увеличения счётчика 'Выполнено за сегодня'")
    def wait_for_today_orders_increase(self, initial_value):
        def condition(driver):
            current = self.get_today_orders_count()
            return current > initial_value
        self.wait.until(condition)
        return self.get_today_orders_count()