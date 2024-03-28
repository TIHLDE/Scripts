import sys

from utils import (
    load_csv,
    add_registration
)


def main():
    if len(sys.argv) > 2:
        X_CSRF_TOKEN = sys.argv[1]
        event_id = sys.argv[2]
    else:
        print("Du må oppgi din X-CSRF-TOKEN og id til arrangement.")
        return

    user_ids = load_csv("registrations/bulkAdd/deltagere.csv")

    for user_id in user_ids:
        try:
            status_code = add_registration(X_CSRF_TOKEN, user_id, event_id)

            match status_code:
                case 201:
                    print(f"Bruker: {user_id} lagt til i arrangement med id: {event_id}.")
                case 400:
                    print(f"Bruker {user_id} er allerede registrert i arrangement med id: {event_id}.")
                case 403:
                    print("Du har ikke tilgang til å legge til brukere i dette arrangementet.")

        except Exception as e:
            print(f"Kunne ikke legge til bruker {user_id} til arrangement {event_id}. Prøv igjen, eller kontakt Index hvis problemet vedtar.")
            print(e)
            continue


if __name__ == "__main__":
    main()