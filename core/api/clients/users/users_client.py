from httpx import Response

from config import settings
from core.api.clients.api_client import APIClient
from core.api.clients.private_http_builder import get_private_http_client
from core.api.clients.users.users_schemas import (
    RequestUpdateUserAvatarSchema,
    RequestUpdateUserPasswordSchema,
    RequestUpdateUserSchema,
)


class UsersClient(APIClient):
    def get_public_users(self) -> Response:
        return self.get(url=f"{settings.http_client.url}users/public")

    def get_current_user(self) -> Response:
        return self.get(url=f"{settings.http_client.url}users/me")

    def get_users(self) -> Response:
        return self.get(url=f"{settings.http_client.url}users/")

    def get_user_by_id(self, user_id: int) -> Response:
        return self.get(url=f"{settings.http_client.url}users/{user_id}")

    def update_user_api(
        self, request: RequestUpdateUserSchema, user_id: int
    ) -> Response:
        return self.put(
            url=f"{settings.http_client.url}users/{user_id}",
            json=request.model_dump(by_alias=True),
        )

    def delete_user_by_id(self, user_id: int) -> Response:
        return self.delete(url=f"{settings.http_client.url}users/{user_id}")

    def update_user_password(
        self, request: RequestUpdateUserPasswordSchema, user_id: int
    ) -> Response:
        return self.put(
            url=f"{settings.http_client.url}users/{user_id}/password",
            json=request.model_dump(by_alias=True),
        )

    def get_tasks_current_user(self, skip: int = 0, limit: int = 100) -> Response:
        query_params = {"skip": skip, "limit": limit}
        return self.get(
            url=f"{settings.http_client.url}users/me/tasks", params=query_params
        )

    def update_user_avatar(
        self, request: RequestUpdateUserAvatarSchema, user_id: int
    ) -> Response:
        return self.put(
            url=f"{settings.http_client.url}users/{user_id}/avatar",
            json=request.model_dump(by_alias=True),
        )

    def get_user_avatar(self, user_id: int) -> Response:
        return self.get(url=f"{settings.http_client.url}users/{user_id}/avatar")


def get_users_client(user=settings.test_admin) -> UsersClient:
    return UsersClient(client=get_private_http_client(user))
