import allure

from core.api.clients.users.users_schemas import UserSchema, RequestUpdateUserSchema
from tools.assertion.base import assert_equal, assert_is_true
from tools.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")


@allure.step("Check users response")
def assert_users_response(response: UserSchema, user: dict[str, str]) -> None:
    logger.info("Check users response")
    assert_equal(response.username, user["name"], "Username")
    assert_equal(response.email, user["email"], "Email")


@allure.step("Check update user response response")
def assert_update_user_response(
    response: UserSchema, user: RequestUpdateUserSchema
) -> None:
    logger.info("Check update user response")
    assert_equal(response.username, user.username, "Username")
    assert_equal(response.email, user.email, "Email")
    assert_equal(response.role, user.role, "Role")
    assert_equal(response.avatar_url, user.avatar_url, "Avatar URL")
