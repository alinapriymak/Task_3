from selenium.webdriver.common.by import By

class OrderHistoryPageLocators:
    """Локаторы для страницы истории заказов"""
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'orderHistory')]//div[contains(@class, 'order')]")
    ORDER_NUMBERS = (By.XPATH, "//div[contains(@class, 'orderHistory')]//p[contains(@class, 'text_type_digits-default')]")
    