from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity
from pydantic import TypeAdapter

from core.api.clients.authentication.registration_schema import CreateUserRequestSchema
from core.api.clients.users.users_client import get_users_client
from core.api.clients.users.users_schemas import UserSchema
from tools.allure.allure_enum import AllureEpics, AllureFeature, AllureStory, AllureTags
from tools.assertion.base import assert_status_code
from tools.assertion.schema import validate_json_schema
from tools.assertion.users import assert_users_response


@allure.epic(AllureEpics.TMS)
@allure.feature(AllureFeature.USERS)
@allure.story(AllureStory.ADMINISTRATION)
@allure.tag(AllureTags.ADMINISTRATION)
@allure.severity(Severity.CRITICAL)
@pytest.mark.api
class TestUsersApi:
    @allure.title("Test endpoint get public users")
    def test_get_public_users(self):
        client = get_users_client()
        response = client.get_public_users()
        response_data = response.json()

        adapter = TypeAdapter(list[UserSchema])
        adapter.validate_python(response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.title("Test endpoint get current user")
    def test_get_current_user(
            self,
            create_user,
            delete_user
    ):
        try:
            user, user_cred = create_user
            client = get_users_client(user)
            response = client.get_current_user()
            response_data = UserSchema.model_validate_json(response.text)

            assert_status_code(response.status_code, HTTPStatus.OK)
            assert_users_response(response_data, user_cred)
            validate_json_schema(response.json(), response_data.model_json_schema())

        finally:
            delete_user.append(user.email)



