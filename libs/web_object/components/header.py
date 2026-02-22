import allure
from playwright.sync_api import Page

from libs.web_object.components.base_component import BaseComponent
from libs.web_object.elements.button import Button
from libs.web_object.elements.link import Link
from libs.web_object.elements.text import Text


class Header(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.automation_lab_link = Link(
            page, name="Automation Lab Link", locator="header a"
        )

        self.brand_title = Text(
            page, name="Brand Title", locator="header div.brand-title"
        )

        self.brand_subtitle = Text(
            page, name="Brand Subtitle", locator="header div.brand-subtitle"
        )
        self.header_user_info_button = Button(
            page, name="User Info Button", locator="[data-qa='header-user-info']"
        )

        self.header_user_info_button_user_name = Text(
            page, name="User Name", locator="[data-qa='header-username]"
        )

        self.header_user_dropdown_name = Text(
            page, name="User Name", locator="header div.header-user-dropdown-name"
        )

        self.header_user_dropdown_email = Text(
            page, name="User Email", locator="header div.header-user-dropdown-email"
        )
        self.header_user_dropdown_role = Text(
            page, name="User Role", locator="header div.header-user-dropdown-role"
        )
        self.header_user_dropdown_logout_button = Button(
            page, name="User Logout Button", locator="[data-qa='header-logout-button']"
        )

    @allure.step("Automation Lab Link clik")
    def click_automation_lab_link(self):
        self.automation_lab_link.check_visible()
        self.automation_lab_link.click()

    @allure.step("Check brand title has text {text}")
    def check_brand_title_have_text(self, text: str, nth: int = 0, **kwargs):
        self.brand_title.check_visible()
        self.brand_title.check_have_text(text, nth=nth, **kwargs)

    @allure.step("Check brand subtitle has text {text}")
    def check_brand_subtitle_have_text(self, text: str, nth: int = 0, **kwargs):
        self.brand_subtitle.check_visible()
        self.brand_subtitle.check_have_text(text, nth=nth, **kwargs)

    @allure.step("Click user info button")
    def click_user_info_button(self):
        self.header_user_info_button.check_visible()
        self.header_user_info_button.click()

    @allure.step("Check user info button has text {text}")
    def check_user_info_button_have_text(self, text: str, nth: int = 0, **kwargs):
        self.header_user_info_button_user_name.check_visible()
        self.header_user_dropdown_name.check_have_text(text, nth=nth, **kwargs)

    @allure.step("Check header dropdown user info has user name {text}")
    def check_header_dropdown_have_user_name(self, text: str, nth: int = 0, **kwargs):
        self.header_user_info_button.click()
        self.header_user_dropdown_name.check_visible()
        self.header_user_dropdown_name.check_have_text(text, nth=nth, **kwargs)
        self.header_user_info_button.click()

    @allure.step("Check header dropdown user info has user email {text}")
    def check_header_dropdown_have_user_email(self, text: str, nth: int = 0, **kwargs):
        self.header_user_info_button.click()
        self.header_user_dropdown_email.check_visible()
        self.header_user_dropdown_email.check_have_text(text, nth=nth, **kwargs)
        self.header_user_info_button.click()

    @allure.step("Check header dropdown user info has user role {text}")
    def check_header_dropdown_have_user_role(self, text: str, nth: int = 0, **kwargs):
        self.header_user_info_button.click()
        self.header_user_dropdown_role.check_visible()
        self.header_user_dropdown_role.check_have_text(text, nth=nth, **kwargs)
        self.header_user_info_button.click()

    @allure.step("Click logout button")
    def click_logout_button(self):
        self.header_user_info_button.click()
        self.header_user_dropdown_logout_button.check_visible()
        self.header_user_dropdown_logout_button.click()
