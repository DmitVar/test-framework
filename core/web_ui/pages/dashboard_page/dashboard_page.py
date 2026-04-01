from playwright.sync_api import Locator, Page

from core.web_ui.components.create_board_modal import CreateBoardModal
from core.web_ui.components.dashboard import Dashboard
from core.web_ui.components.header import Header
from core.web_ui.components.popup import Popup
from core.web_ui.components.sidebar import Sidebar
from core.web_ui.elements.button import Button
from core.web_ui.elements.text import Text
from core.web_ui.pages.base_page import BasePage


class DashboardPage(BasePage):
    base_url = "http://localhost:3000/dashboard"

    def __init__(self, page: Page):
        super().__init__(page)

        self.create_board_button = Button(
            page,
            name="Create Board",
            locator="[data-qa='dashboard-create-board-button']",
        )

        self.empty_board_title = Text(
            page, name="Empty Board Title", locator="h3.empty-state-title"
        )
        self.empty_board_message = Text(
            page, name="Empty Board Message", locator="p.empty-state-message"
        )

        self.header = Header(page)
        self.sidebar = Sidebar(page)
        self.boards_dashboard = Dashboard(page, "dashboard-stat-total-boards")
        self.tasks_dashboard = Dashboard(page, "dashboard-stat-total-tasks")
        self.in_progress_dashboard = Dashboard(page, "dashboard-stat-in-progress")
        self.done_dashboard = Dashboard(page, "dashboard-stat-done")
        self.cards_list = page.locator("div.card.card-clickable").all()
        self.create_board_modal = CreateBoardModal(page)
        self.popup = Popup(page)

    def get_card(self, index) -> Locator:
        return self.cards_list[index]

    def check_user_name(self, user_name: str) -> None:
        self.header.header_user_info_button.check_have_text(user_name)

    def create_board(
        self,
        board_name: str,
        board_description: str | None = None,
        is_public: bool = False,
    ) -> None:
        self.create_board_button.click()
        self.create_board_modal.create_board(board_name, board_description, is_public)

    def find_board_by_name(self, board_name: str) -> Locator | None:
        for board in self.cards_list:
            board_title = board.locator("h3").text_content()
            if board_title == board_name:
                return board
        return None

    def is_board_public(self, board: Locator) -> bool:
        return board.locator(".pill--public").count() > 0

    def click_board(self, board: Locator) -> None:
        boar_link = board.locator("a")
        boar_link.click()

    def get_board_url(self, board: Locator) -> str:
        href = board.locator("a").get_attribute("href")
        return href

    def go_to_boards_page(self) -> None:
        self.sidebar.click_boards_link()
