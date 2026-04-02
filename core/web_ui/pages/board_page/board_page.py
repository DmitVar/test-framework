from playwright.sync_api import Page

from core.web_ui.components.header import Header
from core.web_ui.components.sidebar import Sidebar
from core.web_ui.elements.button import Button
from core.web_ui.elements.select import Select
from core.web_ui.elements.text import Text
from core.web_ui.pages.base_page import BasePage


class BoardPage(BasePage):
    base_url = "http://localhost:3000/boards/"

    def __init__(self, page: Page, board_id: str):
        super().__init__(page)
        self.base_url = f"{self.base_url}{board_id}"

        self.board_title = Text(
            page,
            name="Board Title",
            locator="[data-qa='board-title']",
        )
        self.board_description = Text(
            page,
            name="Board Description",
            locator="[data-qa='board-description']",
        )
        self.edit_board_button = Button(
            page,
            name="Edit Board",
            locator="[data-qa='board-edit-button']",
        )
        self.delete_board_button = Button(
            page,
            name="Delete Board",
            locator="[data-qa='board-delete-button']",
        )
        self.members_button = Button(
            page,
            name="Members",
            locator="[data-qa='board-members-button']",
        )
        self.create_task_button = Button(
            page,
            name="Create Task",
            locator="[data-qa='board-create-task-button']",
        )
        self.select_task_status = Select(
            page,
            name="Task Status",
            locator="[data-qa='board-status-filter']",
        )
        self.select_task_priority = Select(
            page,
            name="Task Priority",
            locator="[data-qa='board-priority-filter']",
        )
        self.column_todo = self.page.locator("[data-qa='kanban-column-todo']")
        self.column_in_progress = self.page.locator(
            "[data-qa='kanban-column-in_progress']"
        )
        self.column_done = self.page.locator("[data-qa='kanban-column-done']")

        self.header = Header(page)
        self.sidebar = Sidebar(page)

    def check_title_has_text(self, title: str):
        self.board_title.check_have_text(title)
