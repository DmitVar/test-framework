from playwright.sync_api import Page

from core.web_ui.components.edit_user_modal import EditUserModal
from core.web_ui.components.sidebar import Sidebar
from core.web_ui.components.table import Table
from core.web_ui.components.table.table_headr import TableHeader
from core.web_ui.elements.button import Button
from core.web_ui.elements.input import Input
from core.web_ui.components.table.table_row import TableRow
from core.web_ui.elements.text import Text
from core.web_ui.pages.base_page import BasePage


class AdminPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = Text(
            page,
            name="Title",
            locator="h1"
        )
        self.header = TableHeader(page)
        self.sidebar = Sidebar(page)

        self.search_user_input = Input(
            page,
            name="Search User Input",
            locator="[data-qa='boards-search-input']"
        )
        self.user_table = Table(page)
        self.edit_user_modal = EditUserModal(page)
        self.delete_user_modal = EditUserModal(page)

    def edit_user(self, user_id: int, user_param: dict[str, str]):
        edit_user_button = Button(
            page=self.page,
            name="Edit",
            locator=f"[data-qa='edit-user-button-{user_id}']"
        )
        edit_user_button.click()

    def delete_user(self, user_id: int):
        delete_user_button = Button(
            page=self.page,
            name="Delete",
            locator=f"[data-qa='delete-user-button-{user_id}']"
        )

    def get_row_by_text(self, text: str) -> TableRow:
        return self.user_table.body.get_row_by_cell_text(text)
