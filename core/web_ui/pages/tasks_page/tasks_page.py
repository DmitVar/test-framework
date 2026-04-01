from playwright.sync_api import Page

from core.web_ui.components.header import Header
from core.web_ui.components.sidebar import Sidebar
from core.web_ui.components.table.table import Table
from core.web_ui.elements.select import Select
from core.web_ui.elements.input import Input
from core.web_ui.pages.base_page import BasePage


class TaskPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = Header(page)
        self.sidebar = Sidebar(page)
        self.task_search_input = Input(
            page, name="Task Search Input", locator="[data-qa='tasks-search-input']"
        )
        self.task_status = Select(
            page, name="Task Status", locator="[data-qa='tasks-status-filter']"
        )

        self.task_priority = Select(
            page, name="Task Priority", locator="[data-qa='tasks-priority-filter']"
        )
        self.tasks_table = Table(page, page.locator("table"))
