from core.web_ui.components.table.table_cell import TableCell
from core.web_ui.elements.text import Text


class TableHeaderCell(TableCell):
    @property
    def cell(self) -> Text:
        return Text(self.page, name="Table Header Cell", locator="th")
