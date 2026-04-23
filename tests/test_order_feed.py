import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage
from pages.personal_account_page import PersonalAccountPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("Открытие всплывающего окна с деталями заказа")
    def test_click_on_order_opens_details_modal(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        with allure.step("Открыть главную страницу и авторизоваться"):
            main_page.open(main_page.url)
            main_page.click_personal_account()
            login_page.login(test_user["email"], test_user["password"])
        
        with allure.step("Создать заказ"):
            main_page.drag_bun_to_basket()
            main_page.drag_sauce_to_basket()
            main_page.drag_filling_to_basket()
            main_page.checkout_order()
            main_page.close_order_modal()   
            
        
        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
            order_feed_page.wait_for_feed_loaded()
        
        with allure.step("Кликнуть на первый заказ в ленте"):
            order_feed_page.click_first_order()
            
        
        with allure.step("Проверить, что открылось модальное окно с деталями"):
            assert order_feed_page.is_order_details_modal_displayed()
        
    

    @allure.title("Отображение заказов пользователя на странице «Лента заказов»")
    def test_user_orders_displayed_in_order_feed(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        
        with allure.step("Открыть главную страницу и авторизоваться"):
            main_page.open(main_page.url)
            main_page.click_personal_account()
            login_page.login(test_user["email"], test_user["password"])
        
        with allure.step("Создать заказ и получить его номер"):
            main_page.drag_bun_to_basket()
            main_page.drag_sauce_to_basket()
            main_page.drag_filling_to_basket()
            main_page.checkout_order()
            order_number = main_page.get_order_number_from_modal()
            main_page.close_order_modal()
        
        with allure.step("Перейти в историю заказов"):
            main_page.click_personal_account()
            personal_account_page.click_order_history()
        
        with allure.step("Получить номер заказа из истории"):
            order_history_page.get_user_order_numbers()
        
        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
            order_feed_page.wait_for_feed_loaded()
            order_feed_page.wait_for_order_in_feed(order_number)
            feed_orders = order_feed_page.get_order_numbers_in_feed()
        
        with allure.step("Проверить, что заказ отображается в ленте"):
            assert order_number in feed_orders

    
    @allure.title("Увеличение счётчика 'Выполнено за всё время' при создании заказа")
    def test_total_orders_counter_increases(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        with allure.step("Открыть главную страницу и авторизоваться"):
            main_page.open(main_page.url)
            main_page.click_personal_account()
            login_page.login(test_user["email"], test_user["password"])
        
        with allure.step("Перейти в ленту заказов и получить начальное значение счётчика"):
            main_page.click_order_feed()
            initial_total = order_feed_page.get_total_orders_count()
        
        with allure.step("Вернуться в конструктор и создать заказ"):
            main_page.click_constructor()
            main_page.drag_bun_to_basket()
            main_page.drag_sauce_to_basket()
            main_page.drag_filling_to_basket()
            main_page.checkout_order()
            main_page.close_order_modal()
        
        with allure.step("Снова перейти в ленту заказов"):
            main_page.click_order_feed()
            order_feed_page.wait_for_feed_loaded()
        
        with allure.step("Проверить, что счётчик увеличился"):
            new_total = order_feed_page.get_total_orders_count()

            assert new_total > initial_total

    
    @allure.title("Увеличение счётчика 'Выполнено за сегодня' при создании заказа")
    def test_today_orders_counter_increases(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        with allure.step("Открыть главную страницу и авторизоваться"):
            main_page.open(main_page.url)
            main_page.click_personal_account()
            login_page.login(test_user["email"], test_user["password"])
        
        with allure.step("Перейти в ленту заказов и получить начальное значение счётчика"):
            main_page.click_order_feed()
            initial_today = order_feed_page.get_today_orders_count()
        
        with allure.step("Вернуться в конструктор и создать заказ"):
            main_page.click_constructor()
            main_page.drag_bun_to_basket()
            main_page.drag_sauce_to_basket()
            main_page.drag_filling_to_basket()
            main_page.checkout_order()
            main_page.close_order_modal()
        
        with allure.step("Снова перейти в ленту заказов"):
            main_page.click_order_feed()
        
        with allure.step("Проверить, что счётчик увеличился"):
            new_today = order_feed_page.wait_for_today_orders_increase(initial_today)
            assert new_today > initial_today

    
    @allure.title("Появление номера заказа в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, driver, test_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
    
        with allure.step("Открыть главную страницу и авторизоваться"):
            main_page.open(main_page.url)
            main_page.click_personal_account()
            login_page.login(test_user["email"], test_user["password"])
    
        with allure.step("Создать заказ и получить его номер"):
            main_page.drag_bun_to_basket()
            main_page.drag_sauce_to_basket()
            main_page.drag_filling_to_basket()
            main_page.checkout_order()
        
            order_number = main_page.get_order_number_from_modal()
        
            main_page.close_order_modal()
    
        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
            
    
        with allure.step("Проверить, что номер заказа появился в разделе 'В работе'"):
        
            assert order_feed_page.wait_for_order_in_progress(order_number)