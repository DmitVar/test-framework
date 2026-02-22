import allure
from playwright.sync_api import expect

from libs.web_object.elements.base_element import BaseElement


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "text"

    def get_text(self, nth: int = 0, **kwargs) -> str:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Get {self.type_of} with name {self.name}"):
            return locator.text_content()

    def check_have_text(self, text: str, nth: int = 0, **kwargs) -> bool:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(
            f"Check {self.type_of} with name '{self.name}' has text '{text}'"
        ):
            expect(locator).to_have_text(text)
