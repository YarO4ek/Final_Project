from .locators import BasePageLocators, LoginPageLocators
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        if 'promo' in url:
            self.promo = True
        else:
            self.promo = False
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_button_view_basket(self):
        assert self.is_element_present(*BasePageLocators.VIEW_BASKET_BUTTON), "View basket button is not present"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "There is no LoginForm on page"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
        except NoAlertPresentException:
            print("No first alert presented")
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except (NoAlertPresentException, TimeoutException):
            print("No second alert presented")

    def view_basket_button_click(self):
        view_basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()
        assert 'basket' in self.browser.current_url, "There is no basket page when click view basket button from main page"
