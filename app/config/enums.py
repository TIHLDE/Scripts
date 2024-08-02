from enum import Enum


class BingoConfigEnum(Enum):
    PDFS_FOLDER = 'pdfs_folder'
    PDF_NAME = 'pdf_name'
    SENTENCES = 'sentences'
    NUMBER_OF_SHEETS = 'number_of_sheets'
    CELL_WIDTH = 'cell_width'
    CELL_HEIGHT = 'cell_height'
    X_START = 'x_start'
    X_OFFSET = 'x_offset'
    Y_START = 'y_start'
    Y_OFFSET = 'y_offset'
    FONT = 'font'
    FONT_SIZE = 'font_size'
    LINE_HEIGHT = 'line_height'
    MAX_CHARS_DIVIDER = 'max_chars_divider'
    ROWS = 'rows'
    COLS = 'cols'

    @classmethod
    def all(cls) -> list[str]:
        return [key.value for key in cls]