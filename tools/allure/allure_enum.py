from enum import StrEnum


class AllureEpics(StrEnum):
    TMS = "Task Management System"
    ADMINISTRATION = "Administration System"
    USER = "User System"


class AllureFeature(StrEnum):
    AUTHENTICATION = "Authentication"
    USERS = "Users"


class AllureStory(StrEnum):
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"
    ADMINISTRATION = "Administration"


class AllureTags(StrEnum):
    AUTHORIZATION = "AUTHORIZATION"
    USER_LOGIN = "USER_LOGIN"
    REGISTRATION = "REGISTRATION"
    CREATE_USER = "CREATE_USER"
    ADMINISTRATION = "Administration"
