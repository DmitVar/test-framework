import allure
from playwright.sync_api import Locator


class TableCell:
    def __init__(self, locator: Locator):
        self.locator = locator
        self.name = "Table Cell"

    @property
    def type_of(self) -> str:
        return "head_cels"

    def get_cell_text(self, nth: int = 0, **kwargs) -> str:
        with allure.step(f"Get {self.type_of} with name {self.name}"):
            return self.locator.text_content()
