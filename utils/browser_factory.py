from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class BrowserFactory:
    """Фабрика для создания драйверов браузеров"""
    
    @staticmethod
    def get_driver(browser_name):
        if browser_name.lower() == "chrome":
            options = ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-notifications")
            driver = webdriver.Chrome(options=options)
            return driver
        
        elif browser_name.lower() == "firefox":
            options = FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)
            return driver
        
        else:
            raise ValueError(f"Browser {browser_name} is not supported")