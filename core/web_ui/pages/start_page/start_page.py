from playwright.sync_api import Page

from core.web_ui.components.feature_card import FeatureCard
from core.web_ui.components.header import Header
from core.web_ui.elements.text import Text
from core.web_ui.pages.base_page import BasePage


class StartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = Header(page)
        self.click_feature_card = FeatureCard(page, 1)
        self.data_cards_feature_card = FeatureCard(page, 2)
        self.subscription_feature_card = FeatureCard(page, 3)
        self.task_management_feature_card = FeatureCard(page, 4)

        self.page_title = Text(page, name="Page Title", locator="h2")

        self.page_description = Text(
            page, name="Page Description", locator="p.hero-description"
        )
