from app.api import (
    get_registrations_that_allow_photo,
    get_users_with_not_allowed_photo
)
from app.utils.registrations import parse_registrations
from app.utils.users import parse_users
from app.utils.events import get_event_id


def allows_photo_by_event(token: str):
    """
    Download a list of registrations with info about allowance of being taken photo of for a specific event.
    """
    event_id = get_event_id()

    page = 1

    print("\nHenter registreringer...\n")

    json = get_registrations_that_allow_photo(
        token=token,
        event_id=event_id,
        page=page
    )

    registrations = json["results"]
    has_next_page = json["next"]

    while has_next_page:
        page += 1

        json = get_registrations_that_allow_photo(
            token=token,
            event_id=event_id,
            page=page
        )

        registrations += json["results"]
        has_next_page = json["next"]
    
    users = parse_registrations(registrations, event_id)

    users.sort(key=lambda user: user.allow_photo)

    file_name = f"downloads/event_{event_id}_registrations_allow_photo.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        for user in users:
            f.write(f"{user.user_id} - {user.first_name} {user.last_name} - {user.email} - Vil bli tatt bilde av: {user.allow_photo}\n")
    
    print(f"Registreringer lagret i {file_name}")


def allows_photo(token: str):
    """
    Download a list of users that don't allow being taken photo of for all events by default.
    """

    page = 1

    print("\nHenter brukere...\n")

    json = get_users_with_not_allowed_photo(
        token=token,
        page=page
    )

    users = json["results"]
    has_next_page = json["next"]

    while has_next_page:
        page += 1

        json = get_users_with_not_allowed_photo(
            token=token,
            page=page
        )

        users += json["results"]
        has_next_page = json["next"]
    
    users = parse_users(users)

    file_name = f"downloads/all_users_not_allow_photo.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        for user in users:
            f.write(f"{user.user_id} - {user.first_name} {user.last_name} - {user.email} - Vil bli tatt bilde av: False\n")
    
    print(f"Brukere lagret i {file_name}")