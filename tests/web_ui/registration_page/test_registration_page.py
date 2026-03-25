import allure
import pytest
from allure_commons.types import Severity
from faker import Faker
from playwright.sync_api import Page

from core.web_ui.pages.dashboard_page.dashboard_page import DashboardPage
from core.web_ui.pages.registration_page.registration_page import RegistrationPage
from tools.allure.allure_enum import AllureTags, AllureStory, AllureFeature, AllureEpics

fake = Faker()

@allure.epic(AllureEpics.TMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.tag(AllureTags.REGISTRATION, AllureTags.CREATE_USER)
@allure.severity(Severity.CRITICAL)
@pytest.mark.ui
@pytest.mark.authorization
class TestRegistrationPage:
    @allure.title("Test create new user")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_registration_user(self, playwright_page: Page, delete_user):
        new_user_name = fake.first_name()
        new_user_email = fake.email(domain="example.com")
        new_user_password = fake.password(length=10, upper_case=True, lower_case=True, special_chars=True, digits=True)
        try:
            registration_page = RegistrationPage(playwright_page)
            registration_page.go()
            registration_page.registration_new_user(
                user_name=new_user_name,
                email=new_user_email,
                password=new_user_password,
                confirm_password=new_user_password
            )
            registration_page.wait_page_loaded()
            expected_url = "http://localhost:3000/dashboard"
            registration_page.check_current_url(expected_url)

            dashboard_page = DashboardPage(registration_page.page)
            dashboard_page.popup.check_popup_text("Регистрация успешна!")
        finally:
            delete_user.append(new_user_email)
