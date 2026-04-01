from playwright.sync_api import Page, expect

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.button import Button
from core.web_ui.elements.text import Text


class Popup(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.text = Text(
            page,
            name="Popup Text",
            locator="div.toast-container p.toast-message",
        )
        self.close_button = Button(
            page, name="Close", locator="div.toast-container button.toast-close-btn"
        )

    def get_popup_text(self) -> str:
        return self.text.get_text()

    def close_popup(self):
        self.close_button.click()

    def check_popup_text(self, text: str):
        locator = self.text.get_locator()
        expect(locator).to_have_text(text)
