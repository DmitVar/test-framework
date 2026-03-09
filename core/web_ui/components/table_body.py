from playwright.sync_api import Page

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.table_row import TableRow


class TableBody(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.table_rows = self.page.locator("tbody tr").all()


    def get_all_rows(self)->list[TableRow]:
        return  [TableRow(row) for row in self.table_rows]

    def get_row_by_index(self, index: int)->TableRow:
        return self.get_all_rows()[index]

    def get_row_by_cell_text(self, cell_text: str) -> TableRow:
        rows = self.get_all_rows()
        for row in rows:
            cells = row.get_all_cells("td")
            for cell in cells:
                if cell.get_cell_text() == cell_text:
                    return row

    def get_row_index_by_cell_text(self, cell_text: str) -> int:
        rows = self.get_all_rows()
        for index, row in enumerate(rows):
            cells = row.get_all_cells("td")
            for cell in cells:
                if cell.get_cell_text() == cell_text:
                    return index

    def get_cell_by_index(self, index: int, **kwargs):
        return self.header_row.get_cell_by_index("td", index, **kwargs)