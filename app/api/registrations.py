import json

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

def add_registration(token: str, event_id: str, user_id: str) -> dict:
    """
    Add a registration to an event.
    """
    headers = {
        "Content-Type": "application/json",
        "x-csrf-token": token
    }

    payload = json.dumps({
        "user": user_id
    })

    url = f"{URLS.events}/{event_id}/{URLS.add_registrations}"

    response = fetch(
        url=url,
        headers=headers,
        method="POST",
        data=payload
    )

    return response 