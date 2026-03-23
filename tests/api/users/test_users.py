from http import HTTPStatus

import allure
from allure_commons.types import Severity
from pydantic import TypeAdapter

from core.api.clients.users.users_client import get_users_client
from core.api.clients.users.users_schemas import UserSchema
from tools.allure.allure_enum import AllureEpics, AllureFeature, AllureStory, AllureTags
from tools.assertion.base import assert_status_code
from tools.assertion.schema import validate_json_schema


@allure.epic(AllureEpics.TMS)
@allure.feature(AllureFeature.USERS)
@allure.story(AllureStory.ADMINISTRATION)
@allure.tag(AllureTags.ADMINISTRATION)
@allure.severity(Severity.CRITICAL)
class TestUsersApi:
    def test_get_public_users(self):
        client = get_users_client()
        response = client.get_public_users()
        response_data = response.json()

        adapter = TypeAdapter(list[UserSchema])
        adapter.validate_python(response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)

