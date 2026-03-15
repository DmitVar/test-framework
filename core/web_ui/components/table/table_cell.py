from dataclasses import dataclass
import allure
from playwright.sync_api import Locator, Page, expect
from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.text import Text


@dataclass
class Cell:
    nth: int
    text: str


class TableCell(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.current_cell = None
        self._current_base_locator = None

    def cell(self, base_locator: Locator) -> Text:
        self._current_base_locator = base_locator
        self.current_cell = Text(
            self.page,
            base_locator=base_locator,
            name="Table Cell Text",
            locator="td"
        )
        return self.current_cell

    def cell_inner_text(self, nth: int, **kwargs) -> str:
        return self.current_cell.get_text(nth=nth, **kwargs)

    def check_visible(self, nth: int):
        self.current_cell.check_visible(nth=nth)

    def check_cell_have_text(self, nth: int, text: str):
        self.current_cell.check_have_text(text, nth=nth)

    def click(self, nth: int):
        self.current_cell.click(nth=nth)
