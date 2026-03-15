from playwright.sync_api import Page, Locator, expect

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.components.table.table_cell import TableCell
from core.web_ui.components.table.table_row import TableRow


class TableBody(BaseComponent):
    def __init__(self, page: Page, table: Locator):
        super().__init__(page)

        self.table = table

    @property
    def table_body(self)->Locator:
        return self.table.locator("tbody")

    @property
    def row(self)->TableRow:
        return TableRow(self.page, self.table_body)

    def check_row_visible(self, row: TableRow):
        self.row.check_visible(row)

    def check_row_visible_by_cells(self, cells: list[TableCell]):
        self.row.check_visible_by_cells(cells)

    def check_rows_visible(self, rows: list[TableRow]):
        for row in rows:
            self.row.check_visible(row)

    def check_number_of_rows(self, number_of_rows: int):
        expect(self.table_body.locator("tr")).to_have_count(number_of_rows)

    def check_not_number_of_rows(self, number_of_rows: int):
        expect(self.table_body.locator("tr")).not_to_have_count(number_of_rows)

    def click_cell(self, row_nth: int, cell_nth: int):
        self.row.click_cell(row_nth=row_nth, cell_nth=cell_nth)

    def get_all_rows(self)->list[Locator]:
        return self.table_body.locator("tr").all()

    def get_row_by_cell_text(self, cell_text: str):
        rows = self.get_all_rows()
        for row in rows:
            cells = row.locator('td').all()
            for cell in cells:
                text = cell.inner_text()
                if cell.inner_text() == cell_text:
                    return row
        return None

