import sys

from app.exceptions import (
    FunctionNotSpecified,
    InvalidFunction
)
from app.enums import FunctionName
from app.exceptions import ScriptError
from app.config import (
    ALLOW_PHOTO_BY_DEFAULT,
    ADD_REGISTRATIONS,
    ALLOW_PHOTO_BY_EVENT,
    CREATE_BINGO,
    DELETE_FILE,
    UPLOAD_FILE
)


def describe_function():
    """
    Describe the function.
    """
    try:
        if len(sys.argv) < 2:
            raise FunctionNotSpecified("Du må oppgi en funksjon for å få en beskrivelse av den.")
        
        function = sys.argv[1]

        match function:
            case FunctionName.ALLOW_PHOTO_BY_EVENT.value:
                print(ALLOW_PHOTO_BY_EVENT)
            case FunctionName.ALLOW_PHOTO_BY_DEFAULT.value:
                print(ALLOW_PHOTO_BY_DEFAULT)
            case FunctionName.CREATE_BINGO.value:
                print(CREATE_BINGO)
            case FunctionName.ADD_REGISTRATIONS.value:
                print(ADD_REGISTRATIONS)
            case FunctionName.UPLOAD_FILE.value:
                print(UPLOAD_FILE)
            case FunctionName.DELETE_FILE.value:
                print(DELETE_FILE)
            case _:
                raise InvalidFunction()
    except Exception as e:
        if isinstance(e, ScriptError):
            print(f"\n{e}\n")
            return
        
        print(f"\nEn ukjent feil oppstod, med følgende beskjed: \n\n{e}\n\nVennligst prøv igjen. Hvis problemet vedvarer, kontakt Index.")


if __name__ == "__main__":
    describe_function()