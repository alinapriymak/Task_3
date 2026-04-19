from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)
        
    
    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    
    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    
    @allure.step("Ввести текст {text}")
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text
    
    
    @allure.step("Проверить видимости элемента")
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
        
    
    @allure.step("Ожидание появления элемента")
    def wait_for_element(self, locator, timeout=10):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    
    @allure.step("Кликнуть на элемент через JavaScript")
    def js_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)


    @allure.step("Проверить, что элемент не отображается")
    def is_element_not_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
            return False
        except TimeoutException:
             return True
    