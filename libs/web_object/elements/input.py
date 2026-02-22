import allure
from playwright.sync_api import expect

from libs.web_object.elements.base_element import BaseElement


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs)

    def get_row_locator(self, nth: int = 0, **kwargs):
        return f"{super().get_row_locator(nth, **kwargs)}"

    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(
            f"Clear {self.type_of} with name '{self.name}' and locator: {locator}"
        ):
            locator.clear()
            with allure.step(f"Fill {self.type_of} to value '{value}'"):
                locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(
            f"Check {self.type_of} with name '{self.name}' has value '{value}'"
        ):
            expect(locator).to_have_value(value)

    def check_enabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Check {self.type_of} with name '{self.name}' is enabled"):
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(
            f"Check {self.type_of} with name '{self.name}' is not enabled"
        ):
            expect(locator).to_be_disabled()
