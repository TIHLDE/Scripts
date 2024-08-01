import os

from app.exceptions import FileNotFound


def load_csv(file_path: str, error_message: str | None = None) -> list[tuple]:
    """
    Load a CSV file and return a list of strings.
    """
    if not os.path.exists(file_path):
        raise FileNotFound(
            error_message if error_message
            else "Kunne ikke finne filen."
        )

    with open(file_path, encoding="UTF-8") as f:
        lines = f.readlines()
        return [line.strip() for line in lines]