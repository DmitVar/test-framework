from http import HTTPStatus
from typing import Any

import allure
import pytest
from allure_commons.types import Severity
from pydantic import TypeAdapter

from core.api.clients.errors_schema import InternalErrorResponseSchema
from core.api.clients.users.users_client import get_users_client
from core.api.clients.users.users_schemas import (
    UserSchema,
    RequestUpdateUserSchema,
    RequestUpdateUserPasswordSchema,
    UserTaskSchema,
    RequestUpdateUserAvatarSchema,
    ResponseGetUserAvatarSchema,
)
from tools.allure.allure_enum import AllureEpics, AllureFeature, AllureStory, AllureTags
from tools.assertion.base import assert_status_code
from tools.assertion.schema import validate_json_schema
from tools.assertion.users import assert_users_response, assert_update_user_response


@allure.epic(AllureEpics.TMS)
@allure.feature(AllureFeature.USERS)
@allure.story(AllureStory.ADMINISTRATION)
@allure.tag(AllureTags.ADMINISTRATION)
@allure.severity(Severity.CRITICAL)
@pytest.mark.api
class TestUsersApi:

    @staticmethod
    def searches_user_by_email(
        users: list[dict[str, Any]], email: str
    ) -> dict[str, Any] | None:
        for user in users:
            if user["email"] == email:
                return user
        return None

    @staticmethod
    def parse_change_user_dict(
        change_dict: dict[str, str], old_dict: dict[str, str]
    ) -> dict[str, str]:
        for key, value in change_dict.items():
            old_dict[key] = value
        return old_dict

    @allure.title("Test endpoint get public users")
    def test_get_public_users(self):
        client = get_users_client()
        response = client.get_public_users()
        response_data = response.json()

        adapter = TypeAdapter(list[UserSchema])
        adapter.validate_python(response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.title("Test endpoint get current user")
    def test_get_current_user(self, create_user, delete_user):
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

    @allure.title("Test endpoint get all users")
    def test_get_all_users(self):
        client = get_users_client()
        response = client.get_users()
        response_data = response.json()

        adapter = TypeAdapter(list[UserSchema])
        adapter.validate_python(response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.title("Test endpoint get user by valid id")
    def test_get_user_by_valid_id(self):
        client = get_users_client()
        response = client.get_user_by_id(6)
        response_data = UserSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Test endpoint get user by invalid id")
    def test_get_user_by_invalid_id(self):
        client = get_users_client()
        response = client.get_user_by_id(138)
        response_data = InternalErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Test endpoint update user")
    @pytest.mark.parametrize(
        "change_dict",
        [
            {
                "username": "Aladin",
                "email": "aladin@email.com",
                "role": "guest",
                "avatar_url": "/home/image/aladin.png",
            },
            {
                "username": "Aladin",
            },
            {
                "email": "aladin@email.com",
            },
            {
                "role": "admin",
            },
            {
                "avatar_url": "/home/image/aladin.png",
            },
        ],
        ids=["all_creds", "username", "email", "role", "avatar_url"],
    )
    def test_update_user(self, create_user, delete_user, change_dict):
        try:
            user, user_cred = create_user
            client = get_users_client()
            all_users_response = client.get_users()
            all_users = all_users_response.json()
            all_user_creds = self.searches_user_by_email(all_users, user_cred["email"])
            update_user = self.parse_change_user_dict(change_dict, all_user_creds)
            user = RequestUpdateUserSchema(**update_user)
            response = client.update_user_api(user, all_user_creds["id"])
            response_data = UserSchema.model_validate_json(response.text)

            assert_status_code(response.status_code, HTTPStatus.OK)
            assert_update_user_response(response_data, user)
            validate_json_schema(response.json(), response_data.model_json_schema())
        finally:
            delete_user.append(user.email)

    @allure.title("Test endpoint delete user")
    def test_delete_user(self, create_user):
        _, user_cred = create_user
        client = get_users_client()
        all_users_response = client.get_users()
        all_users = all_users_response.json()
        all_user_creds = self.searches_user_by_email(all_users, user_cred["email"])
        user_id = all_user_creds["id"]
        response = client.delete_user_by_id(user_id)

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)

    @allure.title("Test endpoint update user password")
    @pytest.mark.parametrize(
        "new_password, expected_cod", [("fguerhu12fger", 200), ("  ", 422)]
    )
    def test_update_user_password(
        self, create_user, delete_user, new_password, expected_cod
    ):
        try:
            user, _ = create_user
            client = get_users_client(user)
            current_user_creds_response = client.get_current_user()
            user_creds = current_user_creds_response.json()
            request = RequestUpdateUserPasswordSchema(new_password=new_password)
            response = client.update_user_password(
                user_id=user_creds["id"], request=request
            )
            if expected_cod == 200:
                assert_status_code(response.status_code, HTTPStatus.OK)
            else:
                assert_status_code(
                    response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY
                )
        finally:
            delete_user.append(user.email)

    @allure.title("Test endpoint get current user tasks")
    def test_get_current_user_tasks(self):
        client = get_users_client()
        response = client.get_tasks_current_user()
        response_data = response.json()

        adapter = TypeAdapter(list[UserTaskSchema])
        adapter.validate_python(response_data)
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.title("Test endpoint update user avatar")
    def test_update_user_avatar(self, create_user, delete_user):
        try:
            user, _ = create_user
            client = get_users_client(user)
            response_current_user = client.get_current_user()
            all_user_creds = response_current_user.json()
            request = RequestUpdateUserAvatarSchema(avatar_url="/home/image/aladin.png")
            response = client.update_user_avatar(
                request=request, user_id=all_user_creds["id"]
            )
            assert_status_code(response.status_code, HTTPStatus.OK)
        finally:
            delete_user.append(user.email)

    @allure.title("Test endpoint get user avatar")
    def test_get_user_avatar(self):
        client = get_users_client()
        response_current_user = client.get_current_user()
        all_user_creds = response_current_user.json()
        response = client.get_user_avatar(user_id=all_user_creds["id"])
        response_data = ResponseGetUserAvatarSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())
