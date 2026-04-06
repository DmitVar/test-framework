import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page

from config import settings
from conftest import AllureLogger
from core.web_ui.pages.login_page.login_page import LoginPage
from tools.allure.allure_enum import AllureEpics, AllureFeature, AllureStory, AllureTags

logger = AllureLogger()


@allure.epic(AllureEpics.TMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.tag(AllureTags.AUTHORIZATION, AllureTags.USER_LOGIN)
@allure.severity(Severity.CRITICAL)
@pytest.mark.ui
@pytest.mark.authorization
class TestLoginPage:
    @allure.title("Login with incorrect email")
    def test_input_incorrect_email(self, playwright_page: Page):
        login_page = LoginPage(playwright_page)
        login_page.login("masvrev@rergr", "12345678")

        login_page.check_email_alert_visible()
        login_page.check_email_alert_have_text("Неверный формат email")

    @pytest.mark.parametrize(
        "email, password, expected",
        [
            (settings.test_user.email, "12345678", "Неверный пароль"),
            (
                "example@example.com",
                settings.test_user.password,
                "Пользователь с таким email не найден в системе",
            ),
        ],
        ids=["incorrect password", "incorrect email"],
    )
    @allure.title("Login with incorrect email or password")
    def test_input_incorrect_email_and_password(
        self, playwright_page: Page, email: str, password: str, expected: str
    ):
        login_page = LoginPage(playwright_page)
        login_page.login(email, password)
        login_page.check_message_visible()
        login_page.check_message_have_text(expected)

    @allure.title("Login with correct email or password")
    @pytest.mark.smoke
    def test_login_with_correct_email_and_password(self, playwright_page: Page):
        login_page = LoginPage(playwright_page)
        login_page.login(settings.test_user.email, settings.test_user.password)
        login_page.wait_page_loaded()
        expected_url = "http://localhost:3000/dashboard"
        login_page.check_current_url(expected_url)
