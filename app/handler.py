import sys

from app.exceptions import (
    FunctionNotSpecified,
    InvalidFunction
)
from app.enums import FunctionName


def handle_function_call():
    """
    Handle function call.
    """
    
    if len(sys.argv) < 2:
        raise FunctionNotSpecified()
    
    function = sys.argv[1]

    match function:
        case FunctionName.ALLOW_PHOTO_BY_EVENT.value:
            from app.scripts.events import allows_photo_by_event
            allows_photo_by_event()
        case FunctionName.ALLOW_PHOTO_BY_DEFAULT.value:
            from app.scripts.events import allows_photo
            allows_photo()
        case FunctionName.CREATE_BINGO.value:
            from app.scripts.bingo import create_bingo_sheets
            create_bingo_sheets()
        case FunctionName.ADD_REGISTRATIONS.value:
            from app.scripts.events import bulk_add
            bulk_add()
        case FunctionName.UPLOAD_FILE.value:
            from app.scripts.files import upload
            upload()
        case FunctionName.DELETE_FILE.value:
            from app.scripts.files import delete
            delete()
        case _:
            raise InvalidFunction()