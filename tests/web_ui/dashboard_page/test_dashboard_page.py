import allure
from playwright.sync_api import Page

from config import settings
from core.web_ui.pages.dashboard_page.dashboard_page import DashboardPage


class TestDashboardPage:
    @allure.title("Check user name on dashboard page")
    def test_check_user_name_on_dashboard_page(
            self,
            playwright_page_with_user_state: Page,
            user_name: str = settings.test_user.username,
    ):
        page = playwright_page_with_user_state
        dashboard_page = DashboardPage(page)
        dashboard_page.go()
        dashboard_page.check_user_name(user_name)

    @allure.title("Check admin name on dashboard page")
    def test_check_admin_name_on_dashboard_page(
            self,
            playwright_page_with_admin_state: Page,
            user_name: str = settings.test_admin.username,
    ):
        page = playwright_page_with_admin_state
        dashboard_page = DashboardPage(page)
        dashboard_page.go()
        dashboard_page.check_user_name(user_name)