import os
import random

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from PyPDF2 import PdfMerger

from app.exceptions import (
    FileNotFound,
    DirectoryNotFound
)
from app.config import config


conf = config.bingo

def get_number_of_sheets() -> int:
    number = input(f"Hvor mange bingobrett vil du generere? (Standard er {conf.number_of_sheets}): ")

    if not number:
        return conf.number_of_sheets
    
    try:
        return int(number)
    except ValueError:
        return conf.number_of_sheets


def extract_sentences() -> list[str]:
    path = conf.sentences

    if not os.path.exists(path):
        raise FileNotFound(f"Kunne ikke finne filen med setningene. Du må følgende fil: '{path}'")
    
    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:
        return [line.strip() for line in file]


def generate_pdf(index: int, sentences: list[str]):
    unique_sentences = list(set(sentences)) 
    directory = conf.pdfs_folder

    if not os.path.exists(directory):
        raise DirectoryNotFound(f"Kunne ikke finne mappen '{directory}'.")

    pdf_file = f"{directory}/bingo{index + 1}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    c.setFont(conf.font, conf.font_size)

    CELL_WIDTH = conf.cell_width
    CELL_HEIGHT = conf.cell_height
    X_START = conf.x_start
    Y_START = conf.y_start

    random.shuffle(unique_sentences)

    for row in range(conf.rows):
        for col in range(conf.cols):
            sentence = unique_sentences.pop(0)

            x = X_START + col * CELL_WIDTH
            y = Y_START - row * CELL_HEIGHT

            c.rect(x, y, CELL_WIDTH, CELL_HEIGHT)

            max_chars = int(
                CELL_WIDTH / conf.max_chars_divider
            )

            lines = []
            current_line = ""
            for word in sentence.split():
                if len(current_line) + len(word) <= max_chars:
                    current_line += word + " "
                else:
                    lines.append(current_line.strip())
                    current_line = word + " "
            if current_line:
                lines.append(current_line.strip())

            line_height = conf.line_height

            for i, line in enumerate(lines):
                c.drawString(
                    x + conf.x_offset,
                    y + CELL_HEIGHT - (i * line_height) - conf.y_offset,
                    line
                )

    c.save()


def merge_pdfs():
    merger = PdfMerger()
    pdf_folder = conf.pdfs_folder
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_folder, filename)
            merger.append(file_path)
    
    merger.write(f"{config.download_folder}/{conf.pdf_name}.pdf")
    merger.close()


def clean_up():
    pdf_folder = conf.pdfs_folder
    for filename in os.listdir(pdf_folder):
        file_path = os.path.join(pdf_folder, filename)
        os.remove(file_path)