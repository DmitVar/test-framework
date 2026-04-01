from core.web_ui.components.table.table_body import TableBody
from core.web_ui.components.table.table_header_row import TableHeaderRow


class TableHeader(TableBody):
    @property
    def table_body(self):
        return self.table.locator("thead")

    @property
    def row(self) -> TableHeaderRow:
        return TableHeaderRow(self.page, self.table_body)

    def click_cell(self, row_nth: int, cell_nth: int):
        self.row.click_cell(row_nth=row_nth, cell_nth=cell_nth)
