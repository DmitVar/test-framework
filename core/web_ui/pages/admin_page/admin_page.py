from playwright.sync_api import Page, Locator

from core.web_ui.components.delete_user_modal import DeleteUserModal
from core.web_ui.components.edit_user_modal import EditUserModal
from core.web_ui.components.header import Header
from core.web_ui.components.sidebar import Sidebar
from core.web_ui.components.table.table import Table
from core.web_ui.elements.button import Button
from core.web_ui.elements.input import Input
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
        self.header = Header(page)
        self.sidebar = Sidebar(page)

        self.search_user_input = Input(
            page,
            name="Search User Input",
            locator="[data-qa='input']"
        )

        self.user_table = Table(page, page.locator("table"))
        self.edit_user_modal = EditUserModal(page)
        self.delete_user_modal = DeleteUserModal(page)

    def edit_user(self, user_id: int, user_param: dict[str, str]) -> None:
        edit_user_button = Button(
            page=self.page,
            name="Edit",
            locator=f"[data-qa='edit-user-button-{user_id}']"
        )
        edit_user_button.click()
        self.edit_user_modal.edit_user(user_param)

    def delete_user(self, user_id: int) -> None:
        delete_user_button = Button(
            page=self.page,
            name="Delete",
            locator=f"[data-qa='delete-user-button-{user_id}']"
        )
        delete_user_button.click()
        self.delete_user_modal.delete_user()

    def get_row_by_text(self, text: str) -> Locator | None:
        return self.user_table.body.get_row_by_cell_text(text)
