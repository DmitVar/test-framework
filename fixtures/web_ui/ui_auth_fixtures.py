import json

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from config import settings
from fixtures.api.api_fixtures import get_token_user_session
from tools.playwright.init_page import init_page


def create_storage_state(token: str):
    origin = "http://localhost:3000"
    auth_storage_value = {
        "state": {
            "token": token,
            "user": None,
            "isAuthenticated": True
        },
        "version": 0
    }

    return {
        "cookies": [],
        "origins": [
            {
                "origin": origin,
                "localStorage": [
                    {"name": "token", "value": token},
                    {"name": "auth-storage", "value": json.dumps(auth_storage_value)}
                ]
            }
        ]
    }

@pytest.fixture(params=settings.browser)
def playwright_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from init_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
    )

@pytest.fixture(params=settings.browser)
def playwright_page_with_admin_state(request: SubRequest, playwright: Playwright, get_token_admin_session) -> Page:
    token = get_token_admin_session
    state = create_storage_state(token)
    yield from init_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=state
    )

@pytest.fixture(params=settings.browser)
def playwright_page_with_user_state(request: SubRequest, playwright: Playwright, get_token_user_session) -> Page:
    token = get_token_user_session
    state = create_storage_state(token)
    yield from init_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=state
    )
