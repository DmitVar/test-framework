from playwright.sync_api import Page

from core.web_ui.components.header import Header
from core.web_ui.elements.button import Button
from core.web_ui.elements.input import Input
from core.web_ui.elements.link import Link
from core.web_ui.elements.text import Text
from core.web_ui.pages.base_page import BasePage


class RegistrationPage(BasePage):
    base_url = "http://localhost:3000/register"

    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = Text(page, name="Title", locator="[data-qa='register-title']")

        self.user_name_input = Input(
            page, name="User Name", locator="[data-qa='register-username-input']"
        )

        self.email_input = Input(
            page, name="Email", locator="[data-qa='register-email-input']"
        )

        self.password_input = Input(
            page, name="Password", locator="[data-qa='register-password-input']"
        )

        self.password_confirm_input = Input(
            page,
            name="Password Confirm",
            locator="[data-qa='register-confirm-password-input']",
        )

        self.registration_button = Button(
            page, name="Register", locator="[data-qa='register-submit-button']"
        )

        self.login_page_link = Link(
            page, name="Login Page Link", locator="main a[href='/login']"
        )

        self.email_alert = Text(
            page, name="Email Alert", locator="p:text('Неверный формат email')"
        )

        self.confirm_password_alert = Text(
            page, name="Confirm Password Alert", locator="p:text('Пароли не совпадают')"
        )

        self.header = Header(page)

    def registration_new_user(
        self, user_name: str, email: str, password: str, confirm_password: str
    ) -> None:
        self.user_name_input.fill(user_name)
        self.user_name_input.check_have_value(user_name)
        self.email_input.fill(email)
        self.email_input.check_have_value(email)
        self.password_input.fill(password)
        self.password_input.check_have_value(password)
        self.password_confirm_input.fill(confirm_password)
        self.password_confirm_input.check_have_value(confirm_password)
        self.registration_button.click()
