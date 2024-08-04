import os
import json

from app.exceptions import ConfigKeyNotFound
from app.config.enums import (
    ConfigEnum,
    BingoConfigEnum,
    AllowsPhotoByEventEnum,
    AllowsPhotoEnum,
    UploadFileEnum
)
from app.config.classes import (
    BingoConfig,
    AllowsPhotoByEventConfig,
    AllowsPhotoConfig,
    UploadFileConfig
)

class Config:

    CONFIG_PATH = "config.json"
    
    config: dict = {}

    def load_config(self) -> dict:
        if os.path.exists(self.CONFIG_PATH):
            self.config = self.read_config()
        else:
            self.config = self.default_config()
        self.write_config()
    
    def read_config(self) -> dict:
        with open(self.CONFIG_PATH, "r") as f:
            return json.load(f)
    
    def write_config(self):
        with open(self.CONFIG_PATH, "w") as f:
            json.dump(self.config, f, indent=4)
    
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
                },
                "upload_file": {
                    "upload_folder": "upload",
                }
            }
        }
    
    def validate(
        self,
        values: dict,
        enum: ConfigEnum
    ):
        for key in values:
            if key not in enum.all():
                raise ConfigKeyNotFound(f"Nøkkel '{key}' ble ikke funnet i konfigurasjonsfilen til '{enum.name}'.")

    def get_config(self) -> dict:
        return self.config
    
    def get(self, key: str) -> str | dict:
        value = self.config.get(key, None)
        if value is None:
            raise ConfigKeyNotFound(f"Nøkkel '{key}' ble ikke funnet i konfigurasjonsfilen.")
        return value
    
    @property
    def download_folder(self) -> str:
        return self.get("download_folder")

    def prompt(self) -> bool:
        return self.get("prompt") == "true"
    
    @property
    def bingo(self) -> BingoConfig:
        values = self.get("scripts").get("bingo")
        self.validate(values, BingoConfigEnum)
        return BingoConfig(**values)
    
    @property
    def __events(self) -> dict:
        return self.get("scripts").get("events")
    
    @property
    def __allows_photo(self) -> dict:
        return self.__events.get("allows_photo")

    @property
    def allows_photo_by_event(self) -> AllowsPhotoByEventConfig:
        values: dict = self.__allows_photo.get("by_event")
        self.validate(values, AllowsPhotoByEventEnum)
        with_event_id = values.get("with_event_id") == "true"
        return AllowsPhotoByEventConfig(
            with_event_id=with_event_id,
            file_name=values.get("file_name")
        )

    @property
    def allows_photo(self) -> AllowsPhotoConfig:
        values: dict = self.__allows_photo.get("all")
        self.validate(values, AllowsPhotoEnum)
        return AllowsPhotoConfig(**values)

    @property
    def upload_file(self) -> UploadFileConfig:
        values = self.get("scripts").get("upload_file")
        self.validate(values, UploadFileEnum)
        return UploadFileConfig(**values)


config = Config()