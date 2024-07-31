import sys

from app.exceptions import (
    FunctionNotSpecified,
    InvalidFunction
)
from app.enums import FunctionName
from app.exceptions import ScriptError


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
                print(
"""
Dette programmet henter ut informasjon om alle brukere som har plass på et arrangement, og viser om brukeren har tillatt å bli tatt bilde av eller ikke.

Du vil bli spurt om ID til arrangementet for å kunne bruke denne funksjonen. Du finner ID til arrangementet ved å gå til https://tihlde.org, og velge et arrangement. ID til arrangementet vil være tallet i URL-en.

Eksempel på bruk:
make start args="get_registrations_that_allow_photo_by_event"

Husk at du må ha en gyldig API-nøkkel og riktig rettigheter for å kunne bruke denne funksjonen.
"""
                )
            case FunctionName.ALLOW_PHOTO_BY_DEFAULT.value:
                print(
"""
Dette programmet henter ut informasjon om alle brukere som ikke har tillatt å bli tatt bilde av som standard. Dette vil si at brukeren ikke har krysset av for at de tillater å bli tatt bilde av i arrangementer.

Eksempel på bruk:
make start args="get_users_with_not_allowed_photo_by_default"

Husk at du må ha en gyldig API-nøkkel og riktig rettigheter for å kunne bruke denne funksjonen.
"""
                )
            case _:
                raise InvalidFunction()
    except Exception as e:
        if isinstance(e, ScriptError):
            print(f"\n{e}\n")
            return
        
        print(f"\nEn ukjent feil oppstod, med følgende beskjed: \n\n{e}\n\nVennligst prøv igjen. Hvis problemet vedvarer, kontakt Index.")


if __name__ == "__main__":
    describe_function()