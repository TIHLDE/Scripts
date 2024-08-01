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

Du vil bli spurt om ID til arrangementet for å kunne bruke denne funksjonen. Du finner ID til arrangementet ved å gå til https://tihlde.org/arrangementer, og velge et arrangement. ID til arrangementet vil være tallet i URL-en.

Eksempel på bruk:
make start args="get_registrations_that_allow_photo_by_event"

Husk at du må ha en gyldig API-token og riktig rettigheter for å kunne bruke denne funksjonen.
"""
                )
            case FunctionName.ALLOW_PHOTO_BY_DEFAULT.value:
                print(
"""
Dette programmet henter ut informasjon om alle brukere som ikke har tillatt å bli tatt bilde av som standard. Dette vil si at brukeren ikke har krysset av for at de tillater å bli tatt bilde av i arrangementer.

Eksempel på bruk:
make start args="get_users_with_not_allowed_photo_by_default"

Husk at du må ha en gyldig API-token og riktig rettigheter for å kunne bruke denne funksjonen.
"""
                )
            case FunctionName.CREATE_BINGO.value:
                print(
"""
Dette programmet genererer bingobrett og slår sammen dem til en PDF-fil. Programmet bruker en liste med setninger som du kan endre i fila 'sentences.txt'. Du finner filen i 'app/scripts/bingo'.

Eksempel på bruk:
make start args="create_bingo_sheets"

Du trenger ingen API-token for å kunne bruke denne funksjonen. Resultatet vil bli lagret i mappen 'downloads'. Hvis du kjører programmet flere ganger, vil det overskrive det gamle bingobrettet. Hvis du vil beholde det gamle bingobrettet, må du flytte det til en annen mappe før du kjører programmet på nytt.
"""
                )
            case FunctionName.ADD_REGISTRATIONS.value:
                print(
"""
Dette programmet legger til brukere i et arrangement. Du må legge ved en CSV-fil med brukerinformasjon i filen 'users.csv' i 'app/scripts/events/bulk_add/'. Programmet vil lese filen og legge til brukerne i arrangementet.

Filen skal være i følgende format:
user_id,mame,email

Eksempel på bruk:
make start args="bulk_add_registrations_to_event"

Husk at du må ha en gyldig API-token og riktig rettigheter for å kunne bruke denne funksjonen.
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