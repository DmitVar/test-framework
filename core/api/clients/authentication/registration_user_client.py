import allure
from httpx import Response

from config import settings
from core.api.clients.api_client import APIClient
from core.api.clients.authentication.registration_schema import CreateUserRequestSchema, CreateUserResponseSchema
from core.api.clients.public_http_builder import get_public_http_client


class RegistrationUserClient(APIClient):
    @allure.step('Register user')
    def register_user_api(self, request: CreateUserRequestSchema)->Response:
        return self.post(
            url=f"{settings.http_client.url}auth/register",
            json=request.model_dump(by_alias=True)
        )

    def register_user(self, request: CreateUserRequestSchema)->CreateUserResponseSchema:
        response = self.register_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

    def register_admin_api(self, request: CreateUserRequestSchema)->Response:
        return self.post(
            url=f"{settings.http_client.url}auth/register-admin",
            json=request.model_dump(by_alias=True)
        )
    def register_admin(self, request: CreateUserRequestSchema)->CreateUserResponseSchema:
        response = self.register_admin_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

    def register_guest_api(self, request: CreateUserRequestSchema)->Response:
        return self.post(
            url=f"{settings.http_client.url}auth/register-guest",
            json=request.model_dump(by_alias=True)
        )
    def register_guest(self, request: CreateUserRequestSchema)->CreateUserResponseSchema:
        response = self.register_guest_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_registration_user_client() -> RegistrationUserClient:
    return RegistrationUserClient(client=get_public_http_client())




