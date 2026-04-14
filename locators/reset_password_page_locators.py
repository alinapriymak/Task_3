from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:
    """Локаторы для страницы сброса пароля"""
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BTN = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
    SAVE_BTN = (By.XPATH, "//button[text()='Сохранить']")
    