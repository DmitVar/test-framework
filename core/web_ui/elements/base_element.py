import allure
from playwright.sync_api import Page, expect, Locator
from ui_coverage_tool import ActionType, SelectorType

from tools.logger import get_logger
from core.web_ui.elements.ui_coverage import tracker

loger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(
        self, page: Page, locator: str, name: str, base_locator: Locator | None = None
    ):
        self.locator = locator
        self.name = name
        self.page = page
        self.base_locator = base_locator

    @property
    def type_of(self) -> str:
        return "base element"

    @staticmethod
    def get_data_qa(value: str) -> str:
        return f"[data-qa='{value}']"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        if self.base_locator:
            base = self.base_locator
        else:
            base = self.page
        locator = self.locator.format(**kwargs)
        with allure.step(
            f"Get locator: {self.locator} of element with name: {self.name} at index {nth}"
        ):
            return base.locator(locator).nth(nth)

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f"{self.locator.format(**kwargs)}[{nth}]"

    def track_coverage(self, action_type: ActionType, nth: int = 0, **kwargs):
        tracker.track_coverage(
            selector=self.get_raw_locator(nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.CSS,
        )

    def click(self, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Click {self.type_of} of element with name: {self.name}"):
            locator.click()
        self.track_coverage(ActionType.CLICK, nth, **kwargs)

    def check_visible(self, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Check {self.type_of} with name {self.name} is visible"):
            expect(locator).to_be_visible()
        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)

    def check_have_text(self, text: str, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Check {self.type_of} with name {self.name} has text {text}"):
            expect(locator).to_have_text(text)
        self.track_coverage(ActionType.TEXT, nth, **kwargs)

    def check_enabled(self, nth: int = 0, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Check {self.type_of} with name {self.name} is enabled"):
            expect(locator).to_be_enabled()
        self.track_coverage(ActionType.ENABLED, nth, **kwargs)

    def check_disabled(self, nth: int, **kwargs) -> None:
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Check {self.type_of} with name {self.name} is disabled"):
            expect(locator).to_be_disabled()
        self.track_coverage(ActionType.DISABLED, nth, **kwargs)
