from enum import StrEnum


class AllureEpics(StrEnum):
    TMS = "Task Management System"
    ADMINISTRATION = "Administration System"
    USER = "User System"


class AllureFeature(StrEnum):
    AUTHENTICATION = "Authentication"
    USERS = "Users"
    BOARDS = "Boards"


class AllureStory(StrEnum):
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"
    ADMINISTRATION = "Administration"
    TASK_MANAGEMENT = "Task Management"
    BOARD_OPERATIONS = "Board Operations"
    TASK_LIFECYCLE = "Task Lifecycle"


class AllureTags(StrEnum):
    AUTHORIZATION = "AUTHORIZATION"
    USER_LOGIN = "USER_LOGIN"
    REGISTRATION = "REGISTRATION"
    CREATE_USER = "CREATE_USER"
    ADMINISTRATION = "Administration"
    CREATE_BOARD = "CREATE_BOARD"
    BOARD = "BOARD"
