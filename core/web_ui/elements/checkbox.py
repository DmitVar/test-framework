import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from core.web_ui.elements.base_element import BaseElement



class Checkbox(BaseElement):
    @property
    def type_of(self) -> str:
        return "checkbox"

    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs)


    def is_checked(self, nth = 0, **kwargs) -> bool:
        locator = self.get_locator(nth = 0, **kwargs)
        return locator.is_checked()

    def check(self, nth = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.check()