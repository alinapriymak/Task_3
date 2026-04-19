from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    """Локаторы для страницы восстановления пароля"""
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVER_BTN = (By.XPATH, "//button[text()='Восстановить']")
    