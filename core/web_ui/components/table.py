from playwright.sync_api import Page

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.components.table_body import TableBody
from core.web_ui.components.table_headr import TableHeader


class Table(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = TableHeader(page)
        self.body = TableBody(page)