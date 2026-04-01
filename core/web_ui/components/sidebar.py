import allure
from playwright.sync_api import Page

from core.web_ui.components.base_component import BaseComponent
from core.web_ui.elements.link import Link


class Sidebar(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.home_link = Link(
            page, name="Home Link", locator="[data-qa='sidebar-home-link']"
        )
        self.boards_link = Link(
            page, name="Boards Link", locator="[data-qa='sidebar-boards-link']"
        )
        self.tasks_link = Link(
            page, name="Tasks Link", locator="[data-qa='sidebar-tasks-link']"
        )
        self.admin_link = Link(
            page, name="Admin Link", locator="[data-qa='sidebar-admin-link']"
        )

    @allure.step("Click on home link")
    def click_home_link(self):
        self.home_link.check_visible()
        self.home_link.click()

    @allure.step("Click on boards link")
    def click_boards_link(self):
        self.boards_link.check_visible()
        self.boards_link.click()

    @allure.step("Click on tasks link")
    def click_tasks_link(self):
        self.tasks_link.check_visible()
        self.tasks_link.click()

    @allure.step("Click on admin link")
    def click_admin_link(self):
        self.admin_link.check_visible()
        self.admin_link.click()
