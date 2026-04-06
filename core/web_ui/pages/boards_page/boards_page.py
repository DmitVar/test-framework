from playwright.sync_api import Locator, Page

from core.web_ui.components.sidebar import Sidebar
from core.web_ui.components.table.table import Table
from core.web_ui.elements.button import Button
from core.web_ui.elements.checkbox import Checkbox
from core.web_ui.elements.input import Input
from core.web_ui.elements.text import Text
from core.web_ui.pages.base_page import BasePage
from core.web_ui.pages.board_page.board_page import BoardPage


class BoardsPage(BasePage):
    base_url = "http://localhost:3000/boards"

    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = Text(page, name="Title", locator="h1")
        self.sidebar = Sidebar(page)

        self.create_board_button = Button(
            page,
            name="Create Board Button",
            locator="[data-qa='boards-create-board-button']",
        )
        self.search_board_input = Input(
            page, name="Search Board Input", locator="[data-qa='boards-search-input']"
        )
        self.checkbox_only_public_boards = Checkbox(
            page,
            name="Checkbox Only Public Boards",
            locator="[data-qa='boards-public-only-checkbox']",
        )
        self.boards_table = Table(page, page.locator("table"))

    def search_board_by_title(self, board_title: str) -> Locator | None:
        self.search_board_input.fill(board_title)
        return self.boards_table.body.get_row_by_cell_text(board_title)

    def get_cell(self, board_title: str) -> Text:
        row = self.search_board_by_title(board_title)
        return self.boards_table.body.row.cell.cell(row)

    def go_to_board(self, board_title: str):
        row = self.search_board_by_title(board_title)
        row.locator("td").all()[-1].click()
        self.page.wait_for_timeout(timeout=2)
        board_id = self.page.url.split("/")[-1]
        board_page = BoardPage(self.page, board_id)
        board_page.go()
        return board_page
