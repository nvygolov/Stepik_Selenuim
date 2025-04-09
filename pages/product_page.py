from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        """
        Нажимает кнопку "Добавить в корзину".
        """
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        """
        Получает название товара с главной страницы.
        """
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        """
        Получает цену товара с главной страницы.
        """
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message_with_correct_product_name(self, expected_name):
        """
        Проверяет, что название товара в сообщении совпадает с заголовком товара.
        """
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_name == success_message, "Product name in success message is incorrect"

    def should_be_correct_basket_total(self, expected_price):
        """
        Проверяет, что стоимость корзины совпадает с ценой товара.
        """
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert expected_price == basket_total, "Basket total is incorrect"