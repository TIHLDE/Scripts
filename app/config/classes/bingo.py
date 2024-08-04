

class BingoConfig:
    def __init__(
        self,
        pdfs_folder: str,
        pdf_name: str,
        sentences: str,
        number_of_sheets: int,
        cell_width: int,
        cell_height: int,
        x_start: int,
        x_offset: int,
        y_start: int,
        y_offset: int,
        font: str,
        font_size: int,
        line_height: int,
        max_chars_divider: int,
        rows: int,
        cols: int
    ):
        self.pdfs_folder = pdfs_folder
        self.pdf_name = pdf_name
        self.sentences = sentences
        self.number_of_sheets = number_of_sheets
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.x_start = x_start
        self.x_offset = x_offset
        self.y_start = y_start
        self.y_offset = y_offset
        self.font = font
        self.font_size = font_size
        self.line_height = line_height
        self.max_chars_divider = max_chars_divider
        self.rows = rows
        self.cols = cols
        
