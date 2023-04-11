from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def should_not_be_proceed_to_checkout_button(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT_BUTTON), \
            "Proceed to checkout button is present but should not"

    def should_be_empty_basket_message(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, \
            "'Your basket is empty' message is not present but should be"

    def should_not_be_product_in_basket_title(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET_TITLE), \
            "Basket is not empty but it should"
