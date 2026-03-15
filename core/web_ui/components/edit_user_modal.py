from playwright.sync_api import Page

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.button import Button
from core.web_ui.elements.input import Input
from core.web_ui.elements.select import Select


class EditUserModal(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.user_name_input = Input(
            page,
            name="User Name Input",
            locator="[data-qa='text']"
        )
        self.user_email_input = Input(
            page,
            name="User Email Input",
            locator="[data-qa='edit-user-email-input']"
        )
        self.user_role_select = Select(
            page,
            name="User Role",
            locator="[data-qa='edit-user-role-select']"
        )
        self.user_avatar_url_input = Input(
            page,
            name="User Avatar URL Input",
            locator="[data-qa='edit-user-avatar-input']"
        )
        self.save_button = Button(
            page,
            name="Save",
            locator="[data-qa='edit-user-save-button']"
        )
        self.cancel_button = Button(
            page,
            name="Cancel",
            locator="[data-qa='edit-user-cancel-button']"
        )
        self.close_button = Button(
            page,
            name="Close",
            locator="[data-qa='modal-close-button']"
        )