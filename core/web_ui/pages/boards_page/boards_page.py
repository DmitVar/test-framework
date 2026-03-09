from playwright.sync_api import Page

from core.web_ui.components.sidebar import Sidebar
from core.web_ui.components.table import Table
from core.web_ui.components.table_headr import TableHeader
from core.web_ui.elements.button import Button
from core.web_ui.elements.checkbox import Checkbox
from core.web_ui.elements.input import Input
from core.web_ui.elements.text import Text
from core.web_ui.pages.base_page import BasePage


class BoardsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = Text(
            page,
            name="Title",
            locator="h1"
        )
        self.header = TableHeader(page)
        self.sidebar = Sidebar(page)

        self.create_board_button = Button(
            page,
            name="Create Board Button",
            locator="[data-qa='boards-create-board-button]"
        )
        self.search_board_input = Input(
            page,
            name="Search Board Input",
            locator="[data-qa='boards-search-input']"
        )
        self.checkbox_only_public_boards = Checkbox(
            page,
            name="Checkbox Only Public Boards",
            locator="[data-qa='boards-public-only-checkbox']"
        )
        self.boards_table = Table(page)