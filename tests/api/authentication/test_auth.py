import allure
import pytest
from allure_commons.types import Severity
from faker import Faker
from http import HTTPStatus

from config import settings
from core.api.clients.authentication.authentication_client import get_authentication_client
from core.api.clients.authentication.authentication_schema import LoginResponseSchema
from core.api.clients.authentication.registration_schema import CreateUserRequestSchema, CreateUserResponseSchema
from core.api.clients.authentication.registration_user_client import get_registration_user_client
from core.api.clients.errors_schema import InternalErrorResponseSchema
from core.api.clients.private_http_builder import AuthenticationUserSchemas
from tools.allure.allure_enum import AllureEpics, AllureFeature, AllureStory, AllureTags
from tools.assertion.authentication import assert_register_response
from tools.assertion.base import assert_status_code
from tools.assertion.schema import validate_json_schema

faker = Faker()
@allure.epic(AllureEpics.TMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.tag(AllureTags.REGISTRATION, AllureTags.CREATE_USER)
@allure.severity(Severity.CRITICAL)
@pytest.mark.authorization
@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.registration
class TestAuthentication:
    def test_get_info_about_current_user(self):
        user = AuthenticationUserSchemas(email=settings.test_admin.email, password=settings.test_admin.password)
        client = get_authentication_client()
        response = client.login_api(user)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_register_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_register_user(self, delete_user):
        user = CreateUserRequestSchema(username=faker.first_name(), email=faker.email(), password=faker.password())
        client = get_registration_user_client()
        response = client.register_user_api(user)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_register_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
        delete_user.append(user.email)

    def test_register_admin(self, delete_user):
        user = CreateUserRequestSchema(username=faker.first_name(), email=faker.email(), password=faker.password())
        client = get_registration_user_client()
        response = client.register_admin_api(user)
        response_data = InternalErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)
        validate_json_schema(response.json(), response_data.model_json_schema())
        delete_user.append(user.email)

    def test_register_guest(self, delete_user):
        user = CreateUserRequestSchema(username=faker.first_name(), email=faker.email(), password=faker.password())
        client = get_registration_user_client()
        response = client.register_guest_api(user)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_register_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
        delete_user.append(user.email)
