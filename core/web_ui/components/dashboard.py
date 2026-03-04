import allure
from playwright.sync_api import Page, expect

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.text import Text


class Dashboard(BaseComponent):
    def __init__(
            self,
            page: Page,
            dashboard_data_qa_value: str
    ):
        super().__init__(page)
        self.locator_string = f"div[data-qa='{dashboard_data_qa_value}']"
        self.dashboard = page.locator(f"{self.locator_string}")

        self.dashboard_title = Text(
            page,
            name="Dashboard Title",
            locator=f"{self.locator_string} p.stat-label"
        )

        self.dashboard_value = Text(
            page,
            name="Dashboard Value",
            locator=f"{self.locator_string} p.stat-label"
        )
        self.dashboard_icon = page.locator(f"{self.locator_string} svg")

    @allure.step("Check dashboard title")
    def check_title(self, text: str):
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text(text)

    @allure.step("Check dashboard value")
    def check_dashboard_value(self, text: str):
        self.dashboard_value.check_visible()
        self.dashboard_value.check_have_text(text)

    @allure.step("Check dashboard icon")
    def check_dashboard_icon(self,):
        locator = f"{self.locator_string} svg"
        expect(locator).to_be_visible()






