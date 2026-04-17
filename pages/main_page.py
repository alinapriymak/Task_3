from pages.base_page import BasePage
from utils.urls import MAIN_PAGE
import allure
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = MAIN_PAGE
    
    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BTN)

    
    @allure.step("Кликнуть на 'Лента заказов'")
    def click_order_feed(self):
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", element)

    
    @allure.step("Кликнуть на 'Личный кабинет'")
    def click_personal_account(self):
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    
    @allure.step("Дождаться успешной авторизации")
    def wait_for_successful_login(self):
        self.wait.until(EC.url_to_be(MAIN_PAGE))
    

    @allure.step("Дождаться перехода на главную страницу")
    def wait_for_main_page(self):
        self.wait.until(EC.url_to_be(self.url))
        return self.driver.current_url == self.url
    
    
    @allure.step("Проверить, что текущий URL содержит 'feed'")
    def is_feed_url(self):
        return "feed" in self.driver.current_url

    
    @allure.step("Кликнуть на ингредиент 'Булка'")
    def click_bun_ingredient(self):
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.BUN_INGREDIENT))
        self.driver.execute_script("arguments[0].click();", element)

    
    @allure.step("Кликнуть на ингредиент 'Соус'")
    def click_sauce_ingredient(self):
        self.click(MainPageLocators.SAUCE_INGREDIENT)

    
    @allure.step("Кликнуть на ингредиент 'Начинка'")
    def click_filling_ingredient(self):
        self.click(MainPageLocators.FILLING_INGREDIENT)

    
    @allure.step("Закрыть модальное окно с деталями ингредиента")
    def close_ingredient_modal(self):
    
        close_btn = self.wait.until(EC.presence_of_element_located(MainPageLocators.CLOSE_MODAL_BTN))
    
        self.driver.execute_script("arguments[0].click();", close_btn)
        time.sleep(0.5)

    
    @allure.step("Проверить, что модальное окно с деталями отображается")
    def is_ingredient_modal_displayed(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)
    
    
    @allure.step("Проверить, что модальное окно закрыто")
    def is_ingredient_modal_closed(self):
        return self.is_element_not_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL, timeout=3)
    
    
    @allure.step("Получить название ингредиента в модальном окне")
    def get_ingredient_name_in_modal(self):
        return self.get_text(MainPageLocators.INGREDIENT_NAME)
    
    
    @allure.step("Получить значение каунтера булки")
    def get_bun_counter_value(self):
        try:
            element = self.wait.until(EC.presence_of_element_located(MainPageLocators.BUN_COUNTER))
            return int(element.text) if element.text else 0
        except:
            return 0
    
    
    @allure.step("Получить значение каунтера соуса")
    def get_sauce_counter_value(self):
        element = self.find_element(MainPageLocators.SAUCE_COUNTER)
        return int(element.text) if element.text else 0
    
    
    @allure.step("Получить значение каунтера начинки")
    def get_filling_counter_value(self):
        element = self.find_element(MainPageLocators.FILLING_COUNTER)
        return int(element.text) if element.text else 0
    
    @allure.step("Оформить заказ")
    def checkout_order(self):
        self.click(MainPageLocators.CHECKOUT_BTN)

    
    @allure.step("Проверить, что кнопка оформления заказа отображается")
    def is_checkout_button_displayed(self):
        return self.is_element_visible(MainPageLocators.CHECKOUT_BTN)
    

    @allure.step("Перетащить элемент в корзину (универсальный метод)")
    def drag_to_basket(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        
        # Прокручиваем к элементам
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", source)
        time.sleep(0.3)
        
        # Определяем браузер
        browser_name = self.driver.capabilities['browserName'].lower()
        
        if browser_name == 'firefox':
            # Для Firefox используем JavaScript эмуляцию
            self._drag_and_drop_js(source, target)
        else:
            # Для Chrome используем ActionChains
            action_chains = ActionChains(self.driver)
            action_chains.drag_and_drop(source, target).perform()
        
        time.sleep(0.5)
    
    
    # Добавлен метод для эмуляции перетаскивания ингредиентов в корзину для Firefox, 
    # поскольку там есть проблемы с drag-and-drop в Selenium
    def _drag_and_drop_js(self, source, target):
        """Эмуляция drag-and-drop через JavaScript для Firefox"""
        js_code = """
        function simulateDragDrop(source, target) {
            // Создаем события
            var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            var dragOverEvent = new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            var dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            var dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            
            // Диспатчим события
            source.dispatchEvent(dragStartEvent);
            target.dispatchEvent(dragOverEvent);
            target.dispatchEvent(dropEvent);
            source.dispatchEvent(dragEndEvent);
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js_code, source, target)

    
    @allure.step("Перетащить булку в корзину")
    def drag_bun_to_basket(self):
        self.drag_to_basket(MainPageLocators.BUN_INGREDIENT, MainPageLocators.BASKET_CONTAINER)
    
    @allure.step("Перетащить соус в корзину")
    def drag_sauce_to_basket(self):
        self.drag_to_basket(MainPageLocators.SAUCE_INGREDIENT, MainPageLocators.BASKET_CONTAINER)
    
    @allure.step("Перетащить начинку в корзину")
    def drag_filling_to_basket(self):
        self.drag_to_basket(MainPageLocators.FILLING_INGREDIENT, MainPageLocators.BASKET_CONTAINER)


    @allure.step("Перетащить булку в корзину и дождаться обновления каунтера")
    def drag_bun_to_basket_and_wait(self, initial_counter):
        self.drag_bun_to_basket()

        def counter_changed(driver):
            current = self.get_bun_counter_value()
            return current != initial_counter
    
        self.wait.until(counter_changed)


    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        element = self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER_MODAL))
    
        self.wait.until(lambda driver: element.text != '9999')
    
        number = element.text
        print(f"=== Номер заказа: '{number}' ===")
        return number
    

    @allure.step("Закрыть модальное окно с номером заказа")
    def close_order_modal(self):
         # Ждем появления номера заказа
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER_MODAL))
    
        # Находим и кликаем по кнопке закрытия
        close_btn = self.wait.until(EC.element_to_be_clickable(MainPageLocators.CLOSE_MODAL_BTN))
        self.driver.execute_script("arguments[0].click();", close_btn)
    
        # Ждем, пока модальное окно закроется
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.ORDER_NUMBER_MODAL))