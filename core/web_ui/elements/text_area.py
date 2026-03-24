import allure
from playwright.sync_api import expect, Locator
from ui_coverage_tool import ActionType

from core.web_ui.elements.base_element import BaseElement


class TextArea(BaseElement):
    @property
    def type_of(self):
        return "textarea"

    def get_text(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator("textarea").first

    def fill(self, value: str, nth: int = 0, **kwargs) -> None:
        with allure.step(f"Fill {self.type_of} '{self.name}' to value '{value}'"):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)
        self.track_coverage(ActionType.FILL, nth, **kwargs)

    def check_have_value(self, value: str, nth: int = 0, **kwargs) -> None:
        with allure.step(f"Checking that {self.type_of} '{self.name}' has a value '{value}'"):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)
        self.track_coverage(ActionType.VALUE, nth, **kwargs)
