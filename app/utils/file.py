import os

from io import BytesIO

from app.config import config
from app.utils.dir import list_files


def get_file_path() -> tuple[str, str]:
    upload_folder = config.upload_file.upload_folder
    list_files(upload_folder)

    try:
        file_name = input("Skriv navnet til filen du vil laste opp: ")
        if not os.path.exists(f"{upload_folder}/{file_name}"):
            raise FileNotFoundError()
        
        return f"{upload_folder}/{file_name}", file_name
    except:
        print("Denne filen eksisterer ikke.")
        return get_file_path()


def blob_to_file(blob: bytes, name: str) -> BytesIO:
    file = BytesIO(blob)
    file.name = name
    return file


def extract_file_info_from_url(url: str) -> tuple[str, str]:
    """
    Extract container name and blob name from the URL.
    """
    parts = url.split("/")
    return parts[-2], parts[-1]


def get_blob(path: str) -> bytes:
    with open(path, "rb") as file:
        return file.read()


def parse_file(response: dict) -> str:
    return response.get("url", None)


def save_url(url: str):
    if not os.path.exists(f"{config.download_folder}/uploaded_files.txt"):
        with open(
            f"{config.download_folder}/uploaded_files.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(f"{url}\n")
        return

    with open(
        f"{config.download_folder}/uploaded_files.txt",
        "a",
        encoding="utf-8"
    ) as f:
        f.write(f"{url}\n")


def get_url() -> str:
    list_uploaded_files()

    return input("Skriv url til filen du vil slette: ").strip()


def update_uploaded_files(url: str):
    with open(
        f"{config.download_folder}/uploaded_files.txt",
        "r",
        encoding="utf-8"
    ) as f:
        urls = f.readlines()
    
    urls = [u.strip() for u in urls if u.strip() != url]

    with open(
        f"{config.download_folder}/uploaded_files.txt",
        "w",
        encoding="utf-8"
    ) as f:
        for u in urls:
            f.write(f"{u}\n")


def list_uploaded_files():
    if not os.path.exists(f"{config.download_folder}/uploaded_files.txt"):
        print("Ingen filer er lastet opp.")
        return

    with open(
        f"{config.download_folder}/uploaded_files.txt",
        "r",
        encoding="utf-8"
    ) as f:
        urls = f.readlines()
    
    print("\nOpplastede filer:")
    for i, url in enumerate(urls):
        print(f" {i + 1}. {url.strip()}")
    print()