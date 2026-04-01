import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from core.web_ui.elements.base_element import BaseElement


class Select(BaseElement):
    @property
    def type_of(self) -> str:
        return "select"

    def select_by_value(self, value: str, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Select option with value '{value}' in {self.name}"):
            locator.select_option(value=value)
        self.track_coverage(ActionType.SELECT, nth, **kwargs)

    def select_by_text(self, text: str, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Select option with text '{text}' in {self.name}"):
            locator.select_option(label=text)
        self.track_coverage(ActionType.SELECT, nth, **kwargs)

    def select_by_index(self, index: int, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Select option with index {index} in {self.name}"):
            locator.select_option(index=index)
        self.track_coverage(ActionType.SELECT, nth, **kwargs)

    def check_selected_value(self, value: str, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Check {self.name} has selected value '{value}'"):
            expect(locator).to_have_value(value)
        self.track_coverage(ActionType.TEXT, nth, **kwargs)
