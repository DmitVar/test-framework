import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page

from libs.web_object.pages.login_page.login_page import LoginPage
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags


@allure.epic(AllureEpics.TMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.tag(AllureTags.AUTHORIZATION, AllureTags.USER_LOGIN)
@allure.severity(Severity.CRITICAL)
@pytest.mark.authorization
class TestLoginPage:
    @allure.title("Login with incorrect email")
    def test_input_incorrect_email(self, playwright_page: Page):
        login_page = LoginPage(playwright_page)
        login_page.go()
        login_page.login("masvrev@rergr", "12345678")

        login_page.check_email_alert_visible()
        login_page.check_email_alert_have_text("Неверный формат email")

    @pytest.mark.parametrize(
        "email, password, expected",
        [
            ("admin@example.com", "12345678", "Incorrect email or password"),
            ("example@example.com", "admin123", "Incorrect email or password"),
        ],
        ids=["incorrect password", "incorrect email"],
    )
    @allure.title("Login with incorrect email or password")
    def test_input_incorrect_email_and_password(
        self, playwright_page: Page, email: str, password: str, expected: str
    ):
        login_page = LoginPage(playwright_page)
        login_page.go()
        login_page.login(email, password)
        login_page.check_message_visible()
        login_page.check_message_have_text(expected)
