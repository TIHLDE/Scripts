import requests


def get_users(token: str, page: int) -> list[tuple]:
    """
    Get a list of users that have not allowed photo.
    """
    headers = {
        "Content-Type": "application/json",
        "x-csrf-token": token
    }

    url = f"https://api.tihlde.org/users/?has_allowed_photo=false&page={page}"

    response = requests.get(
        url=url,
        headers=headers
    )

    return response.json()