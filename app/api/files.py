from io import BufferedReader

from app.api.api import fetch
from app.api.urls import URLS


def upload_file(token: str, file: BufferedReader) -> dict:
    """
    Upload a file to the server.
    """
    files = {
        "file": file
    }

    headers = {
        "x-csrf-token": token
    }

    response = fetch(
        url=URLS.file_upload,
        headers=headers,
        method="POST",
        files=files
    )

    return response


def delete_file(token: str, container_name: str, blob_name: str):
    """
    Delete a file from the server.
    """
    headers = {
        "content-type": "application/json",
        "x-csrf-token": token
    }

    response = fetch(
        url=f"{URLS.delete_file}{container_name}/{blob_name}/",
        headers=headers,
        method="DELETE",
    )