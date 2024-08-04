from enum import Enum


class ConfigEnum(Enum):
    @classmethod
    def all(cls) -> list[str]:
        return [key.value for key in cls]
    
    @property
    def name(self) -> str:
        return self.__class__.__name__


class BingoConfigEnum(ConfigEnum):
    PDFS_FOLDER = "pdfs_folder"
    PDF_NAME = "pdf_name"
    SENTENCES = "sentences"
    NUMBER_OF_SHEETS = "number_of_sheets"
    CELL_WIDTH = "cell_width"
    CELL_HEIGHT = "cell_height"
    X_START = "x_start"
    X_OFFSET = "x_offset"
    Y_START = "y_start"
    Y_OFFSET = "y_offset"
    FONT = "font"
    FONT_SIZE = "font_size"
    LINE_HEIGHT = "line_height"
    MAX_CHARS_DIVIDER = "max_chars_divider"
    ROWS = "rows"
    COLS = "cols"


class AllowsPhotoByEventEnum(ConfigEnum):
    FILE_NAME = "file_name"
    WITH_EVENT_ID = "with_event_id"


class AllowsPhotoEnum(ConfigEnum):
    FILE_NAME = "file_name"


class UploadFileEnum(ConfigEnum):
    UPLOAD_FOLDER = "upload_folder"