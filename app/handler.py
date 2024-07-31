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
            from app.events import allows_photo_by_event
            allows_photo_by_event(token)
        case FunctionName.ALLOW_PHOTO_BY_DEFAULT.value:
            from app.events import allows_photo
            allows_photo(token)
        case _:
            raise InvalidFunction()