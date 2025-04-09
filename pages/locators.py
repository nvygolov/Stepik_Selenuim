from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")