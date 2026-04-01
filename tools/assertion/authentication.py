import allure
from core.api.clients.authentication.registration_schema import CreateUserResponseSchema
from tools.assertion.base import assert_equal, assert_is_true
from tools.logger import get_logger

logger = get_logger("AUTHENTICATION_ASSERTIONS")


@allure.step("Check login response")
def assert_register_response(response: CreateUserResponseSchema):
    logger.info("Check register response")
    assert_equal(response.token_type, "bearer", "token_type")
    assert_is_true(response.access_token, "access_token")
