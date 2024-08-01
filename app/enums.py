from enum import Enum


class APIMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class FunctionName(Enum):
    ALLOW_PHOTO_BY_EVENT = "get_registrations_that_allow_photo_by_event"
    ALLOW_PHOTO_BY_DEFAULT = "get_users_with_not_allowed_photo_by_default"
    CREATE_BINGO = "create_bingo_sheets"
    ADD_REGISTRATIONS = "bulk_add_registrations_to_event"

    @classmethod
    def all(cls) -> list[str]:
        return [function.value for function in cls]


class FileFormat(Enum):
    TXT = "txt"
    CSV = "csv"