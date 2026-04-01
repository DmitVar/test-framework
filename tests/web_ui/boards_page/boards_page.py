from playwright.sync_api import Page

from core.web_ui.pages.boards_page.boards_page import BoardsPage


class TestBoardsPage:
    def test_board(
        self,
        playwright_page_with_user_state: Page,
        board_title: str = "Дизайн Системы",
    ):
        boards_page = BoardsPage(playwright_page_with_user_state)
        boards_page.go()
        boards_page.go_to_board(board_title)
        url = boards_page.page.url
        t = 22
