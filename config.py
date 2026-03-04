from enum import StrEnum
from typing import Self

from pydantic import BaseModel, EmailStr, HttpUrl, DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float
    @property
    def client_url(self) -> str:
        return str(self.url)

class Browser(StrEnum):
    CHROME = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"

class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    role: str

class TestUser(User):
    role: str = "user"

class TestAdmin(TestUser):
    role: str = "admin"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",

        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )
    app_url: HttpUrl
    headless: bool
    browser: list[Browser]
    test_user: TestUser
    test_admin: TestAdmin
    allure_results_dir: DirectoryPath
    video_dir: DirectoryPath
    tracing_dir: DirectoryPath
    user_state_file: FilePath
    admin_state_file: FilePath
    max_browser_state_file_age: int = 3600
    http_client: HTTPClientConfig

    @classmethod
    def initialize_settings(cls) -> Self:
        video_dir = DirectoryPath("./video")
        tracing_dir = DirectoryPath("./tracing")
        allure_results_dir = DirectoryPath("./allure-results")
        user_state_file = FilePath(".auth/user_state.json")
        admin_state_file = FilePath(".auth/admin_state.json")

        video_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)
        user_state_file.touch(exist_ok=True)
        admin_state_file.touch(exist_ok=True)

        return Settings(
            video_dir=video_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            user_state_file=user_state_file,
            admin_state_file=admin_state_file,
        )

    def get_base_url(self) -> str:
        return f"{self.app_url}"

settings = Settings.initialize_settings()