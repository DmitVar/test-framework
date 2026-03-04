import allure_commons
import pytest

from tools.logger import get_logger

logger = get_logger("ALLURE")

pytest_plugins = [
    "fixtures.web_ui.ui_auth_fixtures",
    "fixtures.allure",
    "fixtures.api.api_fixtures",
]

class AllureLogger:
    @allure_commons.hookimpl
    def start_step(self, title):
        logger.info(f" {title}")

allure_commons.plugin_manager.register(AllureLogger())

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_logreport(report):
    yield
    if report.when == 'call' or (report.when == 'setup' and report.skipped):
        print()
