import allure
from playwright.sync_api import expect

from libs.web_object.elements.base_element import BaseElement


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Check {self.type_of} with name {self.name} is enabled"):
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Check {self.type_of} with name {self.name} is not enabled"):
            expect(locator).to_be_disabled()
