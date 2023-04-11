from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_url.click()
        assert ("login" in self.browser.current_url), "Wrong login-page"

    def should_be_login_form(self):
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "There is no LoginForm on page"

    def should_be_register_form(self):
        register_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "There is no RegisterForm on page"

    def register_new_user(self, email, password):
        try:
            registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
            registration_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
            registration_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
            register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        except NoSuchElementException:
            print("There is no one of registration fields or button")
        registration_email.send_keys(email)
        registration_password1.send_keys(password)
        registration_password2.send_keys(password)
        register_button.click()
