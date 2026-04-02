from playwright.sync_api import Page
from core.web_ui.pages.boards_page.boards_page import BoardsPage


class TestBoardsPage:
    def test_transition_to_the_board_page(
        self,
        playwright_page_with_user_state: Page,
        board_title: str = "Дизайн Системы",
    ):
        boards_page = BoardsPage(playwright_page_with_user_state)
        boards_page.go()
        board_page = boards_page.go_to_board(board_title)
        board_page.check_title_has_text(board_title)
