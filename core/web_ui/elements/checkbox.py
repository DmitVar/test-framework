import allure
from playwright.sync_api import Locator

from core.web_ui.elements.base_element import BaseElement



class Checkbox(BaseElement):
    @property
    def type_of(self) -> str:
        return "checkbox"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs)

    @allure.step("Checking that a checkbox is selected")
    def is_checked(self, nth = 0, **kwargs) -> bool:
        locator = self.get_locator(nth, **kwargs)
        return locator.is_checked()

    @allure.step("Select checkbox")
    def check(self, nth = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        locator.check()