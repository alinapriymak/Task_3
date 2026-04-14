from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    """Локаторы для страницы личного кабинета"""
   # PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BTN = (By.XPATH, "//button[text()='Выход']")
    USER_EMAIL = (By.XPATH, "//input[@name='name']")
