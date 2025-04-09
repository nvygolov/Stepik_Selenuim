from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CODERS_AT_WORK_TEXT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div')
    BASKET_QUALIFIES_TEXT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div')
    BASKET_TOTAL_TEXT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    GO_BTN = (By.CSS_SELECTOR, '#language_selector > button')
    LANGUAGE = (By.NAME, 'language')
    LANGUAGE_ACCEPT = (By.XPATH, '//*[@id="language_selector"]/button')