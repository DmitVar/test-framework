import allure
import pytest
from faker import Faker
from playwright.sync_api import Page

from config import settings
from core.web_ui.pages.boards_page.boards_page import BoardsPage
from core.web_ui.pages.dashboard_page.dashboard_page import DashboardPage

faker = Faker()

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

    @allure.title("Test create new board on dashboard page")
    @pytest.mark.parametrize("board_title, board_description, is_public",
                             [
                                 (faker.text(max_nb_chars=30), faker.text(max_nb_chars=100), True),
                                 (faker.text(max_nb_chars=30), faker.text(max_nb_chars=100), False),
                             ],
                             ids=["public", "private"]
                             )
    def test_create_board_on_dashboard_page(
            self,
            playwright_page_with_user_state: Page,
            board_title: str,
            board_description: str,
            is_public: bool,
            delete_board
    ):
        dashboard_page = DashboardPage(playwright_page_with_user_state)
        dashboard_page.go()
        dashboard_page.create_board(board_title, board_description, is_public)
        dashboard_page.go_to_boards_page()
        boards_page = BoardsPage(dashboard_page.page)
        cell = boards_page.get_cell(board_title)
        cell.check_have_text(board_title, nth=1)
        delete_board.append(board_title)

