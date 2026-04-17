import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from utils.urls import MAIN_PAGE

@allure.feature("Основной функционал")
class TestConstructor:
    
    @allure.title("Переход в «Конструктор»")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open(main_page.url)
        
        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
        
        with allure.step("Кликнуть на 'Конструктор'"):
            main_page.click_constructor()
        
        with allure.step("Проверить, что произошел возврат в Конструктор"):
            assert main_page.wait_for_main_page()

    
    @allure.title("Переход в «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open(main_page.url)
        
        with allure.step("Кликнуть на 'Лента заказов'"):
            main_page.click_order_feed()
        
        with allure.step("Проверить, что URL содержит 'feed'"):
            assert main_page.is_feed_url()

    
    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open(main_page.url)
        
        with allure.step("Кликнуть на ингредиент 'Булка'"):
            main_page.click_bun_ingredient()
        
        with allure.step("Проверить, что открылось модальное окно"):
            assert main_page.is_ingredient_modal_displayed()

    
    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open(main_page.url)
        
        with allure.step("Кликнуть на ингредиент 'Булка'"):
            main_page.click_bun_ingredient()
        
        with allure.step("Закрыть модальное окно"):
            main_page.close_ingredient_modal()
        
        with allure.step("Проверить, что модальное окно закрылось"):
            assert main_page.is_ingredient_modal_closed()

    
    @allure.title("Увеличение каунтера ингредиента при добавлении в заказ")
    def test_counter_increases_when_adding_ingredient(self, driver):
        main_page = MainPage(driver)
    
        with allure.step("Открыть главную страницу"):
            main_page.open(main_page.url)
    
        with allure.step("Получить начальное значение каунтера булки"):
            initial_counter = main_page.get_bun_counter_value()
    
        with allure.step("Перетащить булку в корзину"):
            main_page.drag_bun_to_basket()
    
        with allure.step("Получить новое значение каунтера булки"):
            new_counter = main_page.get_bun_counter_value()
    
        with allure.step("Проверить, что каунтер увеличился"):
            assert new_counter > initial_counter


    @allure.title("Оформление заказа авторизованным юзером")
    def test_logged_in_user_can_checkout(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
    
        with allure.step("Открыть главную страницу"):
            main_page.open(main_page.url)
    
        with allure.step("Кликнуть на 'Личный кабинет'"):
            main_page.click_personal_account()
    
        with allure.step("Авторизоваться"):
            login_page.login(test_user["email"], test_user["password"])
    
        with allure.step("Перетащить булку в корзину"):
            main_page.drag_bun_to_basket()
    
        with allure.step("Перетащить соус в корзину"):
            main_page.drag_sauce_to_basket()
    
        with allure.step("Перетащить начинку в корзину"):
            main_page.drag_filling_to_basket()
    
        with allure.step("Оформить заказ"):
            main_page.checkout_order()
    
        with allure.step("Проверить, что появился номер заказа"):
            assert main_page.is_element_visible(MainPageLocators.ORDER_NUMBER_MODAL, timeout=10)
