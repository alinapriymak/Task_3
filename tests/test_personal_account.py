import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage

@allure.feature("Личный кабинет")
class TestPersonalAccount:
    
    @allure.title("Переход в личный кабинет по клику на «Личный кабинет»")
    def test_go_to_personal_account(self, driver, test_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
    
        with allure.step("Открыть главную страницу"):
            main_page.open(main_page.url)
    
        with allure.step("Кликнуть на 'Личный кабинет'"):
            main_page.click_personal_account()
    
        with allure.step("Авторизоваться"):
            login_page.login(test_user["email"], test_user["password"])
    
        with allure.step("Снова кликнуть на 'Личный кабинет'"):
            main_page.click_personal_account()
    
        with allure.step("Проверить, что открылась страница профиля"):
            assert personal_account_page.wait_for_profile_page()

    
    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history(self, driver, test_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open(main_page.url)
        
        with allure.step("Кликнуть на 'Личный кабинет'"):
            main_page.click_personal_account()
        
        with allure.step("Авторизоваться"):
            login_page.login(test_user["email"], test_user["password"])
        
        with allure.step("Дождаться успешной авторизации"):
            main_page.wait_for_successful_login()
        
        with allure.step("Перейти в личный кабинет"):
            main_page.click_personal_account()
        
        with allure.step("Дождаться загрузки страницы профиля"):
            personal_account_page.wait_for_profile_page()
        
        with allure.step("Кликнуть на 'История заказов'"):
            personal_account_page.click_order_history()
        
        with allure.step("Проверить, что открылась страница истории заказов"):
            assert personal_account_page.wait_for_order_history_page()

    
    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, driver, test_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open(main_page.url)
        
        with allure.step("Кликнуть на 'Личный кабинет'"):
            main_page.click_personal_account()
        
        with allure.step("Авторизоваться"):
            login_page.login(test_user["email"], test_user["password"])
        
        with allure.step("Дождаться успешной авторизации"):
            main_page.wait_for_successful_login()
        
        with allure.step("Перейти в личный кабинет"):
            main_page.click_personal_account()
        
        with allure.step("Дождаться загрузки страницы профиля"):
            personal_account_page.wait_for_profile_page()
        
        with allure.step("Кликнуть на кнопку 'Выход'"):
            personal_account_page.click_logout()
        
        with allure.step("Проверить, что произошел переход на страницу логина"):
            assert login_page.is_login_page()