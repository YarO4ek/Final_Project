from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "There is no Add_To_Cart button on page"

    def add_product_to_cart(self):
        promo = False
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        add_to_cart_button.click()
        if self.promo:
            self.solve_quiz_and_get_code()
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART).text

        assert (product_name == product_name_in_cart), "Wrong product's name in cart"
        assert (product_price == product_price_in_cart), "Wrong product's price in cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_mesage(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"
