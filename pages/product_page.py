from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):

        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):

        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):

        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message_with_correct_product_name(self, expected_name):

        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_name == success_message, "Product name in success message is incorrect"

    def should_be_correct_basket_total(self, expected_price):

        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert expected_price == basket_total, "Basket total is incorrect"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET), \
            "Product is present in the basket, but should not be"
        
    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*ProductPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty" in empty_basket_message, \
            "Empty basket message is not displayed"
        
    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()
        