from playwright.sync_api import Page, Locator

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.components.table.table_body import TableBody
from core.web_ui.components.table.table_headr import TableHeader


class Table(BaseComponent):
    def __init__(self, page: Page, table: Locator):
        super().__init__(page)
        self.table = table

    @property
    def header(self)->TableHeader:
        return TableHeader(self.page, self.table)

    @property
    def body(self)->TableBody:
        return TableBody(self.page, self.table)
