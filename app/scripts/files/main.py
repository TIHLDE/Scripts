from app.api import (
    upload_file,
    delete_file
)
from app.utils.file import (
    blob_to_file,
    extract_file_info_from_url,
    get_blob,
    get_file_path,
    parse_file,
    save_url,
    get_url,
    update_uploaded_files
)
from app.config import config
from app.utils.token import get_api_token


def upload():
    """
    Upload a file to the server.
    """
    token = get_api_token()

    file_path, file_name = get_file_path()
    
    blob = get_blob(file_path)

    file = blob_to_file(blob, file_name)

    response = upload_file(token, file)
    
    url = parse_file(response)

    save_url(url)
    print(f"Fil lastet opp til {url}. Du kan se alle opplastede filer i {config.download_folder}/uploaded_files.txt")


def delete():
    """
    Delete a file from the server.
    """
    token = get_api_token()

    url = get_url()

    container_name, blob_name = extract_file_info_from_url(url)

    delete_file(token, container_name, blob_name)
    update_uploaded_files(url)

    print(f"Fil slettet fra {url}")