import pytest
from .page.product_page import ProductPage
from .page.basket_page import BasketPage
from .page.login_page import LoginPage
import time

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_cart()
    page.should_disappear_success_mesage()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_view_basket()
    page.view_basket_button_click()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket_title()
    basket_page.should_be_empty_basket_message()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, product_link)
        self.link = self.page.url
        self.page.open()
        self.page.go_to_login_page()
        email = "tester" + str(int(time.time())) + "@mymail.org"
        password = "tester_password"
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_add_to_cart_button()
        page.add_product_to_cart()
