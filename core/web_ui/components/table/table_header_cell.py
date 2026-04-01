from playwright.sync_api import Locator

from core.web_ui.components.table.table_cell import TableCell
from core.web_ui.elements.text import Text


class TableHeaderCell(TableCell):
    def cell(self, base_locator: Locator) -> Text:
        return Text(self.page, name="Table Header Cell", locator="th")
