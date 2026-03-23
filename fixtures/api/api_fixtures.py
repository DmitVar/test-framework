import pytest

from config import settings
from core.api.clients.authentication.authentication_client import get_authentication_client
from core.api.clients.authentication.authentication_schema import LoginRequestSchema


@pytest.fixture
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


@pytest.fixture
def delete_board():
    boards_title = []
    yield boards_title
    request = LoginRequestSchema(email=settings.test_user.email, password=settings.test_user.password)
    client = get_authentication_client()
    response = client.login(request=request)
    response_data = response.model_dump()
    headers = {"Authorization": f"Bearer {response_data['access_token']}"}
    response = client.get(url=f"{settings.http_client.url}boards/", headers=headers)
    boards = response.json()
    for board in boards:
        if board["title"] in boards_title:
            client.delete(url=f"{settings.http_client.url}boards/{board['id']}", headers=headers)

@pytest.fixture()
def get_token_admin_session():
    request = LoginRequestSchema(email=settings.test_admin.email, password=settings.test_admin.password)
    client = get_authentication_client()
    response = client.login(request=request)
    response_data = response.model_dump()
    token = response_data["access_token"]
    return token

@pytest.fixture
def get_token_user_session():
    request = LoginRequestSchema(email=settings.test_user.email, password=settings.test_user.password)
    client = get_authentication_client()
    response = client.login(request=request)
    response_data = response.model_dump()
    token = response_data["access_token"]
    return token