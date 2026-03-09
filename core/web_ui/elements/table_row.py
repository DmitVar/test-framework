from playwright.sync_api import Locator

from core.web_ui.elements.table_cell import TableCell


class TableRow:
    def __init__(self, locator: Locator):
        self.locator = locator
        self.name: str = "Table Row"


    def get_all_cells(self, cell_locator: str, **kwargs) -> list[TableCell]:
        return [TableCell(cell) for cell in self.locator.locator(cell_locator, **kwargs).all()]

    def get_cell_by_index(self, cell_locator:str, index: int, **kwargs) -> TableCell:
        cells = self.get_all_cells(cell_locator, **kwargs)
        return TableCell(cells[index])

    def get_cell_by_text(self, cell_locator: str, text: str, **kwargs) -> TableCell:
        cells = self.get_all_cells(cell_locator, **kwargs)
        for cell in cells:
            if cell.get_cell_text() == text:
                return TableCell(cell)

