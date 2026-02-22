import allure
from playwright.sync_api import Locator, Page, expect


class BaseElement:
    def __init__(self, page: Page, locator: Locator, name: str):
        self.locator = locator
        self.name = name
        self.page = page

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs):
        locator = self.locator.format(**kwargs)
        with allure.step(
            f"Get locator: {locator} of element with name: {self.name} at index {nth}"
        ):
            return self.page.locator(locator).nth(nth)

    def get_row_locator(self, nth: int = 0, **kwargs):
        return f"{self.locator.format(**kwargs)}[{nth}]"

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(
            f"Click {self.type_of} {locator} of element with name: {self.name}"
        ):
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(
            f"Check {self.type_of} with name {self.name} {locator} is visible"
        ):
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(
            f"Check {self.type_of} with name {self.name} {locator} has text {text}"
        ):
            expect(locator).to_have_text(text)
