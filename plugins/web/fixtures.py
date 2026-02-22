from pathlib import Path
from time import time

import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from libs.web_object.pages.login_page.login_page import LoginPage

AUTH_FILE = Path(".auth/user_state.json")
MAX_FILE_AGE = 3600


@pytest.fixture()
def playwright_page(
    request: SubRequest, playwright: Playwright, use_browser="Chrome"
) -> Page:
    browser = None
    match use_browser:
        case "Chrome":
            browser = playwright.chromium.launch(headless=False)
        case "Firefox":
            browser = playwright.firefox.launch(headless=False)
        case "WebKit":
            browser = playwright.webkit.launch(headless=False)

    context = browser.new_context(record_video_dir="./video")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f"./tracing/{request.node.name}.zip")
    browser.close()
    allure.attach.file(
        f"./tracing/{request.node.name}.zip", name="trace", extension=".zip"
    )
    allure.attach.file(
        page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM
    )


@pytest.fixture(scope="session")
def session_logged_in(playwright_page: Page):
    """
    Фикстура уровня сессии. Выполняет логин один раз за весь запуск.
    """
    is_expired = False
    if AUTH_FILE.exists():
        file_age = time.time() - AUTH_FILE.stat().st_mtime
        is_expired = file_age > MAX_FILE_AGE

    if not AUTH_FILE.exists() or is_expired:
        context = playwright_page.context
        page = playwright_page
        login_page = LoginPage(page)

        login_page.go()
        login_page.login("user_name", "password")

        page.wait_for_url("http://localhost:3000/dashboard", timeout=10000)

        context.storage_state(path=str(AUTH_FILE))
        context.close()

    return AUTH_FILE


@pytest.fixture
def playwright_page_with_state(
    playwright: Playwright, session_logged_in, request: SubRequest, use_browser="Chrome"
) -> Page:
    """
    Фикстура создает страницу, которая уже авторизована
    """
    browser = None
    match use_browser:
        case "Chrome":
            browser = playwright.chromium.launch(headless=False)
        case "Firefox":
            browser = playwright.firefox.launch(headless=False)
        case "WebKit":
            browser = playwright.webkit.launch(headless=False)

    context = browser.new_context(
        storage_state=str(session_logged_in), record_video_dir="./video"
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    context.tracing.stop(path=f"./tracing/{request.node.name}.zip")
    browser.close()

    allure.attach.file(
        f"./tracing/{request.node.name}.zip", name="trace", extension=".zip"
    )
    allure.attach.file(
        page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM
    )
