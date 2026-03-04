import allure
from httpx import Response

from core.api.clients.api_client import APIClient
from core.api.clients.public_http_builder import get_public_http_client
from core.api.clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from config import settings

class AuthenticationClient(APIClient):
    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.post(
            url=f"{settings.http_client.url}auth/login",
            json=request.model_dump(by_alias=True)
        )

    def login(self, request: LoginRequestSchema) -> Response:
        response = self.login_api(request=request)
        return LoginResponseSchema.model_validate_json(response.text)

def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())