import os

from app.exceptions import ConfigKeyNotFound
from app.config.enums import (
    BingoConfigEnum
)
from app.config.classes import (
    BingoConfig
)

class Config:

    CONFIG_PATH = "config.json"

    def __init__(self):
        self.config: dict = self.load_config()

    def load_config(self) -> dict:
        if os.path.exists(self.CONFIG_PATH):
            with open(self.CONFIG_PATH, "r") as f:
                return f.read()
        
        return self.default_config()
    
    def default_config(self) -> dict:
        return {
            "download_folder": "downloads",
            "prompt": "true",
            "scripts": {
                "bingo": {
                    "pdfs_folder": "app/scripts/bingo/pdfs",
                    "pdf_name": "bingo",
                    "sentences": "app/scripts/bingo/sentences.txt",
                    "number_of_sheets": 10,
                    "cell_width": 120,
                    "cell_height": 120,
                    "x_start": 5,
                    "x_offset": 10,
                    "y_start": 625,
                    "y_offset": 20,
                    "font": "Helvetica",
                    "font_size": 10,
                    "line_height": 20,
                    "max_chars_divider": 6,
                    "rows": 5,
                    "cols": 5
                },
                "events": {
                    "allows_photo": {
                        "by_event": {
                            "file_name": "registrations_allow_photo",
                            "with_event_id": "true"
                        },
                        "all": {
                            "file_name": "all_users_not_allow_photo"
                        }
                    },
                    "bulk_add": {
                        "users_csv": "app/scripts/events/bulk_add/users.csv"
                    }
                }
            }
        }
    
    def validate(
        self,
        values: dict,
        keys: list[str],
        title: str
    ):
        for key in values:
            if key not in keys:
                raise ConfigKeyNotFound(f"Nøkkel '{key}' ble ikke funnet i konfigurasjonsfilen til '{title}'.")

    def get_config(self) -> dict:
        return self.config
    
    def get(self, key: str) -> str | dict:
        value = self.config.get(key, None)
        if value is None:
            raise ConfigKeyNotFound(f"Nøkkel '{key}' ble ikke funnet i konfigurasjonsfilen.")
    
    @property
    def download_folder(self) -> str:
        return self.get("downloads_folder")

    def prompt(self) -> bool:
        return self.get("prompt") == "true"
    
    @property
    def bingo(self) -> BingoConfig:
        values = self.get("scripts").get("bingo")
        self.validate(values, BingoConfigEnum.all(), "bingo")
        return values


config = Config()