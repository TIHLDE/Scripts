from app.utils.events import get_event_id
from app.utils.csv import load_csv
from app.api import add_registration
from app.utils.users import parse_csv_users
from app.exceptions import ScriptError


def bulk_add(token: str):
    """
    Bulk add participants to event.
    """
    event_id = get_event_id()

    CSV_PATH = "app/scripts/events/bulk_add/users.csv"

    users = load_csv(
        CSV_PATH,
        error_message="CSV-filen mangler. Legg til en fil med navn 'users.csv' med bruker informasjon i app/scripts/events/bulk_add/."
    )

    users = parse_csv_users(users)

    print("\nLegger til brukere...\n")

    for user in users:
        try:
            add_registration(
                token=token,
                event_id=event_id,
                user_id=user.user_id
            )
            print(f" - Bruker {user.name} lagt til i arrangement med id: {event_id}.")
        except Exception as e:
            if isinstance(e, ScriptError):
                print(f"Følgende feil skjedde:\n\n {e}\n\nHopper over bruker.")
            else:
                print(f"Kunne ikke legge til bruker {user.name} til arrangement {event_id}. Hopper over bruker")
    
    print("\nAlle brukere lagt til i arrangementet.\n")
