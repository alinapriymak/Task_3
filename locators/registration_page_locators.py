from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    """Локаторы для страницы регистрации"""
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BTN = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MSG = (By.XPATH, "//p[contains(@class, 'input__error')]")
    