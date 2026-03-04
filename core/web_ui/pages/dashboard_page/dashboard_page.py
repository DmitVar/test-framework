from playwright.sync_api import Locator

from config import settings
from core.web_ui.components.card import Card
from core.web_ui.components.dashboard import Dashboard
from core.web_ui.components.header import Header
from core.web_ui.components.sidebar import Sidebar
from core.web_ui.elements.button import Button
from core.web_ui.pages.base_page import BasePage


class DashboardPage(BasePage):
    base_url = "http://localhost:3000/dashboard"

    def __init__(self, page):
        super().__init__(page)

        self.create_board_button = Button(
            page,
            name="Create Board",
            locator="[data-qa='dashboard-create-board-button']"
        )

        self.header = Header(page)
        self.sidebar = Sidebar(page)
        self.boards_dashboard = Dashboard(page, "dashboard-stat-total-boards")
        self.tasks_dashboard = Dashboard(page, "dashboard-stat-total-tasks")
        self.in_progress_dashboard = Dashboard(page, "dashboard-stat-in-progress")
        self.done_dashboard = Dashboard(page, "dashboard-stat-done")
        self.cards_list = page.locator('div.card.card-clickable').all()

    def get_card(self, index) -> Locator:
        return self.cards_list[index]

    def check_user_name(self, user_name: str) -> None:
        self.header.header_user_info_button.check_have_text(user_name)
