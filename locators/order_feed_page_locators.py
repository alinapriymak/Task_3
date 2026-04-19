from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    """Локаторы для страницы ленты заказов"""
    ORDER_ITEMS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]//li/a")
    ORDER_NUMBERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]//p[contains(@class, 'text_type_digits-default')]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]")
    CLOSE_MODAL_BTN = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]/following-sibling::button[contains(@class, 'Modal_modal__close')]")
    
    # Счётчики заказов
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'order_list')]//li")
    
    # Заказ в работе
    ORDER_IN_PROGRESS = (By.XPATH, "//div[contains(@class, 'OrderFeed')]//ul[contains(@class, 'order_list')]//li//p[contains(@class, 'digits-default')]")
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")
