from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.components.table.table_cell import TableCell, Cell


@dataclass
class Row:
    nth: int
    cells: list[Cell]


class TableRow(BaseComponent):
    def __init__(self, page: Page, table_body: Locator):
        super().__init__(page)

        self.table_body = table_body
    @property
    def cell(self)->TableCell:
        return TableCell(self.page)

    def find_row_index(self, cells: list[Cell] ) -> int:
        rows_locator = self.table_body.locator('tr')
        for row_index in range(rows_locator.count()):
            row_locator = rows_locator.nth(row_index)
            row_found = all(
                cell.text in self.cell.cell_inner_text(cell.nth, row_locator) for cell in cells
            )
            if row_found:
                return row_index

    def find_row_locator(self, cells: list[Cell] ) -> Locator:
        row_index = self.find_row_index(cells)
        row_locator = self.table_body.locator('tr')
        return row_locator.nth(row_index)

    def check_visible_by_cells(self, cells: list[Cell]):
        row = self.find_row_index(cells, self.table_body)
        for cell in cells:
            self.cell.check_visible(cell, row)

    def check_visible(self, row: Row):
        table_row = self.table_body.locator('tr').nth(row.nth)
        for cell in row.cells:
            self.cell.check_visible(cell, table_row)

    def click_cell(self,row_nth: int, cell_nth: int):
        table_row = self.table_body.locator('tr').nth(row_nth)
        self.cell.click(cell_nth, table_row)

