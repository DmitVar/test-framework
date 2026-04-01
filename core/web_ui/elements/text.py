import allure
from playwright.sync_api import expect, Locator

from core.web_ui.elements.base_element import BaseElement


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "text"

    def get_text(
        self, nth: int = 0, base_locator: Locator | None = None, **kwargs
    ) -> str:
        with allure.step(f"Get {self.type_of} with name {self.name}"):
            if base_locator:
                final_locator = base_locator.locator(self.locator)
            elif self.base_locator:
                final_locator = self.base_locator.locator(self.locator)
            else:
                final_locator = self.page.locator(self.locator)
            final_locator = final_locator.nth(nth)
            return final_locator.inner_text()

    def check_have_text(self, text: str, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(
            f"Check {self.type_of} with name '{self.name}' has text '{text}'"
        ):
            expect(locator).to_have_text(text)
