from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки навигации
    PERSONAL_ACCOUNT_BTN = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_BTN = (By.XPATH, "//a[@href='/']")
    ORDER_FEED_BTN = (By.XPATH, "//a[@href='/feed']")
    
    # Ингредиенты
    BUN_INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]")
    SAUCE_INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa72')]")
    FILLING_INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6f')]")
    
    # Каунтеры
    BUN_COUNTER = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]//p[contains(@class, 'counter')]")
    SAUCE_COUNTER = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa72')]//p[contains(@class, 'counter')]")
    FILLING_COUNTER = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6f')]//p[contains(@class, 'counter')]")
    
    # Контейнер корзины для drag-and-drop
    BASKET_CONTAINER = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")

    # Кнопка оформления заказа
    CHECKOUT_BTN = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Модальное окно
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'modal')]")
    CLOSE_MODAL_BTN = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER_MODAL = (By.XPATH, "//div[contains(@class, 'modal')]//h2[contains(@class, 'text_type_digits-large')]")