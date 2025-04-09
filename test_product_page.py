import pytest
import time
import math
from selenium import webdriver
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.locators import BasePageLocators, ProductPageLocators  # Добавляем импорт ProductPageLocators

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Открываем страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        # Генерируем уникальный email
        email = str(time.time()) + "@fakemail.org"
        password = "StrongPassword123!"
        # Регистрируем нового пользователя
        page.register_new_user(email, password)
        # Проверяем, что пользователь залогинен
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()  # Вызов метода из BasePage
        page.should_be_success_message_with_correct_product_name(product_name)
        page.should_be_correct_basket_total(product_price)