import pytest

from config import settings
from core.api.clients.authentication.authentication_client import get_authentication_client
from core.api.clients.authentication.authentication_schema import LoginRequestSchema


@pytest.fixture()
def delete_user():
    users_email = []
    yield users_email
    request = LoginRequestSchema(email=settings.test_admin.email, password=settings.test_admin.password)
    client = get_authentication_client()
    response = client.login(request=request)
    response_data = response.model_dump()
    headers = {"Authorization": f"Bearer {response_data['access_token']}"}
    response = client.get(url=f"{settings.http_client.url}users/", headers=headers)
    users = response.json()
    for user in users:
        if user["email"] in users_email:
            client.delete(url=f"{settings.http_client.url}users/{user['id']}", headers=headers)
            return

    print(f"User {user['id']} not found.")
