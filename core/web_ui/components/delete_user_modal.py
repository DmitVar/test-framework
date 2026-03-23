from playwright.sync_api import expect

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.button import Button
from core.web_ui.elements.text import Text


class DeleteUserModal(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.cancel_button = Button(
            page,
            name="Cancel",
            locator="[data-qa='delete-user-cancel-button']"
        )

        self.delete_button = Button(
            page,
            name="Delete",
            locator="[data-qa='delete-user-confirm-button']"
        )
        self.close_button = Button(
            page,
            name="Close",
            locator="[data-qa='modal-close-button']"
        )
        self.delete_user_title = Text(
            page,
            name="Delete User",
            locator="h2.modal-title.text-gradient"
        )
        self.text_with_user_name_and_email = Text(
            page,
            name="Text With User Name and Email",
            locator="div.modal-body p:nth-child(1)"
        )
        self.warning_text = Text(
            page,
            name="Warning Text",
            locator="div.modal-body p:nth-child(2)"
        )

    def cancel(self):
        self.close_button.check_visible()
        self.cancel_button.click()

    def close(self):
        self.close_button.check_visible()
        self.close_button.click()

    def delete_user(self):
        self.delete_button.check_visible()
        self.delete_button.click()