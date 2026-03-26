from httpx import Client
from pydantic import BaseModel, EmailStr

from core.api.clients.authentication.authentication_client import  get_authentication_client
from core.api.clients.authentication.authentication_schema import LoginRequestSchema
from core.api.clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings

class AuthenticationUserSchemas(BaseModel):
    email: EmailStr
    password: str

def get_private_http_client(user: LoginRequestSchema) -> Client:
    authenticated_client = get_authentication_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authenticated_client.login(login_request)
    access_token = login_response.access_token

    return Client(
        timeout=settings.http_client.timeout,
        base_url=f"{settings.http_client.url}",
        headers={"Authorization": f"Bearer {access_token}" },
        event_hooks={"request": [curl_event_hook, log_request_event_hook], "response": [log_response_event_hook, ]}
    )
