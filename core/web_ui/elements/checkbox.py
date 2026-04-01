import allure

from core.web_ui.elements.base_element import BaseElement


class Checkbox(BaseElement):
    @property
    def type_of(self) -> str:
        return "checkbox"

    @allure.step("Checking that a checkbox is selected")
    def is_checked(self, nth=0, **kwargs) -> bool:
        locator = self.get_locator(nth, **kwargs)
        return locator.is_checked()

    @allure.step("Select checkbox")
    def check(self, nth=0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        locator.check()
