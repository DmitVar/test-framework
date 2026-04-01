from playwright.sync_api import Locator

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.link import Link
from core.web_ui.elements.text import Text


class Card(BaseComponent):
    def __init__(self, page, locator: Locator):
        super().__init__(page)
        self.root = locator

        self.card_title = Text(page, name="card-title", locator=self.root.locator("h3"))
        self.card_link = Link(page, name="card-link", locator=self.root.locator("a"))

        self.card_text = Text(page, name="card-text", locator=self.root.locator("p"))
        self.card_date = Text(
            page, name="card-date", locator=self.root.locator("span:first-child")
        )
        self.public_label = Text(
            page,
            name="public-label",
            locator=self.root.locator("span:text('Публичная')"),
        )
