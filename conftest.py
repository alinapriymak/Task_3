import pytest
from utils.browser_factory import BrowserFactory
from utils.api_client import APIClient
from utils.user_generator import generate_test_user
import allure

def pytest_addoption(parser):
    """Добавление опции командной строки для выбора браузера"""
    parser.addoption("--selenium-browser", action="store", default="chrome", 
                     help="Browser: chrome or firefox")
    parser.addoption("--headless-mode", action="store_true", default=False,
                     help="Run browser in headless mode")

@pytest.fixture(scope="function")
def driver(request):
    """Фикстура для создания драйвера браузера"""
    browser = request.config.getoption("--selenium-browser")
    no_headless = request.config.getoption("--headless-mode")
    headless = not no_headless
    driver = BrowserFactory.get_driver(browser, headless)
    driver.maximize_window()

    if browser.lower() == "firefox":
        driver.implicitly_wait(10)
        
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def test_user():
    """Фикстура для создания тестового пользователя через API"""
    with allure.step("Создание тестового пользователя через API"):
        user_data = generate_test_user()
        response = APIClient.create_user(
            user_data["email"], 
            user_data["password"], 
            user_data["name"]
        )
        
        if response.get("success"):
            user_data["access_token"] = response.get("accessToken")
            user_data["refresh_token"] = response.get("refreshToken")
    
    yield user_data
    
    
