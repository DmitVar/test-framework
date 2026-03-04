from enum import StrEnum


class AllureEpics(StrEnum):
    TMS = "Task Management System"
    ADMINISTRATION = "Administration System"
    USER = "User System"

class AllureFeature(StrEnum):
    AUTHENTICATION = "Authentication"

class AllureStory(StrEnum):
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"

class AllureTags(StrEnum):
    AUTHORIZATION = "AUTHORIZATION"
    USER_LOGIN = "USER_LOGIN"
    REGISTRATION = "REGISTRATION"
    CREATE_USER = "CREATE_USER"
