from typing import Any

from playwright.sync_api import Page

from core.api.clients.users.users_schemas import UserRole
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

    def fill_fields_edit_user_form(self, user: dict[str, Any]) -> None:
        field_handlers = {
            "username": lambda value: self.user_name_input.fill(value),
            "email": lambda value: self.user_email_input.fill(value),
            "role": lambda value: self.user_role_select.select_by_value(
                value.value if isinstance(value, UserRole) else value),
            "avatar_url": lambda value: self.user_avatar_url_input.fill(value),
        }
        for field, value in user.items():
            handler = field_handlers.get(field)
            if handler is None:
                raise ValueError(f"Unsupported edit user field: {field}")
            handler(value)
            
    def edit_user(self, user_param: dict[str, Any]) -> None:
        self.fill_fields_edit_user_form(user_param)
        self.save_button.click()
