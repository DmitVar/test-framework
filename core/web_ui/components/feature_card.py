from playwright.sync_api import Page

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.link import Link
from core.web_ui.elements.text import Text


class FeatureCard(BaseComponent):
    def __init__(self, page: Page, card_index: int):
        super().__init__(page)

        self.feature_card_locator = f"div.feature-card:nth-child({card_index})"

        self.feature_title = Text(
            page=page,
            name="Feature Title",
            locator=f"{self.feature_card_locator} h4",
        )
        self.feature_description = Text(
            page=page,
            name="Feature Description",
            locator=f"{self.feature_card_locator} p",
        )

        self.button_open = Link(
            page,
            name="Open",
            locator=f"{self.feature_card_locator} a",
        )
