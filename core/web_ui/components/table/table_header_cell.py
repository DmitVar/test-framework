from core.web_ui.components.table.table_cell import TableCell
from core.web_ui.elements.text import Text


class TableHeaderCell(TableCell):
    def cell(self, name="Table Header Cell") -> Text:
        return Text(self.page, name=name, locator="th")
