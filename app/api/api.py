import requests

from io import BufferedReader

from app.enums import APIMethod
from app.exceptions import InvalidAPIResponse


def fetch(
    url: str,
    headers: dict,
    method: str,
    data: dict | None = None,
    files: dict[str, BufferedReader] | None = None
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
            data=data,
            files=files
        )
    elif method == APIMethod.DELETE.value:
        response = requests.delete(
            url=url,
            headers=headers
        )
    
    try:
        response_json = response.json()
    except ValueError:
        response_json = None

    if response.status_code not in [200, 201, 204]:
        error_message = response_json["detail"] if response_json and "detail" in response_json else response.text
        raise InvalidAPIResponse(error_message)

    return response_json if response_json is not None else {}