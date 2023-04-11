from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button:nth-child(7)")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, ".alert-info > .alertinner strong")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "div.alert:nth-child(1) > .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1) > div.alertinner")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")
    PRODUCTS_IN_BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
