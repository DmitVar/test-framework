from config import settings
from core.api.clients.private_http_builder import get_private_http_client, AuthenticationUserSchemas


def test_get_info_about_current_user():
    user = AuthenticationUserSchemas(email=settings.test_admin.email, password=settings.test_admin.password)
    client = get_private_http_client(user)
    response = client.get('/users/me')
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['email'] == settings.test_admin.email
