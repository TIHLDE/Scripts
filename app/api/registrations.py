from app.api.api import fetch
from app.api.urls import URLS


def get_registrations_that_allow_photo(token: str, event_id: str, page: int) -> dict:
    """
    Get a list of registrations that allow photo.
    """
    headers = {
        "Content-Type": "application/json",
        "x-csrf-token": token
    }

    url = f"{URLS.events}/{event_id}/registrations/?&is_on_wait=false&page={page}"

    response = fetch(url=url, headers=headers, method="GET")

    return response