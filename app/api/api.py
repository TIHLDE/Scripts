import requests

from app.enums import APIMethod
from app.exceptions import InvalidAPIResponse


def fetch(
    url: str,
    headers: dict,
    method: str,
    data: dict | None = None
) -> dict:
    """
    Make a request to the API.
    """
    if method == APIMethod.GET.value:
        response = requests.get(
            url=url,
            headers=headers
        )
    elif method == APIMethod.POST.value:
        response = requests.post(
            url=url,
            headers=headers,
            data=data
        )

    if response.status_code not in [200, 201, 204]:
        json = response.json()
        error_message = json["detail"] if "detail" in json else "Unknown error"
        raise InvalidAPIResponse(error_message)

    return response.json()