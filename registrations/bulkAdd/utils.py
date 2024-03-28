import requests
import json

from settings import (
    DEV_EVENT_ENDPOINT,
    DEV_ADD_REGISTRATION_ENDPOINT
)


def load_csv(file_path: str) -> list[tuple]:
    """
    Load a CSV file and return a list of strings.
    """
    data = []
    with open(file_path, encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(",")
            data.append(line[0])
    return data


def add_registration(token: str, user_id: str, event_id: str) -> None:
    """
    Add a registration to the database.
    """
    headers = {
        "Content-Type": "application/json",
        "x-csrf-token": token
    }

    payload = json.dumps({
        "user": user_id
    })

    url = f"{DEV_EVENT_ENDPOINT}{event_id}{DEV_ADD_REGISTRATION_ENDPOINT}"

    response = requests.post(
        url=url,
        headers=headers,
        data=payload
    )
    
    return response.status_code
