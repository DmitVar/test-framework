import allure

from core.api.clients.users.users_schemas import UserSchema
from tools.assertion.base import assert_equal, assert_is_true
from tools.logger import get_logger

logger = get_logger('USERS_ASSERTIONS')


@allure.step('Check users response')
def assert_users_response(response: UserSchema, user: dict[str, str]) -> None:
    logger.info('Check users response')
    user
    assert_equal(response.username, user['name'], "Username")
    assert_equal(response.email, user['email'], "Email")
