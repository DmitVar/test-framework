import json
from pathlib import Path
from time import time

import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright, BrowserContext

from core.web_ui.pages.login_page.login_page import LoginPage
from config import settings, Browser, User
from tools.playwright.init_page import init_page


def get_storage_state_path(user_role: str) -> Path:
    """Возвращает путь к файлу состояния для указанной роли"""
    match user_role:
        case "admin":
            return settings.admin_state_file
        case "user":
            return settings.user_state_file
        case _:
            return None

def ensure_user_logged_in(user: User, playwright: Playwright) -> Path:
    storage_path = get_storage_state_path(user.role)
    if not storage_path:
        raise ValueError(f"Unknown user role: {user.role}")

    should_login = False
    if not storage_path.exists():
        should_login = True
    else:
        if storage_path.stat().st_size == 0:
            should_login = True
        else:
            st_t = storage_path.stat().st_mtime
            file_age = time() - storage_path.stat().st_mtime
            should_login = file_age > settings.max_browser_state_file_age
            if not should_login:
                try:
                    with open(storage_path, "r") as f:
                        json.load(f)
                except json.JSONDecodeError:
                    should_login = True

    if should_login:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        login_page = LoginPage(page)
        login_page.go()
        login_page.login(user.email, user.password)
        page.wait_for_url("http://localhost:3000/dashboard", timeout=10000)

        context.storage_state(path=storage_path)
        browser.close()

    return storage_path

@pytest.fixture(params=settings.browser)
def playwright_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from init_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
    )

@pytest.fixture(params=settings.browser)
def playwright_page_with_admin_state(request: SubRequest, playwright: Playwright) -> Page:
    storage_path = ensure_user_logged_in(settings.test_admin, playwright)
    storage_path_str = str(storage_path)
    yield from init_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=storage_path_str,
    )

@pytest.fixture(params=settings.browser)
def playwright_page_with_user_state(request: SubRequest, playwright: Playwright) -> Page:
    storage_path = ensure_user_logged_in(settings.test_user, playwright)
    storage_path_str = str(storage_path)
    yield from init_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=storage_path_str,
    )
