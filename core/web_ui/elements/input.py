import allure
from playwright.sync_api import expect, Locator
from ui_coverage_tool import ActionType

from core.web_ui.elements.base_element import BaseElement


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs)

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f"{super().get_raw_locator(nth, **kwargs)}"

    def fill(self, value: str, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Clear {self.type_of} with name '{self.name}'"):
            locator.clear()
        with allure.step(f"Fill {self.type_of} with name '{self.name}'"):
            locator.fill(value)
        self.track_coverage(ActionType.FILL, nth, **kwargs)

    def check_have_value(self, value: str, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Check {self.type_of} with name '{self.name}'"):
            expect(locator).to_have_value(value)
        self.track_coverage(ActionType.VALUE, nth, **kwargs)
