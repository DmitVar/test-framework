from typing import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    base_url = "http://localhost:3000/"

    def __init__(self, page: Page):
        self.page = page

    def go(self):
        with allure.step(f"Go to {self.base_url}"):
            self.page.goto(self.base_url, wait_until="networkidle")

    def reload(self):
        with allure.step(f"Reload page with url {self.base_url}"):
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f"Check current url {expected_url}"):
            expect(self.page).to_have_url(expected_url)

    def wait_page_loaded(self, event_state="load", timeout=10000):
        with allure.step(f"Wait page loaded"):
            self.page.wait_for_load_state(state=event_state, timeout=timeout)
