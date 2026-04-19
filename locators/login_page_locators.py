from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Локаторы для страницы авторизации"""
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")