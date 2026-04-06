import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page

from core.web_ui.pages.boards_page.boards_page import BoardsPage
from tools.allure.allure_enum import AllureEpics, AllureFeature, AllureStory, AllureTags


@allure.epic(AllureEpics.TMS)
@allure.feature(AllureFeature.BOARDS)
@allure.story(AllureStory.BOARD_OPERATIONS)
@allure.tag(AllureTags.BOARD)
@allure.severity(Severity.MINOR)
@pytest.mark.ui
@pytest.mark.regression
class TestBoardsPage:
    @allure.title("Test open board page by by board name")
    def test_transition_to_the_board_page(
        self,
        playwright_page_with_user_state: Page,
        board_title: str = "Дизайн Системы",
    ):
        boards_page = BoardsPage(playwright_page_with_user_state)
        boards_page.go()
        board_page = boards_page.go_to_board(board_title)
        board_page.check_title_has_text(board_title)
