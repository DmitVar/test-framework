from core.web_ui.components.table.table_header_cell import TableHeaderCell
from core.web_ui.components.table.table_row import TableRow


class TableHeaderRow(TableRow):
    @property
    def cell(self)->TableHeaderCell:
        return TableHeaderCell(self.page)