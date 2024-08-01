import sys

from app.exceptions import (
    FunctionNotSpecified,
    InvalidFunction
)
from app.enums import FunctionName


def handle_function_call(token: str):
    """
    Handle function call.
    """
    
    if len(sys.argv) < 2:
        raise FunctionNotSpecified()
    
    function = sys.argv[1]

    match function:
        case FunctionName.ALLOW_PHOTO_BY_EVENT.value:
            from app.scripts.events import allows_photo_by_event
            allows_photo_by_event(token)
        case FunctionName.ALLOW_PHOTO_BY_DEFAULT.value:
            from app.scripts.events import allows_photo
            allows_photo(token)
        case FunctionName.CREATE_BINGO.value:
            from app.scripts.bingo import create_bingo_sheets
            create_bingo_sheets()
        case FunctionName.ADD_REGISTRATIONS.value:
            from app.scripts.events import bulk_add
            bulk_add(token)
        case _:
            raise InvalidFunction()