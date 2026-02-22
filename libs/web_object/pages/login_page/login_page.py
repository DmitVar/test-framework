import allure
from playwright.sync_api import Page

from libs.web_object.components.header import Header
from libs.web_object.elements.button import Button
from libs.web_object.elements.input import Input
from libs.web_object.elements.text import Text
from libs.web_object.pages.base_page import BasePage


class LoginPage(BasePage):
    base_url: str = "http://localhost:3000/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(
            page, locator="[data-qa='login-title']", name="Title Login Page"
        )

        self.email_input = Input(
            page, locator="[data-qa='login-email-input']", name="Input Email"
        )

        self.password_input = Input(
            page, locator="[data-qa='login-password-input']", name="Input Password"
        )

        self.login_button = Button(
            page, locator="[data-qa='login-submit-button']", name="Login Button"
        )

        self.email_alert = Text(page, locator="p[role='alert']", name="Email Alert")

        self.message = Text(page, locator="p.toast-message", name="Message")
        self.close_message_button = Button(
            page, locator="button.toast-close-btn", name="Close Button"
        )
        self.header = Header(page)

    @allure.step("User authorization with email: {1}")
    def login(self, email: str, password: str):
        self.email_input.check_visible()
        self.email_input.fill(email)

        self.password_input.check_visible()
        self.password_input.fill(password)

        self.login_button.check_visible()
        self.login_button.click()

    def check_email_alert_visible(self):
        self.email_alert.check_visible()

    def check_email_alert_have_text(self, text: str):
        self.email_alert.check_have_text(text)

    def check_message_visible(self):
        self.message.check_visible()

    def check_message_have_text(self, text: str):
        self.message.check_have_text(text)
