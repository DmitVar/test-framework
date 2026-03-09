from playwright.sync_api import Page

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.table_row import TableRow


class TableHeader(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header_row = TableRow(page.locator("thead tr"))

    def get_all_cells(self, **kwargs):
        return  self.header_row.get_all_cells("th", **kwargs)

    def get_cell_by_index(self, index: int, **kwargs):
        return self.header_row.get_cell_by_index("th", index, **kwargs)

