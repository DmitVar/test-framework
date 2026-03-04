from playwright.sync_api import Page

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.button import Button
from core.web_ui.elements.checkbox import Checkbox
from core.web_ui.elements.input import Input
from core.web_ui.elements.text import Text
from core.web_ui.elements.text_area import TextArea


class CreateBoardModal(BaseComponent):
    def __init__(self, page: Page):
        super().__init__()

        self.title = Text(
            page,
            name="Title",
            locator="h2.modal-title"
        )
        self.close_button = Button(
            page,
            name="Close Button",
            locator="[data-qa='modal-close-button']"
        )
        self.board_name_input_title = Text(
            page,
            name="Board Name Input Title",
            locator="[for='label-create-board-title-input']"
        )
        self.board_name_input = Input(
            page,
            name="Board Name Input",
            locator="[data-qa='create-board-title-input']"
        )
        self.board_description_textarea_title = Text(
            page,
            name="Board Description Textarea Title",
            locator="lable:text('Описание (необязательно)')"
        )
        self.board_description_textarea = TextArea(
            page,
            name="Board Description Textarea",
            locator="[data-qa='create-board-description-textarea']"
        )
        self.public_board_checkbox = Checkbox(
            page,
            name="Public Board Checkbox",
            locator="[data-qa='create-board-public-checkbox']"
        )
        self.cancel_button = Button(
            page,
            name="Cancel Button",
            locator="[data-qa='create-board-cancel-button']"
        )
        self.create_board_button = Button(
            page,
            name="Create Board Button",
            locator="[data-qa='create-board-submit-button']"
        )

    def create_board(self, board_name: str, description: str | None = None, is_public: bool = False) -> None:
        self.board_name_input.fill(board_name)
        self.board_description_textarea.fill(description)
        if is_public:
            self.public_board_checkbox.check()

        self.create_board_button.click()
