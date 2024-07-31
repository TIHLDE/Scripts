from app.api.api import fetch
from app.api.urls import URLS


def get_users_with_not_allowed_photo(token: str, page: int) -> list[tuple]:
    """
    Get a list of users that have not allowed photo.
    """
    headers = {
        "Content-Type": "application/json",
        "x-csrf-token": token
    }

    url = f"{URLS.users}?has_allowed_photo=false&page={page}"

    response = fetch(url=url, headers=headers, method="GET")

    return response